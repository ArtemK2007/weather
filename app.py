from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "8292190e0d8110db3385199884f65846"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None

    if request.method == "POST":
        city = request.form.get("city")

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=uk"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data.get("sys", {}).get("country") == "RU":
                weather = "💩"
            else:
                weather = data
        else:
            weather = {"error": "Місто не знайдено"}

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
