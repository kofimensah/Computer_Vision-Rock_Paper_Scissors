import random

rps_options = ['Rock', 'Paper', 'Scissors']
ans = ''
guess = ''

def get_computer_choice():
    ans = random.choice(rps_options)
    return ans

def get_user_choice():
    guess = input("Please guess the object: Rock, Paper or Scissors").capitalize()
    return guess 

def get_winner(computer_choice, user_choice):
    print(f"Computer = {computer_choice}, User = {user_choice}")
    if computer_choice == "Rock" and user_choice == "Paper":
        return "User Wins"
    elif computer_choice == "Rock" and user_choice == "Scissors":
        return "Computer Wins"
    elif computer_choice == "Paper" and user_choice == "Rock":
        return "Computer Wins"
    elif computer_choice == "Paper" and user_choice == "Scissors":
        return "User Wins"
    elif computer_choice == "Scissors" and user_choice == "Rock":
        return "User Wins"
    elif computer_choice == "Scissors" and user_choice == "Paper":
        return "Computer Wins"
    else:
        return "Try Again"
