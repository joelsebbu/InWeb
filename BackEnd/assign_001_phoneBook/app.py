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
            <li><h3>/contacts</h3>
                <ul>to list all contacts</ul>
            </li>
        </ol>
    '''

@app.route('/contacts',methods=["GET"])
def contacts():
    return jsonify(pb.listAll())

@app.route('/contact-name/<string:name>')
def contact_name(name):
    return jsonify(pb.searchByName(name))

@app.route('/contact-number/<int:number>')
def contact_number(number):
    return jsonify(pb.searchByNumber(number))
    
app.run(port=5000,debug=True)
