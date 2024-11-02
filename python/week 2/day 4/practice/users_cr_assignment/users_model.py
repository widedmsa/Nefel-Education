from mysqlconnection import connectToMySQL
class Users:
    DB = 'userss_schema'
    def __init__( self , data ):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']



    @classmethod #(interacts directly with the databse) 
    def get_all(cls) :
        query = "SELECT * FROM userss;" #getting all data from the userss table in the database
        results = connectToMySQL(cls.DB).query_db(query) #storing the data retrieved from the database in a variable "results" 
        users = []
        for user in results:
            users.append( cls(user) ) #converts the data fetched (which is a dictionary) into a User object by calling cls(user) (where cls refers to the User class).
            #and then append it to the users list
        return users


    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM posts WHERE id = %(id)s ;"
        results=connectToMySQL(DB).query_db(query,{"id":id})
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO userss (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results


    @classmethod
    def updates(cls,data):
        query="UPDATE users SET (first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)

    
    @classmethod
    def delete(cls,data):
        query="DELETE FROM users WHERE id =%(id)s;"
        return  connectToMySQL(DB).query_db(query,data)

