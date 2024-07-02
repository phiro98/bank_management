from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import mongo
from app.controllers import is_banker, accounts, allTransactions 
from app.utils import makeResponse

banker = Blueprint('banker', __name__)

@banker.route('/accounts', methods=['GET'])
@jwt_required()
def list_accounts():
    try:
        current_user = get_jwt_identity()
        if not is_banker(current_user):
            return makeResponse("","Unauthorized", 403) 
        return makeResponse(accounts(),"",200)
    except Exception as e:
        print(e)
        return makeResponse("","something went wrong", 500)  
          
@banker.route('/all-transactions', methods=['GET'])
@jwt_required()
def all_transactions():
    try:
        current_user = get_jwt_identity()
        if not is_banker(current_user):
            return makeResponse("","Unauthorized", 403) 

        return makeResponse(allTransactions(),"",200)
    except Exception as e:
        print(e)
        return makeResponse("","something went wrong", 500)    