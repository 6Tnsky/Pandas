import pandas as pd

df = pd.read_csv('dz.csv')

#Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv
df.fillna(value=0, inplace=True)
print(df)

group = df.groupby('City')['Salary'].mean().round(2)
print(group)