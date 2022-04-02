# ************************ Birinci Hafta **************************************
from matplotlib import pyplot as plt         #cizim islemi icin
import numpy as np
import sigsys
n = np.arange(-5, 10)
x = sigsys.drect(n, N=3)                     # Ayrik Dikdortgen cizdirmek icin
plt.figure(1)                            # Sekil almis oluyor
plt.title("Ayrik Zamanli N = 3 Ornekli Dikdortgen isareti")
plt.stem(n, x)                           # Ayrik cizdirmek islemini yapiyor
plt.show()                               # Grafik gostermek icin




from numpy import arange
from sigsys import tri
t = arange(-1, 5, .01)
x = tri(t, 1.0)                             # Ucgen Cizme islemi
plt.figure(6)
plt.title("Surekli Zamanli Ucgen isareti")
plt.plot(t, x)                              # Surekli cizdirme islemini yapiyor
plt.show()