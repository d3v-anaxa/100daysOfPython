from functools import reduce

ls = [1, 2, 3, 4, 5, 6]
print("list :\t", ls)

ls_cube = list(map(lambda x: x**3, ls))
print("map :\t", ls_cube)

ls_filter = list(filter(lambda x: x > 3**3, ls_cube))
print("filter :", ls_filter)

ls_reduce = reduce(lambda x, y: x*y, ls)
print(ls_reduce)
