from flask import Flask, render_template,redirect,request,session
from todos_model import Todo
app=Flask(__name__)
app.secret_key="password123"
list_of_todos=[
    {
        "id":1,
        "name":"Learning flask",
        "status":"pending"
    },
    {
        "id":2,
        "name":"Learning SQL",
        "status":"in progress"
    },
    {
        "id":3,
        "name":"Learning ERD",
        "status":"completed"
    },
    {
        "id":4,
        "name":"Learning OOP",
        "status":"not yet started"
    }
]
@app.route('/todos',methods=["GET"]) 
def get_todos():
    return render_template('todos.html')

if __name__ == "__main__":
    app.run( debug = True, port = 5001 )