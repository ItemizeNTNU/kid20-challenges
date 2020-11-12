from flask import Blueprint, render_template, make_response

logout_blueprint = Blueprint('logout', __name__)

@logout_blueprint.route("/logout")
def logout():
	resp = make_response(render_template('index.html', message="You are now logged out of the service", logout=True))
	resp.set_cookie('username_cookie_monster', '', expires=0)
	return resp



