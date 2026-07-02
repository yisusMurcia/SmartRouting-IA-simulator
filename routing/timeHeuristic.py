import math, numpy as np
import json

MAX_SPEED = 120  # km/h, for heuristic estimation

def getExpectedTime(cityNode: str, endCity: str)-> float:
    coordinates = loadCoordinates()
    lat1, lon1 = coordinates[cityNode]["lat"], coordinates[cityNode]["lon"]
    lat2, lon2 = coordinates[endCity]["lat"], coordinates[endCity]["lon"]
    if(lat1 == lat2 and lon1 == lon2):
        return 0.0
    # Calculate the Haversine distance
    R = 6371  # Earth radius in kilometers
    dLat = np.radians(lat2 - lat1)
    dLon = np.radians(lon2 - lon1)
    distance=  2*R* math.asin(math.sqrt(math.sin(dLat/2)**2 + math.cos(np.radians(lat1)) * math.cos(np.radians(lat2)) * math.sin(dLon/2)**2)) #km

    return distance/MAX_SPEED * 60 # Return estimated time in minutes, assuming max speed

def loadCoordinates():
    with open('data/coordinates.json', 'r') as f:
        coordinates = json.load(f)
    return coordinates