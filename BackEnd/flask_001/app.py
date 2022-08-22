from flask import Flask,redirect,url_for,request

app= Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>'

@app.route('/admin')
def admin():
    return redirect(url_for('user',name='admin'))

@app.route('/login',methods=['GET'])
def login():
    username = request.args.get('username')
    email = request.args.get('email')
    password = request.args.get('password')
    return f'<h1>Username: {username}, Email: {email}, Password: {password}</h1>'

    # username =request.form.get('name') 
    # email = request.form.get('email')
    # password = request.form.get('password')
    # return f'<h1>Hello, {username}!</h1><h2>{email}</h2><h3>{password}</h3>'


if __name__ == '__main__':
    app.run(port=5000, debug=True)