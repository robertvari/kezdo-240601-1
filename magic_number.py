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
    print("Wrong guess! Try again.")
    player_number = input("What is your guess? ")

print(f"You win! {magic_number} was my number! :)")