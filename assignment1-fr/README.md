# ML-4812 Assignment Submission

## Included files
- `02_supervised_regression.ipynb`
- `03_unsupervised_clustering.ipynb`
- `predict.py`
- `models/` (all `.joblib` artifacts)

## Environment
```bash
source /home/nurrrdaulet/aitu/codingstuff/ml/ml-venv/bin/activate
```

## Reproduce
1. Run all cells in `02_supervised_regression.ipynb`.
2. Run all cells in `03_unsupervised_clustering.ipynb`.

Artifacts are saved to `models/`:
- `preprocessor.joblib`
- `regression_model.joblib`
- `pca_model.joblib`
- `clustering_model.joblib`

## Inference
```bash
python predict.py --input '{"duration":0,"protocol_type":"tcp","service":"http","flag":"SF","src_bytes":181,"dst_bytes":5450,"land":0,"wrong_fragment":0,"urgent":0,"hot":0,"num_failed_logins":0,"logged_in":1,"num_compromised":0,"root_shell":0,"su_attempted":0,"num_root":0,"num_file_creations":0,"num_shells":0,"num_access_files":0,"num_outbound_cmds":0,"is_host_login":0,"is_guest_login":0,"count":8,"srv_count":8,"serror_rate":0.0,"srv_serror_rate":0.0,"rerror_rate":0.0,"srv_rerror_rate":0.0,"same_srv_rate":1.0,"diff_srv_rate":0.0,"srv_diff_host_rate":0.0,"dst_host_count":9,"dst_host_srv_count":9,"dst_host_same_srv_rate":1.0,"dst_host_diff_srv_rate":0.0,"dst_host_same_src_port_rate":0.11,"dst_host_srv_diff_host_rate":0.0,"dst_host_serror_rate":0.0,"dst_host_srv_serror_rate":0.0,"dst_host_rerror_rate":0.0,"dst_host_srv_rerror_rate":0.0}'
```

## Dataset reference
- KDD Cup 1999 Data: https://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html

Local file used in this project: `corrected`.
