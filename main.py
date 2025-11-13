# Let's code a rock, paper & Scissor shot
"""
0 for rock
1 for paper
-1 for scissor
"""

#let's set the random input for the computer
import random
computer = random.choice([0, 1, -1])

print("Welcome to Rock, Paper & Scissors!")
print("-----------------------------------")
print("Rules:\n- Rock beats Scissor\n- Paper beats Rock\n- Scissor beats Paper\n")
input("Press Enter to start the game...")

#Take input from user
user = input("Enter your choice: ")

#Make a dictionary to store keys
userdict = {"r":0, "p":1, "s":-1}
#Making a reverse dictionary for the system
reversed_dict = {0: "Rock", 1: "Paper", -1: "Scissor"}
# Convert user input to numeric value
you = userdict[user]

# Print choices
print(f"You chose {reversed_dict[you]}")
print(f"Computer chose {reversed_dict[computer]}")
#Define conditions
if(computer == you):
    print("It's a draw!")
else:
    if(computer == -1 and you == 0):
        print("You win!")
    elif(computer == 1 and you == 0):
        print("You lose!")
    elif(computer == 0 and you == -1):
        print("You lose!")
    elif(computer == 0 and you == 1):
        print("You win!")
    elif(computer == 1 and you == -1):
        print("You win!")
    elif(computer == -1 and you == 1):
        print("You lose!")
    else:
        print("something went wrong")