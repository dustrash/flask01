from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/<str>")
def number(str):
    return render_template("index.html", str=str)

if __name__ == '__main__':
    app.run()