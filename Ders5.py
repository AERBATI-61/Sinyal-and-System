'''
object oriented programming
'''


class SaymaTiklama:
    """ Tıklamayı sayma işlemi """

    # constructor
    def __init__(self, sayac=0):  # C++'da this -> self
        self.sayac = sayac  # field

    # toString() #Java'da
    def __repr__(self):
        return f"SaymaTiklama(sayac={self.sayac})"

    def tikla(self, tikla_sayi=1):
        self.sayac += tikla_sayi

    def oku(self):
        return self.sayac

    def sifirla(self):
        self.sayac = 0


tiklayici = SaymaTiklama()
print(tiklayici)

tiklayici1 = SaymaTiklama(100)
tiklayici2 = SaymaTiklama(sayac=100)
print(tiklayici1)
tiklayici1.tikla()
print(tiklayici1.oku())
tiklayici1.sifirla()
print(tiklayici1.oku())
assert tiklayici1.oku() == 0, "sayac 0 degerini alir"


# is a
class SifirlamaIptalTiklama(SaymaTiklama):
    def sifirla(self):  # overriding
        pass


tiklayici3 = SifirlamaIptalTiklama()
tiklayici3.tikla()
assert tiklayici3.oku() == 1
tiklayici3.sifirla()
assert tiklayici3.oku() == 1, "sifirla fonksiyonu islem yapmaz"

'''
iterable and generator
'''
for k in [0, 1, 2, 3, 4]:
    print(k)

x = iter([0, 1, 2, 3, 4])
while True:
    try:
        k = next(x)
    except StopIteration:  # try catch()
        break
    print(k)

uretici = [k for k in range(5)]
for k in uretici:
    print(k)


def uretici_aralik(n):
    i = 0
    while i < n:
        yield i
        i += 1


for k in uretici_aralik(5):
    print(f"k: {k}")

k = uretici_aralik(5)
print(iter(k) is k)
print(f"k: {next(k)}")
print(f"k: {next(k)}")
print(f"k: {next(k)}")
print(f"k: {next(k)}")
print(f"k: {next(k)}")


def dogal_sayilar():
    """geri donus degeri 1,2,3,...sonsuz"""
    n = 1
    while True:
        yield n
        n += 1


# for k in dogal_sayilar():
#  print(k)

yirmi_altinda_cift = (i for i in uretici_aralik(20) if i % 2 == 0)
for k in yirmi_altinda_cift:
    print(k)

veri = dogal_sayilar()
ciftler = (x for x in veri if x % 2 == 0)
cift_kareler = (x ** 2 for x in ciftler)
cift_kareler_alti_ile_kalan = (x for x in cift_kareler if x % 10 == 6)

k = next(cift_kareler_alti_ile_kalan)
print(f"k: {k}")
k = next(cift_kareler_alti_ile_kalan)
print(f"k: {k}")

adlar = ["Ali", "Ayse", "Baris", "Derya"]

for k in range(len(adlar)):
    print(f"ad {k} {adlar[k]}")

k = 0
for ad in adlar:
    print(f"ad {k} {adlar[k]}")
    k += 1

for k, ad in enumerate(adlar):
    print(f"ad {k} {adlar[k]}")

'''
random
'''
import random

random.seed(10) # baslangicta ne urettiyse bidahakindede aynisini uretiyor.
print(random.random())
random.seed(10)
print(random.random())

random.seed(10)
dort_uniform_sayi = [random.random() for _ in range(4)]
print(dort_uniform_sayi)

print(random.randrange(10))
print(random.randrange(10, 20))

ona_kadar_sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(ona_kadar_sayilar)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] karistiriyor.
print(ona_kadar_sayilar)

en_iyi_arkadas = random.choice(["Ali", "Ayse", "Hasan"]) # choice secme islemini yapiyor.
print(en_iyi_arkadas)

cekilis_rakamlar = range(60)
kazanan_rakamlar = random.sample(cekilis_rakamlar, 6) # sample ornek alma islemini yapiyor. # ayni rakam birden fazla uretilemez
print(kazanan_rakamlar)

tekrarli_dort_sayi = [random.choice(range(10)) for _ in range(4)] # ayni rakam birden fazla uretilebilir
print(tekrarli_dort_sayi)








#hoca girmedi
import re  # duzenli ifade

re_ornekler = [
    not re.match("o", "pyhton"),
    re.search("o", "python"),
    not re.search("a", "python"),
    3 == len(re.split("[rb]", "araba")),  # split stringi diziye donusturur
    "P_T_O_" == re.sub("[HYN]", "_", "PYTHON")
]
dizi = re.split("[rb]", "araba")
print(dizi[0])
print(dizi[1])
print(dizi[2])

print(not re.match("o", "pyhton"))
print(re.search("o", "python"))
print(not re.search("a", "python"))
print(len(re.split("[rb]", "araba")))
print(re.sub("[YHN]", "_", "PYTHON"))
print(re.split("[rb]", "araba"))

assert all(re_ornekler), "butun ornekler dogru olmali"








'''
zip and unpack
'''
liste1 = ['a', 'b', 'c']
liste2 = [1, 2, 3]
ciftler = [cift for cift in zip(liste1, liste2)]
print(ciftler)

ciftler = [('a', 1), ('b', 2), ('c', 3)]

harfler, sayilar = zip(*ciftler)
print(harfler, sayilar)
harfler, sayilar = zip(*[('a', 1), ('b', 2), ('c', 3)])     # list oldugu icin * kullaniliyor
harfler, sayilar = zip(('a', 1), ('b', 2), ('c', 3))

print(harfler, sayilar)









def topla(a: int, b: int) -> int:  # -> return tamsayi
    return a + b


print(topla(2, 3))
print(topla("Ali ", "CAN"))











# enumerate
# random.seed(10)
# shuffle
# choice
# sample

























# def topla(a, b):
#     return a + b
#
#
# topla(1, 2)
#
# try:
#     topla([1, 2])
# except TypeError:
#     print("iki girdinin toplanmasi beklenir")
# topla(*[1, 2])
#
# '''
# args and kwargs
# '''
#
#
# def ikikatci(f):
#     def g(x):
#         return 2 * f(x)
#
#     return g
#
#
# def f1(x):
#     return x + 1
#
#
# g = ikikatci(f1)
#
# assert g(3) == 8, "(3+1)*2 8'e esit olmalı"
# assert g(-1) == 0, "(-1+1)*2 0'e esit olmalı"
#
#
# def f2(x, y):
#     return x + y
#
#
# g = ikikatci(f2)
# try:
#     g(1, 2)
# except TypeError:
#     print("tanimlandigi gibi, g yalnizca tek parametre alir")
#
#
# def sihirli(*args, **kwargs):
#     print("isimsiz args:", args)
#     print("anahtar args:", kwargs)  # keyword
#
#
# demet = tuple()
# demet = 1, 2, 3
# print("demet=", demet)
#
# sihirli(1, 2, 4, 5, 67, anahtar="sozcuk", anahtar2="sozcuk2")
#
#
# def diger_sihirli_yol(x, y, z):
#     return x + y + z
#
#
# x_y_liste = [1, 2]  # unzip
# z_sozluk = {"z": 3}
# assert diger_sihirli_yol(*x_y_liste, **z_sozluk) == 6, "1+2+3 6'ya esit olmali"
#
#
# def ikikatci_duzeltilmis(f):
#     def g(*args, **kwargs):
#         return 2 * f(*args, **kwargs)
#
#     return g
#
#
# g = ikikatci_duzeltilmis(f2)
# assert g(1, 2) == 6, 'ikikatci simdi calisiyor olmali'
#
# '''
# type and annotations
# '''
#
#
# def topla(a, b):
#     return a + b
#
#
# assert topla(10, 5) == 15, "+ sayilar icin gecerli"
# assert topla([1, 2], [3]) == [1, 2, 3], "+ listeler icin gecerli"
# assert topla("merhaba ", "pyhton") == "merhaba pyhton", "+stringler icin gecerli"
#
# try:
#     topla(10, "bes")
# except TypeError:
#     print("tamsayi ile string toplanamaz")
#
# print(10 * "ali")




# from typing import List
#
#
# def toplam(xs: List[float]) -> float:
#     return sum(xs)
#
#
# x: int = 5
#
# degerler = []
# en_iyisi = None  # NULL
#
# from typing import Dict, Iterable, Tuple
#
# sayac: Dict[str, int] = {'veri': 1, 'bilim': 2}
# print(sayac)
#
# tembel = True
# if tembel:
#     ciftler: Iterable[int] = (x for x in range(10) if x % 2 == 0)
#     print(ciftler)
# else:
#     ciftler = (0, 2, 4, 6, 8)
# print(next(ciftler), next(ciftler))
#
# uclu: Tuple[int, float, int] = (10, 2.3, 5)
# print(uclu)
#
# from typing import Callable
#
#
# def ikikere(tekrarlayici: Callable[[str, int], str], s: str) -> str:
#     return tekrarlayici(s, 2)
#
#
# def komut_tekrarlayici(s: str, n: int) -> str:
#     n_kopya = [s for _ in range(n)]
#     return ', '.join(n_kopya)
#
#
# assert ikikere(komut_tekrarlayici, "tip bildirimi") == "tip bildirimi, tip bildirimi"
#
# Sayi = int
# Sayilar = List[Sayi]
#
#
# def toplam(xs: List[int]) -> int:
#     return sum(xs)
#
#
# def toplam(xs: Sayilar) -> Sayi:
#     return sum(xs)
#
#
# xs: List[Sayi] = [1, 2]
# print(toplam(xs))