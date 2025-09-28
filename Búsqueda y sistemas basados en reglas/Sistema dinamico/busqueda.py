'''Algoritmo A* para búsqueda de rutas en un grafo ponderado.
'''
import heapq

def heuristica(nodo, objetivo):
    """
    Heurística simple: distancia estimada.
    Como ejemplo, se devuelve 1 para todos y ademas se puede personalizar las coordenadas
    de cada nodo y calcular la distancia euclidiana entre ellos.
    """
    return 1  

def a_estrella(grafo, inicio, objetivo):
    # Cola necesaria con (costo_total_estimado, nodo, ruta, costo_real)
    frontera = [(0, inicio, [inicio], 0)]
    visitados = set()

    while frontera:
        costo_estimado, nodo, ruta, costo_real = heapq.heappop(frontera)

        if nodo in visitados:
            continue
        visitados.add(nodo)

        # Si llegamos al destino quebramos y retornamos la ruta y el costo 
        if nodo == objetivo:
            return ruta, costo_real

        for vecino, peso in grafo.get(nodo, {}).items():
            if vecino not in visitados:
                nuevo_costo = costo_real + peso
                estimado = nuevo_costo + heuristica(vecino, objetivo)
                heapq.heappush(frontera, (estimado, vecino, ruta + [vecino], nuevo_costo))

    return None, float("inf")
