# Lekcja 05 - Zadanie 10

modele = ['LogisticRegression', 'RandomForest', 'XGBoost', 'SVM']
polaczone = ", ".join(modele)
sql = f"SELECT model FROM ({polaczone})"
odtworzona_lista = polaczone.split(", ")
print(polaczone)
print(sql)
print("Czy listy identyczne?", odtworzona_lista == modele)
