from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash
import re   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 



class User :
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']



    
    @classmethod
    def save(cls,data):
        query="INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s) ;"
        results= connectToMySQL(DB).query_db(query,data)
        return results 


    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s ;"
        result=connectToMySQL(DB).query_db(query,data)
        if result :
            return cls(result[0])
        return False

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s ;"
        results=connectToMySQL(DB).query_db(query,data)
        user = User(results[0])
        return user


    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 3:
            flash("First name must contain at least 3 characters", "first_name_validation")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last name must contain at least 3 characters", "last_name_validation")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!", "email_validation")
            is_valid = False
        elif User.get_by_email({'email': user['email']}):
            flash("Email already exists", "email_validation")
            is_valid = False
        if len(user['password']) < 7:
            flash("Password must contain at least 7 characters", "password_validation")
            is_valid = False
        elif user['password'] != user['confirm_password']:
            flash("Passwords must match", "confirm_password_validation")
            is_valid = False
        return is_valid