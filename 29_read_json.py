import json

with open("user_data.json") as f:
    user_data = json.load(f)

print(user_data["name"])
print(user_data["address"])
print(user_data["email"])