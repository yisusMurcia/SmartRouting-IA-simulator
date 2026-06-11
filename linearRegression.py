import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from feature_vector import buildVectorStructure, phi
import numpy as np
from optimizers.SthocasticGradientDescent import stochasticGradientDescent


def lossFunction(trainingData, w):
    return 1/len(trainingData) * sum((y - w.dot(x))**2 for x, y in trainingData)

def gradientLossFunction(x, y, w):
    return (2 * (w.dot(x) - y) * x)

def initializeWeights(x):
    w = np.zeros(len(x))
    return w

def linearRegression(trainingData):
    xArr = []
    for x, y in trainingData:
        xArr.append(x)

    vectorStructure = buildVectorStructure(xArr)
    for i in range(len(trainingData)):
        trainingData[i][0] = phi(vectorStructure, trainingData[i][0])
    w = np.zeros(len(vectorStructure) + 1)

    return stochasticGradientDescent(lossFunction, gradientLossFunction, trainingData, w)