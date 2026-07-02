import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from routing.AStar import search
from routing.routeImportation import getRoutes
from models.trainModel import buildFeatureVector

def weatherProbChanges(weather: str, accident: float, block: float):
    if weather == "rainy":
        accident *= 1.5
        block *= 1.5
    elif weather == "cloudy":
        accident *= 1.2
        block *= 1.2
        
    if accident + block > 1:
        accident = 1 - block
    return accident, block

def modifyTimeCost(time: float, roadStatus):
    if roadStatus == "accident":
        time *= 2.5  # Incremento por accidente
    elif roadStatus == "block":
        time *= 3.0  # Incremento por bloqueo
    return time

def expectimax(node: str, endCity: str, hour: float, graph = getRoutes(), model = buildFeatureVector(), time: float = 0, depth: int = 5) -> tuple[float, list]:
    # CASO BASE 1: Llegamos al destino con éxito
    if node == endCity:
        return 0.0, [node]
    
    # CASO BASE 2: Límite de profundidad (usamos la heurística optimista)
    if depth == 0:
        path, cost = search(node, endCity, hour, graph, model)
        return cost, [node] + path[1:]  # Excluimos el nodo actual del camino para evitar duplicados

    min_cost = float('inf')
    best_path = []

    for neighbor, data in graph[node].items():
        x = data.copy()
        x["hour"] = (hour + time/60) % 24  
        edge_cost = model.wDotPhi(x)

        accident_prob, block_prob = weatherProbChanges(data["weather"], data.get("accident", 0.1), data.get("block", 0.05))
        normal_prob = 1 - accident_prob - block_prob
        
        probabilities = {
            "normal": normal_prob,
            "accident": accident_prob,
            "block": block_prob
        }

        neighbor_expected_cost = 0
        neighbor_sub_paths = {}

        for status, prob in probabilities.items():
            modified_cost = modifyTimeCost(edge_cost, status)
            
            cost_from_neighbor, execution_path = expectimax(
                neighbor, endCity, x["hour"], graph, model, time + modified_cost, depth - 1
            )
            
            neighbor_expected_cost += prob * (modified_cost + cost_from_neighbor)
            
            neighbor_sub_paths[status] = execution_path
 
        # una vez conocemos el verdadero costo esperado total de este vecino.
        if neighbor_expected_cost < min_cost:
            min_cost = neighbor_expected_cost
            best_path = [node] + neighbor_sub_paths[max(neighbor_sub_paths.keys(), key=lambda k: probabilities[k])]

    return min_cost, best_path