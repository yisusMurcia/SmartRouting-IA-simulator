import numpy as np
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from models.feature_vector import phi
from routing.HaversineFormula import getExpectedTime

def search(startCity: str, end: str, graph: dict, w, vectorStructure, locationDict, startingHour = 0):
    visited = set()

    queue = [(getExpectedTime(startCity, end, locationDict),0, startCity, [])]  # (cost, estimation, city, path)

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
                estimation = cost + edge_cost + getExpectedTime(neighbor, end, locationDict)
                queue.append((estimation, cost + edge_cost, neighbor, path))

        queue.sort(key=lambda x: x[0])  # Sort by estimation

    return None, float('inf')  # No path found