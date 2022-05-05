import random

rps_options = ['Rock', 'Paper', 'Scissors']
ans = ''
guess = ''

def get_computer_choice():
    ans = random.choice(rps_options)
    return ans

def get_user_choice():
    guess = input("Please guess the object: Rock, Paper or Scissors")
    return guess 