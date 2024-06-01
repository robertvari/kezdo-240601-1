print("Hello there! Let's play a little game.")
print("Give me your name and I give back its encrypted version.")

name = input("What is your name? ")

print(f"Your encrypted name is: {name[::-1]}")
print(f"{name[0]}{name.split()[-1]}")