#Simple Rock, Paper, Scissors
#January 7 2021
#Anjali Bhardwaj

import random

#Welcome meassage
print('\nWelcome to Rock, Paper, Scissors!')

#Play function
def play():
        #dictionaty for keys of rock, paper, scissors
        keys_ = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

        #user input
        user = input("\nEnter 'r' for rock, 'p' for paper, 's' for scissors: ")

        #randomly generate computer choice
        computer = random.choice(['r', 'p', 's'])

        #if the user and computer choices are the same return tie
        if user == computer:
            return 'Computer guess the same thing. It is a tie.'

        #if the user wins, return "You Win!"
        if win(user, computer):
            print(f'The computer had chosen "{keys_[computer]}"...')
            return 'You Win!'

        #if the computer wins, return "You Lose!"
        print(f'The computer had chosen "{keys_[computer]}"...')
        return 'You lose...'

#Function to check if computer wins
def win(player, opponent):
    #return true if the player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
    or (player == 'p' and opponent == 'r'):
        return True

#Play until user does not want to anymore 
play_ = 'y'
while play_.lower() == 'y':
    print(play())
    play_ = input("Would you like to play again? (Y/N)")
else:
    exit()
