from flask import Flask 
app= Flask(__name__)
app.secret_key = "key"
DB = "dojos_survey_schema"