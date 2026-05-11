from flask import Flask, request, render_template_string
import requests
import datetime
import os

app = Flask(__name__)

AUTHOR = "Nikodem Kamiński"
PORT = int(os.environ.get("PORT", 8080))

# Informacje w logach po uruchomieniu kontenera
print(f"Data uruchomienia: {datetime.datetime.now()}")
print(f"Autor aplikacji: {AUTHOR}")
print(f"Port TCP: {PORT}")

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Aplikacja pogodowa</title>
</head>
<body>
    <h2>Sprawdź aktualną pogodę</h2>

    <form method="post">
        Kraj:<br>
        <input type="text" name="country" required><br><br>

        Miasto:<br>
        <input type="text" name="city" required><br><br>

        <input type="submit" value="Sprawdź pogodę">
    </form>

    {% if weather %}
        <h3>Aktualna pogoda:</h3>
        <p>{{ weather }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None

    if request.method == "POST":
        city = request.form["city"]

        # Pobranie aktualnej pogody
        url = f"https://wttr.in/{city}?format=3"

        try:
            response = requests.get(url)
            weather = response.text
        except Exception as e:
            weather = f"Błąd: {e}"

    return render_template_string(HTML, weather=weather)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)