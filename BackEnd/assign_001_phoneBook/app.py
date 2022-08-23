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

@app.route('/contacts',methods=['POST'])
def new_contact():
    request_data = request.json
    if len(request_data) == 2:
        return jsonify(pb.addRecord(request_data["name"],int(request_data["number"])))    
    else:
        abort(404)
    

@app.route('/contact-name/<string:name>',methods=['GET','DELETE','PUT'])
def contact_name(name):
    rt=None
    if request.method =='GET':
        rt =jsonify(pb.searchByName(name))
    elif request.method == 'DELETE':
        rt = jsonify(pb.deleteByName(name)) 
    elif request.method == 'PUT':
        pass       
    return rt

@app.route('/contact-number/<int:number>',methods=['GET','DELETE','PUT'])
def contact_number(number):
    rt=None
    if request.method =='GET':
        rt =jsonify(pb.searchByNumber(number))
    elif request.method == 'DELETE':
        rt= jsonify(pb.deleteByNumber(number))
    elif request.method == 'PUT':
        pass       
    return rt

app.run(port=5000,debug=True)
