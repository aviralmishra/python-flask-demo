from flask import Flask

from ..weather.weather import get_weather_forecast

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello there!</p>"

@app.route("/weather")
def weather():
    return get_weather_forecast({'lat': 30.2748,'lon': -97.7404})
