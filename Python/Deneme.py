k = 3
l = 6
m = 9
print(m ** 0.5)#kök alma
a= "süheyla"
print(a[-7])
print(2, 'Hello', 6)
print("merhaba\n" "Süheyla\t  melike" )


# type fonksiynu verilen değerini türünü belirtmek için kullanılan fonkiyondur
print(type(56))
# sep= fonksiyonu veriler arasında ne konulmak istediğini belirtmek için kullanılır
print(1,2,3,4,5,6,7,8,9,0, sep="\n")
print(*"süheyla", sep="/")
print(*"TBMM", sep=".")

# formatlama işlemi
a=3
b=4
print("{}+{}={}" .format(a,b,a+b))

# ondalılklı sayının istenilen kdarını alma
x=7.123456789
print("{:.2f}".format(x))
liste=["hello",1,"world",2,0]
print(liste)
print(len(liste))

# liste veri tipleri
print(list("merhaba"))

# geriye doğru yazdırma
liste=[0,1,2,3,4,5,6,7,8,9,]
print(liste[: : -1])

# Liste toplama
liste1=[1,2,3]
liste2=[4,5,6]
liste3=liste1+liste2
print(liste3)

#listeeki eleman değiştirme
liste2[1]=10
print(liste1+liste2)
liste2[:2]=[8,9]
print(liste2)

# Listeye yeni eleman eklemek için kullanılan fonksiyondur
liste.append("Python")
print(liste)

#içine bir değer vermezsek son elemanı atıyor
#İçine başka bir değer girilirse o değerdeki elemanı atar
liste.pop(10)
print(liste)

# sort metodu sıralamak için kullanılır.
liste=[34,5,3,78,6,7,23,56,123,7]
liste.sort()
print(liste)
liste.sort(reverse=True)
print(liste)
liste=["php","python","java"]
liste.sort()
print(liste)

# liste içinde liste
liste=[[1,2],[3,4],[5,6]]
print(liste[1][1])

# demet veri tipleri
demet=(1,2,3,4,5,6,7,8,9,0)
print(type(demet))
print(demet[-1])
print(demet[::-1])

# count fonksiyonu
demet=(1,1,1,1,1,1,2,3,4,5,6,7)
print(demet.count(1))

#index fonksiyonu
demet=("python","Php","C","Java")
print(demet.index("python"))
print(demet)

# demetler değiştirilemez
#Uygulamada değiştirilmesini istemediğimiz şeyleri demetlerin içine yazabiliriz

# Sözlükler
sözlük={"bir":1,"iki":2,"üç":3,"dört":4}
print(type(sözlük))
print(sözlük["bir"])

#sözlüğe eleman ekleme
sözlük["beş"]=5
print(sözlük)

sözlük1={"bir":[1,2,3,4],"iki":[5,6,7,8],"üç":10}
print(sözlük1["bir"][1])
sözlük1["üç"]=15
print(sözlük1)
sözlük1["üç"]+=10
print(sözlük1)

# iç içe sözlükler
sözlük2={"sayılar":{"bir":1,"iki":2,"üç":3},"meyveler":{"kiraz":"yaz","portakal":"kış","erik":"yaz"}}
print(sözlük2["sayılar"])
print(sözlük2["meyveler"]["erik"])

#keys() metodu sözlüğün anahtarlarını bir liste olarak döner
print(sözlük.keys())

# values() metodu sözlüğün değerlerini bir liste olarak döndürür
print(sözlük.values())

# items() metodu sözlüğün anahtar ve değerlerini bir liste içinde demet olarak döner
print(sözlük.items())

#Kullanıcıdan girdi alma
#a=input("Lütfen bir sayı giriniz" "\n")
#print(a*3)

#Kullanıcıdan belirtmeden girdi alırsak bunu string cinsinden alıcaktır bunu engllemek için çrvirme yapılır
#a=int(input("LÜTFEN BİR SAYI GİRİNİZ:" "\n"))
#print(a*3)

#bool
# bool içine sayı yazdığımız zaman sadece sıfıra eşitse False döndürür diğer durumlarda True döndürür
a=True
print(type(a))

# Pythond'da bir değişkene değer atama işini daha sonra yapmak istiyorsak değere None değeri atanır.

#MANTIKSAL BAĞLAÇLAR
# and Operatörü
print(1<2 and 3<4)  #true
print(1<2 and 4<3)  #false
# or Operatörü
print(1<2 or 3<4)   #true
print(1<2 or 4<3)   #true
print(2<1 or 4<3)   #false
# not Operatörü
print(not 1==1)     #false
print(not 1==2)     #true

# in Operatörü
# elemanın bir stringin içinde olup olmadığını araştırmak için kullanılır
print(5 in [1,2,3,4])  #false

# for döngüsü
liste=[1,2,3,4,5,6,7]
toplam=0
for eleman in liste:
    toplam+=eleman
    print("Toplam:{} Eleman: {} ".format(toplam,eleman))
liste=[1,3,4,5,6,7,87,3,5,8,456,434,6,367,34]
for eleman in liste:
    if eleman%2==0:
        print(eleman)
demet={(1,2),(3,4),(5,6),(7,8),(9,0)}
for (i,j) in demet:
    print("{}  {} ".format(i,j))
"""
#while döngüsü
#rakam girme oyunu
sayi=int(input("GİRİŞ YAPINIZ \n"))
while 0<=sayi<10:
    print("RAKAM GİRDİN")
    sayi=int(input("GİRİŞ YAPINIZ  \n"))
print("KAYBETTİN")"""

#range fonksiyonu
print(*range(0,20))
print(*range(0,20,2))
# break içinde bulunduğu döngüyü sonlandırmak için kullanılır
# continue geri kalan işlemleri yapmadan bloğun başına döner

#List Comprehension
liste1=[1,2,3,4,5,6,7,8]
liste2=list()
for i in liste1:
    liste2.append(i)
print(liste2)
liste3=[i*3 for i in liste1]
print(liste3)
liste=[(1,2),(3,4),(5,6),(7,8)]
liste2=[i*j for i,j in liste]
print(liste2)

liste4=list()
for i in liste:
    for j in i:
        liste4.append(j)
print(liste4)

liste4=[x for i in liste for x in i]
print(liste4)

#FONKSİYONLAR
def selamla():
    print("MERHABA")
    print("NASILSINIZ?")
print(selamla())