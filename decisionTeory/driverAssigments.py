import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
try:
    from .transportationClasses import Driver, Shipping
except ImportError:
    from transportationClasses import Driver, Shipping
from routing.AStar import search

def updateDomains(shipStartTime: float, shipEndTime: float, driver: Driver, shippings: list[Shipping]):
    affectedShippings = [shipping for shipping in shippings if driver in shipping.domain]
    for shipping in affectedShippings:
        shippingEndTime = shipping.leavingHour + shipping.time
        if shipping.leavingHour < shipEndTime and shippingEndTime > shipStartTime:
            shipping.removeDriverFromDomain(driver)
    return affectedShippings

def checkFeasibility(driver: Driver, shipping: Shipping) -> tuple[bool, float]:
    # Check workday constraints
    shippings = list(driver.shippings)
    shippings.append(shipping)
    shippings.sort(key=lambda x: x.leavingHour)
    hour = driver.workdayStart
    location = driver.ubication
    for i in range(len(shippings)):
        nextLocation = shippings[i].road[0]
        if location != nextLocation:
            path, travelTime = search(location, nextLocation, hour)
            if not path:
                return False, 0
            hour += travelTime/60

        if hour > shippings[i].leavingHour:
            return False, 0

        hour = shippings[i].leavingHour + shippings[i].time
        location = shippings[i].road[-1]

        if hour > driver.workdayEnd:
            return False, 0
    return True, shipping.leavingHour

def assignShippingsToDrivers(Shippings: list[Shipping], drivers: list[Driver]) -> bool:
    for shipping in Shippings:
        shipping.setDomain(drivers)
    return backtracking(Shippings, drivers)

def backtracking(shippings: list[Shipping], drivers: list[Driver]) -> bool:
    if all(shipping.driver is not None for shipping in shippings):
        return True  # All shippings have been assigned

    unassigned = [shipping for shipping in shippings if shipping.driver is None]
    unassigned.sort(key=lambda x: len(x.domain))
    shipping = unassigned[0]

    candidates = sorted(shipping.domain, key=lambda x: len(x.shippings))

    for driver in candidates:
        feasible, startTime = checkFeasibility(driver, shipping)
        if not feasible:
            continue

        previous_domains = {item: list(item.domain) for item in shippings}
        previous_driver_shippings = {item: list(item.shippings) for item in drivers}
        previous_shipping_driver = shipping.driver

        shipping.assignDriver(driver)
        affectedShippings = updateDomains(startTime, shipping.leavingHour + shipping.time, driver, shippings)

        if backtracking(shippings, drivers):
            return True

        for item in shippings:
            item.domain = previous_domains[item]
        for item in drivers:
            item.shippings = previous_driver_shippings[item]
        shipping.driver = previous_shipping_driver

    return False  # No valid assignment found
