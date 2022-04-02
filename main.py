# ************************ Birinci Hafta **************************************
# import matplotlib.pyplot as plt          #cizim islemi icin
# import numpy as np
# import sigsys
# n = np.arange(-5, 10)
# x = sigsys.drect(n, N=3)                     # Ayrik Dikdortgen cizdirmek icin
# plt.figure(1)                            # Sekil almis oluyor
# plt.title("Ayrik Zamanli N = 3 Ornekli Dikdortgen isareti")
# plt.stem(n, x)                           # Ayrik cizdirmek islemini yapiyor
# plt.show()                               # Grafik gostermek icin



# import matplotlib.pyplot as plt
# from numpy import arange
# from sigsys import tri
# t = arange(-1, 5, .01)
# x = tri(t, 1.0)                             # Ucgen Cizme islemi
# plt.figure(6)
# plt.title("Surekli Zamanli Ucgen isareti")
# plt.plot(t, x)                              # Surekli cizdirme islemini yapiyor
# plt.show()


# ************************ Ikinci Hafta **************************************

for i in [1, 2, 3]:
    for j in [1, 2, 3]:
        print(i, j)

a = 1 +\
    2
print(a)

b = (1 +
     2)
print(b)

c = [1 +
     2]
print(c)

d = {1 +
     2}
print(d, "\n")


match = 10
print(match)
from re import *
print(match, "\n")


f = compile("[0-9]")
print(f.search("f icinde herhangi bir 5 sayisi var mi?"))


from collections import defaultdict, Counter
bakalim = defaultdict(int)
sayalim = Counter()
print(bakalim, sayalim)




def fonk1():
    print("Merhaba")

def fonk2(x):
    return x*x
print(fonk2(3))



def fonk3(x):
    return x*x
def fonk4(f):
    return f(3)
print(fonk4(fonk3))
print(fonk4(lambda x: x**2))


g = (lambda x: x**2)
print(g(10))


def fonk5(x=5):
    return x**2
print(fonk5())



string = "Arafat " \
         "Rahile " \
         "Meryem " \
         "Emin"
print(string)




try:
    print(0/0)
except ZeroDivisionError:
    print("Can not divide by zero")
print("/0")












