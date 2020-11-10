from flask import Blueprint, render_template, request
import mysql.connector 

register_blueprint = Blueprint('register', __name__)

config = {
        'user': 'db_user',
        'password': 'db_password',
        'host': 'db',
        'port': '3306',
        'database': 'db_test'}


@register_blueprint.route("/register", methods=['post', 'get'])
def register():
	if (request.method == 'POST'):
		username = request.form.get('username')
		password = request.form.get('password')
		name = request.form.get('name')
		favmuppet = request.form.get('favmuppet')
		favsound = request.form.get('favsound')

		connection = mysql.connector.connect(**config)
		crsr = connection.cursor(prepared=True)
		sql = 'INSERT INTO Users VALUES (%s, %s, %s, %s, %s)'
		
		try:
			crsr.execute(sql, (username, password,name, favmuppet, favsound))
			connection.commit()
			message = "Registration sucessfull, you can now login"
			newpage = 'login.html' 
		except:
			message = "Registration failed, username already exists"
			newpage = 'register.html'
		
		connection.close()
		return render_template(newpage,message = message)
	else: 
		return render_template('register.html')



