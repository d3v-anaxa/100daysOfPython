# decorators can be used to structurize a list of functions and statements to execute at certain order by modifying other functions

def greet(fx):
    def mfx(*args, **kwargs):
        print("decorator")
        fx(*args, **kwargs)
        print("end fx")
    return mfx

# @greet 
# def hello():
#     print("Hello world")

@greet
def add(a : int, b : int):
    print(10+0b1010+a+b)

add(10, 78)
