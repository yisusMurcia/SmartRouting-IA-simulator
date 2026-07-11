# Architecture

## General system view

This system is disigned by independent but conected phases:

1. Prediction phase: Calculate the stimate traffic and time cost of a road using machine learning
2. Routing phase: Find the optimal route in a road network graph using the cost prediction created in phase 1.

## Layout

This project implements a modular structure fir scalability and maintenance.
- [Models](../models/) Contains the logic representation of the data and the prediction model.
- [Optimizers](../optimizers/) it´s the module with the mathematical optimization algorithms.
- [Routing](../routing/) implement graph search algorithms
- [Docs](../Docs/) Techincal documentation.
- [Data](../data/) Contain data necesary about the program
- [Logs](../logs/)

## Data flow and components
1. The time prediction vector is trained/loaded.
2. The city graph and the location dictionary are loaded.
3. For each driver estimate the time using expectimax for incidents in road chances and A* for optimizate the search (implementing the time prediction model)
4. Use each shipping data and travel time calculated for assign it to a set of drivers

⚠️ In development

## Technical specifications

### Time prediction

Using a linear regression model taking the next characteristic:
- Hour: this variable is treated as a 4 grade polynomial.
- Weather: This variable is taking as an aditional value for the weight vector, in $\phi(x)$ it´s a binary variable.
- Street_length: it represents the distance in meters, in $\phi(x)$ is divided by 1000.

The liniear regression uses a stochastic gradient descned as an optimizer.

### Fuel consumption

$FuelConsumption = d\cdot [ \alpha \cdot (V_{avg})^2 + \beta \cdot (w_{empty} + w_{load})]$
- d: Distance
- $\alpha$: Aerodynamic drag coefficient and engine efficiency at speed.
- $\beta$: Rolling resistance coefficient.
- $w_{empty}$: Vehicle weight.
- $w_{load}$: Shipping weight.

$\alpha$ and $\beta$ are aproximated values for each vehicle

## Data consistency and persistence

The system interacts with the [Data](../data/) directory, here you find:
- ### [Model](../data/model.json)

    Contains the feature vector and its weight, each line is estrucured like this:

- ### [road-time](../data/roadTime.json)

    Contains a list of data about the roads and the time

- ### [Train log](../data/train_log.txt)

    Contains data about the training process, include the error in the trainig, validaton data and some test data.

- ### [City coordinates](../data/coordinates.json)
    Contains each city location in lat and lon values, it´s used for the heuristic in the A* algorithm

- ### [City grap](../data/cityGraph.json)
    Contians the conections between cities and the probabilities of an accident or block in the road

    ```JSON
    "Zipaquira": {
            "Nemocon": {
                "weather": "sunny", 
                "street_length": 12000.0, 
                "accident": 0.04, 
                "block": 0.01
            },
            "Ubate": {
                "weather": "sunny", 
                "street_length": 51000.0, 
                "accident": 0.08, 
                "block": 0.02
            }
        }
    ```