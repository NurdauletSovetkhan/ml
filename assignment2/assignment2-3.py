import pandas as pd
import numpy as np

sales = pd.read_csv('sales.csv')
targets = pd.read_csv('targets.csv')

sales = sales[sales['amount'].notnull() & (sales['amount'] > 0)]

sales['category'] = sales['category'].str.lower().str.strip()

print('Transaction per category')
print(sales['category'].value_counts())
city_stats = sales.groupby('city')['amount'].agg(['sum', 'mean'])
print('\nCity stats:')
print(city_stats)

city_stats = city_stats.reset_index()
merged = pd.merge(city_stats, targets, on='city', how='inner')

merged['met_target'] = merged['sum'] >= merged['sales_target']
print('\nCities below target:')
print(merged[merged['met_target'] == False])

pct = merged['met_target'].mean() * 100
print(f'\n{pct:.1f}% of cities met their sales target.')
