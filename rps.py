import sys
import random

player_input = input("Please enter a value:\n1 for Rock\n2 for Paper\n3 for "
                     "Scissors\n\nYour input: ")

player_choice = int(player_input)

if player_choice <1 or player_choice >3:
    sys.exit("Invalid choice. Please try again.") # Will exit the control flow bc error

computer_input = random.choice("123")
computer_choice = int(computer_input)
print(computer_choice)

print("")
print("You chose " + player_input+ ".")
print("Python chose " + computer_input + ".")
print("")

if player_choice > computer_choice:
    print("You won!!!")
elif computer_choice > player_choice:
    print("You lost! Python won.")
else:
    print("It's a tie! Play again.")