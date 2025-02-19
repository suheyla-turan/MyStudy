yarıçap=int(input("Dairenin yarıçapını giriniz"))
print("Yapmak istediğiiz işlemi seçiniz "
      "1=Daire alan 2=Daire çevre")
işlem=int(input("İşlem:"))
if(işlem==1):
    Alan=yarıçap*yarıçap*3
    print("Alan=",Alan)
elif(işlem==2):
    çevre=2*3*yarıçap
    print("Çevre=",çevre)
else:
    print("Hatalı giriş")