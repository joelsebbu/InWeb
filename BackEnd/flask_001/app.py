import re
from flask import Flask,redirect,url_for,request,jsonify,abort
import requests

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
    return jsonify(booklist)

@app.route('/book/<int:id>')
def book(id):
    rt_book =list(filter(lambda t: t['id']==id,booklist))
    if len(rt_book)==0:
        return jsonify({'message':'Book not found'}) ,404
    return jsonify(rt_book)

@app.route('/books',methods=["POST"])
def create_book():
    if not request.json:
        abort()
    
    book={
        'id': booklist[-1]['id']+1,
        'title': request.json.get('title'),
        'author':request.json.get('author'),
    }
    booklist.append(book)
    return jsonify({'book':book}), 201

@app.route('/book/<int:id>',methods=['PUT'])
def update_book(id):
    book =[book for book in booklist if book['id'] == id]
    if len(book) == 0:
        abort(404)
    if 'title' in request.json and type(request.json.get('title'))!= str:
        abort(400)
    if 'author' in request.json and type(request.json.get('author')) != str:
        abort(400)
    book[0]['title'] = request.json.get('title')
    book[0]['author'] = request.json.get('author')

    return jsonify(book)

@app.route('/book/<int:id>', methods=["DELETE"])
def delete_book(id):
    book =[book for book in booklist if book['id'] == id]
    if len(book) == 0:
        abort(404)
    booklist.remove(book[0])
    return jsonify({"status":"deleted"})


#install a module called requests to send the API request
#using the command pip install requests
#defining the API url
API_URL = ('https://api.genderize.io/?name={}')

#createw a new function for sending the api requeset to the url
def send_api(name):
    print(API_URL)
    try:
        data = requests.get(API_URL.format(name)).json()
    except Exception as e: 
        print(e)
        data =None
    return data


@app.route('/gender/<name>')
def gender(name):
    response = send_api(name)
    rt =response["name"]+" is "+response["gender"]
    return rt
if __name__ == '__main__':
    app.run(port=5000, debug=True)