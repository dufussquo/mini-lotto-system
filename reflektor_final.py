# -*- coding: utf-8 -*-
import json
from datetime import datetime

print("🧠 Reflektor analizuje zmiany...")

try:
    with open("changelog.json", "r", encoding="utf-8") as f:
        changelog = json.load(f)
except FileNotFoundError:
    print("❌ Brak pliku changelog.json – nie można przeprowadzić analizy.")
    exit()

if not changelog:
    print("ℹ️ Brak zmian do analizy.")
    exit()

# Analiza typów zmian
positive = sum(1 for entry in changelog if entry.get("ocena") == "pozytywna")
negative = sum(1 for entry in changelog if entry.get("ocena") == "negatywna")
neutral  = sum(1 for entry in changelog if entry.get("ocena") == "neutralna")

print("🧪 ANALIZA ZMIAN W SYSTEMIE:")
print(f"📈 Ostatnie zmiany – pozytywne: {positive}, negatywne: {negative}, neutralne: {neutral}")

# Propozycja działania
if negative >= 2:
    print("❗ ZALECENIE: rozważyć wycofanie ostatnich zmian lub aktywację trybu awaryjnego.")
elif positive >= 2:
    print("✅ ZALECENIE: kontynuować aktualny kierunek optymalizacji.")
else:
    print("🟡 ZALECENIE: zachowaj ostrożność, brak wystarczających danych do oceny.")