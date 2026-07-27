# SmartRouting IA simulator

A dispatch and route simulation that solves congestion prediction, route planning under uncertainty, fleet assignment and autonomus navigation. This software analyze traffic flow, time traveling and accident chances for assign the best route to make a ship and with this assigment the program determines who is the best driver for make the trip.

## Requirements:

### Functional requirements:
- [x] Traffic prediction: Predict travel time between two points taking in count the time day, weather and historical congestion.
- [x] Optimal routing: Calculate and display the lowest-cost time path between an origin and destination over a graph.
- [x] Driver scheduling: generate a weekly work schedule for N drivers with limited vehicles ensuring all buisness constraints are met without conflicts.
- [x] Incident simulation: The simulation must suport random traffic incidents and recalculate.

### Non-functional requirements:
- [x] Functional modularity: Search state transitions and mathematical loss estimators must be impleneted as functions.
- [ ] Model accuracy: average time prediction error < 10%.
- [ ] Performance: Route computation under 10ms for a 100-node graph.

## Resources and technologies:
- Lenguage: Python.
- Libraries: NumPy, Pytest
