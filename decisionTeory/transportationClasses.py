class Truck:
    def __init__(self, driverName: str, maxWeight: float, ubication: str, workdayStart: float, workdayEnd: float, truckWeight = 11000, fuel = 450, alpha = 2.1e-4, beta = 6.2e-6):
        self.driverName = driverName
        self.maxWeight = maxWeight
        self.ubication = ubication
        self.workdayStart = workdayStart
        self.workdayEnd = workdayEnd if workdayEnd > workdayStart else workdayStart + 24
        self.truckWeight = truckWeight
        self.fuel = fuel
        self.alpha = alpha
        self.beta = beta
        self.domain:list[Shipping] = []
        self.shippings: list[Shipping] = []

    def calculateFuelConsumption(self, distance: float, time: float, weight: float) -> float:
        distance = distance / 1000 #convert m to Km
        avgSpeed = distance / time
        fuelC = distance * (self.alpha * avgSpeed**2 + self.beta* (weight + self.truckWeight)) 
        print(f"driver {self.driverName}: {fuelC} L")
        return fuelC

class Shipping:
    id = 0
    def __init__(self,  road: list[str], leavingHour: float, weight: float, time: float, distance: float):
        self.id = Shipping.id
        self.road = road
        self.leavingHour = leavingHour
        self.weight = weight
        self.time = time
        self.truck: None | Truck = None
        self.domain: list[Truck] = []
        self.distance = distance
        Shipping.id += 1

    def setDomain(self, domain: list[Truck]):
        self.domain = [Truck for Truck in domain if (self.weight <= Truck.maxWeight and self.leavingHour >= Truck.workdayStart and (self.leavingHour + self.time) <= Truck.workdayEnd)]
        self.domain.sort(key=lambda x: x.workdayStart)

    def removeTruckFromDomain(self, Truck: Truck):
        if Truck in self.domain:
            self.domain.remove(Truck)

    def assignTruck(self, Truck: Truck):
        self.Truck = Truck
        if self not in Truck.shippings:
            Truck.shippings.append(self)
        self.removeTruckFromDomain(Truck)

    def removeTruck(self):
        if self.Truck:
            if self.Truck not in self.domain:
                self.domain.append(self.Truck)
            if self in self.Truck.shippings:
                self.Truck.shippings.remove(self)
            self.Truck = None
