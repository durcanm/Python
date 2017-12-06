def powers_of_n(n):
    for i in range(65):
        p = lambda x: n ** i
        print(n, "^", i, "=", p(i))


powers_of_n(3)


# --------------------------------------------
def is_divisible_by(i,j):
    return i % j == 0


print("4 is divisible by 2 :",is_divisible_by(4,2))
print("5 is divisible by 3 :",is_divisible_by(5,3))

# --------------------------------------------

k = lambda a: a % 13 == 0
print(k(13))

# --------------------------------------------

x = list(range(10, 200))
print("x:", x)

y = list(filter(lambda a: a % 13 == 0, x))
print("y:", y)

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


