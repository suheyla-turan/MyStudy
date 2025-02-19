#Değiştirilemezler
#ver yapısı
t=("apple","banana","")
print(type(t))
#t[0:2]=("apple","banana")



#Sözlükler
sozluk={"Vİze":30,"Final": 70, "Kısa sınav":90}
print(sozluk)
print(sozluk ["Kısa sınav"])
sozluk["Final"] = 100
print(sozluk)
sozluk["değelendirme"]=90
print(sozluk)
liste=("apple","banana")
sozluk[3]=liste
print(sozluk)


#Setler (Kümeler)
#Tekrar edilemezler
l=[1,2,3,4,5,6,7,8,9]
s = set(l)
print(dir(s))
set1 = {[1,2,3]}
set2 = {[4,5,6]}
set1.intersection(set2)#kesişişm
set2.intersection(set1)
