import time
time = int(time.strftime("%H"))

if (time >= 21 or time < 6) :
    print ("Good Night")

elif (time >= 18 and time < 21) :
    print("Good Evening")
    
elif (time >= 12 and time < 18) :
    print("Good Afternoon")

else :
    print("Good Morning")

age = int(input("Enter your age : "))

if (age >= 18) :
    print("You can drive!!")

else :
    print("You cannot drive")

budget = int(input("Enter your budget : "))
apple_rate = int(input("Enter apple rate : "))
if (budget/apple_rate >= 0.1) :
    print ("Buy", budget/apple_rate, "kg apple")

else :
    print("I'll buy some peanut")
