class Account:
    def __init__(self, name, balance=0):
        self.owner = name
        self.balance = balance

    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: {self.balance}'

    def deposit(self, add_amount):
        self.balance += int(add_amount)
        print('Deposit Accepted')

    def withdraw(self, withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance -= int(withdraw_amount)
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')

acct1 = Account('Jose',100)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
print(acct1.balance)
acct1.withdraw(75)
print(acct1.balance)
acct1.withdraw(500)