import pandas as pd

## Загрузка данных из файла titanic.csv
#titanic_df = pd.read_csv('datasets/titanic.csv')
## Выбор нужных столбцов для нового датасета
#new_df = titanic_df[['Pclass', 'Sex', 'Age']]
## Сохранение нового датасета в файл
#new_df.to_csv('datasets/dataset_3clmns.csv', index=False)
df = pd.read_csv('datasets/dataset_3clmns.csv')
#mean_age = df['Age'].mean()
#df['Age'].fillna(mean_age, inplace=True)
sex_one_hot = pd.get_dummies(df['Sex'])
df = pd.concat([df, sex_one_hot], axis=1)
df = df.drop('Sex', axis=1)

df.to_csv('datasets/dataset_3clmns.csv', index=False)
