import json
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from decisionTeory.transportationClasses import Driver, Shipping
from decisionTeory.expectiMax import expectimax

DATA_FILE_NAME = "data/transportationData.json"

def loadDriversData()->list[Driver]: # Return a list of dictionaries with the driver data
    data = []
    with open(DATA_FILE_NAME, "r", encoding="utf-8") as f:
        driverData = json.load(f)

    records = driverData.get("drivers_data", driverData) if isinstance(driverData, dict) else driverData

    for record in records:
        if isinstance(record, dict):
            driver = Driver(record["name"], record["max_weight"], record["ubication"], record["workday_start"], record["workday_end"])
            data.append(driver)
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
        shipping = Shipping(road, record["leaving_hour"], record["weight"], time/60)
        shippings.append(shipping)

    return shippings