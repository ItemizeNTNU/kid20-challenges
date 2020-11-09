from flask import Flask, render_template, request, redirect
import orjson
import codecs

app = Flask(__name__)

# Check cookie for pickled user object, if changed, allow pwn
@app.route('/')
def hello_world():
    user = request.cookies.get('user')
    if user is None:
        return redirect('/login')

    user = orjson.loads(codecs.decode(request.cookies.get('user').encode(), "base64"))
    if user.get('show_flag'):
        return render_template('flag.html')
    return render_template('no_access.html', user=user)

# Set pickled user object as cookie
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        resp = redirect('/')
        username = request.form.get('username')
        password = request.form.get('password')
        user = { 'username': username, 'password': password, 'show_flag': False }
        base64_user = codecs.encode(orjson.dumps(user), "base64")
        resp.set_cookie('user', base64_user)
        return resp
    return render_template('login.html')

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
