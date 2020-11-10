from flask import Blueprint, render_template, request
import mysql.connector 

account_blueprint = Blueprint('account', __name__)


config = {
        'user': 'db_user',
        'password': 'db_password',
        'host': 'db',
        'port': '3306',
        'database': 'db_test'}

@account_blueprint.route('/account', methods=['post', 'get'])
def account():
	username = request.cookies.get('username')
	connection = mysql.connector.connect(**config)
	crsr = connection.cursor(prepared=True)
	sql = 'SELECT * FROM Users WHERE username=%s'

	crsr.execute(sql, (username,))
	result = crsr.fetchone()
	connection.close()
	if (result is None):
		return render_template('login.html',message = "Login first to see account")
	else:
		return render_template('account.html',name=result[2], favmuppet=result[3], favsound=result[4])