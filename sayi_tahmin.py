import random

def sayi_tut():
     sayi = random.randint(1,100)
     #print(sayi)
     print("1-100 arası sayı tutma oyunu ******")
     devam = True
     adet = 0
     while devam:
          tahmin = int(input("tahmin et?  "))
          adet += 1
          if tahmin > sayi:
               print("daha küçük")
          elif tahmin < sayi:
               print("daha büyük")
          else:
               print("tabrikler !!!!!!", adet, "kerede bildin")
               devam=False
               tekrar = str(input("tekrar oynayalım mı (e/h) ?"))
               if tekrar=="e":
                    sayi_tut()
               else:
                    print("hoşçakal.......")

sayi_tut()
