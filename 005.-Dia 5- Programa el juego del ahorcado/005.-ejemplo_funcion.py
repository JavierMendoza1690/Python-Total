#lista de tuples
precios_cafe = [('capuchino',1.5),('Expresso',2.2),('Moka',1.9)]

#------------------------------CREANDO FUNCION-----------------------------------
#funcion para saber cual es el cafe mas caro
def cafe_mas_caro(lista_precios):
    precio_mayor=0
    cafe_mas_caro=''

    #for que recorra la lista de tuplas
    for nombre_cafe, precio_cafe in precios_cafe:

        if( precio_cafe > precio_mayor):
            precio_mayor    = precio_cafe
            cafe_mas_caro   = nombre_cafe
        else:
            pass

    #la funcion es una tupla
    return (cafe_mas_caro,precio_mayor)


#--------------------------------INVOCANDO FUERA DE LA FUNCION-----------------------------

#incovando la funcion
tupla_resultado = cafe_mas_caro(precios_cafe)
#desestructurando tupla
cafe, precio = tupla_resultado
print(tupla_resultado)
print(f'\nDesestructurado\nCafe:{cafe}\nPrecio:{precio}')

