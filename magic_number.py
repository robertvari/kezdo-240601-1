import random

# Game rules
min_number = 1
max_number = 10
try_count = 3

# Get random number between min_number-max_number
magic_number = str(random.randint(min_number, max_number))

# Get a number from player
player_number = input("What is your guess? ")


# check player's number. If wrong ask again.
while magic_number != player_number:
    try_count -= 1
    if try_count == 0:
        break

    print(f"Wrong guess! You have {try_count} tries left. Try again.")
    player_number = input("What is your guess? ")


if magic_number == player_number:
    print(f"You win! {magic_number} was my number! :)")
else:
    print(f"You lost the game. My number was {magic_number}.")