class Koltuk:
    def __init__(self, sira: str, numara: int):
        self.sira = sira
        self.numara = numara
        self.is_rezerve = False

    def rezerve_et(self):
        if self.is_rezerve:
            print(f"❌ {self.sira}{self.numara} numaralı koltuk zaten rezerve edilmiş.")
        else:
            self.is_rezerve = True
            print(f"✅ {self.sira}{self.numara} numaralı koltuk başarıyla rezerve edildi.")

    def iptal_et(self):
        if not self.is_rezerve:
            print(f"⚠️ {self.sira}{self.numara} numaralı koltuk zaten boş.")
        else:
            self.is_rezerve = False
            print(f"🔄 {self.sira}{self.numara} numaralı koltuk rezervasyonu iptal edildi.")

    def __str__(self):
        status = "[X]" if self.is_rezerve else "[O]"
        return f"{self.sira}{self.numara}{status}"


class Salon:
    def __init__(self, salon_adi: str, sira_sayisi: int, koltuk_sayisi: int):
        self.salon_adi = salon_adi
        self.koltuklar = []

        sira_harfleri = ["A", "B", "C", "D", "E", "F", "G"]
        
        for i in range(sira_sayisi):
            sira = sira_harfleri[i]
            for numara in range(1, koltuk_sayisi + 1):
                yeni_koltuk = Koltuk(sira, numara)
                self.koltuklar.append(yeni_koltuk)

    def koltuklari_goster(self):
        print(f"\n=== {self.salon_adi} KOLTUK DÜZENİ ===")
        print("         [ E K R A N ]\n")

        gecerli_sira = ""
        for koltuk in self.koltuklar:
            if koltuk.sira != gecerli_sira:
                gecerli_sira = koltuk.sira
                print()
            print(koltuk, end="  ")
        print("\n")


# === TEST KISMI ===
# 3 sıra (A,B,C) ve her sırada 5 koltuk olan bir salon oluşturalım:
salon1 = Salon("Salon 1 (Kırmızı Salon)", sira_sayisi=3, koltuk_sayisi=5)

# Koltukları ekrana basalım
salon1.koltuklari_goster()