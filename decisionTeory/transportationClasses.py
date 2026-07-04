class Shipping:
    id = 0
    def __init__(self,  road: list[str], leavingHour: float, weight: float, time: float):
        self.id = Shipping.id
        self.road = road
        self.leavingHour = leavingHour
        self.weight = weight
        self.time = time
        self.driver: None | Driver = None
        Shipping.id += 1

class Driver:
    id = 0

    def __init__(self, name: str, maxWeight: float, ubication: str, workdayStart: float, workdayEnd: float):
        self.name = name
        self.id = Driver.id
        self.maxWeight = maxWeight
        self.ubication = ubication
        self.workdayStart = workdayStart
        self.workdayEnd = workdayEnd        
        Driver.id += 1
        self.domain:list[Shipping] = []
        self.shippings: list[Shipping] = []

    def setDomain(self, domain: list[Shipping]):
        self.domain = [shipping for shipping in domain if (shipping.weight <= self.maxWeight and shipping.leavingHour >= self.workdayStart and (shipping.leavingHour + shipping.time) <= self.workdayEnd)]
        self.domain.sort(key=lambda x: x.leavingHour)

    def removeFromDomain(self, shipping: Shipping)->bool:
        if shipping in self.domain:
            self.domain.remove(shipping)
            return True
        return False
    
    def assignShipping(self, shipping: Shipping)->bool:
        if shipping in self.domain:
            shipping.driver = self
            self.domain.remove(shipping)
            self.shippings.append(shipping)
            return True
        return False
    
    def removeShipping(self, shipping: Shipping)->bool:
        if shipping in self.shippings:
            shipping.driver = None
            self.shippings.remove(shipping)
            return True
        return False