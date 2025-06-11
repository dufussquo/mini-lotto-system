# -*- coding: utf-8 -*-
import json
import datetime

now = datetime.datetime.now().isoformat()

nowy_entry = {
    "data": now,
    "typ": "neutralna",
    "modul": "system_start",
    "opis": "Pierwsze uruchomienie changeloga",
    "ocena": None
}

nowy_entry_2 = {
    "data": now,
    "typ": "negatywna",
    "modul": "modul_sieci",
    "opis": "Błąd krytyczny w module analizującym dane sieciowe.",
    "ocena": None
}

try:
    with open("changelog.json", "r", encoding="utf-8") as f:
        changelog = json.load(f)
except FileNotFoundError:
    changelog = []

changelog.append(nowy_entry)
changelog.append(nowy_entry_2)

with open("changelog.json", "w", encoding="utf-8") as f:
    json.dump(changelog, f, indent=4, ensure_ascii=False)

print("✅ Zmiana została zapisana w changelogu.")