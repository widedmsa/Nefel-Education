from flask import Flask, render_template 
app = Flask(__name__)   

@app.route('/play')          
def html():
    return render_template('index.html',number=3) 


@app.route('/play/<int:x>')
def html():
    return render_template('index.html', number=x)


@app.route('/play/<int:x>')
def html():
    return render_template('index.html',number=x)


@app.route('/play/<int:x>/<col>')
def display() :
    return render_template('index.html',number=x,color=col)





if __name__=="__main__":      
    app.run(debug=True)    

