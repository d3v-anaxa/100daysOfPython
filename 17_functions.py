def gcd(n1 ,n2):
    if (n2 == 0):
         return n1
    return gcd(n2, n1 % n2)
    pass
 
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
res = gcd(n1, n2)
print("GCD is :", res)
