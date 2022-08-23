from flask import Flask, render_template
from flask_material import Material
app = Flask(__name__)
# app.config['SECRETE']
Material(app)


@app.route('/user/<string:name>')
def user(name):
    return render_template('user.html',username = name, n= 5)

@app.route('/material/<string:name>')
def material(name):
    return render_template('material.html',username = name, n= 5)

app.run(port=5000,debug=True)