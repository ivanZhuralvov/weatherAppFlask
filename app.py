from flask import Flask, render_template, url_for, request, redirect
import requests
from pprint import pprint
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/weather',methods=["POST","GET"])
def weather():
    if request.method == 'POST':
        city_nam = request.form['city_name']

        url = 'https://api.openweathermap.org/data/2.5/find?q={}&units=metric&appid=377fb9885e37aaeef0bcc11c38b98c79'.format(city_nam)
        resp = requests.get(url)
        data = resp.json()

        #pprint(data) #the fucntion pprint helps for your to perceive json better

        return render_template('city_weather.html',data=data)
    else:
        return render_template("weather.html")


@app.route('/team')
def city_weather():
    return render_template("team.html")

    

if __name__ == "__main__":
    app.run(debug=True)