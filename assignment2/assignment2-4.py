import pandas as pd
import numpy as np

df = pd.read_csv('clean_patients.csv')
X = df.drop(columns=['over_60'])
y = df['over_60']
print(f'Features shape: {X.shape}, Labels shape: {y.shape}')


before = len(X)
X = X.dropna()
y = y.loc[X.index]
print(f'Rows removed due to missing values: {before - len(X)}')

X['ward'] = pd.Categorical(X['ward']).codes
for col in X.select_dtypes(include='number').columns:
    col_min = X[col].min()
    col_max = X[col].max()

    X[col] = (X[col] - col_min) / (col_max - col_min)

split_idx = int(0.8 * len(X))
X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

print(f'Training samples : {len(X_train)}')
print(f'Test samples : {len(X_test)}')
print('Data preparation complete. Ready for training.')