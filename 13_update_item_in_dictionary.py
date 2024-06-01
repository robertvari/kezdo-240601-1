import pprint

phonebook = {
    "06201234567": {"name": "Kiss Csaba", "address": "Budapest", "age": 30},
    "06201235376": {"name": "Kovács Krisztina", "address": "Pécs", "age": 25}
}

# update an item in phonebook
phonebook["06201235376"] = {"name": "Kiss Béla", "address": "Debrecen", "age": 42}
phonebook["06201235376"]["address"] = "Budapest"
pprint.pprint(phonebook)