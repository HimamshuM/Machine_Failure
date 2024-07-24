import pickle
from flask import Flask,request,app, jsonify,url_for,render_template
import pandas as pd
import numpy as np 


app = Flask(__name__)
# load the model
regmodel = pickle.load(open('regmodel.plk', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    