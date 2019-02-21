from src import db
from src.utils.bCrypt import hash_pass, check_pass
from flask_validator import ValidateString, ValidateEmail

class ToDoTable(db.Model):

    # custom table name
    __tablename__ = 'ToDoTable'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    hash_pass = db.Column(db.String(128), nullable=False)
    state = db.Column(db.TEXT, nullable=True)

    def __init__(self, username, email, password, state=None):
        self.username = username
        self.email = email
        self.state = state
        self.hash_pass = hash_pass(password)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    # class method is method that not the instance but the class can call, similar to static method
    # the different is classmethod has object that refer to class itself
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()
    
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email = email).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()
    
    def verify_hash(self, password):
        return check_pass(self.hash_pass, password)

    def __repr__(self):
        return f"username is {self.username} and state is {self.state}"
    
    #validator
    @classmethod
    def __declare_last__(cls):
        ValidateString(cls.username, False, True, "The username is not valid. Please check it")
        ValidateEmail(cls.email, False, True, "The e-mail is not valid. Please check it")
        ValidateString(cls.state, True, True, "The state is not valid. Please check it")
