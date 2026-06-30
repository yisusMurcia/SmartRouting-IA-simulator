# dict structure {hour: int, weather: string, street_length: float}
import numpy as np

class Model:

    def __init__(self, trainingData: list[dict], w:dict = {}):
        if w:
            self.featureVector = w
            arr = np.zeros(len(w), dtype=float)
            for key in w:
                arr = w[key]
            self.__w = arr
            
        else:
            self.featureVector = {}
            self.buildFeatureVector(trainingData)
            arr = np.zeros(len(self.featureVector), dtype=float)

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
    
    def initializeW(self)->np.ndarray:
        return np.zeros(len(self.featureVector), dtype=float)

    def assignW(self, w:np.ndarray)->bool:
        if len(w) == len(self.featureVector):
            i = 0
            for key in self.featureVector:
                self.featureVector[key] = float(w[i])
                i+=1
            self.__w = w
            return True
        return False
    
    def wDotPhi(self, x):
        if isinstance(x, np.ndarray):
            phiX = x
        else:
            phiX = self.phi(x)
        return self.__w.dot(phiX)