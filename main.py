import modul_sieci_final
import panel
import reflektor_final
import pomysly_final
import changelog
import modul_podejrzanych_final
import json
import os
import datetime

print("\U0001F7E3 ROZPOCZĘTO SKANOWANIE SIECI (GLITCH ONLINE)")

# WERSJA SYSTEMU
version = "v0.3.6 (PRODUKCYJNY)"
print(f"\U0001F539 WERSJA SYSTEMU: {version}")

# Wczytaj wyniki z pliku JSON
try:
    with open("dane.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print("\u274C Brak pliku dane.json - nie można kontynuować.")
    exit()

print(f"\U0001F4C5 Wyniki z {data['date']} to: {data['results']}")
print("\U0001F4DD Tu możesz dodać analizę podejrzanych wpisów itp.")
print("\u2705 SKAN ZAKOŃCZONY")

# ZAPIS DO HISTORII WYNIKÓW:
print("\n\U0001F4BE ZAPIS DO HISTORII WYNIKÓW...")
today = data["date"]
nowy_wpis = {
    "data": today,
    "liczby": data["results"]
}

try:
    with open("baza_wynikow.json", "r", encoding="utf-8") as f:
        baza = json.load(f)
        if isinstance(baza, dict) and "historia" in baza:
            baza = baza["historia"]
except FileNotFoundError:
    baza = []

dzisiejsza_data = data["date"]
nowy_wpis = {
    "data": dzisiejsza_data,
    "liczby": data["results"]
}

istnieje = any(
    isinstance(wpis, dict) and wpis.get("data") == dzisiejsza_data
    for wpis in baza
)

if not istnieje:
    baza.append(nowy_wpis)
    with open("baza_wynikow.json", "w", encoding="utf-8") as f:
        json.dump({"historia": baza}, f, indent=2, ensure_ascii=False)
    print("🟢 Nowe wyniki dodane do historii.")
else:
    print("🔁 Wyniki z tego dnia już istnieją w historii.")
    
# AUTOMATYCZNE ANALIZY PO LOSOWANIU
print("\n📊 URUCHAMIANIE MODUŁÓW ANALIZY...")

try:
    import analiza_statystyk
    analiza_statystyk.analiza_statystyk()
except Exception as e:
    print(f"❌ Błąd podczas analizy statystyk: {e}")

try:
    import analiza_kombinacji
    analiza_kombinacji.analiza_kombinacji()
except Exception as e:
    print(f"❌ Błąd podczas analizy kombinacji: {e}")    
