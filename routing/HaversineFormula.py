import math, numpy as np

MAX_SPEED = 120  # km/h, for heuristic estimation

def getExpectedTime(cityNode: str, endCity: str, dictDict)-> float: #dictCity is a dict of cities with their geographic ubication (latitud and longitud)
    lat1, lon1 = dictDict[cityNode]["lat"], dictDict[cityNode]["lon"]
    lat2, lon2 = dictDict[endCity]["lat"], dictDict[endCity]["lon"]
    if(lat1 == lat2 and lon1 == lon2):
        return 0.0
    # Calculate the Haversine distance
    R = 6371  # Earth radius in kilometers
    dLat = np.radians(lat2 - lat1)
    dLon = np.radians(lon2 - lon1)
    distance=  2*R* math.asin(math.sqrt(math.sin(dLat/2)**2 + math.cos(np.radians(lat1)) * math.cos(np.radians(lat2)) * math.sin(dLon/2)**2)) #km

    return distance/MAX_SPEED * 60 # Return estimated time in minutes, assuming max speed