
try:
    n1 = int(input("Enter a number : "))
    print(f"Multiplication table of {n1} is:")
    for i in range(10):
        print(f"{n1} x {'0'+str(i+1)  if i+1 < 10 else i+1} = {n1 * (i+1)}")
    else:
        print("end of loop")

except Exception as e:
    print(e)
