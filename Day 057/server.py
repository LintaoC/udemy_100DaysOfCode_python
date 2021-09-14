from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route("/guess/<input_name>")
def guess(input_name):
    r_age = requests.get(url=f"https://api.agify.io?name={input_name}")
    r_gender = requests.get(url=f"https://api.genderize.io?name={input_name}")
    data_age = r_age.json()
    data_gender = r_gender.json()
    estimated_age = data_age["age"]
    estimated_gender = data_gender["gender"] 
    
    return render_template("guess.html", name=input_name.title(), age=estimated_age, gender=estimated_gender)

if __name__ == "__main__":
    app.run(debug=False)