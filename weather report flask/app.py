import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return """<h1>Welcome to weather app
    type your city name using / after the url</h1>"""
@app.route('/<city>')
def search_city(city):
    API_KEY = '545e4dda108efcb1fd2411dbf65603b7'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}'
    response = requests.get(url).json()
    if response.get('cod') != 200:
        message = response.get('message', '')
        return f"<h1 style='color:red'>Error getting temperature for {city.title()}. Error message = {message}</h1>"
    current_temperature = response.get('main', {}).get('temp')
    if current_temperature:
        current_temperature_celsius = round(current_temperature - 273.15, 2)
        return f"<h1 style='color:coral'>Current temperature of {city.title()} is {current_temperature_celsius} &#8451;</h1>"
    else:
        return f"<h1 style='color:red'>Error getting temperature for {city.title()}</h>"

app.run(host="localhost", port=80, debug=True)