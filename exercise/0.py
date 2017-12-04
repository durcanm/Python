def powers(n):
    for i in range(65):
        p = lambda x: n ** i
        print(n, "^", i, "=", p(i))


powers(3)


# --------------------------------------------
def m(i):
    return i % 2 == 0


print(m(2))
print(m(3))

# --------------------------------------------

k = lambda a: a % 13 == 0
print(k(13))

# --------------------------------------------

x = list(range(10, 200))
y = list(filter(lambda a: a % 13 == 0, x))
print(y)

# --------------------------------------------
print(dir())

import calendar

yy = 2017;
mm = 11
print(calendar.month(yy, mm))


# --------------------------------------------

def greetPerson(*name):
    print('Hello', name)
    print(type(name))


greetPerson('Frodo', 'Sauron')


