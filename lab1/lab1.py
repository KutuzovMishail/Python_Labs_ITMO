import pandas as pd
#Считывание файла, смена разделителя на точку с запятой,
file = pd.read_csv('books.csv', encoding="windows-1251", delimiter=";")
df1 = file['Название']
print('Количество записей', len(df1))
count = 0

#Поиск всех записей с названием длинее  30_ти символов
for i in df1:
    if len(i)>30:
        count+=1
print('Количество записей с названием длинее 30 символов', count)

data_cols = ['Автор', 'Название', 'Цена поступления']
df2 = file[data_cols]
author = 'Людмила Петрановская'
author_df = df2.loc[df2['Автор'] == author]
#Для каждого x из столбца Цена поступления меняю запятую на точку и перевожу в флоат
author_df['Цена поступления'] = [float(x.replace(',', '.')) for x in author_df['Цена поступления']]
price_df = author_df.loc[author_df['Цена поступления'] >= 200]
print(price_df['Название'].unique())

dc = ['Автор', 'Название', 'Дата поступления']
df3 = file[dc]
#Выделение года из колонки Дата поступления
df_test=file['Дата поступления']
year=[]
for i in df_test:
    year.append(i[6:11])

import random

count1=0
doc=open('links', 'w')

for i, row in df3.iterrows():
    fl = random.randrange(0, 2)
    if fl==1:
        m=(count1, row[0], row[1], '-', row[2][6:11])
        doc.write(str(m))
        count1+=1
        if count1==20:
            break