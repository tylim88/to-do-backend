import string, requests, json
from src import app
from flask import request
from validators import email
from flask_restful import abort
from src.models.toDoList import ToDoTable

def validateUsername(username):
    invalidChars = set(string.punctuation)
    if len(username) < 4:
        abort(400, message='name must be longer than 3 characters')
    elif not username[0].isalpha():
        abort(400, message='name must start with alphabet')
    elif any(char in invalidChars for char in username) or ' ' in username:
        abort(400, message='invalid character')
    elif len(username) > 20:
        abort(400, message='name must be shorter than 20 characters')

    try:    
        user = ToDoTable.find_by_username(username)
    except:
        abort(500, message='something went wrong')
        
    if user:
        abort(400, message='user already exist')

def validateEmail(mail):
    if not email(mail):
        abort(400, message='incorrect email format')

    try:    
        user = ToDoTable.find_by_email(mail)
    except:
        abort(500, message='something went wrong')

    if  user:
        abort(400, message='email already exist')

    # check if the email is truly owned by someone
    if requests.get(app.config['VERIFY_EMAIL'] + mail).json()['status'] != 1:
        abort(400, message='this email is not belong to anyone')