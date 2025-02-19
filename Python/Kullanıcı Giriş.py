print("***** KULLANICI GİRİŞİ *****")
kullancı_adı="Murat"
parola="12345"
girişhakkı=3
while True:
    kullanıcıAdı=input("KULLANICI ADI: \n")
    parolA=input("PAROLA: \n")
    if (kullanıcıAdı==kullancı_adı and parolA!=parola):
        print("YANLIŞ PAROLA")
        girişhakkı-=1
    elif (kullanıcıAdı!=kullancı_adı and parolA!=parola):
        print("KULLANICI ADI YANLIŞ")
        girişhakkı-=1
    elif (kullanıcıAdı!=kullancı_adı and parolA==parola):
        print("KULLANICI ADI YANLIŞ")
        girişhakkı-=1
    else:
        print("HOŞGELDİNİZ")
        break
    if(girişhakkı==0):
        print("GİRİŞ HAKKINIZ BİTTİ")
        break