import json

def getRoutes():
    with open("data/cityGraph.json", "r", encoding="utf-8") as f:
        routes = json.load(f)
    return routes