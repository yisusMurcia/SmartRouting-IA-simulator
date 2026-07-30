from models.trainModel import buildFeatureVector
from routing.routeImportation import getRoutes
from decisionTeory.transportation_data_loading import loadTrucksData, buildShipments
from decisionTeory.driverAssigments import assignShipmentsToDrivers

model = buildFeatureVector()
routes = getRoutes()

drivers = loadTrucksData()
shippings = buildShipments(routes, model)

if assignShipmentsToDrivers(shippings, drivers):
    for driver in drivers:
        print(f"Driver: {driver.driverName}, Assigned Shippings: {[shipping.id for shipping in driver.shipments]}")
else:
    print ("No feasible assignment found for the given shippings and drivers.")