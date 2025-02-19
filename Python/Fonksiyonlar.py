def hesapMakinesi():
    i = int(input("""işlem Seçiniz
    1->Toplama
    2->Çıkarma
    3->Çarpma
    4->Bölme \n
    """))
    a = int(input("Birinci sayıyı giriniz \n"))
    b = int(input("İkinci sayıyı giriniz \n"))
    if i==1:
        print(a+b)
        return a+b
    elif i==2:
        print(a-b)
        return a-b
    elif i==3:
         print(a*b)
         return a*b
    elif i==4:
        if b!=0:
            print(a/b)
            return a/b
        else:
            print("BÖLEN SIFIR OLAMAZ")
    else:
        print("HATALI GİRİŞ")

def faktoriyel(sayi=0):
    faktoriyel=1
    if(sayi==0 or sayi==1):
        print("{} sayısınının faktöriyeli=".format(sayi),faktoriyel)
    else:
        temp=sayi
        while (temp>=1):
            faktoriyel*=temp
            temp-=1
        print("{} sayısının faktöriyeli=".format(sayi),faktoriyel)
    return faktoriyel

#print(faktoriyel(hesapMakinesi()))
#print(faktoriyel())

def bilgiler(ad="Bilgi Yok",soyad="Bilgi Yok",numara="Bilgi Yok"):
    print("Ad:",ad,"Soyad:",soyad,"numara:",numara,sep="\n")
#print(bilgiler("Süheyla","Turan",1))
#print("süheyla","Melike","Turan",sep="\n")

def toplama(*a):
    toplam=0
    for i in a:
        toplam+=i
    print(toplam)
    return toplam
#print(toplama(1,2,3,4,5,6,7,8,9))

d=5
def fonksiyon():
    global d
    d=3
    return d
#print(fonksiyon())
#print(d)

#lambda
toplama=lambda x,y,z: x+y+z
#print(toplama(1,2,3))

tersçevir=lambda s:s[::-1]
print(tersçevir("pythonproglamlama"))