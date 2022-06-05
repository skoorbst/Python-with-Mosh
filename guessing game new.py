#https://youtu.be/_uQrJ0TkZlc?t=5056

secret_number = 8
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("What is your guess? "))
    guess_count += 1
    if guess == secret_number:
        print("Great work! You guessed it")
        break
else:
    [print("Sorry... you a loser")]