from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

amziu_history = []

def calculate_mars_age(birthdate):
    mars_year_days = 687
    earth_days_in_year = 365.25
    
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    today = datetime.today()
    age_in_days = (today - birthdate).days
    age_in_mars_years = age_in_days / mars_year_days

    return round(age_in_mars_years, 2)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=['POST'])
def results():
    birthdate = request.form['birthdate']
    mars_age = calculate_mars_age(birthdate)
    amziu_history.append({'birthdate': birthdate, 'mars_age': mars_age})
    return render_template("results.html", mars_age=mars_age, birthdate=birthdate)


@app.route('/history')    
def history():
    pass

if __name__ == '__main__':
    app.run(debug=True)
