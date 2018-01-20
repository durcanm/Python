import turtle

bob = turtle.Turtle() # turtle module provides a function called Turtle()
                      # that creates a Turtle object, which we assigned
                      # to a variable named bıb
                    
print(bob)            # <turtle.Turtle object at 0x02D292D0>



'''
move:
     forward()
     backward()
     right()
     left()
     
speed:
      0 : fastest
     10 : fast
      6 : normal
      3 : slow
      1 : slowest
'''


def kare(t,length):
     t.write('kare',align='center')
     t.penup()
     t.goto(-length/2,-length/2)
     t.pendown()
     t.speed(1) #slowest
     
     for i in range(4):
          t.forward(length)
          t.left(90)

def sekil1(t,length):
     t.penup()
     t.goto(-length/2,-length/2)
     t.pendown()
     t.speed(0) #fastest

     for i in range(45):
         t.forward(length)
         t.left(88)

def poligon(t,length,p):     
     angle=360/p
     for i in range(p):
          t.fd(length)
          t.lt(angle)

def desen():
     bob.penup()
     bob.goto(-50,-300)
     bob.pendown()
     for i in range(3,22):
          poligon(bob,100,i)

def daire(t,radius):
     import math     
     circumference = 2 * 3.14 * radius
     print('circumference:',circumference)
     n = int(circumference / 3) + 3
     print('n:',n)
     length = circumference / n
     poligon(t,length,n)

def diken(t,length,n):
     bob.color('red')
     bob.pensize(5)
     angle=360/n
     print('angle:',angle)
     for i in range(n):
          t.fd(length)
          t.lt(180)
          t.fd(length)
          t.rt(180)
          t.rt(angle)

def renkli_daire(t):
     bob.pensize(20)
     bob.color('green', 'yellow')
     bob.begin_fill()
     bob.circle(80)
     bob.end_fill()

def renkli_poligon(t):
     t.penup()
     t.goto(-50,-150)
     t.pendown()
     t.pensize(20)
     renkler=['red','green','blue','yellow','pink','brown','purple','orange','grey']
     for renk in renkler:
          t.color(renk)
          t.forward(150)
          t.left(360/len(renkler))



#kare(bob,100)
#sekil1(bob,200)
#poligon(bob,100,6)
#desen()
#daire(bob,radius=100)
#diken(bob,100,20)
#renkli_daire(bob)
#renkli_poligon(bob)




turtle.mainloop()   # wait for the user to do something
