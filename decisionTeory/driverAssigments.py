import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
try:
    from .transportationClasses import Driver, Shipping
except ImportError:
    from transportationClasses import Driver, Shipping
from routing.AStar import search

def removeShippingToOtherDrivers(shipping: Shipping, drivers: list[Driver]) -> list[Driver]:
    driversDomainAffected = []
    for otherDriver in drivers:
        if otherDriver.removeFromDomain(shipping):
            driversDomainAffected.append(otherDriver)
    return driversDomainAffected

def checkFeasibility(driver: Driver, shipping: Shipping) -> bool:
    # Check workday constraints
    shippings = list(driver.shippings)
    shippings.append(shipping)
    shippings.sort(key=lambda x: x.leavingHour)
    hour = 0
    for i in range(len(shippings)):
        if hour <= shippings[i].leavingHour:
            hour = shippings[i].leavingHour
        else:
            return False  # two shippings overlap in time
        hour = shippings[i].leavingHour + shippings[i].time
        if i > 0:
            location = shippings[i - 1].road[-1]
            nextLocation = shippings[i].road[0]
            if location != nextLocation:
                path, time = search(location, nextLocation, hour)
                if not path:
                    return False
                hour += time/60
        # else:
        #     location = driver.ubication
        #     nextLocation = shippings[i].road[0]
        #     if location != nextLocation:
        #         time = driver.workdayStart
        #         path, travelTime = search(location, nextLocation, time)
        #         print(f"Driver: {driver.name}, Location: {location}, Next Location: {nextLocation}, Time: {time}, Path: {path}, Travel Time: {travelTime}")
        #         if not path:
        #             return False
        #         time = travelTime/60
        #         if time > shippings[i].leavingHour:
        #             return False

        if hour > driver.workdayEnd:
            return False
    return True

def assignShippingsToDrivers(Shippings: list[Shipping], drivers: list[Driver]) -> bool:
    for driver in drivers:
        driver.setDomain(Shippings)
    return backtracking(Shippings, drivers)

def backtracking(shippings: list[Shipping], drivers: list[Driver]) -> bool:
    if all(shipping.driver is not None for shipping in shippings):
        return True  # All shippings have been assigned

    unassigned = [shipping for shipping in shippings if shipping.driver is None]

    shipping_candidates = []
    for shipping in unassigned:
        candidates = [driver for driver in drivers if shipping in driver.domain and checkFeasibility(driver, shipping)]
        if not candidates:
            return False
        shipping_candidates.append((shipping, candidates))

    shipping_candidates.sort(key=lambda item: len(item[1]))
    shipping, candidates = shipping_candidates[0]

    for driver in candidates:
        driver.assignShipping(shipping)
        print(f"{driver.name} assign {shipping.id}")
        affectedDrivers = removeShippingToOtherDrivers(shipping, drivers)

        if backtracking(shippings, drivers):
            return True  # Found a valid assignment
        print(f"{driver.name} remove assign {shipping.id}")
        driver.removeShipping(shipping)
        driver.domain.append(shipping)
        driver.domain.sort(key=lambda x: x.leavingHour)

        for otherDriver in affectedDrivers:
            otherDriver.domain.append(shipping)
            otherDriver.domain.sort(key=lambda x: x.leavingHour)

    return False  # No valid assignment found