import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from decisionTeory.expectiMax import expectimax
from routing.routeImportation import getRoutes
from models.trainModel import buildFeatureVector


graph = getRoutes()
model = buildFeatureVector()

for i in range(25):
    cost, path = expectimax("Bogota", "Villavicencio", i, graph, model)
    print(f"{path}\n\t expected cost: {cost} at hour {i}")