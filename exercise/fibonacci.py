def fibonacci():
     n = input("how many numbers do you want?")
     n = int(n)
     f = [0,1] # initial series

     while len(f) < n:
          f.append( f[-1]+f[-2] )

     print(f)


fibonacci()
