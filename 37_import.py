# 'import' keyword imports module inside a program
# 'from' keyword imports specific functions from a module
# 'as' keyword change modules/functions name
# 'dir' function takes a module as an argument and return a list of all functions of that module

import math as m

print(m.sqrt(8))
print(m.pi)
print("\n".join(dir(m)))