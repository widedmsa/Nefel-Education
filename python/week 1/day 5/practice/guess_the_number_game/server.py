from flask import Flask,render_template,request
app = Flask(__name__)   
import random

@app.route('/')
def display() :
    random_number =random.randint(1, 100)
    session['random_number'] = random_number 		
    return render_template('index.html',)


@app.route('/guess' ,methods=['POST'])
def guess():
    print(request.form)
    user_guess = int(request.form['number'])  
    random_number = request.form['random_number'])
    return render_template('result.html', user_guess=user_guess, random_number=random_number)


    if user_guess < random_number:
        status = "Too low!"
    elif user_guess > random_number:
        status = "Too high!"
    else:
        status = "Correct!"

    return render_template('result.html', status=status)


if __name__=="__main__":      
    app.run(debug=True)   

