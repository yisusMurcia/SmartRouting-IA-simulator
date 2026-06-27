# dict structure {hour: int, weather: string, street_length: float}
import numpy as np

class FeatureVector:

    def __init__(self, trainingData: list[dict]):
        self.featureVector = {}
        self.buildFeatureVector(trainingData)

    def buildFeatureVector(self, data: list[dict]):
        for reg in data:
             for key in self.__buildDict(reg):
                 self.featureVector[key] = 0


    def __buildDict(self, x):
        phi = {}
        for i in range(5):
            phi[f"hour_grade_{i}"] = (x["hour"]/24)**i
        phi["street_length"] = x["street_length"]/1000
        phi[x["weather"]] = x["hour"]

        return phi
    
    def phi(self, x):
        phiDict = self.__buildDict(x);
        phiVector = np.zeros(len(self.featureVector))
        i = 0
        for key in self.featureVector:
            if key in phiDict:
                phiVector[i] = phiDict[key]
            i+= 1
        return phiVector
    
    def initializeW(self):
        return np.zeros(len(self.featureVector))