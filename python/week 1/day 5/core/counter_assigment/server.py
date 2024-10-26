from flask import Flask ,render_template, request, redirect, session
app = Flask(__name__)   
app.secret_key='keep it secret'


@app.route('/count')
def cookies() :
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('index.html',counter=session['counter'])



@app.route('/reset')
def reset():
    session.clear()  
    return render_template('index.html' , counter=1)




if __name__=="__main__":       
    app.run(debug=True)    

