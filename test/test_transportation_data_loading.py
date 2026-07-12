import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from decisionTeory.transportationClasses import Driver, Shipping
from models.trainModel import buildFeatureVector
from routing.routeImportation import getRoutes
from decisionTeory.transportation_data_loading import loadDriversData, loadShippingsData, buildShippings

def test_loadingDriversData():
    drivers = loadDriversData()
    assert isinstance(drivers, list)
    assert all(isinstance(driver, Driver) for driver in drivers)

def test_loadingShippingsData():
    shippings = loadShippingsData()
    assert isinstance(shippings, list)

def test_buildShippings():
    model = buildFeatureVector()
    routes = getRoutes()
    shippings = buildShippings(routes, model)
    assert isinstance(shippings, list)
    assert all(isinstance(shipping, Shipping) for shipping in shippings)