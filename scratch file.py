
secret_number = 98
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("What is your guess? "))
    guess_count += 1
    if guess == secret_number:
        print("Wow. You got it. You win!")
        break
else:
    print("Shit, sorry. You lose. You a loser")

