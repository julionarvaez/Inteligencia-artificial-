"""ESTE ARCHIVO NO TIENE ITERACIÓN CON EL USUARIO.
Implementa
-un sistema basado en reglas reglas logicas para buscar la mejor ruta para moverse desde un punto A a un punto B para encontrar la mejor ruta
entre puntos de un sistema de transporte masivo.



El script contiene:
- KB: hechos (estacion, tramo)
- Motor: vecinos y reglas de coste 
- A*: búsqueda con heurística euclidiana si hay coordenadas
"""

import math
import heapq
from typing import Dict, Tuple, List, Any, Optional


# BASE DE CONOCIMIENTO 
'''Estaciones con coordenadas (opcional, usadas por la heurística)
formato: "estacion_id": (x, y)'''

ESTACIONES_COORD = {
    "A": (0, 0),
    "B": (5, 1),
    "C": (2, 2),
    "D": (6, 3),
    "E": (8, 0),
    "F": (5, -2),
    "G": (10, -1)
}


# Tramos (aristas) entre estaciones con atributos.
''' Cada tramo: (origen, destino): {"tiempo": minutos, "dist": km, "linea": "L1"}
El grafo se asume bidireccional salvo que se especifique lo contrario.'''

TRAMOS = {
    ("A", "C"): {"tiempo": 4, "dist": 1.0, "linea": "L1"},
    ("C", "B"): {"tiempo": 5, "dist": 1.5, "linea": "L1"},
    ("B", "D"): {"tiempo": 8, "dist": 2.0, "linea": "L2"},
    ("C", "D"): {"tiempo": 10, "dist": 3.0, "linea": "L3"},
    ("D", "E"): {"tiempo": 6, "dist": 1.2, "linea": "L2"},
    ("B", "F"): {"tiempo": 7, "dist": 2.1, "linea": "L4"},
    ("F", "E"): {"tiempo": 9, "dist": 3.2, "linea": "L4"},
    ("E", "G"): {"tiempo": 5, "dist": 1.5, "linea": "L2"},
    # ejemplo de tramo dirigido (solo de G a A)
    ("G", "A"): {"tiempo": 20, "dist": 6.5, "linea": "L5"},
}

# Si quieres, añade más tramos. Para que el grafo sea bidireccional:
def build_bidirectional(tramos):
    graph = {}
    for (u, v), attr in tramos.items():
        graph.setdefault(u, []).append((v, attr))
        # Si ya existe el inverso, no lo dupliques:
        if (v, u) not in tramos:
            graph.setdefault(v, []).append((u, attr))
    return graph

GRAFO = build_bidirectional(TRAMOS)



# REGLAS 
TRANSFER_PENALTY = 3.0  # minutos extra por cada transferencia entre líneas

def coste_tramo(attr: Dict[str, Any], linea_actual: Optional[str]) -> float:
    """
    Regla de coste: tiempo base + penalización por transferencia si cambia la línea.
    """
    tiempo = attr.get("tiempo", 0)
    linea = attr.get("linea")
    penalty = 0.0
    if linea_actual is not None and linea != linea_actual:
        penalty += TRANSFER_PENALTY
    return tiempo + penalty



# HEURÍSTICA (Euclidiana sobre coordenadas)

def heuristica(u: str, v: str) -> float:
    if u in ESTACIONES_COORD and v in ESTACIONES_COORD:
        x1, y1 = ESTACIONES_COORD[u]
        x2, y2 = ESTACIONES_COORD[v]
        # convertimos distancia euclidiana a una estimación de tiempo:
        distancia = math.hypot(x2 - x1, y2 - y1)  # km (o unidades)
        # supongamos velocidad promedio 0.5 km/min -> tiempo = distancia / 0.5 = distancia * 2
        return distancia * 2.0
    # si no hay coordenadas, heurística 0 (admisible)
    return 0.0



'''A* que considera 'linea' como parte del estado para contabilizar transfers
Estado en la cola: (f_score, g_score, nodo, linea_actual, camino_lista)'''

def a_star_inicio_fin(start: str, goal: str):
    # heap: (f, g, nodo, linea_actual, camino)
    heap = []
    start_h = heuristica(start, goal)
    heapq.heappush(heap, (start_h, 0.0, start, None, [start]))  # sin línea inicial
    visited = {}  # (nodo, linea_actual) -> mejor g encontrado

    while heap:
        f, g, nodo, linea_actual, camino = heapq.heappop(heap)
        # chequeo de meta
        if nodo == goal:
            return {
                "ruta": camino,
                "tiempo": g,
                "linea_final": linea_actual
            }
        key = (nodo, linea_actual)
        if key in visited and g >= visited[key]:
            continue
        visited[key] = g

        vecinos = GRAFO.get(nodo, [])
        for (vec, attr) in vecinos:
            nueva_linea = attr.get("linea")
            coste = coste_tramo(attr, linea_actual)
            g2 = g + coste
            h2 = heuristica(vec, goal)
            f2 = g2 + h2
            # append nuevo camino
            camino2 = camino + [vec]
            key2 = (vec, nueva_linea)
            if key2 in visited and g2 >= visited[key2]:
                continue
            heapq.heappush(heap, (f2, g2, vec, nueva_linea, camino2))
    return None  # no hay ruta



# print y prueba

def imprimir_resultado(res):
    if not res:
        print("No se encontró ruta.")
        return
    print("Ruta encontrada:")
    print(" -> ".join(res["ruta"]))
    print(f"Tiempo estimado (minutos): {res['tiempo']:.2f}")
    print(f"Línea final: {res['linea_final']}")

def ejemplo_prueba():
    print("Prueba: A -> G")
    resultado = a_star_inicio_fin("A", "G")
    imprimir_resultado(resultado)
    print("\nPrueba: C -> E")
    resultado2 = a_star_inicio_fin("C", "E")
    imprimir_resultado(resultado2)

if __name__ == "__main__":
    ejemplo_prueba()

