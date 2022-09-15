import pandas as pd

file = pd.read_csv('books.csv', encoding="windows-1251", delimiter=";")
print(file['Название'])
