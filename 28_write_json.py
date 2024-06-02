import json

user_data = {
    "name": "Kiss Csaba",
    "address": "Debrecen",
    "emai": "csaba@gmail.com"
}

with open("user_data.json", "w") as f:
    json.dump(user_data, f)