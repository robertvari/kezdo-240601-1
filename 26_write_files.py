name, address, email = input("Name? "), input("Address? "), input("Email? ")

file_name = "user_data.txt"

result = f"Name: {name}\nAddress: {address}\nEmail: {email}"

with open(file_name, "w") as my_file:
    my_file.write(result)