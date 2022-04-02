"""
class Ornek:
    def __init__(self, x=0):
        self.x = x

    def yaz(self):
        print(self.x)

    def __repr__(self):
        return f'x = {self.x}'

nesne = Ornek()
nesne.yaz()
print(nesne)
"""


# 21:36-25:15 dakka
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

genlikA = 1
w = 2 * np.pi * 4 / 2.5  # periyod
teta = 0
t = np.linspace(0, 2.5, 250)
x = genlikA * np.exp(1j * w * t + teta)

plt.figure(1)
ax = plt.axes(projection='3d')
ax.plot3D(t, np.real(x), np.imag(x), 'blue')
# ax.hold(True)
ax.plot3D(t, np.real(x), np.zeros(np.size(t)) - 1.5, 'red')
ax.plot3D(t, np.zeros(np.size(t)) + 1, np.imag(x), 'green')
# ax.hold(False)

# ax.view_init(50, 60)
ax.set_xlabel('Zaman')
ax.set_ylabel('Gercek eksen')
ax.set_zlabel('Sanal Eksen')

plt.figure(2)
plt.plot(t, np.sqrt(np.real(x) * np.real(x) + np.imag(x) * np.imag(x)), 'red')
plt.xlabel('Zaman')
plt.xlabel('Genlik')
plt.show()

t = np.arange(0, 10)
plt.figure(3)
plt.plot(t, w * t + teta, 'red')
plt.xlabel('Zaman')
plt.xlabel('Aci')
plt.show()
"""









import numpy as np
import matplotlib.pyplot as plt

# Periodic degildir pi degeri yok
n = np.arange(0, 50)
x = 1 * np.sin(0.2 * n)
plt.figure(1)
plt.stem(n, x) # Ayrik olarak ciziyor.
plt.show()

# Periodic'tir pi degeri yok
n = np.arange(0, 50)
x = 1 * np.sin(0.2 * np.pi * n)
plt.figure(1)
plt.stem(n, x) # Ayrik olarak ciziyor.
plt.show()


# Surekli zemanli oldugu icin pi olsada olmasada periodic halde ciziyor
n = np.arange(0, 50)
x = 1 * np.sin(0.2 * np.pi * n)
plt.figure(1)
plt.plot(n, x) # Surekli olarak ciziyor.
plt.show()


# Surekli zemanli oldugu icin pi olsada olmasada periodic halde ciziyor
n = np.arange(0, 50)
x = 1 * np.sin(0.2 * n)
plt.figure(1)
plt.plot(n, x) # Surekli olarak ciziyor.
plt.show()




#  Surekli zamanli bir isaretten ayrik zamanli bir isaret nasil elde edilebilir
#  Surekli zamanli bir periyodic isaretten ayrik zamanli periyodic isaret nasil elde edilebilir
# f0 fs0 F0 t0 N0 omg0 OMG0
# Genelde ayrik zamanli isaretlerde hep buyuk harfler kullaniliyor.