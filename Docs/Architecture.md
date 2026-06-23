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

## Data flow and components
1. The time prediction model is trained.
2. The city graph and the location dictionary are defined.
3. Use the prediction model and the city graph for calculate the cost (time) of the travel, and the location is used to estimate the future cost using the Haversine´s formula divided in a selected max speed.
4. Return the optimal secuence of the travel and the estimated time.

⚠️ In development

## Technical specifications

### Time prediction

Using a linear regression model taking the next characteristic:
- Hour: this variable is treated as a 4 grade polynomial.
- Weather: This variable is taking as an aditional value for the weight vector, in $\phi(x)$ it´s a binary variable.
- Street_length: it represents the distance in meters, in $\phi(x)$ is divided by 1000.

The liniear regression uses a stochastic gradient descned as an optimizer.

### City Graph
It´s represented as a dictionary of dictionaries, the key of the graph is the city name, this inner dict has a a value of other city (keys) that are included in the city graph, as values it coontains data about the weather and the street lenght of the road whose connect these cities.

⚠️ In development