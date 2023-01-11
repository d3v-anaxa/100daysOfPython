# using 'raise' keyword to set custom error

inp = input("Enter any number between 2 and 3: ")
if (inp.lower() != 'quit'):
    raise SyntaxError("Only 'quit' allowed as input!!")
