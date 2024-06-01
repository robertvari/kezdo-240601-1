import pprint

phonebook = {
    "06201234567": {"name": "Kiss Csaba", "address": "Budapest", "age": 30},
    "06201235376": {"name": "Kovács Krisztina", "address": "Pécs", "age": 25}
}

# add new item to phonebook
phonebook["06201239876"] = {"name": "Kiss Béla", "address": "Debrecen", "age": 42}

pprint.pprint(phonebook["06201239876"]["name"])