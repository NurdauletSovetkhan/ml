from sklearn.cluster import KMeans
import numpy as np

# Координаты каких-то объектов (например, чеки в магазине)
X = np.array([[1, 2], [1, 4], [1, 0],
              [10, 2], [10, 4], [10, 0]])

# Хотим разбить на 2 группы
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)

# Смотрим, к какой группе приткнули каждую точку
print(f"Метки кластеров: {kmeans.labels_}")