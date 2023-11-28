# STRINGS

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
