from flask import Flask, render_template, request, redirect
import orjson
import base64

app = Flask(__name__, static_url_path="/")

# Check cookie for base64 encoded JSON user object, if show_flag is true, do it.
@app.route('/')
def hello_world():
    user = request.cookies.get('user')
    if user is None:
        return redirect('/login')

    user = orjson.loads(base64.decodebytes(request.cookies.get('user').encode()))
    if user.get('show_flag'):
        return render_template('flag.html')
    return render_template('no_access.html', user=user)

# Set base64 encoded JSON user object as cookie
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        resp = redirect('/')
        username = request.form.get('username')
        password = request.form.get('password')
        user = { 'username': username, 'password': password, 'show_flag': False }
        base64_user = base64.encodebytes(orjson.dumps(user)).replace(b'\n',b'')
        resp.set_cookie('user', base64_user)
        return resp
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
