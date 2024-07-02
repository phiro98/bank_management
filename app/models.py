from flask_pymongo import PyMongo

class User:
    def __init__(self, username, password, is_banker=False):
        self.username = username
        self.password = password
        self.is_banker = is_banker

class Transaction:
    def __init__(self, user_id, amount, transaction_type):
        self.user_id = user_id
        self.amount = amount
        self.transaction_type = transaction_type
