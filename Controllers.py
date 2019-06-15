from app import app
from flask import request, make_response
from Models import *

@app.route('/api', methods=['GET'])
def get_all_contacts():
    return get_all_contacts_db()

@app.route('/api', methods=['POST'])
def post_contact():
    user_name = request.json['user_name']
    first_name = request.json['first_name']
    surname_name = request.json['surname_name']
    emails = request.json['emails']
    return post_contact_db(user_name, first_name, surname_name, emails)

@app.route('/api/<user_name>', methods=['GET'])
def get_contact(user_name):
    return get_contact_db(user_name)

@app.route('/api/<user_name>', methods=['PUT'])
def put_contact(user_name):
    user_name_updated = request.json['user_name']
    first_name = request.json['first_name']
    surname_name = request.json['surname_name']
    emails = request.json['emails']

    return put_contact_db(user_name, user_name_updated,  first_name, surname_name, emails)

@app.route('/api/<user_name>', methods=['DELETE'])
def del_contact(user_name):
    return delete_contact_db(user_name)