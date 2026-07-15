import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from decisionTeory.transportationClasses import Truck, Shipping
from routing.AStar import search
from routing.distanceGetter import getDistance

def updateDomains(shipStartTime: float, shipEndTime: float, driver: Truck, shippings: list[Shipping]):
    affectedShippings = getAffectedShippings(driver, shippings)
    for shipping in affectedShippings:
        shippingEndTime = shipping.leavingHour + shipping.time
        if shipping.leavingHour < shipEndTime and shippingEndTime > shipStartTime:
            shipping.removeTruckFromDomain(driver)
    return affectedShippings

def getAffectedShippings(driver: Truck, shippings: list[Shipping]):
    return [shipping for shipping in shippings if driver in shipping.domain]

def checkFeasibility(driver: Truck, shipping: Shipping) -> tuple[bool, float]:
    # Check workday constraints
    shippings = list(driver.shippings)
    shippings.append(shipping)
    shippings.sort(key=lambda x: x.leavingHour)
    hour = driver.workdayStart
    fuelConsumption = 0
    location = driver.ubication
    for i in range(len(shippings)):
        nextLocation = shippings[i].road[0]
        if location != nextLocation:
            path, travelTime = search(location, nextLocation, hour)
            if not path:
                return False, 0
            hour += travelTime/60
            dist = getDistance(path)
            fuelConsumption += driver.calculateFuelConsumption(dist, travelTime, 0)

        if hour > shippings[i].leavingHour:
            return False, 0
        
        fuelConsumption += driver.calculateFuelConsumption(shipping.distance, shipping.time, shipping.weight)

        hour = shippings[i].leavingHour + shippings[i].time
        location = shippings[i].road[-1]

        if hour > driver.workdayEnd:
            return False, 0
    
    if fuelConsumption > driver.fuel:
        return False, 0
    return True, shipping.leavingHour

def assignShippingsToDrivers(Shippings: list[Shipping], drivers: list[Truck]) -> bool:
    for shipping in Shippings:
        shipping.setDomain(drivers)
    return backtracking(Shippings, drivers)

def backtracking(shippings: list[Shipping], drivers: list[Truck]) -> bool:
    if all(shipping.truck is not None for shipping in shippings):
        return True  # All shippings have been assigned

    unassigned = [shipping for shipping in shippings if shipping.truck is None]
    unassigned.sort(key=lambda x: len(x.domain))
    shipping = unassigned[0]

    candidates = sorted(shipping.domain, key=lambda x: len(getAffectedShippings(x, shippings)), reverse = True)
    
    for driver in candidates:
        feasible, startTime = checkFeasibility(driver, shipping)
        if not feasible:
            continue

        previous_domains = {item: list(item.domain) for item in shippings}
        previous_driver_shippings = {item: list(item.shippings) for item in drivers}
        previous_shipping_driver = shipping.truck

        shipping.assignTruck(driver)
        affectedShippings = updateDomains(startTime, shipping.leavingHour + shipping.time, driver, shippings)

        if backtracking(shippings, drivers):
            return True

        for item in shippings:
            item.domain = previous_domains[item]
        for item in drivers:
            item.shippings = previous_driver_shippings[item]
        shipping.truck = previous_shipping_driver

    return False  # No valid assignment found
