liste=[1,2,3,4,5,6,7,8,9]
liste[1]=10
print(liste)
del liste[3]
print(liste)
dir (liste)  #
print(liste)
liste.append(5) #eklemek
liste.remove(9) #silmek
liste.insert(0,3) # hangi elemanına eklemek istersen
len(liste) # eleman sayısı
liste.insert(len(liste),6)
print(liste)
liste.pop(0) #o indeksi silmek için kullanılır.
print(liste)
print(liste.count(2)) #o elemandan kaç tane olduğunu bulur
liste2=liste.copy();  #listeyi kopyalamak için kullanılır
print(liste2)
liste.extend(["a","b","c"]) #listeleri birleştirmek için kullanılır
print(liste)
#liste.insert("3") #o elemanın kaçıncı indeste olduğunu verir
liste.reverse() #liste elemanlarını terse çevirir
liste2.sort() #liste elemanlarını sıralar
print(liste2)