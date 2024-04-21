from flask import Flask, render_template

app = Flask(__name__)

challenges_list = [
    {'id': 1, 'title': 'Plane Landing', 'description': 'Solve the first problem.',
        'level': "Easy", 'reward': 10, "imageurl": "plane_landing.png"},
    {'id': 2, 'title': 'Plane maneuvering', 'description': 'Solve the second problem.',
        'level': "Medium", 'reward': 50, "imageurl": "plane_maneuvering.png"},
    {'id': 3, 'title': 'Plane in bad weather', 'description': 'Solve the third problem.',
        'level': "Hard", 'reward': 100, "imageurl": "plane_weather.png"}
]


@app.route("/")
def main_page():
    return render_template("base.html")


@app.route("/challenges")
def challenges():
    return render_template("challenges.html", challenges = challenges_list)


@app.route("/forums")
def forums_page():
    return render_template("forums.html")


if __name__ == "__main__":
    app.run(debug=True)