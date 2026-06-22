import numpy as np
import sys
import os
import math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from models.feature_vector import phi

MAX_SPEED = 120  # km/h, for heuristic estimation

def search(startCity: str, end: str, graph: dict, w, vectorStructure, locationDict, startingHour = 0):
    visited = set()

    queue = [(heuristic(startCity, end, locationDict),0, startCity, [])]  # (cost, estimation, city, path)

    while queue:
        estimation, cost, city, path = queue.pop(0)
        if city in visited:
            continue
        visited.add(city)
        path = path + [city]

        if city == end:
            return path, cost

        for neighbor, data in graph[city].items():
            if neighbor not in visited:
                x = data.copy()
                x["hour"] = (startingHour + cost/60) % 24  # Update hour
                edge_cost = w.dot(phi(vectorStructure, x))
                estimation = cost + edge_cost + heuristic(neighbor, end, locationDict)
                queue.append((estimation, cost + edge_cost, neighbor, path))

        queue.sort(key=lambda x: x[0])  # Sort by estimation

    return None, float('inf')  # No path found

def heuristic(cityNode: str, endCity: str, dictDict)-> float: #dictCity is a dict of cities with their geographic ubication (latitud and longitud)
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