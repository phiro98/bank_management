from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.controllers import get_balance, deposit, withdraw, get_transaction_history
from app.utils import makeResponse
import json

main = Blueprint('main', __name__)

@main.route('/balance', methods=['GET'])
@jwt_required()
def balance():
    try:
        current_user = get_jwt_identity()
        balance = get_balance(current_user)
        return makeResponse({"balance": balance},"",200)
    except Exception as e:
        return makeResponse("", str(e), 500)

@main.route('/deposit', methods=['POST'])
@jwt_required()
def deposit_amount():
    data = request.data
    if not data or 'amount' not in json.loads(data):
        return makeResponse("", "Amount is required", 400)
    amount = json.loads(data)["amount"]
    try:
        current_user = get_jwt_identity()    
      
        if amount <= 0:
            return makeResponse("", "Amount must be a positive number", 400)

        result = deposit(current_user, amount)
        return makeResponse({"message":"Deposit successful", "balance":result["balance"]}, "", 200)
    except Exception as e:
        print(e)
        return makeResponse("", str(e), 500)

@main.route('/withdraw', methods=['POST'])
@jwt_required()
def withdraw_amount():
    data = request.data
    if not data or 'amount' not in json.loads(data):
        return makeResponse("", "Amount is required", 400)
    try:
        current_user = get_jwt_identity()    
        amount = json.loads(data)['amount']    
        if not isinstance(amount, (int, float)) or amount <= 0:
            return makeResponse("", "Amount must be a positive number", 400)
        
        result = withdraw(current_user, amount)
        if result:
            return makeResponse({"message":"Withdrawal successful", "balance":result["balance"]}, "", 200)
        else:
            return makeResponse("", "Insufficient funds", 400)
    except Exception as e:
        return makeResponse("", str(e), 500)

@main.route('/transactions', methods=['GET'])
@jwt_required()
def transactions():
    try:
        current_user = get_jwt_identity()
        transactions = get_transaction_history(current_user)
        return makeResponse(transactions, "", 200)
    except Exception as e:
        return makeResponse("", str(e), 500)