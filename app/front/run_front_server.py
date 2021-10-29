import json

from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from requests.exceptions import ConnectionError
from wtforms import IntegerField, SelectField, StringField
from wtforms.validators import DataRequired

import urllib.request
import json

class ClientDataForm(FlaskForm):
    CodingHours = StringField('CodingHours', validators=[DataRequired()]),
    CoffeeCupsPerDay = StringField('CoffeeTime', validators=[DataRequired()]),
    CoffeeTime = StringField('CoffeeTime', validators=[DataRequired()]),
    CodingWithoutCoffee = StringField('CoffeeTime', validators=[DataRequired()]),
    CoffeeType = StringField('CoffeeTime', validators=[DataRequired()]),
    #CoffeeSolveBugs = StringField('CoffeeTime', validators=[DataRequired()]),
    Gender = StringField('CoffeeTime', validators=[DataRequired()]),
    Country = StringField('CoffeeTime', validators=[DataRequired()]),
    AgeRange = StringField('CoffeeTime', validators=[DataRequired()])


app = Flask(__name__)
app.config.update(
    CSRF_ENABLED=True,
    SECRET_KEY='you-will-never-guess',
)

def get_prediction(CodingHours, CoffeeCupsPerDay, CoffeeTime, CodingWithoutCoffee, CoffeeType, Gender, Country, AgeRange):
    body = {'CodingHours': CodingHours,
            'CoffeeCupsPerDay': CoffeeCupsPerDay,
            'CoffeeTime': CoffeeTime,
            'CodingWithoutCoffee': CodingWithoutCoffee,
            'CoffeeType': CoffeeType,
            'Gender': Gender,
            'Country': Country,
            'AgeRange': AgeRange}

    myurl = "http://127.0.0.0:8180/predict"
    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    #print (jsondataasbytes)
    response = urllib.request.urlopen(req, jsondataasbytes)
    return json.loads(response.read())['predictions']

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/predicted/<response>')
def predicted(response):
    response = json.loads(response)
    print(response)
    return render_template('predicted.html', response=response)


@app.route('/predict_form', methods=['GET', 'POST'])
def predict_form():
    form = ClientDataForm()
    data = dict()
    if request.method == 'POST':
        data['CodingHours'] = request.form.get('CodingHours')
        data['CoffeeCupsPerDay'] = request.form.get('CoffeeCupsPerDay')
        data['CoffeeTime'] = request.form.get('CoffeeTime')
        data['CodingWithoutCoffee'] = request.form.get('CodingWithoutCoffee')
        data['CoffeeType'] = request.form.get('CoffeeType')
        data['Gender'] = request.form.get('Gender')
        data['Country'] = request.form.get('Country')
        data['AgeRange'] = request.form.get('AgeRange')

        try:
            response = str(get_prediction(
                                      data['CodingHours'],
                                      data['CoffeeCupsPerDay'],
                                      data['CoffeeTime'],
                                      data['CodingWithoutCoffee'],
                                      data['CoffeeType'],
                                      data['Gender'],
                                      data['Country'],
                                      data['AgeRange']))
            print(response)
        except ConnectionError:
            response = json.dumps({"error": "ConnectionError"})
        return redirect(url_for('predicted', response=response))
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(host='127.0.0.0', port=8181, debug=True)
