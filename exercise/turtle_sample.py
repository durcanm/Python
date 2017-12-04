import turtle

bob=turtle.Turtle() # turtle module provides a function called Turtle()
                    # that creates a Turtle object, which we assigned
                    # to a variable named bıb
                    
print(bob)          # <turtle.Turtle object at 0x02D292D0>



"""
     fd: forward, in pixels
     bk: backward
     lt: left turn, angle in degrees
     rt: right turn
     pu: pen up
     pd: pen down
"""


def kare(t,length):
     for i in range(4):
          t.fd(length)
          t.lt(90)

def sekil1(t):
     for i in range(45):
         t.fd(200)
         t.lt(88)

def poligon(t,length,p):
     angle=360/p
     for i in range(p):
          t.fd(length)
          t.lt(angle)

def desen():
     for i in range(3,10):
          poligon(bob,100,i)

#kare(bob,100)
#sekil1(bob)
#poligon(bob,100,6)
#desen()






import math

def circle(t,radius):
     circumference = 2 * 3.14 * radius
     print("circumference:",circumference)
     n = int(circumference / 3) + 3
     print("n:",n)
     length = circumference / n
     poligon(t,length,n)


#circle(bob,radius=100)




def line(t,length,n):
     angle=360/n
     print("angle:",angle)
     for i in range(n):
          t.fd(length)
          t.lt(180)
          t.fd(length)
          t.rt(180)
          t.rt(angle)


bob.color("red")
bob.pensize(5)

line(bob,100,20)








turtle.mainloop()   # wait for the user to do something
