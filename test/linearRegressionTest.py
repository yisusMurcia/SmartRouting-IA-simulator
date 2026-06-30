import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from models.linearRegression import linearRegression
from models.model import Model

# Datos sintéticos para entrenar y probar el modelo de predicción de tráfico (Fase 1)
traffic_data = [
    {"hour": 8, "weather": "sunny", "street_length": 450.5, "travel_time": 12.3},
    {"hour": 18, "weather": "rainy", "street_length": 800.0, "travel_time": 28.5},
    {"hour": 12, "weather": "cloudy", "street_length": 300.2, "travel_time": 6.8},
    {"hour": 22, "weather": "sunny", "street_length": 1200.5, "travel_time": 15.1},
    {"hour": 7, "weather": "rainy", "street_length": 550.0, "travel_time": 22.4},
    {"hour": 15, "weather": "sunny", "street_length": 950.8, "travel_time": 14.2},
    {"hour": 3, "weather": "foggy", "street_length": 600.0, "travel_time": 11.5},
    {"hour": 17, "weather": "sunny", "street_length": 750.3, "travel_time": 21.0},
    {"hour": 9, "weather": "rainy", "street_length": 400.0, "travel_time": 18.2},
    {"hour": 13, "weather": "cloudy", "street_length": 1100.1, "travel_time": 17.5},
    {"hour": 19, "weather": "sunny", "street_length": 500.0, "travel_time": 13.8},
    {"hour": 2, "weather": "rainy", "street_length": 350.2, "travel_time": 7.2},
    {"hour": 14, "weather": "sunny", "street_length": 900.0, "travel_time": 13.0},
    {"hour": 8, "weather": "foggy", "street_length": 850.5, "travel_time": 26.3},
    {"hour": 16, "weather": "rainy", "street_length": 650.0, "travel_time": 21.9},
    {"hour": 20, "weather": "cloudy", "street_length": 420.7, "travel_time": 9.5},
    {"hour": 11, "weather": "sunny", "street_length": 1300.0, "travel_time": 18.4},
    {"hour": 5, "weather": "sunny", "street_length": 250.0, "travel_time": 3.2},
    {"hour": 18, "weather": "foggy", "street_length": 700.4, "travel_time": 25.1},
    {"hour": 12, "weather": "rainy", "street_length": 500.0, "travel_time": 15.6}
]

training_data = [[dict, dict["travel_time"]] for dict in traffic_data]
featureVector = Model(traffic_data)

xArr = [featureVector.phi(x) for x, y in training_data]
yArr = [y for x, y in training_data]

w, loss = linearRegression(featureVector.initializeW(), xArr[0:15], yArr[0: 15])
featureVector.assignW(w)

print("Validation:")
for i in range(9, 15):
    print(f"Predicted: {featureVector.wDotPhi(xArr[i])}, Actual: {yArr[i]}")

print("Test")
sumValues = 0
for i in range(15, len(training_data)):
    prediction = featureVector.wDotPhi(xArr[i])
    print(f"Predicted: {prediction}, Actual: {yArr[i]}")
    sumValues += (prediction - yArr[i]) ** 2
print(f"Squared error: {sumValues/5}")
print(featureVector.featureVector)