import numpy as np
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from models.model import Model
from routing.timeHeuristic import getExpectedTime
from routing.routeImportation import getRoutes
from models.trainModel import buildFeatureVector

def search(startCity: str, end: str, startingHour = 0.0, graph: dict = getRoutes(), model: Model = buildFeatureVector())-> tuple[list, float]:
    visited = set()

    queue = [(getExpectedTime(startCity, end),0, startCity, [])]  # (cost, estimation, city, path)

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
                edge_cost = model.wDotPhi(x)
                estimation = cost + edge_cost + getExpectedTime(neighbor, end)
                queue.append((estimation, cost + edge_cost, neighbor, path))

        queue.sort(key=lambda x: x[0])  # Sort by estimation

    return [], float('inf')  # No path found