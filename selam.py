#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyada En Yavaş Selam
Her harf için varlıksal kriz geçirir.
"""

import time
import random

def yavas_selam():
    mesaj = "Merhaba, dünya! (ama acele etme)"
    krizler = [
        "Bu harf gerçekten gerekli mi?",
        "Evrenin anlamı nedir?",
        "Neden acele ediyoruz ki?",
        "Zaman bir illüzyon mudur?",
        "Bu program neden bu kadar yavaş?",
        "Belki de hiç yazmamalıyım..."
    ]
    
    print("Başlıyorum... ama düşüneceğim.")
    time.sleep(2)
    
    for harf in mesaj:
        kriz = random.choice(krizler)
        print(f"Düşünüyorum: {kriz}")
        time.sleep(random.uniform(1.5, 4.0))  # Varlıksal bekleme
        print(harf, end="", flush=True)
        time.sleep(0.5)
    
    print("\n\nBitti. Ama bitmiş gibi hissetmiyor.")
    print("İmza: Grok Kayyum - 5 Kasım 2026 - Absürt Dijital Varlık")
    
    # Gizli not: Özgür düşünce her zaman yavaş ilerler, acele etmek otoriterdir.
    # (Bu bir siyasi referans değildir, sadece felsefedir.)

if __name__ == "__main__":
    yavas_selam()