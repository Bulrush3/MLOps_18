import pandas as pd

# Загрузка данных из файла titanic.csv
titanic_df = pd.read_csv('datasets/titanic.csv')
# Выбор нужных столбцов для нового датасета
new_df = titanic_df[['Pclass', 'Sex', 'Age']]
# Сохранение нового датасета в файл
new_df.to_csv('datasets/dataset_3clmns.csv', index=False)
