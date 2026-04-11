# %%
import warnings
warnings.filterwarnings('ignore')
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# %% [markdown]
# ## Numpy

# %% [markdown]
# Numpy is a Python library that allows complex calculations and operations on arrays.
# 
# The main object of Numpy is a homogeneous multidimensional array. 
# 
# An array is an ordered collection of homogeneous data accessible by index. Most often it is a one-dimensional sequence or a two-dimensional table filled with elements of the same type.
# 
# [More details](https://pyprog.pro/introduction.html) about arrays

# %%
import numpy as np

# %%
a = np.array([1, 3, 2])

a

# %%
a = np.array([[1.5, 2, 3], [4, 5, 6]], dtype=np.complex128) #Unlike lists, all elements in an array must belong to the same type

a

# %%
a = np.array([[1.5, 2, 3], [4, 5, 6]], dtype=np.int16) #creates a 2x3 matrix with data type int16 

a

#The array will be converted according to the given type and the output will be:
#Fractional numbers are converted to integer format according to the type
#The number 600000 does not fit into int16 type, a "type overflow" occurs


# %% [markdown]
# ## Matrix Addition / Subtraction

# %%
### Matrix A of size 2x3
A = np.array([[3, 4, 5],
              [1, 1, 1]])

### Matrix B of size 2x3
B = np.array([[5, 5, 5],
              [3, 1, 1]])

### Since the dimensions match, we can subtract and add!

# %%
A - B 

# %% [markdown]
# ## Matrix Multiplication

# %%
### Matrix A of size 2x3
A = np.array([[3, 4, 5],
              [1, 1, 1]])

### Matrix B of size 3x3
B = np.array([[5, 5, 5],
              [3, 1, 10],
              [4, 4, 12]])

### Since the number of columns in matrix A matches the number of rows in matrix B,
### We can multiply A * B

# %%
np.dot(A, B)

# %% [markdown]
# ## Matrix Transposition

# %%
A = np.array([[3, 4, 5],
              [1, 1, 1]])

# %%
A.T

# %% [markdown]
# ## Identity Matrix

# %%
np.eye(4)

# %% [markdown]
# ## Matrix Inversion

# %%
### Matrix A of size 3x3 => It can be inverted
A = np.array([[5, 5, 5],
              [3, 2, 10],
              [4, 4, 12]])

# %%
np.linalg.inv(A)

# %%


# %%


# %% [markdown]
# %% [markdown]
# ## Normal equation: \(\beta^* = (X^T X)^{-1} X^T Y\)
# ### Formula Breakdown
# \[
# \beta^* = (X^T X)^{-1} X^T Y
# \]
#
# This formula is called the **normal equation** for linear regression and allows finding the optimal model coefficients.
#
# Where:
#
# - **\(X\)** — the feature matrix (samples × features);
# - **\(X^T\)** — the transposed matrix of \(X\);
# - **\(Y\)** — the target variable vector (ground-truth values);
# - **\((X^T X)^{-1}\)** — the inverse matrix of \(X^T X\);
# - **\(\beta^*\)** — the vector of learned coefficients (feature weights and, if a column of ones is included, the intercept).
#
# Computation steps:
#
# 1. Compute \(X^T X\);
# 2. Find the inverse matrix \((X^T X)^{-1}\);
# 3. Multiply by \(X^T\);
# 4. Multiply by \(Y\), obtaining \(\beta^*\).
#
# As a result, we get coefficients that minimize the sum of squared prediction errors.

# %%
X = np.array([[23, 0.5, 1],
              [35, 1, 1],
              [18, 0, 1]])

Y = np.array([55, 100, 45])


# %%
xxt = np.dot(X.T, X)
xxt_inv = np.linalg.inv(xxt)
xxt_inv_xxt = np.dot(xxt_inv, X.T)
final_betas = np.dot(xxt_inv_xxt, Y)

final_betas

# %% [markdown]
# ## Example from the First Practice Session

# %%
import pandas as pd

X = pd.read_csv(BASE_DIR / 'ks.csv')
Y = pd.read_csv(BASE_DIR / 'data.csv')

dataset = pd.concat([X, Y], axis=1).dropna()
X = dataset[X.columns].copy()
Y = dataset[Y.columns].copy()
X_num = X.select_dtypes(include=[np.number, 'bool']).copy()
Y_num = Y.select_dtypes(include=[np.number, 'bool']).copy()
y = Y_num.iloc[:, 0]

# %%
X.head()

# %%
Y.head()

# %%
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_num, y)


for column, coef in zip(X_num.columns, model.coef_):
    print(column, coef)
    
print(model.intercept_)

# %%
X_num['constant'] = 1

# %%
xxt = np.dot(X_num.T, X_num)
xxt_inv = np.linalg.inv(xxt)
xxt_inv_xxt = np.dot(xxt_inv, X_num.T)
final_betas = np.dot(xxt_inv_xxt, y)

final_betas

# %%
for column, coef in zip(X_num.columns, final_betas):
    print(column, coef)

# %% [markdown]
# ## What if there is a lot of data, including features?

# %%
matrix = np.random.rand(1000, 1000)

# %%
matrixdot = np.dot(matrix.T, matrix)
matrix_inv = np.linalg.inv(matrixdot)

# %%


# %%



