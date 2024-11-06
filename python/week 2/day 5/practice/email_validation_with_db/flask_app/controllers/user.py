from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user_model import User


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user/registration',methods=['POST'])
def registration():
    if User.validate_email(request.form):
        data = User.save(request.form)
        user_id=User.save(data)
        session['user_id']=user_id
        return redirect('/success')
    return redirect('/')



@app.route('/success')
def get_all():
    users=User.get_all()
    return render_template('success.html',users=users)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')