import time
time = int(time.strftime("%H"))

if (time >= 21 or time < 6):
    print("Good Night")
elif (time >= 18 and time < 21):
    print("Good Evening")
elif (time >= 12 and time < 18):
    print("Good Afternoon")
else:
    print("Good Morning")

print("Time is : ", time)
