from customer import Customer
from account import Account
from transaction import Transaction

class Bank:
    def __init__(self, bank_name):
        self.name = bank_name
        self.customers = []
        self.accounts = []
        self.transactions = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def create_account(self, customer, initial_balance):
        account = Account(customer, initial_balance)
        self.accounts.append(account)

    def process_transaction(self, transaction):
        self.transactions.append(transaction)

    def display_customers(self):
        for customer in self.customers:
            print("Customer:", customer.get_name())

    def display_accounts(self):
        for account in self.accounts:
            print("Account Holder:", account.get_customer().get_name(),
                  ", Balance: $", account.get_balance())

    def display_transactions(self):
        for transaction in self.transactions:
            print("Transaction:", transaction.get_type(),
                  ", Amount: $", transaction.get_amount())

    def run(self):
        # Your banking system logic goes here
        pass
