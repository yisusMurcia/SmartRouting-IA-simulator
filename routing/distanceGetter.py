import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from routing.routeImportation import getRoutes

def getDistance(path: list[str], routes: dict= getRoutes())->float:
    distance = 0
    for i in range(len(path) -1):
        distance += routes[path[i]][path[i+1]]["street_length"]
    return distance