from flask import Flask 
app = Flask(__name__)

@app.route('/') 
def greeting():
    return "Hello World"



@app.route('/dojo') 
def Coding_dojo():
    return "dojo"


@app.route('/say/<str :name>') 
def hello(name):
    return (f"Hello , {name}") 


@app.route('/repeat/<int:num>/<str:name>') 
def repeat(name,num):
    return (f"{name * num}")  

if __name__=="__main__":    
    app.run(debug=True)   
