import random

def sayi_tahmin_oyunu():
     sayi = random.randint(1,100)
     #print(sayi)
     
     print("***** 1-100 arası sayı tahmin oyunu *****")
     
     tahmin = int(input("bir sayı tuttum tahmin et?"))
     tahmin_adedi = 0
     
     while True:
          tahmin_adedi += 1
          
          if tahmin < sayi:
               tahmin = int(input("daha büyük!"))
               
          elif tahmin > sayi:
               tahmin = int(input("daha küçük!"))
               
          else:
               break;

     print("tebrikler!!! {} defada bildin".format(tahmin_adedi))
     tekrar = input("tekrar oynayalım mı? (e/h)")
     
     if tekrar == "e":
          sayi_tahmin_oyunu()
     else:
          print("hoşçakal........")
          #return
          


sayi_tahmin_oyunu()
print(":)")
