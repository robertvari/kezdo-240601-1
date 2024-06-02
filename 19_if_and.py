email = "csaba@gmail.com"
password = "testpas123"

user_email = input("What is your email? ")
user_password = input("Your password? ")

#           True                       True
if (email == user_email) and (password == user_password):
    print("Wellcome back!")
else:
    print("Email or password is not correct.")