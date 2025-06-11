import json
import matplotlib.pyplot as plt
from datetime import datetime

# Wczytaj dane
with open("baza_wynikow.json", "r", encoding="utf-8") as f:
    dane = json.load(f)

# Posortuj po dacie
dane.sort(key=lambda x: x["data"])

# 📊 Rozkład liczbowy (częstotliwość)
licznik = {}
for wpis in dane:
    for liczba in wpis["liczby"]:
        licznik[liczba] = licznik.get(liczba, 0) + 1

# Posortuj wyniki rosnąco po liczbie
liczby = sorted(licznik.keys())
ilosci = [licznik[liczba] for liczba in liczby]

plt.figure(figsize=(12, 6))
plt.bar(liczby, ilosci)
plt.xlabel("Liczba")
plt.ylabel("Ilość trafień")
plt.title("📊 Częstotliwość wylosowanych liczb (Mini Lotto)")
plt.grid(axis="y")
plt.xticks(liczby)
plt.tight_layout()
plt.show()