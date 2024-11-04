from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.users_model import Dojos



@app.route('/')
def create_dojo():
    return render_template('dojo_index.html')