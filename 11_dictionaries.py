phonebook = {
    "06201234567": {"name": "Kiss Csaba", "address": "Budapest", "age": 30},
    "06201235376": {"name": "Kovács Krisztina", "address": "Pécs", "age": 25}
}


car_registry = {
    "ABC-123": {"owner": "Kiss Csaba", "model": "BMW", "date": "2012-03-13"},
    "ABC-456": {"owner": "Kovács Krisztina", "model": "Peugeot", "date": "2010-06-22"}
}

print(phonebook["06201234567"]["address"])
print(car_registry["ABC-123"]["owner"])

print(phonebook["06201235376"]["name"])