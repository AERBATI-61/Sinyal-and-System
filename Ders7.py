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