def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)



n = int(input("input a number:"))
f = factorial(n)

print("factorial of {0} is {1}".format(n,f))
