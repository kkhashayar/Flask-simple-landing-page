from flask import Flask, render_template, url_for


app = Flask(__name__)


app.config["SECRET_KEY"]="mysecret_key"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
