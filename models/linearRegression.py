import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from optimizers.StochasticGradientDescent import stochasticGradientDescent


def lossFunction(trainingData, w):
    return 1/len(trainingData) * sum((y - w.dot(x))**2 for x, y in trainingData)

def gradientLossFunction(x, y, w):
    return (2 * (w.dot(x) - y) * x)

def linearRegression(w, x, y):
    trainData = []
    for i in range(len(x)):
        trainData.append([x[i], y[i]])
    return stochasticGradientDescent(lossFunction, gradientLossFunction, trainData, w)