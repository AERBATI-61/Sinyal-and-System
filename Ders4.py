belge = ("merhaba", "python", "ogrenenler", "merhaba")
sozcuk_sayac = dict() #{} #bos sozluk
#for sozcuk in belge: # for(int=0;i<len(sozcuk_sayac);i++) sozcuk = belge[i]
for i in range(len(belge)):
  sozcuk = belge[i]
  if sozcuk in sozcuk_sayac:
    sozcuk_sayac[sozcuk] += 1
  else:
    sozcuk_sayac[sozcuk] = 1
print( sozcuk_sayac)


sozcuk_sayac = dict() #{}
for sozcuk in belge:
  try:
    sozcuk_sayac[sozcuk] += 1
  except KeyError:
    sozcuk_sayac[sozcuk] = 1



from collections import defaultdict

sozcuk_sayac = defaultdict(int) # key=? value type int

#Key yoksa otomatik olarak başlangıcta sıfır değerini atar
for sozcuk in belge:
   sozcuk_sayac[sozcuk] += 1

print(sozcuk_sayac.keys())
print(sozcuk_sayac.values())
print(sozcuk_sayac.items())

sozluk_liste = defaultdict(list)
sozluk_liste[2].append(1)
print(sozluk_liste)
sozluk_liste[2].append("deneme")
print(sozluk_liste)
sozluk_liste["2"].append(3)
print(sozluk_liste)
sozluk_liste["2"].insert(0,0)
print(sozluk_liste)



"""   inanir misiniz? Hic Anlamadim.
def fonk():
  return [0, 0]
#sozluk_cift = defaultdict(fonk)#lambda: [0, 0])
#anonim fonksiyon lambda ifadesi
sozluk_cift = defaultdict(lambda :[0, 0])
sozluk_cift[2][0] = 1
sozluk_cift[3][0] = 0
sozluk_cift[3][1] = 20
#sozluk_cift[3]
sozluk_cift["yeni_anahtar"]
print(sozluk_cift)
"""

sozluk_string = defaultdict(str) #string
sozluk_string[0] = "pyhton"
print(sozluk_string)






# from collections import defaultdict
from collections import Counter
sozcuk_sayac = Counter(belge) # defaultdict(int) dongu kullanmaya gerek yok
print(sozcuk_sayac)

for degeri, kac_tane in sozcuk_sayac.most_common(1): # 1 degince sadece 1 tane en yaygin ndeger bilgisini veriyor.
  print(degeri, kac_tane)

"""
set
"""
liste = [1,2,2,3,3,3]
kume = set(liste)
print(kume)

liste = list(kume)
print(liste)

"""
if
"""
if 1 > 2:
  ileti="keşke 1 2'den byük olsa"
elif 1 > 3:
  ileti="elif 'else if' yerine gecer"
else:
  ileti="hicbir sart gecerli degilse"
print(ileti)

"""
loop
"""
x = 0
while x < 10:
  print(f"{x} 10'dan kucuktur")
  x += 1

for x in range(10): #[0,1,2,3,4,5,6,7,8,9]
  print(f"{x} 10'dan kucuktur")




'''
True and False
'''
bir_iki_den_kucuk = 1 < 2
print(bir_iki_den_kucuk)

dogru_esit_yanlis = True == False  # bool
print(dogru_esit_yanlis)

x = None  # NULL
assert x == None, "Bu pythonic bir yol degil"
assert x is None, "Bu pythonic bir yol"
print(x)

str = "Python"  # str[0] = 'P'
if str is not None:
    ilk_karakter = str[0]
else:
    ilk_karakter = ""

ilk_karakter = str and str[0]
print(ilk_karakter)

guvenli_x = x or 0
print(guvenli_x)
guvenli_x = x if x is not None else 0

if x is not None:
    guvenli_x = x
else:
    guvenli_x = 0
print(guvenli_x)

# True
print(all([True, 1, (2)]))  # list
print(all([]))  # ya da boş ise
print(any([True, 1, {}]))

# False
print(all([True, 1, []]))
print(any([]))

'''
sort
'''
x = [4, -10, -2, 3]
y = sorted(x, reverse=False) # reverse=True buyukten kucuge dogru siraliyor
print(x, y)
x.sort()
print(x, y)

x = sorted(x, key=abs, reverse=True) # abs mutlak degerini alarak siralama islemini yapiyor.
print(x)





'''
list comprehensions
'''
cift_sayilar_deneme = [x for x in range(5) if x % 2 == 0]  # 0..4
cift_sayilar_deneme = iter(cift_sayilar_deneme)
# print(len(cift_sayilar_deneme))


print(next(cift_sayilar_deneme))
print(next(cift_sayilar_deneme))
print(next(cift_sayilar_deneme))
# print(next(cift_sayilar_deneme))
# print(next(cift_sayilar_deneme))
# print(next(cift_sayilar_deneme))



liste = []
liste = list()
kume = set()

sayilarin_karesi_deneme = list(x ** 2 for x in range(5))
sayilarin_karesi_deneme = [x ** 2 for x in range(-5, 5)]
print(sayilarin_karesi_deneme)
sayilarin_karesi_deneme = set(x ** 2 for x in range(-5, 5))
print(sayilarin_karesi_deneme)

cift_sayilar = [x for x in range(5) if x % 2 == 0]
print(cift_sayilar)




"""
def fonk(x):
  return x % 2 == 0
cift_sayilar1 = list(filter(fonk, range(5)))
"""



cift_sayilar1 = list(filter(lambda x: x % 2 == 0, range(5)))
print(cift_sayilar1)

cift_sayilar2 = []
for x in range(5):
    if x % 2 == 0:
        cift_sayilar2.append(x)
print(cift_sayilar2)





karesi = [x * x for x in range(5)]
print(karesi)

karesi1 = []
for x in range(5):
    karesi1.append(x * x)
print(karesi1)

karesi2 = list(map(lambda x: x ** 2, range(5)))
print(karesi2)

x = iter(range(5))
print("x=", next(x))
print(f"x={next(x)}")

sayi = 9
print("sayi=", sayi, "sayisina esittir")
print(f"sayi={sayi} sayisina esittir")

cift_karesi = [x * x for x in cift_sayilar]
print(cift_karesi)





karesi_sozluk = {}
karesi_sozluk = dict()

karesi_sozluk = {x: x * x for x in range(5)}
print(karesi_sozluk)

karesi_set = {x * x for x in [-2, -1, 0, 1, 2]}
print(karesi_set)

ciftler = [(x, y)
           for x in range(10)
           for y in range(10)
           ]
print(ciftler)

artmis_ciftler = [(x, y)
                  for x in range(10)
                  for y in range(x + 1, 10)]
print(artmis_ciftler)

'''
assert
'''
assert 1 + 1 == 2
assert 1 + 1 == 2, "1+1 2'ye esit olmalı, ama degil"


def enkucuk_eleman(xs):
    return min(xs)
assert enkucuk_eleman([12, 23, 1, 56]) == 1
assert enkucuk_eleman([12, -23, 1, 56]) == -23


def enkucuk_eleman_diger(xs):
    assert xs, "bos liste en kucuk elemana sahip olamaz"
    return min(xs)
enkucuk_eleman_diger(None)









# from collections import defaultdict
# from collections import Counter
# map()
# iter()
# assert
# lambda











