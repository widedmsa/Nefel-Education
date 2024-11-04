from flask import Flask 
app= Flask(__name__)
app.secret_key = "key"
DB = "all_users_schema"