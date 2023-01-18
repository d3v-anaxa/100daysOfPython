import os, termcolor

filename = "new.txt"
f = open( filename, "a")
print("Enter some text [enter \"exit() to get rid of program\"]:\n")

while True:
    text = input()
    if (text == "exit()"):
        break
        
    f.write(f"{text}\n")

os.system("clear")
f.close()


with open(filename, "r") as f:
    print(termcolor.colored("File content ->", "white", "on_black"))
    print(f.read())
