import numpy as np
import pandas as pd

# Simetrik olacak şekilde veri oluşturma
np.random.seed(42)  # Tekrar üretilebilirlik için sabit tohum
data_size = 60

# Yolculuk ve yakıt için simetrik veri üretimi
journey = np.random.randint(50, 500, size=data_size)  # Yolculuk mesafeleri
fuel = np.random.randint(5, 50, size=data_size)  # Yakıt tüketimi

# Veriyi bir DataFrame'e yerleştirme
data = pd.DataFrame({
    "Yolculuk (km)": journey,
    "Yakıt (lt)": fuel
})

# Tabloyu ve dosyayı kaydetme
file_path = "yolculuk_yakit_verisi.csv"  # Çalışma dizinine kaydeder
data.to_csv(file_path, index=False)

print("Veriler kaydedildi:", file_path)
print(data)
