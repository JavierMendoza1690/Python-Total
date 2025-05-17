cliente = {'nombre':'Federico',
           'edad':45,
           'ocupacion':'instructor' }

pelicula = {'titulo': 'matrix',
            'ficha_tecnica': {'protagonista':'Keanu reaves',
                              'director':'Lana y Lilly Wachowsky'}}

elementos = [cliente, pelicula, 'libro']

# usando un loop for para iterar en elementos

for e in elementos:
   match e:
        case {'nombre':nombre,
             'edad': edad,
             'ocupacion': ocupacion}:
           print('Es un cliente')
           print(nombre, edad, ocupacion)

        case {'titulo': titulo,
              'ficha_tecnica': {'protagonista':protagonista, 'director':director}}:
            print('Es una pelicula')
            print(titulo, protagonista, director)
        case _:
            print(e)
            print('No sé que es esto')
