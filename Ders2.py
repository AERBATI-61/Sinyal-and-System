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
    print("Can not divide by zero \\0")
finally:
    print("Her zaman calisiyorum ulan")



name = "Arafat"
surname = "Emin"
print(name + " " + surname)
print("{0} {1}".format(name, surname))
print(f"{name} {surname}")



bos_list = []
tam_sayi = [1, 2, 3]
karisik_liste = ["Arafat", 1, -1, True, False]
icice_liste = [tam_sayi, karisik_liste, bos_list, [10, 20]]
print(icice_liste)
print(len(icice_liste))
print(sum(tam_sayi))
print(icice_liste[-1])
print(icice_liste[0])

try:
    tam_sayi[3] = 4
except IndexError:
    print("Hata")







