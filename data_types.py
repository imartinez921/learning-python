print(" STRINGS ".center(45, "="))

first = "Dave"
second = "Gray"
print(type(first))  # returns <class 'str'>
print(isinstance(first, str))  # returns True
print(type(first) == str)  # returns True

# Multi-line strings - uses triple quotes to create a multi-line string
multiline = """
Hey, how are you?
I'm just checking in with you.
                                         I'm doing well. How are you?
"""
print(multiline)


# Esecape characters using a backslash
chat = "Hey! I'm at work.\n\tHey! Welcome back!\nThanks! Where's this at\\located?"
print(chat)


# String Methods
print(first)
print(first.lower())  # all lowercase
print(first.upper())  # all UPPERCASE
print(first)
print(multiline.title())  # title case
print(multiline.replace("well", "ok"))

print(len(multiline))  # length of string
multiline += "                           "
multiline = "                 " + multiline
print(len(multiline))

print("")

# Terminal Formatting - "Build a menu"
print("MENU".center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# Index and Ranges
print(first[1:-1])
print(first[0:])

# String Boolean Methods
first.startswith("D")
first.endswith("D")


print("")
print(" NUMERIC DATA TYPES ".center(45, "="))

price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

gpa = 3.28
y = float(1.14)
print(type(gpa))
print(isinstance(gpa, int))

# Complex type integers
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(type(comp_value.real))
print(comp_value.imag)
print(type(comp_value.imag))

# Built-In Number Methods
print(round(gpa))
print(round(gpa, 1))

import math

print(math.pi)

zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))
