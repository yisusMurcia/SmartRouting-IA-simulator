# dict structure {hora: int, weather: string, street_length: float}
import numpy as np

def buildVectorStructure(trainingData: list[dict])-> dict:
    weather = set()
    for dict in trainingData:
        weather.add(dict["weather"])

    vectorStructure = {"hora": 1, "street_length": 2}
    index = 3
    for val in weather:
        vectorStructure[val] = index
        index+= 1
    return vectorStructure

def phi(vectorStructure, x):
    phi = np.zeros(len(vectorStructure) + 1)
    phi[0] = 1  # Bias term
    for key in vectorStructure:
        if key == "hora":
            phi[vectorStructure[key]] = x[key]
        elif key == "street_length":
            phi[vectorStructure[key]] = x[key]/1000  # Normalización
        else:
            phi[vectorStructure[key]] = 1 if x["weather"] == key else 0
    return phi