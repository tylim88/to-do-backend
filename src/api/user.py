import json
from flask import request
from src import aPi, app
from flask_restful import Resource, abort, reqparse
from src.models.toDoList import ToDoTable
from src.utils.validation import validateUsername, validateEmail
from flask_jwt_extended import create_access_token, get_jwt_identity

class ValidateUsername(Resource):

    def post(self):

        try:
            data = request.get_json()
            username = data['username']
        except:
            abort(400, message = "invalid format")

        validateUsername(username)

        return {'message': f"{username} is usable"}

aPi.add_resource(ValidateUsername, '/usernameValidation')

class ValidateEmail(Resource):

    def post(self):

        try:
            data = request.get_json()
            email = data['email']
        except:
            abort(400, message = "invalid format")

        validateEmail(email)
            
        return {'message': f"{email} is usable"}

aPi.add_resource(ValidateEmail, '/emailValidation')

parser1 = reqparse.RequestParser()
parser1.add_argument('username', help = 'This field cannot be blank', required = True)
parser1.add_argument('email', help = 'This field cannot be blank', required = True)
parser1.add_argument('password', help = 'This field cannot be blank', required = True)
parser1.add_argument('state', help = 'This field cannot be blank', required = True)

class SignUp(Resource):

    def post(self):
        data = parser1.parse_args()
        username = data['username']
        email = data['email']
        password = data['password']
        state = data['state']

        validateUsername(username)
        validateEmail(email)

        if len(password) < 8:
            abort(400, message = "password must be at least 8 characters")

        user = ToDoTable(username, email, password, state)
        user.save_to_db()

        access_token = create_access_token(identity = username)
        return {
            'message': f"Signed up as {username}",
            'access_token': access_token,
            }
        

aPi.add_resource(SignUp, '/signUp')

parser2 = reqparse.RequestParser()
parser2.add_argument('username', help = 'This field cannot be blank', required = True)
parser2.add_argument('password', help = 'This field cannot be blank', required = True)

class Login(Resource):

    def post(self):
        pass
        data = parser2.parse_args()
        username = data['username']

        try:
            user = ToDoTable.find_by_username(username = username) or ToDoTable.find_by_email(email = username)
        except:
            abort(500, message='something went wrong')

        if user and user.verify_hash(data['password']):
            access_token = create_access_token(identity = user.username)
            return {
                'message': f"Logged in as {user.username}",
                'access_token': access_token,
                'state': user.state
                }
        
        abort(400, message='username and password do not matched')

aPi.add_resource(Login, '/login')