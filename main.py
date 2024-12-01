import pandas as pd

df = pd.read_csv('teams_data.csv')

#Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
print(df.head())

#Выведите информацию о данных (.info()) и статистическое описание (.describe()).
print(df.info())
print(df.describe())
