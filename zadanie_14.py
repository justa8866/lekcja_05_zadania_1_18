# Lekcja 05 - Zadanie 14

sciezka = "/data/processed/2024/experiment_42_v3.csv"
czesci = sciezka.split("/")
nazwa_pliku = czesci[-1]
katalog = "/".join(czesci[:-1])
nazwa_bez_rozszerzenia = nazwa_pliku.rsplit(".", 1)[0]
rozszerzenie = "." + nazwa_pliku.rsplit(".", 1)[1]
rok = czesci[-2]
print(f"{'Nazwa pliku:':<25}{nazwa_pliku}")
print(f"{'Katalog:':<25}{katalog}")
print(f"{'Nazwa bez rozszerzenia:':<25}{nazwa_bez_rozszerzenia}")
print(f"{'Rozszerzenie:':<25}{rozszerzenie}")
print(f"{'Rok:':<25}{rok}")
