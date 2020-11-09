from flask import Flask, Response, render_template
import random
app = Flask(__name__, static_url_path='')

with open("quotes.txt") as f:
    quotes = f.read().strip().split("\n")

@app.route("/")
def quote():
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote)

@app.route("/news")
def news():
    return render_template("news.html")


if __name__ == "__main__":
    print('starting...')
    app.run("0.0.0.0", debug=False)