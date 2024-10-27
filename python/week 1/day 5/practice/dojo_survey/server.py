from flask import Flask ,render_template,request,redirect,session
app = Flask(__name__)    
app.secret_key = 'supersecret'#encrypts our data

@app.route('/')
def display():
    return render_template('index.html')

@app.route('/process',methods=['POST']) #the data entered by the user it will be submitted to the router /process and the redirected to /
def submit():
    print(request.form)
    #extract the form data from the post request 
    # we will create varibales 
    name= request.form['name']
    location=request.form['location']
    languages=request.form['languages']
    comments=request.form['comments']
    #before redirecting our data we want to save our data to session
    session['name']=name
    session['location']=location
    session['languages']=languages
    session['comments']=comments
    
    return redirect('/result')



@app.route('/result')
def result():
    return render_template('result.html')





    # print(request.form,methods=[POST])
    # name=request.form['name']
    # location=request.form['location']
    # langauges=request.form['languages']
    # comments=request.form['comments']

    # session['name']=name
    # session['location']=location
    # session['langauges']=languages
    # session['comments']=comments
    # return redirect('/')

if __name__=="__main__":      
    app.run(debug=True)   

