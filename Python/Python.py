a=int(input("BİRİNCİ SAYIYI GİRİNİZ \n"))
b=int(input("İKİNCİ SAYIYI GİRİNİZ \n"))
print("1=TOPLAMA")
print("2=ÇIKARMA")
print("3=ÇARPMA")
print("4=BÖLME")
işlem=input("İŞLEM GİRİNİZ \n")
if işlem=="1":
    print(a+b)
elif işlem=="2":
    print(a-b)
elif işlem=="3":
    print(a*b)
elif işlem=="4":
    if b!=0:
        print(a/b)
    else:
        print("HATA")
else:
    print("HATA")
