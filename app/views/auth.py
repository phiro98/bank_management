from flask import Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
import re
from app import mongo
from app.controllers import find_by_username, registration_controller
from app.utils import makeResponse

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    confirm_password = request.json.get('confirm_password')
    is_banker = request.json.get('is_banker', False)

    if not (username and password and confirm_password and is_banker):
        return makeResponse("","User Credential Key missing", 403)
    try:
        if find_by_username(username):
            return makeResponse("","Username already exists", 409)
        password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
        if password == confirm_password and bool(password_pattern.match(password)):
            hashed_password = generate_password_hash(password)
            registration_controller(username, hashed_password, is_banker)
            return makeResponse("User registered successfully","", 201)
        else:
            return makeResponse("","Please Provide correct passwords", 403)
    except Exception as e:
        print(e)
        return makeResponse("","something went wrong", 500)    

@auth.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not (username and password):
        return makeResponse("","User Credential Key missing", 403)    
    try:
        user = find_by_username(username)
        if not user or not check_password_hash(user["password"], password):
            return makeResponse("","Invalid credentials", 401)    
        access_token = create_access_token(identity=username)
        return makeResponse({"access_token": access_token},"", 200)    
    except Exception as e:
        print(e)
        return makeResponse("","something went wrong", 500)    

