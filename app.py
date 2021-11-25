from flask import Flask, render_template, request
from flask import jsonify 
import requests
import pickle
import numpy as np
import sklearn 

app = Flask(__name__)
model_1 = pickle.load(open('HL_model.pkl', 'rb'))
model_2 = pickle.load(open('CL_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        X1 = float(request.form['X1'])
        X2 = float(request.form['X2'])
        X3 = float(request.form['X3'])
        X4 = float(request.form['X4'])
        X5 = float(request.form['X5'])
        X6 = float(request.form['X6'])
        X7 = float(request.form['X7'])
        X8 = float(request.form['X8'])
        Load = request.form['Load']
        if(Load=='HL'):
            prediction = model_1.predict([[X1, X2, X3, X4, X5, X6, X7, X8]])
            text = 'Heating Load '
        else:
            prediction = model_2.predict([[X1, X2, X3, X4, X5, X6, X7, X8]])
            text = 'Cooling Load '
            
        output = round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry, Invalid input")
        else:
            return render_template('index.html',prediction_text='''{} is {}'''.format(text, output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
