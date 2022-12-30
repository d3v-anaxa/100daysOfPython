s1 = {1, 6 , 17, 4, 3}
s2 = {3, 2, 6}
s3 = {1, 17}
s5 = {1}

print(s1.union(s2))
print(s1.intersection(s2))
s4 = s2.difference(s1)
print(s4)
print(s1.issuperset(s3))
print(s3.issubset(s1))
print(s5.isdisjoint(s3))
s3.add(31)
print(s3)
s1.remove(6) # error if invalid _value_
print(s1)
s1.discard(6) # no error return
print(s1)
del s5
print(2 in s4) # checking _value_ existance

