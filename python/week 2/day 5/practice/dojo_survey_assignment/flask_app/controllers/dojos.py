from flask_app import app
from flask import render_template,redirect,request,flash
from flask_app.models.dojos_model import Dojos



@app.route('/')
def create_dojo():
    return render_template('dojos_index.html')


@app.route('/dojo/create',methods=['POST'])
def save_to_db():
    
    if not Dojos.validate_data(request.form) :
        
        return redirect('/')
    else:
        dojo_id = Dojos.save(request.form)
        return redirect('/result/'+str(dojo_id))


@app.route('/result/<int:dojo_id>')
def display_dojo(dojo_id):
    dojo=Dojos.get_one({'id':dojo_id})
    print(dojo)
    return render_template('result.html', dojo=dojo)


