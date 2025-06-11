from flask import Flask, render_template, request
from gpio_control import fire_valve
import datetime
import csv
import os

app = Flask(__name__)
LOG_FILE = "logs/events.csv"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        duration = float(request.form["duration"])
        fire_valve(duration)

        # Log the firing event
        with open(LOG_FILE, "a") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.datetime.now(), duration])

        return render_template("index.html", status=f"Fired for {duration} s")

    return render_template("index.html", status="Ready")

if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "duration"])
    app.run(host="0.0.0.0", port=5000)
