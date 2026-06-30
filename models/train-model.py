import sys
import os
import math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from models.model import Model
from linearRegression import linearRegression

DATA_FILE_NAME = "data/road-time.txt"
W_FILE_NAME = "data/model.txt"
TRAIN_LOG_NAME = "data/train_log.txt"

TRAIN_PORCENTAGE = 0.8
VALIDATON_PORCENTAGE = 0.1


def loadData(): # Return pair of x and y
    data_x = []
    data_y = []
    file = open(DATA_FILE_NAME, 'r')
    lines = file.read().split("\n")
    
    for line in lines:
        line = line.strip().rstrip(',')
        if not line:
            continue
        x = {}
        y = 0

        parts = line.split(", ")
        for part in parts:
            key, val = part.split(": ")
            
            # convert if possible
            try:
                if '.' in val:
                    val = float(val)
                else:
                    val = int(val)
            except ValueError:
                pass
            
            if key == "time":
                y = val
            else:
                x[key] = val
                
        data_x.append(x)
        data_y.append(y)

    file.close()
    return data_x, data_y

def saveW(w:dict)->bool: #Save the featureVector of the class, return if the operation succeded
    file = None
    try:
        file = open(W_FILE_NAME, 'w')
        for key, val in w.items():
            file.write(f"{key} {val}\n")
    except:
        return False
    finally:
        if file:
            file.close()
    return True

def readW()->dict:
    w = {}
    try:
        file = open(W_FILE_NAME, 'r')
        lines = file.readlines()
        for line in lines:
            key, val = line.split(" ")
            w[key] = float(val)

        file.close()
    except:
        w = {}
        
    return w


def buildFeatureVector()->Model:
    #Compare dates from road-time and feature-vector, if road-time is more recent retrain the model
    train_data_time = os.path.getmtime(DATA_FILE_NAME)
    w_data_time = 0
    try:
        w_data_time = os.path.getmtime(W_FILE_NAME)
    except FileNotFoundError:
        w_data_time = -1


    featureVector = None
    if w_data_time >= train_data_time: 
        w = readW()
        featureVector = Model([], w)
    else: #train model
        featureVector = trainModel()

    return featureVector


def trainModel()->Model:
    x, y = loadData()
    data_train = x[0:int(len(x)*0.8)]
    fv = Model(x)
    x = [fv.phi(x) for x in x]
    y_train = y[0: len(data_train)]
    x_train = x[0:int(len(x)*0.8)]
    w, loss = linearRegression(fv.initializeW(), x_train, y_train)
    fv.assignW(w)
    saveW(fv.featureVector)

    #Save log
    file = open(TRAIN_LOG_NAME, 'w')
    file.write(f"Square loss: {loss}, loss: {math.sqrt(loss)}\n")
    file.write("Validation:\n")
    square_sum = 0
    size = int(len(x)* VALIDATON_PORCENTAGE)
    for i in range(0, size):
        predicted = fv.wDotPhi(x_train[i])
        file.write(f"Predicted: {predicted}, actual: {y[i]}\n")
        square_sum+= (predicted - y[i])** i
    loss = square_sum/ size
    file.write(f"Square loss: {loss}, loss: {math.sqrt(loss)}\n")


    file.write("Test:\n")
    square_sum = 0
    size = len(x) - len(data_train)
    for i in range(len(data_train), len(x)):
        predicted = fv.wDotPhi(x[i])
        file.write(f"Predicted: {predicted}, actual: {y[i]}\n")
        square_sum+= (predicted - y[i])** 2

    loss = square_sum/ size
    file.write(f"Square loss: {loss}, loss: {loss**(1/2)}\n")

    file.close()

    return fv

buildFeatureVector()