restaurantes = [
    
    ["Embarcadero", "Arroz vegetariano", 19000],
    ["Embarcadero", "Ensalda cuscus", 21900],
    ["Embarcadero", "Hamburguesa vegie Lisa", 18100],

    
    ["Punto crepes","Burrito vegetariano",17400],
    ["Punto crepes","Crepe de tomate y queso",18400],
    ["Punto crepes","Crepe de carne",18100],

   
    ["Punot wok", "Sushi vegetariano",20400],
    ["Punot wok", "Bibimbap vegetariano",18700],
    ["Punot wok", "Ramen de pollo",15800],

    
    ["Kioscos", "Parrilla vegetariana",27900 ],
    ["Kioscos", "Hamburguesa vegetariana",22400 ],
    ["Kioscos", "Milanesa de cerdo", 17300],

    
    ["Punto sandwich","Crispy chedar",9300],
    ["Punto sandwich","Pepperoni 12 cm",13500],
    ["Cipress","Pizza criolla",10500],
    ["Meson","Menu del dia",17300],
    ["Meson","Menu ligero",13600],
    ["Arcos","Minestrone",9500],
]




accion := true                     
opcion : int                       
palabra_clave : string;            
precio_menor, precio_mayor : int  
mas_barato : plato;                
fila, columna : plato             


proc filtrado_palabra_clave(palabra_clave : string) : lista
    
    resultado := []

    
    palabra_clave := toLower(palabra_clave)

   
    do existe fila en restaurantes 

        
        do existe columna en fila 
            if

            
                [] palabra_clave ∈ toLower(str(columna))

               
                    resultado := resultado ∪ {fila}
                
                
                    break
            fi
        od;
    od;

    .
    return resultado
end

proc filtrado_precio_menor(precio_menor : int) : lista

    resultado := []

    do existe fila en restaurantes
        if
            [] fila.precio ≤ precio_menor
                
                
                resultado := resultado ∪ {fila}
        fi
    od;
   
    return resultado
end

proc filtrado_mayor_precio(precio_mayor : int) : lista

    
    resultado := []    
    do existe fila en restaurantes
        if
            [] fila.precio ≥ precio_mayor
                resultado := resultado ∪ {fila}
        fi
    od;

    return resultado
end

proc plato_mas_barato() : string

    mas_barato := restaurantes[0]
  
    do existe plato en restaurantes
        if
          
            [] plato.precio < mas_barato.precio

                    mas_barato := plato
        fi
    od;

    return "El plato más barato es: " + mas_barato.nombre + " en " + mas_barato.restaurante + " por $" + toString(mas_barato.precio)
end

do accion = true
    print("Bienvenido a UniFood, tu lugar de confianza para hacer una correcta eleccion\n")
    print("1. Cual es el plato mas barato de todos los restaurantes?\n")
    print("2. Donde encuentro los platos vegetarianos?\n")
    print("3. En que lugares hay hamburguesas?\n")
    print("4. Si tengo un presupuesto bajo, en que restaurantes puedo almorzar?\n")
    print("5. Si tengo un presupuesto amplio, donde puedo almorzar?\n")
    print("6. Salir")

    opcion := int(input("Que deseas hacer hoy: "))

    if
        
        [] opcion == 1
            print(plato_mas_barato())

        
        [] opcion == 2
            do existe fila en filtrado_palabra_clave("vegetaria")
                print(fila)
            od

        [] opcion == 3
            do existe fila en filtrado_palabra_clave("Hamburguesa")
                print(fila)
            od

       
        [] opcion == 4
            print(filtrado_precio_menor(20000))

        
        [] opcion == 5
            print(filtrado_mayor_precio(25000))

       
        [] opcion == 6
            print("Gracias por utilizar UniFood, te esperamos pronto")
            accion := False

       
        [] (opcion !∈ {1,2,3,4,5,6})
            print("Digite una opcion valida")
    fi
od;

