import math
import unicodedata
restaurants_db = {
   "Embarcadero": {
    "Arroz vegetariano": {"Categoria": "Cocina internacional", "Precio": 19200, "Vegetariano": True},
    "Ensalada de cascús": {"Categoria": "Comida saludable", "Precio": 21900, "Vegetariano": True},
    "Hamburguesa Veggie Lisa": {"Categoria": "Comida rápida", "Precio": 18100, "Vegetariano": True},
    "Fish and chips": {"Categoria": "Cocina internacional", "Precio": 28500, "Vegetariano": False},
    "Pique macho": {"Categoria": "Comida típica", "Precio": 20900, "Vegetariano": False}
  },

  "Punto Crepes": {
    "Burrito vegetariano": {"Categoria": "Comida mexicana", "Precio": 17400, "Vegetariano": True},
    "Crepe de tomate y queso": {"Categoria": "Cocina internacional", "Precio": 18400, "Vegetariano": True},
    "Crepe de pollo en salsa de champiñones": {"Categoria": "Cocina internacional", "Precio": 23000, "Vegetariano": False},
    "Burrito de carne": {"Categoria": "Comida mexicana", "Precio": 21500, "Vegetariano": False},
    "Tacos al pastor": {"Categoria": "Comida mexicana", "Precio": 20900, "Vegetariano": False}
  },

  "Punto Wok": {
    "Domburi - tofu": {"Categoria": "Cocina asiática", "Precio": 26100, "Vegetariano": True},
    "Salteado de verduras y tofu asiático": {"Categoria": "Cocina asiática", "Precio": 29000, "Vegetariano": True},
    "Sushi vegetariano": {"Categoria": "Cocina japonesa", "Precio": 20400, "Vegetariano": True},
    "Ramen de pollo": {"Categoria": "Cocina japonesa", "Precio": 15800, "Vegetariano": False},
    "Pollo kung pao": {"Categoria": "Cocina asiática", "Precio": 24100, "Vegetariano": False}
  },

  "Kioskos": {
    "Parrillada vegetariana": {"Categoria": "Comida a la parrilla", "Precio": 27900, "Vegetariano": True},
    "Hamburguesa vegetariana": {"Categoria": "Comida rápida", "Precio": 22400, "Vegetariano": True},
    "Churrasco gaucho": {"Categoria": "Comida a la parrilla", "Precio": 41300, "Vegetariano": False},
    "Punta de anca kioskos": {"Categoria": "Comida a la parrilla", "Precio": 39500, "Vegetariano": False},
    "Trucha a la plancha": {"Categoria": "Comida típica", "Precio": 27200, "Vegetariano": False}
  },

  "Punto Sandwich": {
    "Atún 25cm": {"Categoria": "Comida rápida", "Precio": 23600, "Vegetariano": False},
    "Cochinita pibil 25cm": {"Categoria": "Comida mexicana", "Precio": 20200, "Vegetariano": False},
    "Pepperoni 25cm": {"Categoria": "Comida rápida", "Precio": 19800, "Vegetariano": False},
    "Crispy chedar": {"Categoria": "Comida rápida", "Precio": 9300, "Vegetariano": False},
    "Papa volcán": {"Categoria": "Comida rápida", "Precio": 9900, "Vegetariano": True}
  }

}

class MenuAndRestaurants:

    def normalizarTexto(self, texto):
    #Aca lo que vamos a hacer va normalizar el texto, para que no se afecte con tiltes y eso
        texto = unicodedata.normalize('NFD', texto)
        texto = ''.join(char for char in texto if unicodedata.category(char) != 'Mn')
        return texto.lower()
    
    def procesarBaseDeDatos(self, restaurants_db):

        platosProcesados = {}

    #Aca lo que vamos a hacer es recorrer nuestra base de datos e ir dandonle especificaciones mas precidas como si el plato es caro o barto 

        for restaurant, platos in restaurants_db.items():
            for nombrePlato, informacion in platos.items():
                identificacionPlato = f"{restaurant}_{nombrePlato}"

                caracteristicas = []
                caracteristicas.append(self.normalizarTexto(informacion["Categoria"].lower()))

                if informacion["Vegetariano"]:
                    caracteristicas.append("vegetariano")
                else:
                    caracteristicas.append("no vegetariano")

                if informacion["Precio"] > 26000:
                    caracteristicas.append("precio alto")
                elif informacion["Precio"] > 20000:
                    caracteristicas.append("precio medio")
                else:
                    caracteristicas.append("precio bajo")
                
                platosProcesados[identificacionPlato] = caracteristicas

                if len(platosProcesados) <= 3:
                    print(f"{nombrePlato}: {caracteristicas}")

        return platosProcesados
    
    def creacionVocabulario(self, platosProcesados):

    #Aca se da lo de la creacion de vocabulario para que el sistema tenga en mente las palabras que va a tener, para el momento de que el usaurio diga la palabra el ya tenga su vocabulario y primero valide que esa palabras si esta dentro de lo que es sabe 
    #Pero ojo aca solo vamor a hacer la creacion, la validacion la hacemos mas adelante 

        vocabulario = set()

        for caracteristicas in platosProcesados.values():
            vocabulario.update(caracteristicas)

        vocabulario = sorted(list(vocabulario))

        return vocabulario

    #Estas dos funciones son para calcular los scores de cada plato 
    #Basicamente aca empelamos el algoritmo, especificamente la parte matematica 
    def calcularTF(self, termino, documento):
        if len(documento) == 0:
            return 0
        return documento.count(termino) / len(documento)

    def calcularIDF(self, termino, todosLosPlatos):
        totalPlatos = len(todosLosPlatos)
        if totalPlatos == 0:
            return 0
    
        platosConTermino = 0 
        for plato in todosLosPlatos.values():
            if termino in plato:
                platosConTermino += 1 
    
        if platosConTermino == 0:
            return 0
        try:
            return math.log(totalPlatos / platosConTermino)
        except:
            return 0
    
    def recomendarPorBusqueda(self, palabraBusqueda, restaurants_db, n=5 ):
        palabraBusqueda = self.normalizarTexto(palabraBusqueda)

        

        platosProcesados = self.procesarBaseDeDatos(restaurants_db)

        count = 0
        for nombre, caract in platosProcesados.items():
            if count < 3:
                print(f"  {nombre}: {caract}")
                count += 1
        
        vocabulario = self.creacionVocabulario(platosProcesados)
    
        
        platosCandidatos = {}
        
        sinonimos = {
            'asiatica': 'cocina asiatica',
            'comida asiatica': 'cocina asiatica', 
            'japonesa': 'cocina japonesa',
            'comida japonesa': 'cocina japonesa',
            'china': 'cocina asiatica',
            'mexicana': 'comida mexicana',
            'rapida': 'comida rapida',
            'internacional': 'cocina internacional',
            'saludable': 'comida saludable',
            'parrilla': 'comida a la parrilla',
            'tipica': 'comida tipica'
        }
        

        termino_busqueda = sinonimos.get(palabraBusqueda, palabraBusqueda)
    

        for nombrePlato, caracteristicas in platosProcesados.items():
            if termino_busqueda in caracteristicas:
                platosCandidatos[nombrePlato] = caracteristicas
            
        
       
        

        if not platosCandidatos:
            return f"No se encontraron platos con '{palabraBusqueda}'"
        
        resultados = {}
        for nombrePlato, caracteristicas in platosCandidatos.items():
            resultadoFinal = 0 
            
            print(f"  Características: {caracteristicas}")
            
            for caracteristica in caracteristicas:
                TF = self.calcularTF(caracteristica, caracteristicas)
                IDF = self.calcularIDF(caracteristica, platosProcesados)
                score_parcial = TF * IDF
                
                print(f"  {caracteristica}: TF={TF:.3f}, IDF={IDF:.3f}, Score={score_parcial:.3f}")
                resultadoFinal += score_parcial
            
            print(f"  SCORE FINAL: {resultadoFinal}")
            resultados[nombrePlato] = resultadoFinal
        

        for nombre, score in resultados.items():
            print(f"  {nombre}: {score}")
        
        recomendacionesOrdenadas = sorted(resultados.items(), key=lambda x: x[1], reverse=True)
        
        for i, (nombre, score) in enumerate(recomendacionesOrdenadas[:3]):
            print(f"  {i+1}. {nombre}: {score}")
        
        resultadosFormateados = []
        for i, (platoIdentificacion, resultado) in enumerate(recomendacionesOrdenadas[:n], 1):
            restaurant, nombrePlato = platoIdentificacion.split('_', 1)
            informacionOriginal = restaurants_db[restaurant][nombrePlato]
            
            resultadosFormateados.append({
                'posicion': i,
                'plato': nombrePlato.replace('_', ' ').title(),
                'restaurante': restaurant.replace('_', ' ').title(),
                'precio': informacionOriginal['Precio'],
                'categoria': informacionOriginal['Categoria'],
                'vegetariano': informacionOriginal['Vegetariano'],
                'score': round(resultado, 3)
            })
        
        return resultadosFormateados
    #Aca vamos a poner el codigo para mostrarlo mas bonito a los ojos del usuario      
    def mostrarRecomendaciones(self, recomendaciones):
        if isinstance(recomendaciones, str):  
            print(recomendaciones)
            return
            
        print(f"\n🍽️  Encontré {len(recomendaciones)} recomendaciones:")
        print("=" * 56)
            
        for rec in recomendaciones:
            print(f"{rec['posicion']}. {rec['plato']} - {rec['restaurante']}")
            print(f"   💰 Precio: ${rec['precio']:,}")
            print(f"   🍽️  Categoría: {rec['categoria']}")
            print(f"   🌱 Vegetariano: {'Sí' if rec['vegetariano'] else 'No'}")
            print(f"   ⭐ Score único: {rec['score']} (más alto = más único)")
            print()