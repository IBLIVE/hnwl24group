from flask import Flask, render_template

app = Flask(__name__)

challenges_list = [
    {'id': 1, 'title': 'Plane Landing', 'description': """

    <h2>Problem: Optimizing Runway Schedules for Plane Landings</h2>
    <p><strong>Description:</strong><br>
    Your task is to help manage the schedule of plane landings at a busy airport to avoid any delays or accidents. Given a series of planes approaching to land and their expected landing times, you need to ensure each plane lands safely while keeping as close as possible to its scheduled time.</p>
    
    <p>The airport has a single runway, and due to safety regulations, there must be a minimum time gap between consecutive landings.</p>
    
    <p><strong>Objective:</strong><br>
    Your goal is to determine if all planes can land at their scheduled times while adhering to the safety time gap. If not, find which planes need to adjust their landing times and by how much.</p>
    
    <p><strong>Input:</strong><br>
    A list of plane identifiers and their scheduled landing times.<br>
    The required minimum time gap between landings.</p>
    
    <p><strong>Output:</strong><br>
    A determination of whether the schedule is feasible without adjustments.<br>
    If adjustments are necessary, provide a new landing schedule that ensures safety.</p>
    
    <p><strong>Example:</strong><br>
    Input: Scheduled landings: ["Plane1: 10:00", "Plane2: 10:05", "Plane3: 10:15"]<br>
    Required time gap: 10 minutes<br>
    Output: False (indicating adjustments are needed)<br>
    Adjusted schedule: ["Plane1: 10:00", "Plane2: 10:10", "Plane3: 10:20"]</p>
    
    <p><strong>Explanation:</strong><br>
    Plane1 is scheduled to land at 10:00. Plane2, scheduled for 10:05, would violate the 10-minute gap required for safety since it is only 5 minutes after Plane1. Adjusting Plane2 to 10:10 and subsequently Plane3 to 10:20 maintains the required safety gap.</p>
    
    <p><strong>Constraints:</strong><br>
    The number of planes scheduled to land will not exceed 100.<br>
    The scheduled times are given in 24-hour format.<br>
    The minimum time gap will be between 5 and 30 minutes.</p>

""",
        'level': "Easy", 'reward': "10 pts", "imageurl": "plane_landing.png"},
    {'id': 2, 'title': 'Plane maneuvering', 'description': """
    <h2>Problem: Precision Maneuvering in Varied Terrain</h2>
    <p><strong>Description:</strong><br>
    As a pilot of a small aircraft, your task is to navigate through challenging terrain where traditional landing techniques are not feasible. This includes maneuvering through narrow valleys, avoiding tall obstacles, and making precision landings on short or uneven surfaces.</p>

    <p>Your aircraft is equipped with advanced navigation aids and variable-response control surfaces that allow precise adjustments in flight dynamics.</p>

    <p><strong>Objective:</strong><br>
    Your goal is to complete a series of maneuvers that are scored based on accuracy, adherence to the flight path, and overall time taken. You must also ensure the safety of your aircraft by maintaining a minimum distance from terrain and obstacles.</p>

    <p><strong>Input:</strong><br>
    A series of geographic coordinates that define the required flight path.<br>
    Environmental conditions such as wind speed and direction.</p>

    <p><strong>Output:</strong><br>
    Your performance score based on precision, time, and safety.<br>
    A log of any safety violations or deviations from the flight path.</p>

    <p><strong>Example:</strong><br>
    Input: Flight path coordinates: [[lat1, lon1], [lat2, lon2], ..., [latN, lonN]]<br>
    Wind conditions: 10 km/h from the northeast<br>
    Output: Score: 95/100<br>
    Violations: None</p>

    <p><strong>Explanation:</strong><br>
    The challenge involves navigating a predefined route marked by waypoints. The pilot must adjust the aircraft's approach at each waypoint considering the wind conditions to optimize the flight path and landing approach. Points are deducted for excessive deviation from the path or unsafe maneuvers.</p>

    <p><strong>Constraints:</strong><br>
    You must complete the course within the specified time to qualify for scoring.<br>
    The aircraft must not come within 50 meters of any obstacle unless landing.</p>
    """,
        'level': "Medium", 'reward': "50 pts", "imageurl": "plane_maneuvering.png"},
    {'id': 3, 'title': 'Plane in bad weather', 'description': """
    <h2>Problem: Navigating Through Severe Weather Conditions</h2>
    <p><strong>Description:</strong><br>
    Pilots must often contend with challenging weather conditions that can significantly impact flight safety and operational efficiency. In this challenge, you will simulate a flight through a series of adverse weather conditions, including heavy rain, strong winds, and low visibility.</p>

    <p>You will be piloting a medium-sized aircraft equipped with standard instrumentation and weather radar. Your primary objectives are to maintain the safety of your aircraft and minimize delays.</p>

    <p><strong>Objective:</strong><br>
    Successfully navigate through the designated flight path while managing the impacts of changing weather conditions. You must make real-time decisions based on weather updates and radar readings to alter your flight path or altitude as necessary for safety.</p>

    <p><strong>Input:</strong><br>
    Real-time weather data along the flight path including wind speed and direction, precipitation levels, and visibility.<br>
    Flight path waypoints detailing the intended route.</p>

    <p><strong>Output:</strong><br>
    A detailed log of any deviations from the original flight plan, including reasons based on weather conditions.<br>
    An overall performance score that considers safety, efficiency, and adherence to air traffic control directives.</p>

    <p><strong>Example:</strong><br>
    Input: Weather data: {"wind": "25 knots from NW", "rain": "heavy", "visibility": "2 km"}<br>
    Flight Path: [[lat1, lon1], [lat2, lon2], ..., [latN, lonN]]<br>
    Output: Deviations: [{"lat": lat2, "lon": lon2, "reason": "diverted due to severe turbulence"}]<br>
    Score: 88/100</p>

    <p><strong>Explanation:</strong><br>
    Given the severe weather conditions encountered during the flight, decisions to divert from the planned route were necessary to avoid areas of turbulence and maintain a safe operating environment. The pilot’s performance is evaluated on their ability to make these adjustments while minimizing disruptions and maintaining communication with air traffic control.</p>

    <p><strong>Constraints:</strong><br>
    All maneuvers and route adjustments must be communicated to and approved by air traffic control.<br>
    The aircraft must maintain a minimum altitude except during takeoff and landing phases.<br>
    Safety protocols for severe weather must be adhered to strictly.</p>
    
    """,
        'level': "Hard", 'reward': "100 pts", "imageurl": "plane_weather.png"}
]


@app.route("/")
def main_page():
    return render_template("main_page.html")


@app.route("/challenges")
def challenges():
    return render_template("challenges.html", challenges = challenges_list)


@app.route("/forums")
def forums_page():
    return render_template("forums.html")


if __name__ == "__main__":
    app.run(debug=True)