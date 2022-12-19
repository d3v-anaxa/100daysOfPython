INT_MAX = 2 ** 31 - 1
INT_MIN = - (2 ** 31)
ls = ["f_name", "m_name", "l_name", True, INT_MAX + INT_MIN]
# list comprehension
ls2 = [i**2 for i in range(10) if i % 2 != 0]

for i in ls2:
    print(i, end=" ")
print()
