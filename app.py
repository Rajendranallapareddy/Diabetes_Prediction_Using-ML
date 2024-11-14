from csv import reader
from flask import *
import joblib
import numpy as np

app = Flask(__name__)

ob = joblib.load('diabetic_model.joblib')
ob2 = joblib.load('diabetic_model.joblib')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Prediction')
def prediction():
    return render_template('predict.html')

@app.route('/About')
def about():
    return render_template('about.html')

@app.route('/Aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/Login')
def login():
    return render_template('login.html')

@app.route('/Register')
def register():
    return render_template('register.html')

@app.route('/Prediction', methods =['POST'])
def raja():
    if request.method == "POST":
       v1 = float(request.form['i1'])     
       v2 = float(request.form['i2'])
       v3 = float(request.form['i3'])
       v4 = float(request.form['i4'])
       v5 = float(request.form['i5'])
       v6 = float(request.form['i6'])
       v7 = float(request.form['i7'])
       v8 = float(request.form['i8'])
    
    a = [[v1,v2,v3,v4,v5,v6,v7,v8]]

    predd1 = ob.predict(a)
    predd2 = ob2.predict(a)


    
    result1 = " "

    if predd1 == predd2 :
       if predd1 == 0:
           result1 = "You do not have diabetes ❤️"
       elif predd1 == 1 :
           result1 = "You are having diabetes 🙁"
    else:
       if predd1 == 0:
           result1 = "You do not have diabetes ❤️"
       elif predd1 == 1 :
           result1 = "You are having diabetes 🙁"
    
    return render_template('result.html',result2=result1)


if __name__=='__main__':
    app.run('127.0.0.2', port=5000,debug=True)


