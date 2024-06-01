# CRUD operations: Create, Retrieve, Update, Delete
my_friends = ["Csaba", "Kriszta", "Tamás", "Aladár"]

my_friends.append("Johnie")

my_lucky_numbers = [1, 2, 3, 4, 5]
my_friends.extend(my_lucky_numbers)

# my_friends += my_lucky_numbers

my_friends.insert(0, 100)

print(my_friends)