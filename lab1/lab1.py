import pandas as pd

file = pd.read_csv('books.csv', encoding="windows-1251", delimiter=";")
df1 = file['Название']
print('Количество записей', len(df1))
count = 0

for i in df1:
    if len(i)>30:
        count+=1
print('Количество записей с названием длиннее 30 символов', count)
data_cols = ['Автор', 'Название', 'Цена поступления']
df2 = file[data_cols]
author = input()
author_df = df2.loc[df2['Автор'] == author]
author_df['Цена поступления'] = [float(x.replace(',', '.')) for x in author_df['Цена поступления']]
price_df = author_df.loc[author_df['Цена поступления'] >= 200]
print(price_df['Название'].unique())