import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# print(RPS.ROCK.value)  # returns 1
# print(RPS(1))  # returns RPS.ROCK and this is a string
# print(RPS(4)) # ValueError: 4 is not a valid RPS
# sys.exit()


# Create prompt for user
player_input = input(
    "Please enter a value:\n1 for Rock\n2 for Paper\n3 for " "Scissors\n\nYour input: "
)

# Change string input to integer in order to compare
player_choice = int(player_input)

# Set up check for appropriate user input
if player_choice < 1 or player_choice > 3:
    sys.exit("Invalid choice. Please try again.")  # Will exit the control flow bc error

# Create the "computer's input"
computer_input = random.choice("123")
computer_choice = int(computer_input)

print("")
print("You chose " + str(RPS(player_choice)).replace("RPS.", ""))
print("Python chose " + str(RPS(computer_choice)).replace("RPS.", ""))
print("")

# if player_choice < computer_choice: # THIS WAS WRONG GAME LOGIC!!! Remember the rules.
#     print("You won!!! 🎉🎉🎉")
# elif computer_choice < player_choice:
#     print("You lost! Python won 😢😢😢")
# else:
#     print("It's a tie! Play again 🤗🤗🤗")


if player_choice == 1 and computer_choice == 2:
    print("You lost! Python won 😢😢😢")
elif player_choice == 1 and computer_choice == 3:
    print("You won!!! 🎉🎉🎉")
elif player_choice == 3 and computer_choice == 1:
    print("You lost! Python won 😢😢😢")
elif player_choice == 3 and computer_choice == 2:
    print("You won!!! 🎉🎉🎉")
elif RPS(player_choice) == RPS.PAPER and computer_choice == 1:
    print("You won!!! 🎉🎉🎉")
elif RPS(player_choice) == RPS.PAPER and computer_choice == 3:
    print("You lost! Python won 😢😢😢")
else:
    print("It's a tie! Play again 🤗🤗🤗")
