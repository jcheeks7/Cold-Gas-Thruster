from flask import Flask, render_template, request
from gpio_control import fire_valve
import csv
from datetime import datetime
import os

app = Flask(__name__)
LOG_FILE = "logs/events.csv"

os.makedirs("logs", exist_ok=True)

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "duration"])

@app.route("/", methods=["GET", "POST"])
def index():
    message = None
    if request.method == "POST":
        try:
            duration = float(request.form["duration"])
            fire_valve(duration)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(LOG_FILE, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([timestamp, duration])
            message = f"Valve fired for {duration:.1f} seconds."
        except Exception as e:
            message = f"Error: {e}"

    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            reader = list(csv.DictReader(file))
            logs = reader[-5:] if len(reader) > 5 else reader

    return render_template("index.html", status="Ready", message=message, logs=logs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
