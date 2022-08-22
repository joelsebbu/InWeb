import json
import phoneBook as pb
import re
from flask import Flask,redirect,url_for,request,jsonify,abort
import requests

app= Flask(__name__)

@app.route('/')
def index():
    return '''
        <ol>
            <li><h3>/contacts</h3><ul>to list all contacts</ul></li>
        </ol>
    '''

@app.route('/contacts',methods=["GET"])
def contacts():
    return jsonify(pb.listAll())

# @app.route('/contact-name/<string:name>')
# def get_name(name):
#     return jsonify(pb.searchByName(name))

# @app.route('/contact-number/<int:number>')
# def get_number(number):
#     return jsonify(pb.searchByNumber(number))
    
# @app.route('/contact-name/<string:name>',methods=['DELETE'])
# def delete_name(name):
#     pass

# @app.route('/contact-number/<int:number>',methods=['DELETE'])
# def delete_number(number):
#     pass

# @app.route('/contact-name/<string:name>',methods=['PUT'])
# def update_name(name):
#     pass

# @app.route('/contact-number/<int:number>',methods=['PUT'])
# def update_number(number):
#     pass

@app.route('/contact',methods=['POST'])
def new_contact():
    pass

@app.route('/contact-name/<string:name>',methods=['GET','DELETE','PUT'])
def contact_name(name):
    rt=None
    if request.method =='GET':
        rt =jsonify(pb.searchByName(name))
    elif request.method == 'DELETE':
        pass 
    elif request.method == 'PUT':
        pass       
    return rt

@app.route('/contact-number/<int:number>',methods=['GET','DELETE','PUT'])
def contact_number(number):
    rt=None
    if request.method =='GET':
        rt =jsonify(pb.searchByNumber(number))
    elif request.method == 'DELETE':
        pass 
    elif request.method == 'PUT':
        pass       
    return rt

app.run(port=5000,debug=True)
