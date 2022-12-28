# def fact(n):
#    '''The factorial ->'''
#    if (n < 0):
#        return "not a positive integer"
#    if (n == 1) | (n == 0):
#        return 1
#    return n * fact(n-1)

# print(fact.__doc__,fact(n))

n = int(input("Enter n : "))

def fib(n):
    '''Fibonacci term ->'''
    if (n == 0) | (n == 1):
        return n
    return fib(n-1) + fib(n-2)

print(fib.__doc__, end=" ")

for i in range(n):
    print(fib(i), end=" ")
print()
