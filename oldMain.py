from models.trainModel import buildFeatureVector
from routing.routeImportation import getRoutes
from decisionTeory.transportation_data_loading import loadTrucksData, buildShippings
from decisionTeory.driverAssigments import assignShippingsToDrivers

model = buildFeatureVector()
routes = getRoutes()

drivers = loadTrucksData()
shippings = buildShippings(routes, model)

if assignShippingsToDrivers(shippings, drivers):
    for driver in drivers:
        print(f"Driver: {driver.driverName}, Assigned Shippings: {[shipping.id for shipping in driver.shippings]}")
else:
    print ("No feasible assignment found for the given shippings and drivers.")