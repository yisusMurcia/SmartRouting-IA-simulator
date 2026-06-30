import math


epochs = 500
penalization = 0.9

def stochasticGradientDescent(functionLoss, gradientFunctionLoss, trainExamples, w):
    iterations = 1
    for i in range(epochs):
        for x, y in trainExamples:
            gradient = gradientFunctionLoss(x, y, w)
            eta = 0.01 / math.sqrt(iterations)  # Learning rate decay
            if eta < 1e-10:
                break
            w = w - eta* (gradient + penalization * w)  # L2 regularization
            iterations += 1
    loss = functionLoss(trainExamples, w)
    print(f"Final Weights: {w}, Loss: {loss}")
    return w, loss