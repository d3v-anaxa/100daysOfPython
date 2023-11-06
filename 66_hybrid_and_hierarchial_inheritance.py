# Hybrid Inheritance

class A:
    pass

class B:
    pass

class C:
    pass

class D:
    pass

class E(A, B):
    pass

class F(C, D, E):
    pass

#   A B  C D
#   | |  | |
#   \ /  | |    
#    E   \ / 
#     \   /
#       F

# Hierarchial Inheritance

class n1:
    pass

class n2(n1):
    pass

class n3(n1):
    pass

class n4(n1):
    pass

class n5(n1):
    pass

class n6(n2):
    pass

#       n1
#       /\
#     n2  n3
#     /\    \
#   n4  n5   n6
