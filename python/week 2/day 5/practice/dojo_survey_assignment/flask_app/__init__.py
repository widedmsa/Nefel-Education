from flask import Flask 
app= Flask(__name__)
app.secret_key = "key"
DB = "dojo_survey_schema"