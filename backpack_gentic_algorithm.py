import random
# leer archivo txt
archivo = open('./GA_mochila/productos.txt', 'r')

# crear lista de productos
lista_productos = []
for linea in archivo:
    lista_productos.append(linea.replace('\n', '').split(' '))

print(f'lista de productos: {lista_productos}')
# print(lista_productos[0][1])

# generar poblacion
poblacion = []
# print(len(poblacion))


def crear_poblacion_inicial(N):
    for i in range(N):
        mochila = [0] * len(lista_productos) 
        puntuacion = [0] * 2
        for j in range(len(mochila)):
            # generar seleccion aleatoria
            cargo_producto = random.randint(0, 1)
            if(cargo_producto == 1):
                mochila[j] = 1
                # caloria
                puntuacion[0] += int(lista_productos[j][1])
                # peso
                puntuacion[1] += float(lista_productos[j][2])
        # añadir puntuacion 
        mochila.extend(puntuacion)
        # añadir a la poblacion
        poblacion.append(mochila)
    print(f'poblacion inicial: {poblacion}')

def cruces_inidividuos(N):
    pass 



crear_poblacion_inicial(10)

# *def mutar_individuo()
# *def ciclo_generacion(max_gen)
# *def mostrar_mejor_mochila()
