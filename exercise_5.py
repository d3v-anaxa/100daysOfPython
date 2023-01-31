# snake water gun game
import random

item = ("snake", "water", "gun")
winning_combo = {
    "snake" : "water",
    "water" : "gun",
    "gun" : "snake",
        }

try:
    player_choice = item[int(input("1. snake\n2. water\n3. gun\nEnter choice : ")) - 1 % 3]
    ai_choice = random.choice(item)
    print(f"Player's choice : {player_choice}\nComputer's choice : {ai_choice}")
    print("PLayer won" if winning_combo[player_choice] is ai_choice else 
          "Match draw" if player_choice is ai_choice else 
          "Player lost")
except Exception as e:
    print("invalid choice")
