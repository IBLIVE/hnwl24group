from flask import Flask

app = Flask(__name__)


@app.route("/")
def main_page():
    return "main page"


@app.route("/challenges")
def challenges_page():
    return "placeholder for challenges"


@app.route("/forums")
def forums_page():
    return "placeholder for forums"

if __name__ == "__main__":
    app.run(debug=True)