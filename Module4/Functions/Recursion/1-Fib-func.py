def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

x = int(input("Enter the no to be fibonised :"))
for n in range(1, x+1):  # testing
    print(n, "->", fib(n))
