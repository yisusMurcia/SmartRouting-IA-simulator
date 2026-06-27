import numpy as np
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from models.feature_vector import FeatureVector

#graph Structure {city{nearCity1: pathData(wather, street:length)}}
def UCS(startCity: str, end: str, graph: dict, w, featureVector: FeatureVector, startingHour=0):
    visited = set()
    queue = [(0, startCity, [])]  # (cost, city, path)

    while queue:
        cost, city, path = queue.pop(0)
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
                edge_cost = w.dot(featureVector.phi(x))
                queue.append((cost + edge_cost, neighbor, path))

        queue.sort(key=lambda x: x[0])  # Sort by cost

    return None, float('inf')  # No path found