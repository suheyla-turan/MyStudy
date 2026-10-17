import datetime
import json
print("Başlangıç bakiyesini giriniz:")
bakiye = float(input())
def add_harcama(bakiye):
    print("Harcama miktarını giriniz:")
    harcama = float(input())
    if harcama > bakiye:
        print("Yetersiz bakiye.")
        return bakiye, None
    bakiye -= harcama
    harcama_gecmisi = datetime.datetime.now()
    print("Güncel bakiye:", bakiye)
    with open("harcama_gecmisi.json", "a") as f:
        json.dump({"miktar": harcama, "tarih": harcama_gecmisi.isoformat()}, f)
        f.write("\n")
    return bakiye, harcama_gecmisi
while True:
 print("""İşlem seçiniz:
 1. Harcama Ekle
 2. Para Yatırma
 3. Bakiye Görüntüleme 
 4. Harcama geçmişi görüntüleme
 5. Para yatırma geçmişi görüntüleme 
 6. Çıkkış """)
 x = int(input())
 if x == 1:
    bakiye, harcama_gecmisi = add_harcama(bakiye)
    if harcama_gecmisi is None:
        continue
    continue
 elif x == 2:
    print("Yatırmak istediğiniz miktarı giriniz:")
    yatirma = float(input())
    bakiye += yatirma
    para_yatirma_gecmisi = datetime.datetime.now()
    with open("para_yatirma_gecmisi.json", "a") as f:
        json.dump({"miktar": yatirma, "tarih": para_yatirma_gecmisi.isoformat()}, f)
        f.write("\n")
    print("Güncel bakiye:", bakiye)
    continue
 elif x == 3:
    print("Güncel bakiye:", bakiye)
    continue
 elif x == 4:
    try:
        with open("harcama_gecmisi.json", "r") as f:
            harcamalar = [json.loads(line) for line in f]
        print("Harcama geçmişi:", harcamalar)
    except FileNotFoundError:
        print("Harcama geçmişi bulunamadı.")
    continue
 elif x == 5:
    try:
        with open("para_yatirma_gecmisi.json", "r") as f:
            yatirmalar = [json.loads(line) for line in f]
        print("Para yatırma geçmişi:", yatirmalar)
    except FileNotFoundError:
        print("Para yatırma geçmişi bulunamadı.")
    continue
 elif x == 6:
    print("Çıkış yapılıyor.")
    break
