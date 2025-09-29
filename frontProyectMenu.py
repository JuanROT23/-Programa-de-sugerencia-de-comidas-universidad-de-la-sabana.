from MenuAndRestaurants import MenuAndRestaurants
from MenuAndRestaurants import restaurants_db

sistema = MenuAndRestaurants()
print("=== SISTEMA DE RECOMENDACIONES TF-IDF ===")

while True:
    print("\n" + "="*50)
    termino = input("¿Qué tipo de comida buscas? (o 'salir' para terminar): ").lower()
    
    if termino == 'salir':
        print("¡Gracias por usar el sistema!")
        break
    
    if not termino.strip():
        print("Por favor ingresa un término válido.")
        continue
    
    # Obtener recomendaciones
    recomendaciones = sistema.recomendarPorBusqueda(termino, restaurants_db, 5)

    # Mostrar resultados
    sistema.mostrarRecomendaciones(recomendaciones)

