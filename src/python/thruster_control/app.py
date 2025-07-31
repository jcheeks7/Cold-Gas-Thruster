from flask import Flask, render_template, request
from gpio_control import fire_valve
import csv, os
from datetime import datetime

app = Flask(__name__)
LOG_FILE = "logs/events.csv"
os.makedirs("logs", exist_ok=True)
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="") as f:
        csv.writer(f).writerow(["timestamp","duration"])

@app.route("/", methods=["GET","POST"])
def index():
    message = None
    if request.method == "POST":
        try:
            duration = float(request.form["duration"])
            fire_valve(duration)  # actual GPIO pulse
            ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(LOG_FILE, "a", newline="") as f:
                csv.writer(f).writerow([ts, duration])
            message = f"✅ Fired for {duration:.1f}s"
        except Exception as e:
            message = f"❌ Error: {e}"

    # load last 5
    logs = []
    with open(LOG_FILE) as f:
        rows = list(csv.DictReader(f))
        logs = rows[-5:]
    return render_template("index.html", message=message, logs=logs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
