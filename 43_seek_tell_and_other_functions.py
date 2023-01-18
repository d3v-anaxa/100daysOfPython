with open("new.txt", "r") as f:
    f.seek(7)  # moves file Pointer to the n th byte of the file
    print(f.tell(), "th byte", sep="")  # finding the position of file pointer
    print(f.read(35))  # reads n bytes only

with open("new.txt", "w") as f:
    for num in range(10):
        f.write(f"Line {num+1}\t")
    f.truncate(63)  # writes only n bytes to the file

with open("new.txt", "r") as f:
    print(f.read())
