users = {
    'user1': 'password1',
    "user2": "password2",
    "user3": "password3",
}


username = input("Enter your username: ")
password = input("Enter your password: ")


if users[username] == password:
    print("Login succesful")
else:
    print("Login failed")