def avg(n1 = 0, n2 = 0, string = "null"):
    print("The average is :", (n1 + n2) / 2)
    print("String :", string)

avg(string = "PYTHON", n2 = 17, n1 = 13)

def maxim(*num) :
    res = 0
    for i in num :
        res = i if i > res else res

    return res

res = maxim(1 ,5, -17, 38, -11)
print(res)
