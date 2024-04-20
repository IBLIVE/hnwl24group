from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("base.html")


@app.route("/challenges")
def challenges():
    return render_template("challenges.html")


@app.route("/challenges")
def challenges_page():
    return "placeholder for challenges"


@app.route("/forums")
def forums_page():
    return "placeholder for forums"

if __name__ == "__main__":
    app.run(debug=True)