import random

def get_choices():
    player_choice = input ("Enter a choice (rock, paper, scissors): ")
    options =  ["paper", "rock", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
        
    return choices

results = get_choices()
print (results)

def check_win(player, computer):
    




