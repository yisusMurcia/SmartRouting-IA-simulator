import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from models.model import Model

test_traffic_data = [
    {"hour": 9, "weather": "sunny", "street_length": 520.0},
    {"hour": 19, "weather": "rainy", "street_length": 750.5},
    {"hour": 11, "weather": "cloudy", "street_length": 310.0},
    {"hour": 23, "weather": "sunny", "street_length": 1150.2},
    {"hour": 6, "weather": "rainy", "street_length": 480.0},
    {"hour": 16, "weather": "sunny", "street_length": 980.4},
    {"hour": 4, "weather": "foggy", "street_length": 550.0},
    {"hour": 18, "weather": "sunny", "street_length": 820.1},
    {"hour": 10, "weather": "rainy", "street_length": 420.5},
    {"hour": 14, "weather": "cloudy", "street_length": 1050.0},
    {"hour": 21, "weather": "sunny", "street_length": 510.8},
    {"hour": 1, "weather": "rainy", "street_length": 300.0},
    {"hour": 13, "weather": "sunny", "street_length": 880.5},
    {"hour": 7, "weather": "foggy", "street_length": 900.0},
    {"hour": 15, "weather": "rainy", "street_length": 600.2},
    {"hour": 22, "weather": "cloudy", "street_length": 450.0},
    {"hour": 10, "weather": "sunny", "street_length": 1250.7},
    {"hour": 4, "weather": "sunny", "street_length": 200.0},
    {"hour": 17, "weather": "foggy", "street_length": 780.3},
    {"hour": 11, "weather": "rainy", "street_length": 490.0}
]

featureVector = Model(test_traffic_data)

for regist in test_traffic_data:
    print(featureVector.phi(regist))