# Lekcja 05 - Zadanie 8

filename = "model_results_2024_Q3.csv"
czesci = filename.split("_")
rok = czesci[2]
kwartal = czesci[3].split(".")[0]
czy_csv = filename.endswith(".csv")
print("Rok:", rok)
print("Kwartał:", kwartal)
print("Czy plik CSV?", czy_csv)
