import pprint

phonebook = {
    "06201234567": {"name": "Kiss Csaba", "address": "Budapest", "age": 30},
    "06201235376": {"name": "Kovács Krisztina", "address": "Pécs", "age": 25}
}

# update an item in phonebook
del phonebook["06201235376"]
pprint.pprint(phonebook)