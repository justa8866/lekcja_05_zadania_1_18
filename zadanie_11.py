# Lekcja 05 - Zadanie 11

log = "2024-01-15 10:23:45 ERROR Training failed due to OOM"
fragmenty = log.split(" ", 3)
data, czas, poziom, wiadomosc = fragmenty[0], fragmenty[1], fragmenty[2], fragmenty[3]
print(f"[{data} {czas}] {poziom}: {wiadomosc}")
poziom_znany = poziom in ['INFO', 'WARNING', 'ERROR', 'DEBUG']
print("Czy poziom znany?", poziom_znany)
