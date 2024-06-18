from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from UserModule import User
from ClientModule import Client

app = Flask(__name__)

user_manager = User()
client_manager = Client()


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/registration', methods=['GET'])
def show_register():
    return render_template('registration.html')


@app.route('/registration', methods=['POST'])
def register():
    last_name = request.form['lastname']
    first_name = request.form['firstname']
    middle_name = request.form['middlename']
    date_of_birth = request.form['birthdate']
    inn = request.form['inn']
    responsible_full_name = request.form['responsible']

    new_client = client_manager.create(last_name, first_name, middle_name, date_of_birth, inn, responsible_full_name)
    return redirect(url_for('home'))


@app.route('/login', methods=['GET'])
def show_login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = user_manager.find_one({'login': username, 'password': password})
    if user:
        return redirect(url_for('account', user_id=user['_id']))
    else:
        return 'Invalid username or password'


if __name__ == '__main__':
    app.run(debug=True)