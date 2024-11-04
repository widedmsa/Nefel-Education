from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.users_model import Users



@app.route('/users')
def display_users():
    users=Users.get_all()
    print(users)
    return render_template('read_all.html', users=users)


@app.route('/users/new')
def create_users() :
    return render_template('create.html')


@app.route('/create/users',methods=['POST'])
def save_data():
    user_id=Users.save(request.form) # inserting a new user record into the database, using data passed from request.form
    return redirect('/users/'+str(user_id))#converting the id which is in the form of a string to int 


@app.route('/users/<int:id>')
def get_one(id):
    user=Users.get_one({'id': id})
    return render_template('read_one.html', user=user)

@app.route('/users/<int:id>/edit')
def edit_user(id):
    user = Users.get_one({'id': id})  #displaying the edit form
    return render_template('edit.html', user=user) 


@app.route('/edit/users/<int:id>', methods=['POST'])
def update_user(id):
    updated_user = {
        'id':id,
        'first_name': request.form['first_name'],  
        'last_name':request.form['last_name'],
        'email': request.form['email'],  
    }
    Users.update(updated_user) 
    return redirect('/users/' + str(id))


@app.route('/delete/<int:id>')
def delete_user(id):
    Users.delete({'id': id})
    return redirect('/users')