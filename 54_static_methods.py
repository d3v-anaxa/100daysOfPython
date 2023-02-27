class Math:
    def __init__(self, num):
        self.num = num

    def add_to_num(self, n):
        self.num += n 

    @staticmethod
    def add(a, b):
        return a + b

#res = Math.add(1, 2)
#print(res)

a = Math(5)
print(a.num)

a.add_to_num(50)
print(a.num)

print(a.add(101, 43))

# This works the same like friend functions in C++
print(Math.add(101, 43))
