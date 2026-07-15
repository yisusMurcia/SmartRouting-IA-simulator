import json
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from decisionTeory.transportationClasses import Truck, Shipping
from decisionTeory.expectiMax import expectimax
from routing.distanceGetter import getDistance

DATA_FILE_NAME = "data/transportationData.json"

def loadTrucksData()->list[Truck]: # Return a list of dictionaries with the Truck data
    data = []
    with open(DATA_FILE_NAME, "r", encoding="utf-8") as f:
        TruckData = json.load(f)

    records = TruckData.get("Trucks_data", TruckData) if isinstance(TruckData, dict) else TruckData

    for record in records:
        if isinstance(record, dict):
            truck = Truck(record["name"], record["max_weight"], record["ubication"], record["workday_start"], record["workday_end"])
            data.append(truck)
    return data

def loadShippingsData()->list[dict]:
    data = []
    with open(DATA_FILE_NAME, "r", encoding="utf-8") as f:
        shippingData = json.load(f)

    records = shippingData.get("shipping_data", shippingData) if isinstance(shippingData, dict) else shippingData

    for record in records:
        if isinstance(record, dict):
            data.append(record)

    return data


def buildShippings(routes, model)->list[Shipping]:
    shippings = []
    data = loadShippingsData()
    for record in data:
        time, road = expectimax(record["start_city"], record["end_city"], record["leaving_hour"], routes, model)
        distance = getDistance(road, routes)
        shipping = Shipping(road, record["leaving_hour"], record["weight"], time/60, distance)
        print(f"shipping {shipping.id}: {distance}")
        shippings.append(shipping)

    return shippings