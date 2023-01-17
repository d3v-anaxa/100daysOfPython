var = 10  # global variable
print(f"global var: {var}")


def func():
    var = 100  # local variable
    print(f"local var: {var}")


def func2():
    global var
    var = 1000
    # print(f"global var: {var}")


func()
print(f"global var: {var}")
func2()
print(f"global var: {var}")


