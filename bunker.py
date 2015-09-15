from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user')
def user():
    return render_template("user.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard/index.html")

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',threaded=True)
