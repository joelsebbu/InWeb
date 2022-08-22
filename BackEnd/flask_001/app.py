from flask import Flask,redirect,url_for,request,jsonify,abort

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
    #POST
    # username =request.form.get('name') 
    # email = request.form.get('email')
    # password = request.form.get('password')
    # return f'<h1>Hello, {username}!</h1><h2>{email}</h2><h3>{password}</h3>'


booklist=[
    {
        'id':1,
        'title':'Harry Potter',
        'author':'J.K. Rowling',
    },
    {
        'id':2,
        'title':'The Alchemist',
        'author':'Paulo Coelho',
    },
    {
        'id':3,
        'title':'Jungle Book',
        'author':'R. Kipling',
    }
]  

@app.route('/books')
def books():
    return jsonify(book)

@app.route('/book/<int:id>')
def book(id):
    rt_book =list(filter(lambda t: t['id']==id,booklist))
    if len(rt_book)==0:
        return jsonify({'message':'Book not found'}) ,404
    return jsonify(rt_book)


if __name__ == '__main__':
    app.run(port=5000, debug=True)