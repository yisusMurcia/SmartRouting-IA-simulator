import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from linearRegression import linearRegression

# Datos sintéticos para entrenar y probar el modelo de predicción de tráfico (Fase 1)
traffic_data = [
    {"hora": 8, "weather": "sunny", "street_length": 450.5, "travel_time": 12.3},
    {"hora": 18, "weather": "rainy", "street_length": 800.0, "travel_time": 28.5},
    {"hora": 12, "weather": "cloudy", "street_length": 300.2, "travel_time": 6.8},
    {"hora": 22, "weather": "sunny", "street_length": 1200.5, "travel_time": 15.1},
    {"hora": 7, "weather": "rainy", "street_length": 550.0, "travel_time": 22.4},
    {"hora": 15, "weather": "sunny", "street_length": 950.8, "travel_time": 14.2},
    {"hora": 3, "weather": "foggy", "street_length": 600.0, "travel_time": 11.5},
    {"hora": 17, "weather": "sunny", "street_length": 750.3, "travel_time": 21.0},
    {"hora": 9, "weather": "rainy", "street_length": 400.0, "travel_time": 18.2},
    {"hora": 13, "weather": "cloudy", "street_length": 1100.1, "travel_time": 17.5},
    {"hora": 19, "weather": "sunny", "street_length": 500.0, "travel_time": 13.8},
    {"hora": 2, "weather": "rainy", "street_length": 350.2, "travel_time": 7.2},
    {"hora": 14, "weather": "sunny", "street_length": 900.0, "travel_time": 13.0},
    {"hora": 8, "weather": "foggy", "street_length": 850.5, "travel_time": 26.3},
    {"hora": 16, "weather": "rainy", "street_length": 650.0, "travel_time": 21.9},
    {"hora": 20, "weather": "cloudy", "street_length": 420.7, "travel_time": 9.5},
    {"hora": 11, "weather": "sunny", "street_length": 1300.0, "travel_time": 18.4},
    {"hora": 5, "weather": "sunny", "street_length": 250.0, "travel_time": 3.2},
    {"hora": 18, "weather": "foggy", "street_length": 700.4, "travel_time": 25.1},
    {"hora": 12, "weather": "rainy", "street_length": 500.0, "travel_time": 15.6}
]

training_data = [[dict, dict["travel_time"]] for dict in traffic_data]

linearRegression(training_data)