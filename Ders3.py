"""
string
"""
#//C'de tek açıklama
"""
/*
C'de birden fazla satır
*/
"""

adi = "Ali"
soyadi = "Veli"

tam_adi = adi+" "+soyadi
tam_adi2 = "{0} {1}".format(adi, soyadi)
tam_adi3 = f"{adi} {soyadi}"
print(tam_adi)
print(tam_adi2)
print(tam_adi3)

"""
exception
"""
#sayi = 6/0

try:
  sayi = 6/0
  print("Normal durum")
except ZeroDivisionError: #tipi
  print("Sorun")
finally:
  print("Her zaman calisir")

"""
list
"""
#vektör
bos_liste = []
tamsayi_liste = [1, 2, 3] # okuma yazma
karisik_liste = ["string", 0.1, True] #Byuk harf True ve False
icice_liste = [tamsayi_liste, karisik_liste, bos_liste, [1,2]]
#print("liste",icice_liste)
liste_uzunluk = len(tamsayi_liste) #uzunluk 3
liste_toplam = sum(tamsayi_liste) #toplama 6
#->   0   1   2  3   -2 -1<-
x = [10, 11, 22, 33] #x[3]
ilk_eleman = x[0]
ikinci_eleman = x[1]
son_eleman = x[-1]

try:
  x[9] = 89
except IndexError:
  print("Hata")

sondan_ikinci = x[-2]
print(sondan_ikinci)

basla = 1 # dahil
sonla = 4 # dahil degil
print(x[basla : sonla : 2])
sonuc = 1 in x
print(sonuc)
x.append(-3) # dizinin sonuna ekleme
print(x[:])
x.insert(1,45)
print(x[:])
x.extend([11,22]) # aynı dizinin sonuna ekler
print(x[:])
x.remove(11)
y = x + [11, 22] # başka bir dizi
print(x[:])
print(y)
print(y[:])

'''
import numpy as np
x = np.array([1, 2])
y = x * np.array([3, 4])
print(y)

y = x.copy()
y[0] = 98
print(x)
print(y)
'''

x = [0, 1, 2, 3] #ayırma
_, _, _, w = x #tuple demet
print(w)

#referans kopyasını oluşturmaz
y = x
y[0] = 890
print(y)
print(x)

#y = x.copy() # numpy'da gecerlidir
y = x[:] # numpy'da gecerli degildir
y[0] = 890
print(y)
print(x)

"""
tuple
"""
demet = (1, 2, 3) #okuma
demet1 = 1, 2, 3
print(demet)
print(demet1)
print(demet[0])

try:
  demet[0] = 3
except TypeError:
  print("Hata")
print(demet[0])

def topla_ve_carp(x, y):
  return x + y, x * y
sonuc = topla_ve_carp(9,8)
print(sonuc)

x, y = (1, 2)
x, y = y, x
print(x, y)

ornek = [1, 1, 9]  #liste
ornek1 = (1, 1, 9) #demet
ornek2 = {1, 1, 9} #kume tekrarlama olmuyo
ornek2.add(99)
ornek2.add(93)
bos_demet = tuple()#() #tuple
bos_liste = list() #[] # list()
bos_kume = set()
bos_sozluk = {} # dict()
print(ornek)
print(ornek1)
print(ornek2)

"""
dictionary
"""
sozluk = {} # pythonic
sozluk1 = dict() # daha az pythonic
          #key (unique) value
sozluk2 = {"adi":"Ayse", "adi":"Hasan","adi":"Ali", "soyadi":"CAN"}
print(sozluk2)
sozluk2["adi"] = "Ayse"
print(sozluk2)

adi_ogren = "adi" in sozluk2
print(adi_ogren)
adi_ogren = sozluk2.get("adi",0) # adi denen key'in degeri yoksa 0 deger ataniyor.
print(adi_ogren)

sozluk2["numara"] = 12345

print(len(sozluk2))

print(sozluk2.keys())
print(sozluk2.values())
print(sozluk2.items())

















