emp_ID_1 = {
    1001 : 7.2,
    1002 : 3.4,
    1003 : 4.5,
    1004 : 8.2,
    1005 : 6.6,
    1006 : 6.0
    }

emp_ID_2 = {
    1046 : 6.3,
    1047 : 2.5,
    1048 : 3.6,
    1049 : 7.3,
    1050 : 5.7,
    1051 : 5.1
    }

print(list(emp_ID_1.items()))
print(list(emp_ID_2.items()))
emp_ID_1.update(emp_ID_2)
print(list(emp_ID_1.items()))
emp_ID_2.clear()
print(list(emp_ID_2.items()))
emp_ID_1.pop(list(emp_ID_1.keys()).pop())
print(list(emp_ID_1.items()))
del emp_ID_1[list(emp_ID_1.keys()).pop()]
print(list(emp_ID_1.items()))
