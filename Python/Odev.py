import numpy as np

# 0-50 arasında 100 adet tam sayı oluştur
veriler = np.random.randint(0, 51, size=85)

# Verileri serilere ayırmak için aralıklar belirle
araliklar = [0, 10, 20, 30, 40, 50]
seriler = {f"{araliklar[i]}-{araliklar[i+1]}": [] for i in range(len(araliklar) - 1)}

# Verileri uygun serilere yerleştir
for veri in veriler:
    for i in range(len(araliklar) - 1):
        if araliklar[i] <= veri < araliklar[i + 1]:
            seriler[f"{araliklar[i]}-{araliklar[i+1]}"].append(veri)

# Serileri simetrik dağılıma yakınlaştırmak için her serideki veri sayısını eşitle
min_veri_sayisi = min(len(v) for v in seriler.values())
for key in seriler:
    seriler[key] = seriler[key][:min_veri_sayisi]

# Sonuçları yazdır
print("Serilere Ayrılmış ve Simetriye Yakınlaştırılmış Veriler:")
for key, values in seriler.items():
    print(f"{key}: {values}")
