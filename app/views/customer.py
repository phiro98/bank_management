from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.controllers import get_balance, deposit, withdraw, get_transaction_history
from app.utils import makeResponse

main = Blueprint('main', __name__)

@main.route('/balance', methods=['GET'])
@jwt_required()
def balance():
    try:
        current_user = get_jwt_identity()
        balance = get_balance(current_user)
        return makeResponse({"balance": balance},"",200)
    except Exception as e:
        print(e)
        return makeResponse("","something went wrong", 500)    


@main.route('/deposit', methods=['POST'])
@jwt_required()
def deposit_amount():
    try:
        current_user = get_jwt_identity()
        amount = request.json.get('amount')
        if amount is None or amount <= 0:
            return makeResponse("", "Invalid amount", 400)
        
        user = deposit(current_user, amount)
        return makeResponse({"message": "Deposit successful", "new_balance": user['balance']}, "", 200)
    except Exception as e:
        print(e)
        return makeResponse("","something went wrong", 500)    
@main.route('/withdraw', methods=['POST'])
@jwt_required()
def withdraw_amount():
    try:
        current_user = get_jwt_identity()
        amount = request.json.get('amount')
        if amount is None or amount <= 0:
            return makeResponse("", "Invalid amount", 400)
        result = withdraw(current_user, amount)
        if result:
            return makeResponse({"message": "Withdrawal successful", "new_balance": result['balance']}, "", 200)
        else:
            return makeResponse("", "nsufficient funds", 400)
    except Exception as e:
        print(e)
        return makeResponse("","something went wrong", 500)    

@main.route('/transactions', methods=['GET'])
@jwt_required()
def transactions():
    try:
        current_user = get_jwt_identity()
        transactions = get_transaction_history(current_user)
        if transactions:
            return makeResponse(transactions, "", 200) 
        else:
            return makeResponse("", "No transactions availabe", 400)
    except Exception as e:
        print(e)
        return makeResponse("","something went wrong", 500)    