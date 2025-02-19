print("Faktöriyel Hesaplama")
print("Programdan çıkmak için 'q' ya basınız")
while True:
    sayı = int(input("Faktöriyeli hesaplamak istediğiniz sayıyı giriniz: \n"))
    if sayı=="q":
        print("Programdan çıkış yapılıyor")
    else:
        faktöriyel = 1
        for i in range(1,sayı+1):
            faktöriyel*=i
        print("{} sayısının faktöriyeli=".format(sayı),faktöriyel)