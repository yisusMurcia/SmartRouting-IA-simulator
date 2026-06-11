# SmartRouting IA simulator

A dispatch and route simulation that solves congestion prediction, route planning under uncertainty, fleet assignment and autonomus navigation.

## Requirements:

### Functional requirements:
- [ ] Traffic prediction: Predict travel time between two points taking in count the time day, weather and historical congestion.
- [ ] Optimal routing: Calculate and display the lowest-cost time path between an origin and destination over a graph.
- [ ] Dr9ver scheduling: generate a weekly work schedule for N drivers with limited vehicles ensuring all buisness constraints are met without conflicts.
- [ ] Incident simulation: The simulation must suport random traffic incidents and recalculate.
- [ ] Autonomous RL Navigation: An intelligent deliver vehicle must autonomously learn to deliver packages while avoid heeavy traffic.

### Non-functional requirements:
- [ ] Functional modularity: Search state transitions and mathematical loss estimators must be impleneted as functions.
- [ ] Model accuracy: average time prediction error < 10%.
- [ ] Performance: Route computation under 10ms for a 100-node graph.

## Resources and technologies:
- Lenguage: Python.
- Libraries: NumPy