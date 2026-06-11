import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from feature_vector import buildVectorStructure, phi

test_traffic_data = [
    {"hora": 9, "weather": "sunny", "street_length": 520.0},
    {"hora": 19, "weather": "rainy", "street_length": 750.5},
    {"hora": 11, "weather": "cloudy", "street_length": 310.0},
    {"hora": 23, "weather": "sunny", "street_length": 1150.2},
    {"hora": 6, "weather": "rainy", "street_length": 480.0},
    {"hora": 16, "weather": "sunny", "street_length": 980.4},
    {"hora": 4, "weather": "foggy", "street_length": 550.0},
    {"hora": 18, "weather": "sunny", "street_length": 820.1},
    {"hora": 10, "weather": "rainy", "street_length": 420.5},
    {"hora": 14, "weather": "cloudy", "street_length": 1050.0},
    {"hora": 21, "weather": "sunny", "street_length": 510.8},
    {"hora": 1, "weather": "rainy", "street_length": 300.0},
    {"hora": 13, "weather": "sunny", "street_length": 880.5},
    {"hora": 7, "weather": "foggy", "street_length": 900.0},
    {"hora": 15, "weather": "rainy", "street_length": 600.2},
    {"hora": 22, "weather": "cloudy", "street_length": 450.0},
    {"hora": 10, "weather": "sunny", "street_length": 1250.7},
    {"hora": 4, "weather": "sunny", "street_length": 200.0},
    {"hora": 17, "weather": "foggy", "street_length": 780.3},
    {"hora": 11, "weather": "rainy", "street_length": 490.0}
]

vectorStructure = buildVectorStructure(test_traffic_data)
print(vectorStructure)

for regist in test_traffic_data:
    print(phi(vectorStructure, regist))