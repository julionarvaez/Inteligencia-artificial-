#  Sistema Inteligente para Rutas de Transporte Masivo 

En este proyecto corresponde a la tercera actividad del curso de Inteligencia Artificial, cuyo prposito es implementar un sistema inteligente basado en el conocimiento utilizando reglas lógicas y estrategias de búsqueda heurística para ayudar a encontar la mejor ruta entre dos puntos dentro de un sistema de transporte masivo local.

##  Objetivos
- Representar el conocimiento del sistema de transporte mediante reglas lógicas.
- Implementar en Python un motor de búsqueda que encuentre la mejor ruta entre dos estaciones que quiera el usuario.
- Aplicar el algoritmo para optimizar el cálculo de rutas.
- Documentar y explicar el funcionamiento del sistema de manera clara y entendible.

##  Bibliografía Recomendada
Benítez, R. (2014). *Inteligencia artificial avanzada*. Barcelona: Editorial UOC.  
- **Capítulo 2:** Lógica y representación del conocimiento  
- **Capítulo 3:** Sistemas basados en reglas  
- **Capítulo 9:** Técnicas basadas en búsquedas heurísticas  

## Tecnologías Utilizadas
- **Lenguaje:** Python, en mi caso la version 3.13.7.
- **Librerías estándar:**  
  - heapq: para la cola de prioridad en A*.  
  - math: para hacer calculos matematicos .
  - collections: esta para estructuras de datos.  

TENER ENCUENTA: Que no es necesario instalar librerías externas.

##  Estructura del Repositorio
|-  Sistema dinamico
|- |- main.py # Programa principal
|  |- reglas.py # Base de conocimiento (grafo con reglas)
|  |- busqueda.py # Algoritmo de búsqueda A*
|
|  |- RuebaTransporte **Es un mismo sistema pero sin interasion con el usuario**
