import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from transportationClasses import Driver, Shipping
from routing.AStar import search

def removeShippingToOtherDrivers(shipping: Shipping, drivers: list[Driver]) ->list[Driver]:
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
    for i in range(0, len(shippings)):
        if hour <= shippings[i].leavingHour:
            hour = shippings[i].leavingHour
        else:
            return False #two shippings overlap in time
        hour = shippings[i].leavingHour + shippings[i].time
        if i < len(shippings) - 1:
            location = shippings[i].road[-1]
            nextLocation = shippings[i+1].road[0]
            if location != nextLocation:
                path, time = search(location, nextLocation, hour)
                if not path:
                    return False
                hour += time
        
        if hour > driver.workdayEnd:
            return False
    return True