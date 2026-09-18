# ROCK PAPER SCISSORS GAME

user = input("Enter your choice (rock, paper, scissors): ").lower() # This line prompts the user to enter their choice and converts it to lowercase.
import random # This line imports the random module, which is used to generate random choices for the computer.
computer = random.choice(["rock", "paper", "scissors"]) # This line randomly selects a choice for the computer from the list of options.
print("Computer chose:", computer) # This line prints the choice made by the computer.
if user == computer: # This line checks if the user's choice is the same as the computer        
    print("It's a tie!") # If the choices are the same, it prints "It's a tie!".    
else: # If the choices are different, it checks the following conditions to determine the winner.
    if (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"): # This line checks if the user wins based on the rules of the game.
        print("You win!") # If the user wins, it prints "You win!".
    else: # If the user does not win, it means the computer wins.
        print("Computer wins!") # It prints "Computer wins!".   