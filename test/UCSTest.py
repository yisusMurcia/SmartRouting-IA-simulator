import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import routing.UCS as UCS
from models.feature_vector import buildVectorStructure
from models.linearRegression import linearRegression

# Estructura de Grafo para UCS (Hora Dinámica)
# Grafo de carreteras colombianas
graph_structure = {
    # Salidas desde Bogotá
    "Bogota": {
        "Chiapinero": {"weather": "sunny", "street_length": 5000.0},
        "Chipaque": {"weather": "cloudy", "street_length": 31000.0}  # Ruta al sur (hacia el destino)
    },
    "Chiapinero": {
        "Usaquen": {"weather": "sunny", "street_length": 7000.0}
    },
    "Usaquen": {
        "Zipaquira": {"weather": "cloudy", "street_length": 38000.0}
    },

    # --- TRAMPA DE BAJO COSTE (Red del Norte) ---
    # Calles cortas y rápidas que enamorarán a UCS pero alejan del destino
    "Zipaquira": {
        "Nemocon": {"weather": "sunny", "street_length": 12000.0},
        "Ubate": {"weather": "sunny", "street_length": 51000.0}
    },
    "Nemocon": {
        "Ubate": {"weather": "sunny", "street_length": 40000.0}
    },
    "Ubate": {
        "Chiquinquira": {"weather": "sunny", "street_length": 34000.0},
        "Raquira": {"weather": "sunny", "street_length": 42000.0}
    },
    "Chiquinquira": {
        "Barbosa": {"weather": "sunny", "street_length": 52000.0},
        "Villa_de_Leyva": {"weather": "sunny", "street_length": 41000.0}
    },
    "Raquira": {
        "Villa_de_Leyva": {"weather": "sunny", "street_length": 15000.0}
    },
    "Villa_de_Leyva": {
        "Tunja": {"weather": "sunny", "street_length": 38000.0}
    },
    "Tunja": {
        "Duitama": {"weather": "sunny", "street_length": 54000.0},
        "Barbosa": {"weather": "sunny", "street_length": 68000.0}
    },
    "Duitama": {
        "Sogamoso": {"weather": "sunny", "street_length": 20000.0}
    },
    "Barbosa": {
        "San_Gil": {"weather": "sunny", "street_length": 72000.0}
    },
    "San_Gil": {
        "Bucaramanga": {"weather": "sunny", "street_length": 98000.0}
    },
    
    # Nodos ciegos del norte (sin salida)
    "Sogamoso": {},
    "Bucaramanga": {},

    # --- CAMINO REAL AL OBJETIVO (Eje de los Llanos) ---
    # Carreteras con distancias respetables y clima complejo (niebla/lluvia)
    "Chipaque": {
        "Caqueza": {"weather": "foggy", "street_length": 15000.0}
    },
    "Caqueza": {
        "Guayabetal": {"weather": "rainy", "street_length": 32000.0}
    },
    "Guayabetal": {
        "Villavicencio": {"weather": "rainy", "street_length": 26000.0}
    },
    "Villavicencio": {} # ¡DESTINO FINAL!
}
#train examples for linear regression, using the same data as in linearRegressionTest.py
# Datos sintéticos para entrenar y probar el modelo de predicción de tráfico (Fase 1)
traffic_data = [
    {"hour": 8, "weather": "sunny", "street_length": 450.5, "travel_time": 12.3},
    {"hour": 18, "weather": "rainy", "street_length": 800.0, "travel_time": 28.5},
    {"hour": 12, "weather": "cloudy", "street_length": 300.2, "travel_time": 6.8},
    {"hour": 22, "weather": "sunny", "street_length": 1200.5, "travel_time": 15.1},
    {"hour": 7, "weather": "rainy", "street_length": 550.0, "travel_time": 22.4},
    {"hour": 15, "weather": "sunny", "street_length": 950.8, "travel_time": 14.2},
    {"hour": 3, "weather": "foggy", "street_length": 600.0, "travel_time": 11.5},
    {"hour": 17, "weather": "sunny", "street_length": 750.3, "travel_time": 21.0},
    {"hour": 9, "weather": "rainy", "street_length": 400.0, "travel_time": 18.2},
    {"hour": 13, "weather": "cloudy", "street_length": 1100.1, "travel_time": 17.5},
    {"hour": 19, "weather": "sunny", "street_length": 500.0, "travel_time": 13.8},
    {"hour": 2, "weather": "rainy", "street_length": 350.2, "travel_time": 7.2},
    {"hour": 14, "weather": "sunny", "street_length": 900.0, "travel_time": 13.0},
    {"hour": 8, "weather": "foggy", "street_length": 850.5, "travel_time": 26.3},
    {"hour": 16, "weather": "rainy", "street_length": 650.0, "travel_time": 21.9},
    {"hour": 20, "weather": "cloudy", "street_length": 420.7, "travel_time": 9.5},
    {"hour": 11, "weather": "sunny", "street_length": 1300.0, "travel_time": 18.4},
    {"hour": 5, "weather": "sunny", "street_length": 250.0, "travel_time": 3.2},
    {"hour": 18, "weather": "foggy", "street_length": 700.4, "travel_time": 25.1},
    {"hour": 12, "weather": "rainy", "street_length": 500.0, "travel_time": 15.6}
]

training_data = [[dict, dict["travel_time"]] for dict in traffic_data[0:15]]
test_data = [[dict, dict["travel_time"]] for dict in traffic_data[15:]]
vector = buildVectorStructure(traffic_data)

w = linearRegression(training_data)

for i in range(25):
    path, cost = UCS.UCS("Bogota", "Barbosa", graph_structure, w, vector, i)
    print(f"Hour {i}:\n\t Optimal Path: {path}, Total Cost: {cost} minutes")