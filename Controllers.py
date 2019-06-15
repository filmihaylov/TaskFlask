from app import app
from flask import request, make_response
from Models import *

@app.route('/api', methods=['GET'])
def get_all_contacts():
    return get_all_contacts_db()

@app.route('/api', methods=['POST'])
def post_contact():
    return "My flask app"

@app.route('/api/<user_name>', methods=['GET'])
def get_contact(user_name):
    return get_contact_db(user_name)

@app.route('/api/<user_name>', methods=['PUT'])
def put_contact(user_name):
    return "My flask app"

@app.route('/api/<user_name>', methods=['DEL'])
def del_contact(user_name):
    return "My flask app"