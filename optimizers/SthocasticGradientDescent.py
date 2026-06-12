epochs = 500

def stochasticGradientDescent(functionLoss, gradientFunctionLoss, trainExamples, w):
    iterations = 1
    for i in range(epochs):
        for x, y in trainExamples:
            gradient = gradientFunctionLoss(x, y, w)
            eta = 0.0001 / (1 + 0.01 * iterations)
            if eta < 1e-10:
                break
            w = w - gradient * eta
            iterations += 1
        print(f"Epoch: {i}, Weights: {w}")
    print(f"Final Weights: {w}, Loss: {functionLoss(trainExamples, w)}")
    return w