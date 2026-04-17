"""Logging utilities for assignment scripts."""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def get_logger(name: str, log_dir: str = "logs") -> logging.Logger:
	"""Create and return a configured logger instance.

	Args:
		name: Logger name.
		log_dir: Directory for log files.

	Returns:
		Configured logger.
	"""
	logger = logging.getLogger(name)
	if logger.handlers:
		return logger

	logger.setLevel(logging.INFO)
	Path(log_dir).mkdir(parents=True, exist_ok=True)

	formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

	file_handler = RotatingFileHandler(
		Path(log_dir) / f"{name}.log",
		maxBytes=2_000_000,
		backupCount=3,
	)
	file_handler.setFormatter(formatter)

	stream_handler = logging.StreamHandler()
	stream_handler.setFormatter(formatter)

	logger.addHandler(file_handler)
	logger.addHandler(stream_handler)
	logger.propagate = False
	return logger
