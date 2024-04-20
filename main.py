from flask import Flask, render_template

app = Flask(__name__)

challenges_list = [
    {'id': 1, 'title': 'Plane Landing', 'description': 'Solve the first problem.', 'level': "Easy", 'reward': 10},
    {'id': 2, 'title': 'Plane maneuvering', 'description': 'Solve the second problem.', 'level': "Medium", 'reward': 50},
    {'id': 3, 'title': 'Plane in bad weather', 'description': 'Solve the third problem.', 'level': "Hard", 'reward': 100}
]

@app.route("/")
def main_page():
    return render_template("base.html")


@app.route("/challenges")
def challenges():
    return render_template("challenges.html", challenges = challenges_list)

@app.route("/challenges/<int:challenge_id>")
def challenge_view(challenge_id):
    challenge = next((c for c in challenges_list if c['id'] == challenge_id), None)
    if challenge:
        return render_template('challenge_detail.html', challenge=challenge)
    else:
        return "Challenge not found", 404




@app.route("/forums")
def forums_page():
    return render_template("forums.html")

if __name__ == "__main__":
    app.run(debug=True)