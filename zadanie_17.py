# Lekcja 05 - Zadanie 17

pole_imie = "    Alice      "
pole_wiek = "    28       "
pole_email = "    alice@EXAMPLE.com       "
pole_imie_czyste = pole_imie.strip()
pole_wiek_czyste = pole_wiek.strip()
pole_email_czyste = pole_email.strip().lower()
czy_imie_ok = pole_imie_czyste.isalpha()
czy_wiek_ok = pole_wiek_czyste.isdigit()
czy_email_ok = '@' in pole_email_czyste
print("Imię:", pole_imie_czyste)
print("Wiek:", pole_wiek_czyste)
print("Email:", pole_email_czyste)
print("Wszystkie pola OK?", czy_imie_ok and czy_wiek_ok and czy_email_ok)
