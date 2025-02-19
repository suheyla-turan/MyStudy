print(""""***ATM MAKİNESİNE HOŞGELDİNİZ***
İŞLEMLER:
1-> Bakiye Sorgulama
2-> Para Yatırma
3-> Para Çekme
Programdan çıkmak için 'q' ya basın.
 """)
bakiye= 100000
while True:
    işlem=input("İŞLEMİ SEÇİNİZ")
    if (işlem=="q"):
        print("ÇIKIŞ YAPILMIŞTIR")
        break
    elif (işlem=="1"):
        print("Bakiyeniz {} tl dir." .format(bakiye))
    elif (işlem=="2"):
        miktar=int(input("Miktarı giriniz:"))
        bakiye+=miktar
    elif (işlem=="3"):
        miktar = int(input("Miktarı giriniz:"))
        if miktar>bakiye:
            print("Bakiyeniz yetersiz")
            continue
        bakiye-=miktar
    else:print("GEÇERSİZ İŞLEM")