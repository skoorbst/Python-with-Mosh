#If name is less than 3 characters long, cannot be used
#If name is longer than 50 characters, cannot be used
#User name must be between 3 and 50 characters long

name = "Jonooooooooooooooooooooooooooooooooo"

if len(name) < 3:
    print("Warning: Name is too short. Needs to be at least 3 characters. Please try again")
elif len(name) > 15:
    print("Warning. Name is too long. Needs to be at least 3 characters. Please try again")
else:
    print("Great. Your name looks good!")

