# %%
from IPython.display import Image
import pandas as pd
import numpy as np

# %%
data = pd.read_csv('ks.csv')

# %%
data.head()

# %%
data.shape

# %%
### Keep only the relevant statuses

data = data[data['Status'].isin(['failed', 'successful'])]

# %% [markdown]
# ### What do we use as the target? 2 options:
# 
# - We will solve a classification task: mark successful projects as 1, and failed ones as 0
# 
# - We can predict the amount of money raised directly, then check if it reaches the goal. That would be a regression task.

# %%
### Create target1 column (binary target)

data.loc[(data['Status'] == 'failed'), 'target1'] = 0
data['target1'] = data['target1'].fillna(1)

# %%
data = data.drop('Status', axis=1)

# %%
### Create target2 column (continuous/regression target)
data = data.rename({'target2':'target2'}, axis=1)
data.head()

# %% [markdown]
# ### To build a feature matrix, we often need to process raw data and extract features that are not explicitly given

# %%
### From date columns, compute the difference in days 
data['Launch_Date'] = pd.to_datetime(data['Publication date'])
data['Deadline'] = pd.to_datetime(data['Deadline'])

# %%


# %%
data['Duration'] = (data['Deadline'] - data['Launch_Date']).dt.days

# %%
### Extract the launch year of the project
data['Launch_Year'] = data['Launch_Date'].dt.year

# %%
data.head()

# %% [markdown]
# ### Sometimes it may seem like we have too few features. Think about what else could explain the target variable.

# %%
Macro = pd.read_excel("macrofeatures.xlsx", engine="openpyxl")

Macro.head()

# %%
### Merge columns. Keep just one macro feature for now.

Macro = Macro[['Close_brent', 'dlk_cob_date']].drop_duplicates()

# %%
Macro['dlk_cob_date'] = pd.to_datetime(Macro['dlk_cob_date'])

# %%
data['Launch_Date'] = data['Launch_Date'].dt.date.astype('datetime64[ns]')

# %%
data = pd.merge(data,
         Macro,
         left_on=['Launch_Date'],
         right_on=['dlk_cob_date'],
         how='left')

# %%
data = data.sort_values('Launch_Date')

# %%
data['Close_brent'] = data['Close_brent'].fillna(34.41)

# %%
data = data.drop(['Deadline', 'Launch_Date', 'dlk_cob_date'], axis=1)

# %%
data.head()

# %% [markdown]
# ### Finally, drop columns that we do not consider features

# %%
### Drop columns: Deadline, Launch Date, Backers, Name, Country

data = data.drop(['Name', 'Country'], axis=1)

# %%
data.head()

# %% [markdown]
# ## One-hot Encoding

# %%
### One-hot Encoding for the Currency column

data = pd.concat((data, pd.get_dummies(data['Currency'])), axis=1)
data = data.drop(['Currency'], axis=1)

data.head()


### Remove redundant columns 
data = data.drop('AUD', axis=1)


### Similarly encode the Main Category
data = pd.concat((data, pd.get_dummies(data['Main category'])), axis=1)
data = data.drop(['Main category'], axis=1)

# %%
data.head()

# %%
data = data.drop('Games', axis=1)

# %%
### What about the Category column?

len(data['Category'].unique())


# %% [markdown]
# ## Mean-Target Encoding (Counters)

# %% [markdown]
# ![%D0%A1%D1%87%D0%B5%D1%82%D1%87%D0%B8%D0%BA%D0%B8.png](attachment:%D0%A1%D1%87%D0%B5%D1%82%D1%87%D0%B8%D0%BA%D0%B8.png)

# %%
### Apply mean-target encoding to the Category column
data['Category'] = data['Category'].map(data.groupby(['Category'])['Amount raised in dollars'].mean())

# %%
data.head()

# %% [markdown]
# ## Define the Target Variable

# %%
data = data.drop('target1', axis=1)

# %%
### Split the data into features and target
X = data.drop(['Amount raised in dollars','Publication date'], axis=1)
Y = data['Amount raised in dollars']

# %%
X

# %%
Y

# %% [markdown]
# ### sklearn

# %%
### Now the magic happens!
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, Y)

X['Prediction'] = model.predict(X)

X.head()

# %%
data.head()

# %%
# Save the result to data.csv
data.to_csv('data.csv', index=False)


