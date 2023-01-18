with open("new.txt", "w") as f:
    for num in range(100):
        f.writelines(f"Line {num+1}\t")

with open("new.txt", "r") as f:
    for line in f.readlines():
        print(line, end="")
print()
