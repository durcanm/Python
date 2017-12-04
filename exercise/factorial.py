def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(10)
print(f)
