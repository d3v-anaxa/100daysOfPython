import time
import termcolor
hour = int(time.ctime().split(" ")[3].split(":")[0])
print(termcolor.colored("Good morning", "white", "on_blue") if (hour < 12 and hour >= 4) else termcolor.colored(
    "Good afternoon", "red", "on_yellow") if (hour >= 12 and hour < 17) else termcolor.colored("Good evening", "white", "on_black") if (hour >= 17 and hour < 21) else termcolor.colored("Good night", "white", "on_black"))
