from flask import Flask, render_template

app = Flask(__name__)



@app.route('/user/<string:name>')
def user(name):
    return render_template('user.html')

@app.route('/nice')
def nice():
    return render_template('nice.html')

@app.route('/material/<string:name>')
def material(name):
    return render_template('material.html',username = name, n= 5)

app.run(port=5000,debug=True)