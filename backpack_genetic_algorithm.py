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
nueva_poblacion = []
mutacion = 1
max_gen = 10
calorias_min = 800
peso_max = 1.3

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

def cruzar_inidividuos(poblacion):
    for i in range(0,len(poblacion),2):
        # obtener individuo
        # print(i)
        individuo1 = poblacion[i][:len(lista_productos)]
        individuo2 = poblacion[i+1][:len(lista_productos)]

        # cruzar individuos
        corte = int(len(individuo1)/2)
        # print(corte)
        mochila = individuo1[0:corte]
        mochila.extend(individuo2[corte:corte*2])
        puntuacion = [0] * 2
        # generar puntuacion 
        for j in range(len(mochila)):
            # print(j)
            if(mochila[j] == 1):
                # caloria
                puntuacion[0] += int(lista_productos[j][1])
                # peso
                puntuacion[1] += float(lista_productos[j][2]) 
         # añadir puntuacion 
        mochila.extend(puntuacion)
        # añadir a la poblacion
        nueva_poblacion.append(mochila)

        # cruzar partes restantes 
        mochila1 = individuo1[corte:corte*2]
        mochila1.extend(individuo2[0:corte])
        puntuacion1 = [0] * 2
        # generar puntuacion 
        for j in range(len(mochila1)):
            # print(j)
            if(mochila1[j] == 1):
                # caloria
                puntuacion1[0] += int(lista_productos[j][1])
                # peso
                puntuacion1[1] += float(lista_productos[j][2]) 
         # añadir puntuacion 
        mochila1.extend(puntuacion1)
        # añadir a la poblacion
        nueva_poblacion.append(mochila1)
    print(f'nueva poblacion: {nueva_poblacion}')

def mutar_individuo(mutacion,nueva_poblacion):
    while(mutacion >= 1):
        individuo = (random.randint(0, len(nueva_poblacion)))
        producto_mutado = random.randint(0, len(lista_productos))
        nueva_poblacion[individuo][producto_mutado] = 1

        for ind in nueva_poblacion:
            puntuacion = [0] * 2
            for i in range(len(ind)-2):
                # print(i)
                if(ind[i] == 1):
                    # caloria
                    puntuacion[0] += int(lista_productos[i][1])
                    # peso
                    puntuacion[1] += float(lista_productos[i][2])
            # añadir puntuacion 
            # print(ind[len(lista_productos)+1])
            ind[8] = puntuacion[0]
            ind[9] = puntuacion[1]
            
        mutacion -= 1
    
def mostrar_mejor_mochila():
    mejor_individuo = nueva_poblacion[0]

    for i in range(len(nueva_poblacion)):
        individuo = nueva_poblacion[i]
        if (individuo[8] >= calorias_min) and (individuo[9] <= peso_max):
            mejor_individuo = individuo
    print(f'mejor individuo: {mejor_individuo}')


def main():
    for gen in range(max_gen):
        if (gen == 0):
            crear_poblacion_inicial(10)
            cruzar_inidividuos(poblacion)
        else:
            cruzar_inidividuos(nueva_poblacion)
            mutar_individuo(mutacion, nueva_poblacion)
    mostrar_mejor_mochila()

if __name__ == '__main__':
    main()