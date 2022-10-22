class User:

    def __init__(self, first_name, last_name, age):
        self.first = first_name,
        self.last = last_name,
        self.age = age
        self.login_attempts = 5

    def describe_user(self):
        user = f"Hello {self.first} {self.last} you are age  {self.age}"
        print(user)

    def increment_login_attempts(self, num):
        self.login_attempts += num

    def login_attempts(self):
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts -= self.login_attempts



user = User("Alex", "Romanov", 32)
user.increment_login_attempts(6)
user.reset_login_attempts()
user.login_attempts()


