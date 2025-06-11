import json
from collections import Counter

print("🧠 ANALIZA HISTORII LOSOWAŃ – tryb uczenia")

try:
    with open("historia_wynikow.json", "r", encoding="utf-8") as f:
        historia = json.load(f)
except FileNotFoundError:
    print("❌ Brak pliku historia_wynikow.json – nie można analizować.")
    exit()

wszystkie_liczby = []

for wpis in historia:
    wszystkie_liczby.extend(wpis["wyniki"])

licznik = Counter(wszystkie_liczby)
najczestsze = licznik.most_common(5)
najrzadsze = licznik.most_common()[:-6:-1]

print("\n📊 TOP 5 najczęściej losowanych liczb:")
for liczba, ile in najczestsze:
    print(f"🔹 Liczba {liczba}: {ile} razy")

print("\n📉 TOP 5 najrzadszych liczb:")
for liczba, ile in najrzadsze:
    print(f"🔸 Liczba {liczba}: {ile} razy")

# Rozkład liczbowy (przedziały)
rozklad = {
    "1-10": 0,
    "11-20": 0,
    "21-30": 0,
    "31-40": 0
}

for liczba in wszystkie_liczby:
    if 1 <= liczba <= 10:
        rozklad["1-10"] += 1
    elif 11 <= liczba <= 20:
        rozklad["11-20"] += 1
    elif 21 <= liczba <= 30:
        rozklad["21-30"] += 1
    elif 31 <= liczba <= 40:
        rozklad["31-40"] += 1

print("\n📈 Rozkład liczbowy (zakresy):")
for zakres, ile in rozklad.items():
    print(f"📦 {zakres}: {ile} trafień")