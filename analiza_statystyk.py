import json
from collections import Counter

print("🔍 ANALIZA STATYSTYK 🔎")

try:
    with open("baza_wynikow.json", "r", encoding="utf-8") as f:
        baza = json.load(f)
except FileNotFoundError:
    print("❌ Brak pliku baza_wynikow.json")
    exit()

wszystkie_liczby = []
dni_tygodnia = []

for wpis in baza:
    # Jeśli wpis jest stringiem (JSON), zdekoduj go
    if isinstance(wpis, str):
        wpis = json.loads(wpis)

    liczby = wpis["liczby"]
    wszystkie_liczby.extend(liczby)

    # Pobieranie dnia tygodnia z daty
    if "data" in wpis:
        from datetime import datetime
        data = datetime.strptime(wpis["data"], "%Y-%m-%d")
        dni_tygodnia.append(data.strftime("%A"))

# TOP 5 najczęściej losowanych liczb
najczestsze = Counter(wszystkie_liczby).most_common(5)
print("\n📊 TOP 5 najczęściej losowanych liczb:")
for liczba, ile in najczestsze:
    print(f"🔹 Liczba {liczba}: {ile} razy")

# Rozkład po dniach tygodnia
print("\n📅 Rozkład losowań wg dni tygodnia:")
for dzien, ile in Counter(dni_tygodnia).items():
    print(f"🔸 {dzien}: {ile} losowań")