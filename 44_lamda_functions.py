def avg(n1, n2):
    return (n1 + n2) / 2


print(avg(10, 30))

avg2 = (lambda n1=int(input("Enter n1 : ")), n2=int(input("Enter n2 : ")): print(f"Average of {n1} and {n2} : {(n1 + n2) / 2}"))()
