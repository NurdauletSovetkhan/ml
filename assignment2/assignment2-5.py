import pandas as pd
import numpy as np

a = pd.read_csv('email_spam.csv')

class_counts_a = a['label'].value_counts()

pct_spam = class_counts_a.get('spam', 0) / len(a) * 100

print('=== Dataset A: Email Spam ===')
print(f' Rows : {len(a)}')
print(f' Label classes : {class_counts_a.to_dict()}')
print(f' Spam percentage : {pct_spam:.1f}%')
print(f' ML type : Supervised | Output type: Classification\n')

# Dataset B: house_prices.csv

b = pd.read_csv('house_prices.csv')

prices = b['price'].to_numpy()

prices = b['price'].to_numpy()
print('\n=== Dataset B: House Prices ===')
print(f' Mean price : {np.mean(prices):.2f}')
print(f' Min price : {np.min(prices):.2f}')
print(f' Max price : {np.max(prices):.2f}')
print(f' ML type : Supervised | Output type: Regression\n')

#  Dataset C: customer_behaviour.csv
c = pd.read_csv('customer_behaviour.csv')

print('\n=== Dataset C: Customer Behaviour ===')
print(f' Rows : {len(c)}')
print(f' Columns : {c.columns.tolist()}')
print(f' ML type : Unsupervised | Reason: no label column exists')

summary = pd.DataFrame({
    'Dataset': ['Email Spam', 'House Prices', 'Customer Behaviour'],
    'ML Type': ['Supervised', 'Supervised', 'Unsupervised'],
    'Output Type': ['Classification', 'Regression', 'N/A']
})

print('\n=== ML Problem Summary ===')
print(summary.to_string(index=False))