import random

reward_stage = 0
reward_money = ("$0", "$100", "$500", "$1000", "$5000", "$10000", "$50000", "$100000", "$500000", "$10000000")
question_list = (
            ("Who is the creator of python language?", "Bjarne Stroustrup", "Guido van Rossum", "Brendan Eich", "James Gosling", 2),
            ("Which type of Programming does Python support?", "object-oriented programming", "structured programming", "functional programming", "all of the mentioned", 4),
            ("Is Python case sensitive when dealing with identifiers?", "no", "yes", "machine dependent", "none of the mentioned", 2),
            ("Which of the following is the correct extension of the Python file?", ".python", ".pl", ".py", ".p", 3),
            ("All keywords in Python are in _________", "Capitalized", "lower case", "UPPER CASE", "None of the mentioned", 4),
            ("Which keyword is used for function in Python language?", "Function", "def", "Fun", "Define", 2)
        )

while (reward_stage <9):
        random_question = random.choice(question_list)
        print("Reward amount -> ", reward_money[reward_stage + 1])
        print(random_question[0])
        print("1 ->", random_question[1])
        print("2 ->", random_question[2])
        print("3 ->", random_question[3])
        print("4 ->", random_question[4])
        n = int(input("Enter choice : "))

        if (n == random_question[5]):
            reward_stage+=1
            print("Congratulations!! you gave the correct answer!!")
        else:
            print("Your answer is incorrect")
            print("Actual answer ->", random_question[random_question[5]])
            print("Better luck next time")
            break;

print("You have won ->", reward_money[reward_stage])
