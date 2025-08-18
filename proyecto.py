#Definicion de listas de restaurantes 

from menu import restaurantes
def filtrado_palabra_clave(palabra_clave):
    resultado = []
    palabra_clave = palabra_clave.lower()
    for fila in restaurantes:
        for columna in fila:
            if palabra_clave in str(columna).lower():
                resultado.append(fila)
                break
    return resultado

def filtrado_precio_menor(precio_menor):
    resultado = []
    for fila in restaurantes:
        if fila[2] <= precio_menor:
            resultado.append(fila)
    return resultado

def filtrado_mayor_precio(precio_mayor):
    resultado = []
    for fila in restaurantes:
        if fila[2] >= precio_mayor:
            resultado.append(fila)
    return resultado     

def plato_mas_barato ():
    mas_barato = restaurantes[0]
    for plato in restaurantes:
        if plato[2] < mas_barato[2]:
            mas_barato = plato
    return f"El plato más barato dentro de la universidad es: {mas_barato[1]} en {mas_barato[0]} por ${mas_barato[2]:,}"

accion = True 

while(accion != False):
    print("Bienvenido a UniFood, tu lugar de confianza para hacer una correcta eleccion\n" \
    "1. Cual es el plato mas barato de todos los restaurantes?\n" \
    "2. Donde encuentro los platos vegetarianos?\n" \
    "3. En que lugares hay hamburguesas?\n" \
    "4. Si tengo un presupuesto bajo, en que restaurantes puedo almorzar?\n" \
    "5. Si tengo un presupuesto amplio, donde puedo almorzar?\n" \
    "6. Salir")
    opcion = int(input("Que deseas hacer hoy: "))

    if opcion == 1:
        print(plato_mas_barato())
    elif opcion == 2:
        for fila in filtrado_palabra_clave("vegetaria"):
            print(fila)
    elif opcion == 3:
        for fila in filtrado_palabra_clave("Hamburguesa"):
            print(fila)
    elif opcion == 4:
        for fila in filtrado_precio_menor(20000):
            print(fila)
    elif opcion == 5:
        for fila in filtrado_mayor_precio(25000):
            print(fila)
    elif opcion == 6:
        print("Gracias por utilizar UniFood, te esperamos pronto")
        accion = False
    else:
        print("Digite una opcion valida")
