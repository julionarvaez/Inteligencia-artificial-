'''ESTE ES EL ARCHIVO DE REGLAS QUE DEFINE LAS CONEXIONES ENTRE ESTACIONES.'''
# Base de conocimiento: conexiones entre estaciones

rutas = {
    "A": {"B": 2, "C": 4},
    "B": {"A": 2, "D": 7, "E": 3},
    "C": {"A": 4, "F": 5},
    "D": {"B": 7, "E": 2, "G": 3},
    "E": {"B": 3, "D": 2, "H": 6},
    "F": {"C": 5, "H": 4},
    "G": {"D": 3, "H": 1},
    "H": {"E": 6, "F": 4, "G": 1}
}
