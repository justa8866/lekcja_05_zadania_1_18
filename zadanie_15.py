# Lekcja 05 - Zadanie 15

kat_a = "   Electronics       "
kat_b = "ELECTRONICS"
print("Przed normalizacją:", repr(kat_a), repr(kat_b))
kat_a_norm = kat_a.strip().lower()
kat_b_norm = kat_b.strip().lower()
print("Po normalizacji:", repr(kat_a_norm), repr(kat_b_norm))
print("Czy identyczne?", kat_a_norm == kat_b_norm)
