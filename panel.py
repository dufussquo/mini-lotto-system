import json
import datetime
import os

def wczytaj_dane():
    try:
        with open("baza_wynikow.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def wczytaj_dzisiejsze():
    try:
        with open("dane.json", "r", encoding="utf-8") as f:
            dane = json.load(f)
            return dane.get("wyniki", [])
    except FileNotFoundError:
        return []

def liczba_trafien(zestaw, dzisiejsze):
    return len(set(zestaw) & set(dzisiejsze))

def pokaz_panel():
    print("\n📊 PANEL SYSTEMU MINI LOTTO")
    print("-" * 40)

    dzisiejsze = wczytaj_dzisiejsze()
    if not dzisiejsze:
        print("❌ Brak dzisiejszych wyników.")
        return

    print(f"🎯 Dzisiejsze wyniki: {dzisiejsze}")

    try:
        with open("historia_wynikow.json", "r", encoding="utf-8") as f:
            historia = json.load(f)
    except FileNotFoundError:
        historia = []

    if historia:
        print("\n📅 Historia:")
        for wpis in historia[-3:]:
            print(f"📌 {wpis['data']}: {wpis['liczby']}")
    else:
        print("\n📌 Brak danych historycznych.")

    print("\n🎲 Trafienia:")
    try:
        with open("dane.json", "r", encoding="utf-8") as f:
            dane = json.load(f)
            zestawy = dane.get("zestawy", [])
            for i, zestaw in enumerate(zestawy):
                trafione = liczba_trafien(zestaw, dzisiejsze)
                print(f"Zestaw {i+1}: {zestaw} ➤ {trafione} trafień")
    except:
        print("❗ Błąd wczytywania zestawów")

    print("-" * 40)

# Automatyczne uruchomienie
if __name__ == "__main__":
    pokaz_panel()