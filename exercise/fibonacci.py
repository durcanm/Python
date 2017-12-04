def fibonacci(n):
     if not isinstance(n,int):
          return "!!! invalid number !!!"

     f = [0,1]
     while len(f) < n:
          f.append( f[-1]+f[-2] )
     return f
         
     

print(fibonacci(20))
