import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from decisionTeory.expectiMax import expectimax
from models.feature_vector import FeatureVector
from models.linearRegression import linearRegression

city_coordinates = {
    # --- Eje Metropolitano e Inicio ---
    "Bogota": {"lat": 4.6097, "lon": -74.0817},
    "Chiapinero": {"lat": 4.6486, "lon": -74.0614},
    "Usaquen": {"lat": 4.7014, "lon": -74.0298},
    
    # --- La Gran Trampa del Norte (Boyacá y Santanderes) ---
    # Una red densa con carreteras cortas que atraerán al algoritmo UCS
    "Zipaquira": {"lat": 5.0256, "lon": -74.0044},
    "Nemocon": {"lat": 5.0669, "lon": -73.8781},
    "Ubate": {"lat": 5.3114, "lon": -73.8153},
    "Chiquinquira": {"lat": 5.6171, "lon": -73.8166},
    "Raquira": {"lat": 5.5394, "lon": -73.6339},
    "Villa_de_Leyva": {"lat": 5.6373, "lon": -73.5244},
    "Tunja": {"lat": 5.5353, "lon": -73.3678},
    "Duitama": {"lat": 5.8271, "lon": -73.0336},
    "Sogamoso": {"lat": 5.7142, "lon": -72.9338},
    "Barbosa": {"lat": 5.9317, "lon": -73.6156},
    "San_Gil": {"lat": 6.5556, "lon": -73.1331},
    "Bucaramanga": {"lat": 7.1193, "lon": -73.1227},
    
    # --- El Camino Real hacia el Objetivo (Ruta al Llano) ---
    # Carreteras con distancias respetables y propensas a climas difíciles
    "Chipaque": {"lat": 4.4372, "lon": -74.0453},
    "Caqueza": {"lat": 4.3853, "lon": -73.9456},
    "Guayabetal": {"lat": 4.2181, "lon": -73.8161},
    "Villavicencio": {"lat": 4.1420, "lon": -73.6266}
}

# Estructura del Grafo de Carreteras
# Los costes bases (street_length) están en metros.
# Las probabilidades de accidente y bloqueo son valores base antes del clima.
graph_structure = {
    # Salidas directas desde la Capital
    "Bogota": {
        "Chiapinero": {
            "weather": "sunny", 
            "street_length": 5000.0, 
            "accident": 0.08, 
            "block": 0.01
        },
        "Chipaque": {
            "weather": "cloudy", 
            "street_length": 31000.0, 
            "accident": 0.12, 
            "block": 0.03
        }  # Ruta al sur (hacia el destino real)
    },
    
    # Eje urbano norte de Bogotá
    "Chiapinero": {
        "Usaquen": {
            "weather": "sunny", 
            "street_length": 7000.0, 
            "accident": 0.05, 
            "block": 0.01
        }
    },
    "Usaquen": {
        "Zipaquira": {
            "weather": "cloudy", 
            "street_length": 38000.0, 
            "accident": 0.10, 
            "block": 0.02
        }
    },

    # --- RED DISTRACTORA DEL NORTE (Trampas de bajo coste para UCS) ---
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
    },
    "Nemocon": {
        "Ubate": {
            "weather": "sunny", 
            "street_length": 40000.0, 
            "accident": 0.05, 
            "block": 0.01
        }
    },
    "Ubate": {
        "Chiquinquira": {
            "weather": "sunny", 
            "street_length": 34000.0, 
            "accident": 0.07, 
            "block": 0.02
        },
        "Raquira": {
            "weather": "sunny", 
            "street_length": 42000.0, 
            "accident": 0.05, 
            "block": 0.01
        }
    },
    "Chiquinquira": {
        "Barbosa": {
            "weather": "sunny", 
            "street_length": 52000.0, 
            "accident": 0.09, 
            "block": 0.03
        },
        "Villa_de_Leyva": {
            "weather": "sunny", 
            "street_length": 41000.0, 
            "accident": 0.06, 
            "block": 0.01
        }
    },
    "Raquira": {
        "Villa_de_Leyva": {
            "weather": "sunny", 
            "street_length": 15000.0, 
            "accident": 0.03, 
            "block": 0.01
        }
    },
    "Villa_de_Leyva": {
        "Tunja": {
            "weather": "sunny", 
            "street_length": 38000.0, 
            "accident": 0.07, 
            "block": 0.02
        }
    },
    "Tunja": {
        "Duitama": {
            "weather": "sunny", 
            "street_length": 54000.0, 
            "accident": 0.08, 
            "block": 0.02
        },
        "Barbosa": {
            "weather": "sunny", 
            "street_length": 68000.0, 
            "accident": 0.09, 
            "block": 0.03
        }
    },
    "Duitama": {
        "Sogamoso": {
            "weather": "sunny", 
            "street_length": 20000.0, 
            "accident": 0.04, 
            "block": 0.01
        }
    },
    "Barbosa": {
        "San_Gil": {
            "weather": "sunny", 
            "street_length": 72000.0, 
            "accident": 0.10, 
            "block": 0.04
        }
    },
    "San_Gil": {
        "Bucaramanga": {
            "weather": "sunny", 
            "street_length": 98000.0, 
            "accident": 0.12, 
            "block": 0.05
        }
    },
    
    # Nodos terminales del norte (puntos ciegos)
    "Sogamoso": {},
    "Bucaramanga": {},

    # --- CORREDOR LOGÍSTICO REAL AL SUR-ORIENTE ---
    # Rutas largas, montañosas e inestables que llevan al destino objetivo
    "Chipaque": {
        "Caqueza": {
            "weather": "foggy", 
            "street_length": 15000.0, 
            "accident": 0.18, 
            "block": 0.08
        }
    },
    "Caqueza": {
        "Guayabetal": {
            "weather": "rainy", 
            "street_length": 32000.0, 
            "accident": 0.22, 
            "block": 0.12
        }
    },
    "Guayabetal": {
        "Villavicencio": {
            "weather": "rainy", 
            "street_length": 26000.0, 
            "accident": 0.20, 
            "block": 0.15
        }
    },
    
    # Destino final
    "Villavicencio": {}
}

#train examples for linear regression, using the same data as in linearRegressionTest.py
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

featureVector = FeatureVector(traffic_data)

w = linearRegression(featureVector.initializeW(), [featureVector.phi(x) for x in traffic_data], [y["travel_time"] for y in traffic_data])

for i in range(25):
    cost, path = expectimax("Bogota", "Villavicencio", graph_structure, w, featureVector, city_coordinates, i)
    print(f"{path}\n\t expected cost: {cost}")