from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import test
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

app = Flask(__name__)

@app.route('/predict_failure', methods = ['GET','POST'])
def prediction():
    data = request.form
    if request.method == 'GET':
        Type = float(data['Type'])
        if Type == 'L':
            Type = 0
        elif Type == 'M':
            Type = 0.5
        else:
            Type = 1
        Air_temperature_K = float(data['Air_temperature_K'])
        Process_temperature_K = float(data['Process_temperature_K'])
        Rotational_speed_rpm = float(data['Rotational_speed_rpm'])
        Torque_Nm = float(data['Torque_Nm'])
        Tool_wear_min = float(data['Tool_wear_min'])
        print('Type,Air_temperature_K,Process_temperature_K,Rotational_speed_rpm,Torque_Nm,Tool_wear_min',Type,Air_temperature_K,Process_temperature_K,Rotational_speed_rpm,Torque_Nm,Tool_wear_min)
        result = test.predict_failure(Type,Air_temperature_K,Process_temperature_K,Rotational_speed_rpm,Torque_Nm,Tool_wear_min)

    if result == 0:
        return 'No failure in machine.'
    else:
        return 'Failure in machine.'
    return 'Failure is: {}'.format(result)

if __name__ == '__main__':
    print('Starting Python Flask Server For Machine Failure Prediction.......')
    app.run(debug=True)