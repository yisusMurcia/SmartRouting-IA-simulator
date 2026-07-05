class Driver:
    id = 0

    def __init__(self, name: str, maxWeight: float, ubication: str, workdayStart: float, workdayEnd: float):
        self.name = name
        self.id = Driver.id
        self.maxWeight = maxWeight
        self.ubication = ubication
        self.workdayStart = workdayStart
        self.workdayEnd = workdayEnd if workdayEnd > workdayStart else workdayStart + 24    
        Driver.id += 1
        self.domain:list[Shipping] = []
        self.shippings: list[Shipping] = []

class Shipping:
    id = 0
    def __init__(self,  road: list[str], leavingHour: float, weight: float, time: float):
        self.id = Shipping.id
        self.road = road
        self.leavingHour = leavingHour
        self.weight = weight
        self.time = time
        self.driver: None | Driver = None
        self.domain: list[Driver] = []
        Shipping.id += 1

    def setDomain(self, domain: list[Driver]):
        self.domain = [driver for driver in domain if (self.weight <= driver.maxWeight and self.leavingHour >= driver.workdayStart and (self.leavingHour + self.time) <= driver.workdayEnd)]
        self.domain.sort(key=lambda x: x.workdayStart)

    def removeDriverFromDomain(self, driver: Driver):
        if driver in self.domain:
            self.domain.remove(driver)

    def assignDriver(self, driver: Driver):
        self.driver = driver
        if self not in driver.shippings:
            driver.shippings.append(self)
        self.removeDriverFromDomain(driver)

    def removeDriver(self):
        if self.driver:
            if self.driver not in self.domain:
                self.domain.append(self.driver)
            if self in self.driver.shippings:
                self.driver.shippings.remove(self)
            self.driver = None
