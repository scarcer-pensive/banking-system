class Transaction:
    def __init__(self, transaction_type, transaction_amount):
        self.type = transaction_type
        self.amount = transaction_amount

    def get_type(self):
        return self.type

    def get_amount(self):
        return self.amount
