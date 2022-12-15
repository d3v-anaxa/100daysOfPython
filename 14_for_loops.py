count = int(input("Enter height : "))

for i in range(count) :
    print(count - i, end="")
    for j in range(2 * count) :
            print("* " if i + j >= count and j - i <= count else "  ", end="")

    print()
