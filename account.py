from customer import Customer

class Account:
    def __init__(self, account_holder, initial_balance):
        self.customer = account_holder
        self.balance = initial_balance

    def get_customer(self):
        return self.customer

    def get_balance(self):
        return self.balance
