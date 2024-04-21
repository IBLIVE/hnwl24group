from flask import Flask, render_template

app = Flask(__name__)

challenges_list = [
    {'id': 1, 'title': 'Aircraft Landing', 'description': """

    <h2>Problem: Optimizing Runway Schedules for Aircraft Landings</h2>
    <p><strong>Description:</strong><br>
    Your task is to help manage the schedule of aircraft landings at a busy airport to avoid any delays or accidents. Given a series of aircrafts approaching to land and their expected landing times, you need to ensure each aircraft lands safely while keeping as close as possible to its scheduled time.</p>
    
    <p>The airport has a single runway, and due to safety regulations, there must be a minimum time gap between consecutive landings.</p>
    
    <p><strong>Objective:</strong><br>
    Your goal is to determine if all aircrafts can land at their scheduled times while adhering to the safety time gap. If not, find which aircrafts need to adjust their landing times and by how much.</p>
    
    <p><strong>Input:</strong><br>
    A list of aircraft identifiers and their scheduled landing times.<br>
    The required minimum time gap between landings.</p>
    
    <p><strong>Output:</strong><br>
    A determination of whether the schedule is feasible without adjustments.<br>
    If adjustments are necessary, provide a new landing schedule that ensures safety.</p>

    <p><strong>Explanation:</strong><br>
    Aircraft1 is scheduled to land at 10:00. Aircraft2, scheduled for 10:05, would violate the 10-minute gap required for safety since it is only 5 minutes after Aircraft1. Adjusting Aircraft2 to 10:10 and subsequently Aircraft3 to 10:20 maintains the required safety gap.</p>
    
    <p><strong>Constraints:</strong><br>
    The scheduled times are given in 24-hour format.<br>
    The minimum time gap will be between 5 and 30 minutes.</p>

""",
        'level': "Easy", 'reward': "10 pts", "imageurl": "plane_landing.png"},

    {'id': 2, 'title': 'Aircraft range test', 'description': """
    <h2>Problem: Testing Aircraft Range for Endurance</h2>
    <p><strong>Description:</strong><br>
    Aircraft range testing is crucial to determine the maximum distance an aircraft can travel on a single fuel load. In this challenge, you are tasked with piloting an aircraft under specific conditions to test its range capabilities. The minimum required range for this test is 50 kilometers.</p>

    <p>You will pilot a light aircraft designed for efficiency and extended flight duration. Your task is to manage fuel, speed, and altitude to maximize the aircraft's range without refueling.</p>

    <p><strong>Objective:</strong><br>
    Complete a flight that exceeds the minimum required range of 50 kilometers while maintaining optimal fuel efficiency. The test will evaluate both the aircraft's capabilities and your skill in managing flight parameters for maximum range.</p>

    <p><strong>Input:</strong><br>
    Initial fuel load (in liters).<br>
    Weather conditions including wind speed and direction.<br>
    Aircraft specifications including fuel consumption rate.</p>

    <p><strong>Output:</strong><br>
    Total distance flown (in kilometers).<br>
    Fuel remaining at the end of the test (if any).</p>

    <p><strong>Explanation:</strong><br>
    Given the conditions and the aircraft's specifications, the pilot must utilize wind conditions advantageously and adjust speed to minimize fuel consumption. Completing the test with fuel remaining after covering the required distance demonstrates successful management of the flight's range capabilities.</p>

    <p><strong>Constraints:</strong><br>
    The test must be conducted within controlled airspace dedicated to the test.<br>
    Air traffic control must be notified of the test plan and receive updates if there are deviations.<br>
    Adherence to all safety protocols for range testing must be strictly followed.</p>
    """,
        'level': "Medium", 'reward': "50 pts", "imageurl": "plane_maneuvering.png"},
    {'id': 3, 'title': 'Aircraft in bad weather', 'description': """
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