from flask import Flask, render_template 
app = Flask(__name__)   

@app.route('/play')          
def html():
    return render_template('index.html',number=3,color=col) 


@app.route('/play/<int:x>')
def display_xtimes():
    return render_template('index.html', number=x,color=col)



@app.route('/play/<int:x>/<col>')
def display_changing_color() :
    return render_template('index.html',number=x,color=col)





if __name__=="__main__":      
    app.run(debug=True)    

