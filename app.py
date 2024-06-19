from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from bson.objectid import ObjectId
from UserModule import User
from ClientModule import Client

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'

user_manager = User()
client_manager = Client()


@app.route('/')
def home():
    if 'user_id' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('show_login'))


@app.route('/login', methods=['GET'])
def show_login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = user_manager.find_one({'login': username, 'password': password})
    if user:
        session['user_id'] = user['_id']
        return redirect(url_for('account', user_id=user['_id']))
    else:
        return 'Invalid username or password'


@app.route('/logout')
def logout():
    if 'user_id' in session:
        session.pop('user_id')
    return redirect(url_for('show_login'))


@app.route('/account/<user_id>')
def account(user_id):
    if 'user_id' in session and session['user_id'] == user_id:
        # Получаем информацию о пользователе из базы данных
        user = user_manager.find_one({'_id': ObjectId(user_id)})
        # Получаем информацию о клиенте из базы данных
        clients = client_manager.find({'responsible_full_name': user['full_name']})
        clients = list(clients)
        # Передаём информацию о клиенте в шаблон
        return render_template('account.html', clients=clients)
    else:
        return redirect(url_for('show_login'))


if __name__ == '__main__':
    app.run(debug=True)