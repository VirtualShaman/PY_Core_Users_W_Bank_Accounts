

class BankAccount:
    # don't forget to add some default values for these parameters!
    bank_name = "Bank of Python"
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        # don't worry about user info here; we'll involve the User class soon

class User:
    # class attributes get defined in the class
    # now our method has 2 parameters!
    def __init__(self, name, email_address):
        # we assign them accordingly
        self.name = name
        self.email = email_address
        # the account balance is set to $0
        self.account = BankAccount(int_rate=.02, balance=0)

    def deposit(self, amount):
        self.account.balance += amount
        return self

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.account.balance,amount):
            self.account.balance -= amount
            return self
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.account.balance -= 5
            return self

    def yield_interest(self):
        if self.account.balance > 0:
            self.account.balance += (self.account.balance * self.account.int_rate)
            return self

    def display_user_balance(self):
        print(f"User:{self.name}, Balance:{self.account.balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        return self

    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

guido.display_user_balance()

guido.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest().display_user_balance()

monty.deposit(100).deposit(100).withdraw(20).withdraw(20).withdraw(20).withdraw(20).yield_interest().display_user_balance()