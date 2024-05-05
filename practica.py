class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

user = User("Viktoriia", "12345")

print(user.username)
print(user.password)