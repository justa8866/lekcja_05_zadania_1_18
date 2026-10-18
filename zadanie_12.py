# Lekcja 05 - Zadanie 12

tabela = "customers"
kolumny = ['id', 'name', 'email', 'city']
warunek = "city = 'New York'"
sql = f"SELECT {', '.join(kolumny)} FROM {tabela} WHERE {warunek}"
print(sql)
