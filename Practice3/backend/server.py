from flask import Flask, url_for, render_template, request, flash, redirect
from flask_mysqldb import MySQL
import os
from hashlib import md5

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e3ed846b8b7024817cbbb5d96bdaff5f22e5b7a4'   # generated by os.urandom(20).hex()
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'dvwa'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dvwa'

mysql = MySQL(app)

################################################

black_list = []
@app.before_request
def load_black_list():
    global black_list
    with open('static/black_list.txt') as fh:
        for line in fh:
            black_list.append(line.strip())

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        psw = request.form['password']

        if psw in black_list:
            return redirect(url_for('confirm'))

        psw_hash = md5(psw.encode('utf-8')).hexdigest()
        # print(psw_hash)

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE user = %(username)s AND password = %(password)s LIMIT 1", {'username': username, 'password': psw_hash})
        res = cursor.fetchone()
        # print(str(res[3]))

        if res:
            flash(f'Welcome to the password protected area, {str(res[3])}', category='success')
        else:
            flash('Username and/or password incorrect', category='error')

        cursor.close()
        return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/confirm')
def confirm():
    link = '/auth/' + os.urandom(20).hex()
    return render_template('authentication.html', link=link)

@app.route('/auth/<auth_code>/')
def auth(auth_code):
    print('ok')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)