"""Inference script for severity score prediction."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import joblib
import pandas as pd

from utils.config import load_config
from utils.logger import get_logger


class PredictionError(Exception):
	"""Custom exception for prediction failures."""


def _load_artifacts(config: dict[str, Any]) -> tuple[Any, Any]:
	"""Load fitted preprocessor and regression model from disk."""
	preprocessor_path = Path(config["paths"]["preprocessor"])
	model_path = Path(config["paths"]["regression_model"])

	if not preprocessor_path.exists():
		raise FileNotFoundError(f"Preprocessor not found: {preprocessor_path}")
	if not model_path.exists():
		raise FileNotFoundError(f"Model not found: {model_path}")

	preprocessor = joblib.load(preprocessor_path)
	model = joblib.load(model_path)
	return preprocessor, model


def _validate_and_prepare_input(
	raw_features: dict[str, Any],
	expected_features: list[str],
	categorical_features: list[str],
) -> pd.DataFrame:
	"""Validate input dictionary and convert it to one-row DataFrame."""
	if not isinstance(raw_features, dict):
		raise PredictionError("Input must be a dictionary with feature names as keys.")

	missing = [feature for feature in expected_features if feature not in raw_features]
	if missing:
		raise PredictionError(f"Missing required features: {missing}")

	unknown = [feature for feature in raw_features if feature not in expected_features]
	if unknown:
		raise PredictionError(f"Unknown features provided: {unknown}")

	categorical_set = set(categorical_features)
	validated: dict[str, Any] = {}
	for feature in expected_features:
		value = raw_features[feature]
		if feature in categorical_set:
			validated[feature] = str(value)
		else:
			try:
				validated[feature] = float(value)
			except (TypeError, ValueError) as exc:
				raise PredictionError(
					f"Feature '{feature}' must be numeric, got value '{value}'."
				) from exc

	return pd.DataFrame([validated], columns=expected_features)


def predict_severity(raw_features: dict[str, Any], config_path: str = "config.yaml") -> float:
	"""Predict severity score in range 0-100 from raw features."""
	config = load_config(config_path)
	logger = get_logger("predict", log_dir=config["paths"].get("logs_dir", "logs"))

	expected_features = config["dataset"]["feature_columns"]
	categorical_features = config["dataset"]["categorical_features"]

	logger.info("Starting prediction for one network event")
	preprocessor, model = _load_artifacts(config)

	try:
		input_frame = _validate_and_prepare_input(
			raw_features=raw_features,
			expected_features=expected_features,
			categorical_features=categorical_features,
		)
		transformed = preprocessor.transform(input_frame)
		prediction = float(model.predict(transformed)[0])
		logger.info("Prediction completed successfully. severity=%.4f", prediction)
		return prediction
	except Exception as exc:
		logger.exception("Prediction failed: %s", exc)
		raise


def _parse_input_payload(raw_input: str) -> dict[str, Any]:
	"""Parse JSON payload from inline JSON string or file path."""
	candidate_path = Path(raw_input)
	payload = candidate_path.read_text(encoding="utf-8") if candidate_path.exists() else raw_input

	try:
		data = json.loads(payload)
	except json.JSONDecodeError as exc:
		raise PredictionError("Input must be valid JSON string or path to JSON file.") from exc

	if not isinstance(data, dict):
		raise PredictionError("Parsed JSON must be an object/dictionary.")
	return data


def main() -> None:
	"""CLI entry point."""
	parser = argparse.ArgumentParser(description="Predict network event severity score")
	parser.add_argument("--input", required=True, help="JSON object string or path to JSON file")
	parser.add_argument("--config", default="config.yaml", help="Path to YAML config")
	args = parser.parse_args()

	payload = _parse_input_payload(args.input)
	score = predict_severity(payload, config_path=args.config)
	print(f"{score:.4f}")


if __name__ == "__main__":
	main()
