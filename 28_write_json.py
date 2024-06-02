import json

user_data = {
    "name": "Kiss Csaba",
    "address": "Debrecen",
    "email": "csaba@gmail.com"
}

with open("user_data.json", "w") as f:
    json.dump(user_data, f)