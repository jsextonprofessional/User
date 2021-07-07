class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"Name: {self.name}, {self.account_balance}")
        return self

first_user = User("Guido van Rossum", "guido@python.com" )
second_user = User("Monty Python", "monty@python.com")
print(first_user.name)	# output: Guido van Rossum
print(second_user.name)	# output: Monty Python
first_user.display_user_balance()
second_user.display_user_balance()
first_user.make_deposit(100)
first_user.make_deposit(200)
second_user.make_deposit(50)
print(first_user.account_balance)	# output: 300
print(second_user.account_balance)	# output: 50

