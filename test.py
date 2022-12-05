import numpy as np
import pickle

RF_model = pickle.load(open('Random_Forest_Classifier.pickle','rb'))

def predict_failure(Type,Air_temperature_K,Process_temperature_K,Rotational_speed_rpm,Torque_Nm,Tool_wear_min):
    x = np.zeros(6)
    x[0] = Type
    x[1] = Air_temperature_K
    x[2] = Process_temperature_K
    x[3] = Rotational_speed_rpm
    x[4] = Torque_Nm
    x[5] = Tool_wear_min

    result = RF_model.predict([x])[0]
    return result
