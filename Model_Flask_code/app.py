import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
from flask_cors import CORS, cross_origin
from sklearn.preprocessing import PolynomialFeatures

app = Flask(__name__)

#Importing our linear model and standard scaler
pm = pickle.load(open('model.pkl', 'rb'))
sm = pickle.load(open('scaler.pkl','rb'))
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def home():
    return render_template('index.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():

    #Getting the user input from the .html dashboard
    int_features = [str(x) for x in request.form.values()]

    print(int_features)

    #Encoding the categorical features

    encode_class = {'Compact Car': [0,0,0,0,0,0,0,0,0,0,0,0],
                'Large Car': [1,0,0,0,0,0,0,0,0,0,0,0],
               'Midsize Car': [0,1,0,0,0,0,0,0,0,0,0,0],
               'Midsize-Large Station Wagon': [0,0,1,0,0,0,0,0,0,0,0,0],
               'Minicompact Car': [0,0,0,1,0,0,0,0,0,0,0,0],
               'Minivan': [0,0,0,0,1,0,0,0,0,0,0,0],
               'Small Pickup Truck': [0,0,0,0,0,1,0,0,0,0,0,0],
               'Small Station Wagon': [0,0,0,0,0,0,1,0,0,0,0,0],
               'Sport Utility Vehicle': [0,0,0,0,0,0,0,1,0,0,0,0],
               'Standard Pickup Truck': [0,0,0,0,0,0,0,0,1,0,0,0],
               'Subcompact Car': [0,0,0,0,0,0,0,0,0,1,0,0],
               'Two Seater': [0,0,0,0,0,0,0,0,0,0,1,0],
               'Van': [0,0,0,0,0,0,0,0,0,0,0,1]}
    encode_drive = {'All-Wheel Drive': [0,0],
               'Front-Wheel Drive': [1,0],
               'Rear-Wheel Drive': [0,1]}
    encode_trany = {'Manual': [1],
               'Automatic': [0]}
    
    engine = [int(int_features[0]), int(int_features[1]), np.log(float(int_features[2]))]

    encoded_class = encode_class[int_features[3]]
    
    encoded_drive = encode_drive[int_features[4]]
    
    encoded_trany = encode_trany[int_features[5]]

    engine_scaled = sm.transform([engine])

    engine = engine_scaled[0].tolist()

    car = engine + encoded_class + encoded_drive + encoded_trany

    car = np.expand_dims(car, axis=0)

    #Checking the format of our new input features

    print(car)

    #Predictin the MPG with the new input features

    pred_y_new = pm.predict(car)

    output = round(pred_y_new[0],2)

    #Printing the prediction to the dashboard

    return render_template('index.html', prediction_text=(f'Estimated miles per gallon: {str(output)}'))
    
if __name__ == "__main__":
    app.run(debug=True)