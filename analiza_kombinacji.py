from collections import Counter
import json
from itertools import combinations

def analiza_kombinacji():
    print("\n📊 ANALIZA KOMBINACJI\n")

    try:
        with open("baza_wynikow.json", "r", encoding="utf-8") as f:
            wyniki = json.load(f)
    except Exception as e:
        print(f"❌ Błąd podczas wczytywania wyników: {e}")
        return

    wszystkie_liczby = [sorted(w["liczby"]) for w in wyniki]

    print("🔗 Najczęstsze kombinacje:")

    for r in range(2, 6):  # kombinacje 2 do 5 liczb
        counter = Counter()
        for zestaw in wszystkie_liczby:
            for c in combinations(zestaw, r):
                counter[c] += 1
        top5 = counter.most_common(5)
        print(f"\n🔹 TOP 5 dla {r}-liczbowych kombinacji:")
        for kombo, ile in top5:
            print(f"  {list(kombo)}: {ile} razy")

    print("\n✅ ANALIZA KOMBINACJI ZAKONCZONA")