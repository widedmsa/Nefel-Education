from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/') 
def first_route():
    return render_template('index.html',columns=8,rows=8)


@app.route('/<int:rows>')
def second_route(rows) :
    return render_template('index.html',columns=8,rows=rows)


@app.route('/<int:rows>/<int:columns>') 
def third_route(rows,columns) :
    return render_template('index.html',columns=columns,rows=rows)

@app.route()




















if __name__=="__main__":      
    app.run(debug=True)   