from flask import Flask, render_template, request, redirect
from users_model import Users
app = Flask(__name__)

@app.route('/users')
def display():
    all_users = Users.get_all() #(we call the users.get_all  to run the class method and retrieve data  from the database(which is a list of dictionaries) storing it in variable
    return render_template('read_all.html',all_users=all_users)#displaying the html file in the browser.

@app.route('/users/new') 
def display_2():
    return render_template('create.html')#displaying the second html page 



@app.route('/users/create', methods=['POST'])
def submit_to_db():
    User.save(request.form)# we call the save class method of the Users class passing the form data to this method(which will inserting the new user data into the database).
    return redirect('/users')


if __name__=="__main__":
    app.run(debug=True)