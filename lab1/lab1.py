import pandas as pd
import random
# Считывание файла, смена разделителя на точку с запятой,
file = pd.read_csv('books.csv', encoding="windows-1251", delimiter=";")
df1 = file['Название']
print('Количество записей', len(df1))
count = 0

# Поиск всех записей с названием длинее  30_ти символов
for i in df1:
    if len(i) > 30:
        count += 1
print('Количество записей с названием длинее 30 символов', count)

data_colums_links = ['Автор', 'Название', 'Цена поступления']
df2 = file[data_colums_links]
author = 'Людмила Петрановская'
author_df = df2.loc[df2['Автор'] == author]
# Для каждого x из столбца Цена поступления меняю запятую на точку и перевожу в флоат
author_df['Цена поступления'] = [float(x.replace(',', '.')) for x in author_df['Цена поступления']]
price_df = author_df.loc[author_df['Цена поступления'] >= 200]
print(price_df['Название'].unique())

dc = ['Автор', 'Название', 'Дата поступления']
df3 = file[dc]
count1 = 0
doc = open('links', 'w')
for i, row in df3.iterrows():
    fl = random.randrange(0, 2)
    if fl == 1:
        m = (count1, row[0], row[1], '-', row[2][6:11])
        doc.write(str(m))
        count1 += 1
        if count1 == 20:
            break


file1 = pd.read_csv('books1.csv', encoding="windows-1251", delimiter=";")
df_teg = file1['Жанр книги']
tegs = []
for j in df_teg:
    j = j.split('#')
    for i in range(1, len(j)):
        tegs.append(j[i])
tegs.sort()
print(tegs[0])
for i in range(1, len(tegs)):
    if tegs[i] != tegs[i-1]:
        print(tegs[i])
d_colum_popular = ['Кол-во выдач', 'Название']
df_popular = file1[d_colum_popular]
# the_best = [[0, 0]]*20
# print(the_best)
df_popular_sort = df_popular.sort_values(by='Кол-во выдач')
print(df_popular_sort.tail(20))
