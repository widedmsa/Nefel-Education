from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash



class Dojos :
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.location=data['location']
        self.favorite_language=data['favorite_language']
        self.comment=data['comment']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']



    @classmethod 
    def get_all(cls):
        query = "SELECT * FROM dojo ;"
        results=connectToMySQL(DB).query_db(query)
        dojos=[]
        for row in results :
            dojos.append(cls(row)) 
        return dojos 


    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojo WHERE id = %(id)s ;"
        results=connectToMySQL(DB).query_db(query,data)
        dojo = Dojos(results[0])
        return dojo


    @classmethod
    def save(cls,data):
        query="INSERT INTO dojo (name,location,favorite_language,comment) VALUES (%(name)s,%(location)s,%(favorite_language)s,%(comment)s) ;"
        results= connectToMySQL(DB).query_db(query,data)
        return results 

    @classmethod
    def update(clas,data) :
        query="UPDATE dojo SET first_name=%(name)s,location=%(location)s,favorite_language=%(favorite_language)s,comment=%(comment)s WHERE  users.id=%(id)s ; "
        return connectToMySQL(DB).query_db(query,data)


    @classmethod
    def delete(clas,data) :
        query="DELETE FROM dojo WHERE id=%(id)s ;"
        return  connectToMySQL(DB).query_db(query,data)




    @staticmethod
    def validate_data(data) :
        name=data['name']
        location=data['location']
        favorite_language=data['favorite_language']
        comment=data['comment']
        is_valid=True
        if len(name) < 3 :
            is_valid=False 
            flash("Name must contain at least 3 characters ","name_validation")
        if not (location) :
            is_valid=False
            flash("You must select a location","location_validation")
        if not (favorite_language) :
            is_valid=False
            flash("You must select a language","favorite_language_validation")
        if len(comment)< 3 :
            is_valid=False
            flash("Comment section must contain at least 3 charactaers","comment_validation")
        return is_valid
