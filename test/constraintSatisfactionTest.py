import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from decisionTeory.transportationClasses import Driver, Shipping
from decisionTeory.driverAssigments import assignShipmentsToDrivers

envios_lista = [
    Shipping(road=["Bogota", "Chiapinero"], leavingHour=12.0, weight=200.0, time=1.0),
    Shipping(road=["Chiapinero", "Usaquen"], leavingHour=13.5, weight=400.0, time=1.0),
    Shipping(road=["Usaquen", "Zipaquira"], leavingHour=15.0, weight=900.0, time=1.5),
    Shipping(road=["Zipaquira", "Nemocon"], leavingHour=16.5, weight=300.0, time=1.0),
    Shipping(road=["Bogota", "Chipaque"], leavingHour=17.5, weight=150.0, time=1.2)
]

conductores_lista = [
    Driver(name="Juan", maxWeight=500.0, ubication="Ubate", workdayStart=6.0, workdayEnd=14.0),
    Driver(name="Carlos", maxWeight=600.0, ubication="Tunja", workdayStart=7.0, workdayEnd=17.0),
    Driver(name="Andres", maxWeight=1200.0, ubication="Ubate", workdayStart=10.0, workdayEnd=18.0),
    Driver(name="Marta", maxWeight=600.0, ubication="Bogota", workdayStart=12.0, workdayEnd=20.0)
]

result = assignShipmentsToDrivers(envios_lista, conductores_lista)
print(result)
assert result is True, "The solver should find a feasible assignment for this test instance."

for driver in conductores_lista:
    print(f"Driver: {driver.name}, Assigned Shippings: {[shipping.id for shipping in driver.shipments]}")