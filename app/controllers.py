from app import mongo

def get_balance(username):
    user = mongo.db.users.find_one({"username": username})
    return user["balance"]

def deposit(username, amount):
    mongo.db.users.update_one({"username": username}, {"$inc": {"balance": amount}})
    mongo.db.transactions.insert_one({"username": username, "amount": amount, "type": "deposit"})
    return mongo.db.users.find_one({"username": username})
def withdraw(username, amount):
    user = mongo.db.users.find_one({"username": username})
    if user["balance"] >= amount:
        mongo.db.users.update_one({"username": username}, {"$inc": {"balance": -amount}})
        mongo.db.transactions.insert_one({"username": username, "amount": amount, "type": "withdraw"})
        return mongo.db.users.find_one({"username": username})
    return False

def get_transaction_history(username):
    transactions = mongo.db.transactions.find({"username": username}, {"_id": 0})
    return list(transactions) 

def is_banker(username):
    user = mongo.db.users.find_one({"username": username})
    return user and user.get('is_banker', False) 

def accounts():
    users = mongo.db.users.find({}, {"username": 1, "balance": 1, "_id": 0})
    return list(users)

def allTransactions():
    transactions = mongo.db.transactions.find({}, {"_id": 0})
    return list(transactions)

def find_by_username(username):
    return mongo.db.users.find_one({"username": username})
def registration_controller(username, hashed_password, is_banker):
    mongo.db.users.insert_one({"username": username, "password": hashed_password, "balance": 0, "is_banker": is_banker})
