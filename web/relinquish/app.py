import flask
import hashlib
import random

app = flask.Flask(__name__, static_url_path="/")

salt = "5ec176e060a3254441a7c747b410f6e0"

with open("users.txt") as f:
    users = f.read().strip().splitlines()

users[273] = 'admin'


def hash(name):
    name = salt + name
    name = name.encode()
    return hashlib.md5(hashlib.sha1(hashlib.sha256(hashlib.sha384(hashlib.sha512(name).digest()).digest()).digest()).digest()).hexdigest()


time = 0
users = [{"username": name, "last_active": (time := time + random.randint(0, 5)), "hash": hash(name)} for name in users]


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/login")
def loginGet():
    return flask.render_template("login.html")


@app.route("/api/active/<int:stop>")
def listUsers(stop):
    return flask.jsonify(users[:stop])


@app.route("/login", methods=['POST'])
def login():
    username = flask.request.form['username']
    password = flask.request.form['password']
    if not password == hash(username):
        return flask.render_template("login.html", error="Wrong username or password.")
    data = "This user does not have any interesting notes."
    if username == "admin":
        data = "KID20{4t_l3a5t_h3_do3sn7_5end_cl3ar7ext_p4s5w0rd5}"
    return flask.render_template("user.html", name=username, data=data)


if __name__ == "__main__":
    print('starting...')
    app.run('0.0.0.0', debug=False)
