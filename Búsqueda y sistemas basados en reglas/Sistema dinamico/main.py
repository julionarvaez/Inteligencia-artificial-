'''ESTE ES EL ARCHIVO PRINCIPAL DEL PROYECTO Y CONTIENE LA LÓGICA PARA INTERACTUAR CON EL USUARIO.
Sistema dinámico de rutas usando búsqueda A*.'''
from reglas import rutas
from busqueda import a_estrella

def main():
    print("=== 🚇 Sistema Inteligente de Rutas ===")
    print("Nodos disponibles:", ", ".join(rutas.keys()))

    inicio = input("Ingrese estación de inicio: ").strip().upper()
    destino = input("Ingrese estación de destino: ").strip().upper()

    if inicio not in rutas or destino not in rutas:
        print("❌ Error: estación no válida.")
        return

    ruta, costo = a_estrella(rutas, inicio, destino)

    if ruta:
        print(f"✅ Mejor ruta encontrada: {' -> '.join(ruta)}")
        print(f"📏 Distancia total: {costo}")
    else:
        print("⚠ No se encontró una ruta posible.")

if __name__ == "__main__":
    main()
