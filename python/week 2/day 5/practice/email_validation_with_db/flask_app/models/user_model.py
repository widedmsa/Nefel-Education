from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash
import re   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User :
    def __init__(self,data):
        self.id=data['id']
        self.email_address=data['email_address']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def save(cls,data):
        query="INSERT INTO users (email_address) VALUES (%(email_address)s) ;"
        results= connectToMySQL(DB).query_db(query,data)
        return results 

    @classmethod
    def get_all(cls) :
        query = "SELECT * FROM users ;"
        results=connectToMySQL(DB).query_db(query)
        users=[]
        for row in results :
            users.append(cls(row)) 
        return users 
    

    @classmethod
    def delete(clas,data) :
        query="DELETE FROM users WHERE id=%(id)s ;"
        return  connectToMySQL(DB).query_db(query,data)

    @staticmethod
    def validate_email(data):
        is_valid=True 
        if not EMAIL_REGEX.match(data['email_address']):
            flash("Invalid email address!", "email_validation")
            is_valid = False
        return is_valid 
