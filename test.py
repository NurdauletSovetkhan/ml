from sklearn.linear_model import LinearRegression
import numpy as np

# Данные: X - часы подготовки, y - балл на экзамене
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([15, 25, 40, 60, 85])

# Создаем и обучаем модель
model = LinearRegression()
model.fit(X, y)

# Предсказываем результат для 6 часов подготовки
prediction = model.predict([[6]])
print(f"Предполагаемый балл: {prediction[0]}")