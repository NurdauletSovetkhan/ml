import pandas as pd

df = pd.read_csv('hospital_patients.csv')

print('Shape : ', df.shape)
print('Dtypes : ')
print(df.dtypes)
print('Nulls : ')
print(df.isnull().sum())
print('Duplicates: ', df.duplicated().sum())

df = df.drop_duplicates()

df['age'] = df['age'].astype('int')

df['length_of_stay'] = df['length_of_stay'].fillna(df['length_of_stay'].median())

df['over_60'] = df['age'] > 60

ward_summary = (
    df.groupby('ward')['length_of_stay'].mean().sort_values(ascending=True)
)

print('\nAverage length of stay by ward:')
print(ward_summary)

df.to_csv('clean_patients.csv', index=False)
print(f'\nCleaned data saved. Final shape: {df.shape}')