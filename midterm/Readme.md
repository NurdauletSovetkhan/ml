# Video Game Commercial Success Predictor 🎮

## Project Overview
This project implements an end-to-end machine learning pipeline to predict whether a video game will become a commercial "Hit" (defined as reaching $\geq$ 1 million global sales). By analyzing historical data, platform ecosystems, and publisher statuses, this repository explores the baseline predictive power of metadata in the gaming industry, moving from exploratory data analysis (EDA) to advanced ensemble modeling with unsupervised clustering features.

## Dataset Information
* **Name:** Video Game Sales & Industry Data (1980 - 2024)
* **Source:** [Kaggle](https://www.kaggle.com/) (Search: "Video Game Sales & Industry Data")
* **License:** Public Domain / CC0 (Standard Kaggle Open Data)

## Repository Structure
```text
├── data/
│   ├── raw/                
│   ├── cleaned.csv          
│   ├── clustered.csv        
├── models/
│   ├── supervised_best.pkl 
├── notebooks/
│   ├── T1_EDA.ipynb
│   ├── T2_Supervised.ipynb
│   ├── T3_Unsupervised.ipynb
│   ├── T4_Ensemble.ipynb
├── reports/                 
├── requirements.txt
└── README.md
```

## Installation & Execution Instructions
1. Clone this repository to your local machine.
2. Ensure you have Python 3.9+ installed.
3. Install the required dependencies:
```
pip install -r requirements.txt
```
4. Place the downloaded dataset into `data/raw/` and name it `vg_sales.csv`.
5. Launch Jupyter Notebook and execute the notebooks strictly in order from T1 to T4 using Kernel $\rightarrow$ Restart & Run All.


## Final Model Results (Tasks 2 & 4)

_Random Forest and XGBoost utilize the unsupervised `cluster_label` as an additional predictive feature._

|**Model**|**Task**|**Accuracy**|**F1 Score**|
|---|---|---|---|
|**Logistic Regression (Baseline)**|Task 2|~0.71|~0.26|
|**Random Forest**|Task 4|~0.75|~0.35|
|**XGBoost**|Task 4|~0.74|~0.32|
