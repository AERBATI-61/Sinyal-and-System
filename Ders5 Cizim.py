"""
from matplotlib import pyplot as plt
yillar = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
veriler = [300, 500, 1000, 1980, 4000, 8000, 10000]

print(len(yillar), len(veriler))

plt.figure(1)       # Sekil cizmek icin
plt.plot(yillar, veriler, color='blue', marker='x', linestyle='dotted') # plot: Surekli cizdirme islemini yapiyor
plt.title("Veriler")
plt.ylabel("Milyon $")
plt.show()
"""



"""
import numpy as np

z_a = 3 + 4j
z_b = -3 + 4j
# z_c = 3 + 4j
# z_d = 3 + 4j
genlik = np.abs(z_a)
aci = np.angle(z_a)
derece = np.angle(z_a, deg=True)

genlik = np.abs(z_b)
aci = np.angle(z_b)
derece = np.angle(z_b, deg=True)

z_c = 2*np.exp(1j*np.pi/3.0) # 1j = sqrt(-1)
print(z_c)

print(genlik)
print(aci)
print(derece)
"""





"""
import numpy as np
from matplotlib import pyplot as plt

plt.figure(1)
ax = plt.axes(projection='3d')                  # axes: 3 boyutlu iz dusumu yap
z = np.linspace(0, 15, 100)                     # 0-100 arasinda 15 deger al
x = np.cos(z)
y = np.sin(z)
ax.plot3D(x, y, z, 'blue')
ax.view_init(-125, 30)                          # bakilacak aciyi vermis oluyor
plt.show()
"""


"""
import numpy as np
from matplotlib import pyplot as plt

# Deterministik isaret
t = np.linspace(0, 5, 200)                     # 0-200 arasinda 5 deger al
x1 = 1.5 * np.cos(2 * np.pi * 1 * t + np.pi / 3)  # aci = pi/3.     wt = 2 * np.pi * 1 * t.   genlik = 1.5
plt.figure(1)
plt.plot(t, x1)
plt.show()


# Rasgele isaret
plt.figure(2)
for k in range(0, 5):
    x2 = (1.5 + np.random.rand(1) - 0.5) * np.cos(2 * np.pi * 1 * t + np.pi / 2 * np.random.rand(1))
    # aci = np.pi / 2 * np.random.rand(1).     wt = 2 * np.pi * 1 * t.   genlik = 1.5
    plt.plot(t, x2, 'g')

plt.show()

"""



import numpy as np
from matplotlib import pyplot as plt


# np.random.normal => Beyaz Gous Goruntusunu ureiyor
mu, sigma = 0, 0.1
noice = np.random.normal(mu, sigma, 200) # mu = ortalama her zaman 0. sigma = sitart sapma
print(noice)
plt.figure(1)
plt.plot(noice) # goruntusunu ciziyor
plt.show()

plt.figure(2)
plt.hist(noice, 200)  # hist: istatiksel bilgi oldugunu anlariz yani Gous Goruntusu
plt.show()






