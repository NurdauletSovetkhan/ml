import pandas as pd

# Названия колонок вытаскиваем из файла wine.names
# Первая колонка в этом датасете — это целевой класс (сорта вина: 1, 2 или 3)
columns = [
    "Class", "Alcohol", "Malic_acid", "Ash", "Alcalinity_of_ash", 
    "Magnesium", "Total_phenols", "Flavanoids", "Nonflavanoid_phenols", 
    "Proanthocyanins", "Color_intensity", "Hue", "OD280_OD315_of_diluted_wines", "Proline"
]

# Грузим данные, явно указывая, что заголовка в файле нет (header=None)
wine_df = pd.read_csv('data/wine/wine.data', header=None, names=columns)

# Проверяем, что всё прочиталось ровно
print(wine_df.head())
print(f"Размерность датасета: {wine_df.shape}")