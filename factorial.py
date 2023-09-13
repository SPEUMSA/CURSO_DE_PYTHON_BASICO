def factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac = i * fac
    return fac


c = factorial(5)
print(c)
