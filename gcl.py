# Definición de la lista de restaurantes con sus platos y precios
restaurantes = [
    # Restaurante Embarcadero
    ["Embarcadero", "Arroz vegetariano", 19000],
    ["Embarcadero", "Ensalda cuscus", 21900],
    ["Embarcadero", "Hamburguesa vegie Lisa", 18100],

    # Restaurante Punto crepes
    ["Punto crepes","Burrito vegetariano",17400],
    ["Punto crepes","Crepe de tomate y queso",18400],
    ["Punto crepes","Crepe de carne",18100],

    # Restaurante Punto wok
    ["Punot wok", "Sushi vegetariano",20400],
    ["Punot wok", "Bibimbap vegetariano",18700],
    ["Punot wok", "Ramen de pollo",15800],

    # Restaurante Kioscos
    ["Kioscos", "Parrilla vegetariana",27900 ],
    ["Kioscos", "Hamburguesa vegetariana",22400 ],
    ["Kioscos", "Milanesa de cerdo", 17300],

    # Otros Restaurantes
    ["Punto sandwich","Crispy chedar",9300],
    ["Punto sandwich","Pepperoni 12 cm",13500],
    ["Cipress","Pizza criolla",10500],
    ["Meson","Menu del dia",17300],
    ["Meson","Menu ligero",13600],
    ["Arcos","Minestrone",9500],
]



# Definición de variables
accion := true                     # Variable de control del ciclo principal
opcion : int                       # Opción elegida por el usuario
palabra_clave : string;            # Para búsqueda por palabra
precio_menor, precio_mayor : int   # Variables para filtros de precio
mas_barato : plato;                # Plato más barato encontrado
fila, columna : plato              # Iteradores sobre la lista de restaurantes

# Procedimiento: Filtrar restaurantes que contengan una palabra clave.
proc filtrado_palabra_clave(palabra_clave : string) : lista
    # Se inicializa una lista vacía donde se guardarán los resultados.
    resultado := []

    # Se pasa la palabra clave a minúsculas para comparar sin importar mayúsculas/minúsculas.
    palabra_clave := toLower(palabra_clave)

    # Se recorre cada fila de la lista "restaurantes".
    do existe fila en restaurantes 

        # Dentro de cada fila, se recorren las columnas (atributos del restaurante).
        do existe columna en fila 
            if

            # Si la palabra clave está contenida en el valor de la columna (convertida a minúsculas).
                [] palabra_clave ∈ toLower(str(columna))

                # Se agrega la fila completa (el restaurante) al resultado.
                    resultado := resultado ∪ {fila}
                
                # Termina el ciclo.
                    break
            fi
        od;
    od;

    # Se retorna la lista resultado.
    return resultado
end


# Procedimiento: Filtrar restaurantes cuyo precio sea menor o igual al límite.
proc filtrado_precio_menor(precio_menor : int) : lista

    # Se inicializa la lista de resultados como vacía.
    resultado := []

    # Se recorre cada fila de la lista "restaurantes".
    do existe fila en restaurantes
        if
            # Si el precio del restaurante es menor o igual al límite dado.
            [] fila.precio ≤ precio_menor
                
                # Se agrega el restaurante (fila) al resultado.
                resultado := resultado ∪ {fila}
        fi
    od;

    # Se devuelve la lista de restaurantes filtrados.
    return resultado
end


# Procedimiento: Filtrar restaurantes cuyo precio sea mayor o igual al valor dado
proc filtrado_mayor_precio(precio_mayor : int) : lista

    # Se inicializa la lista de resultados como vacía.
    resultado := []

    # Se recorre cada fila de la lista "restaurantes".
    do existe fila en restaurantes
        if
            # Si el precio del restaurante es mayor o igual al valor dado.
            [] fila.precio ≥ precio_mayor

                # Se agrega el restaurante (fila) al resultado.
                resultado := resultado ∪ {fila}
        fi
    od;

    # Se devuelve la lista de restaurantes filtrados.
    return resultado
end


# Procedimiento: Encontrar el plato más barato.
proc plato_mas_barato() : string

    # Se inicializa la variable "mas_barato" con el primer plato de la lista restaurantes.
    mas_barato := restaurantes[0]

     # Se recorre cada plato en la lista "restaurantes".
    do existe plato en restaurantes
        if
            # Si el precio del plato actual es menor al del más barato registrado
            [] plato.precio < mas_barato.precio

                # Se actualiza "mas_barato" con este plato.
                mas_barato := plato
        fi
    od;

    # Se devuelve un print con la información del plato más barato encontrado.
    return "El plato más barato es: " + mas_barato.nombre + " en " + mas_barato.restaurante + " por $" + toString(mas_barato.precio)
end

# Ciclo principal del menú
do accion = true
    print("Bienvenido a UniFood, tu lugar de confianza para hacer una correcta eleccion\n")
    print("1. Cual es el plato mas barato de todos los restaurantes?\n")
    print("2. Donde encuentro los platos vegetarianos?\n")
    print("3. En que lugares hay hamburguesas?\n")
    print("4. Si tengo un presupuesto bajo, en que restaurantes puedo almorzar?\n")
    print("5. Si tengo un presupuesto amplio, donde puedo almorzar?\n")
    print("6. Salir")

    opcion := int(input("Que deseas hacer hoy: "))

    # Selección de opciones según el valor de "opcion".
    if
        # Caso 1: Mostrar el plato más barato.
        [] opcion == 1
            print(plato_mas_barato())

        # Caso 2: Filtrar restaurantes que contengan la palabra "vegetaria" y mostrarlos.
        [] opcion == 2
            do existe fila en filtrado_palabra_clave("vegetaria")
                print(fila)
            od

        # Caso 3: Filtrar restaurantes que contengan la palabra "Hamburguesa" y mostrarlos
        [] opcion == 3
            do existe fila en filtrado_palabra_clave("Hamburguesa")
                print(fila)
            od

        # Caso 4: Mostrar restaurantes cuyo precio sea menor o igual a $20.000
        [] opcion == 4
            print(filtrado_precio_menor(20000))

        # Caso 5: Mostrar restaurantes cuyo precio sea mayor a 25000.
        [] opcion == 5
            print(filtrado_mayor_precio(25000))

        # Caso 6: Se muestra mensaje de despedida y finaliza el ciclo.
        [] opcion == 6
            print("Gracias por utilizar UniFood, te esperamos pronto")
            accion := False

        # En caso de que no se digite una opción válida, se muestra:
        [] (opcion !∈ {1,2,3,4,5,6})
            print("Digite una opcion valida")
    fi
od;
