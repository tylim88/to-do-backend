import json
from src import aPi, app, db
from flask import request
from flask_restful import Resource, abort, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.models.toDoList import ToDoTable
from flask_cors import cross_origin

class updateItems(Resource):

    @jwt_required
    def post(self):

        try:
            data = request.get_json()
        except:
            abort(400, message = "invalid format")
        
        try:
            user = ToDoTable.find_by_username(get_jwt_identity())
            user.state = json.dumps(data)
            db.session.commit()
            return f"{user.username} state {data} is updated"
        except:
            abort(500, message = "something went wrong")

aPi.add_resource(updateItems, '/updateitems')

class getItems(Resource):

    @jwt_required
    def get(self):

        try:
            user = ToDoTable.find_by_username(get_jwt_identity())
            return {'state': user.state, 'username': user.username}
        except:
            abort(500, message = "something went wrong")   

aPi.add_resource(getItems, '/getItems')