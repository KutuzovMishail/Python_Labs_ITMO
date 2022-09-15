import pandas as pd

file = pd.read_csv('books.csv', encoding="windows-1251", delimiter=";")
df1 = file['Название']

count = 0

for i in df1:
    if len(i)>30:
        count+=1
print('Количество записей с названием длиннее 30 символов',count)
