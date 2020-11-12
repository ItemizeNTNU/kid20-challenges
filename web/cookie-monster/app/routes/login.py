from flask import Blueprint, render_template, request, make_response, url_for

import mysql.connector 

login_blueprint = Blueprint('login', __name__)

config = {
        'user': 'db_user',
        'password': 'db_password',
        'host': 'db',
        'port': '3306',
        'database': 'db_test'}


@login_blueprint.route("/login", methods=['post', 'get'])
def login():
	if (request.method == 'POST'):
		username = request.form.get('username')  # access the data inside 
		password = request.form.get('password')

		connection = mysql.connector.connect(**config)
		crsr = connection.cursor(prepared=True)
		sql = 'SELECT username FROM Users WHERE username=%s AND password=%s'

		crsr.execute(sql, (username, password,))
		result = crsr.fetchone()
		connection.close()

		if (result is None):
			return render_template('login.html',message = "Login failed")
		resp = make_response(render_template('index.html', message="You are now logged in as " + username +". Enjoy your stay :)", username=username))
		resp.set_cookie('username_cookie_monster', username)
		return resp

	else: 
		return render_template('login.html')



