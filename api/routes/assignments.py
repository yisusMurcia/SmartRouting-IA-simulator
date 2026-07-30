from fastapi import APIRouter, Depends
from api.utilities.request import get_model, get_routes
from decisionTeory.transportation_data_loading import loadTrucksData, buildShipments
from decisionTeory.driverAssigments import assignShipmentsToDrivers

router = APIRouter()

@router.get("/")
async def make_assignments(model = Depends(get_model), routes = Depends(get_routes)):
    drivers = loadTrucksData()
    shipments = buildShipments(routes, model)
    assignation = {}
    if assignShipmentsToDrivers(shipments, drivers):
        for driver in drivers:
            assignation[driver.driverName] = [shipment.id for shipment in driver.shipments]
    return assignation