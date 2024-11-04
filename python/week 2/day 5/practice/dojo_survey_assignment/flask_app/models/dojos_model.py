from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB



class Users :
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
        query = "SELECT * FROM users ;"
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
        query="INSERT INTO dojo (name,location,favorite_language,comment) VALUES (%(name)s,%(location)s,%(favorite_langauge)s,%(comment)s ;"
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
