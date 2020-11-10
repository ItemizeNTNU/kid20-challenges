from flask import Flask, render_template
#from routes import *
from routes.index import index_blueprint
from routes.account import account_blueprint
from routes.login import login_blueprint
from routes.register import register_blueprint
from routes.logout import logout_blueprint

app = Flask(__name__)

app.register_blueprint(index_blueprint)
app.register_blueprint(account_blueprint)
app.register_blueprint(register_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(logout_blueprint)

if __name__ == '__main__':
    print('starting...')
    app.run('0.0.0.0', debug=False)
