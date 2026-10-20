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
    def koltuk_bul(self, sira: str, numara: int):
        for koltuk in self.koltuklar:
            if koltuk.sira == sira and koltuk.numara == numara:
                return koltuk
        return None
class Film:
    def __init__(self, ad: str, süre: int, tur: str):
        self.ad = ad
        self.süre = süre
        self.tur = tur
    def __str__(self):
        return f"{self.ad} ({self.tur}, {self.süre} dk)"
class Seans:
    def __init__(self, film: Film, salon: Salon, zaman: str):
        self.film = film
        self.salon = salon
        self.zaman = zaman

    def __str__(self):
        return f"{self.film} - {self.salon.salon_adi} - {self.zaman}"
class Bilet:
    def __init__(self, seans: Seans, koltuk: Koltuk):
        self.seans = seans
        self.koltuk = koltuk

    def __str__(self):
        return f"{self.seans.film.ad} - {self.seans.salon.salon_adi} - {self.seans.zaman} - {self.koltuk}"
class SinemaSistemi:
    def __init__(self):
        self.seanslar = []

    def seans_ekle(self, seans: Seans):
        self.seanslar.append(seans)

    def seanslari_goster(self):
        for i, seans in enumerate(self.seanslar, start=1):
            print(f"{i}. {seans}")

    def seans_bul(self, index: int):
        if 0 < index <= len(self.seanslar):
            return self.seanslar[index - 1]
        return None

    def bilet_al(self, seans_index: int, sira: str, numara: int):
        seans = self.seans_bul(seans_index)
        if not seans:
            print("⚠️ Geçersiz seans seçimi.")
            return None
        koltuk = seans.salon.koltuk_bul(sira, numara)
        if not koltuk:
            print("⚠️ Geçersiz koltuk seçimi.")
            return None
        if koltuk.is_rezerve:
            print("⚠️ Bu koltuk zaten rezerve edilmiş.")
            return None
        koltuk.rezerve_et()
        bilet = Bilet(seans, koltuk)
        return bilet

    def biletleri_goster(self, biletler: list):
        if not biletler:
            print("Henüz alınmış bilet yok.")
            return
        for i, bilet in enumerate(biletler, start=1):
            print(f"{i}. {bilet}")      
class main:
    def __init__(self):
        self.sinema_sistemi = SinemaSistemi()
        self.biletler = []

    def menu(self):
        while True:
            print("1. Seansları Göster")
            print("2. Bilet Al")
            print("3. Biletleri Göster")
            print("4. Çıkış")
            secim = input("Seçiminiz: ")
            if secim == "1":
                self.sinema_sistemi.seanslari_goster()
            elif secim == "2":
                seans_index = int(input("Seans numarası: "))
                sira = input("Koltuk sırası: ")
                numara = int(input("Koltuk numarası: "))
                bilet = self.sinema_sistemi.bilet_al(seans_index, sira, numara)
                if bilet:
                    self.biletler.append(bilet)
            elif secim == "3":
                self.sinema_sistemi.biletleri_goster(self.biletler)
            elif secim == "4":
                break
            else:
                print("Geçersiz seçim.")

if __name__ == "__main__":
    app = main()
    app.menu()