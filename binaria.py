'''
Titulo: Busqueda binaria 
Descripcion: Este programa realiza la busqueda binaria dada la posicion del elemento que el usuario quiera buscar, en este caso, los elementos se cargar a traves de un txt
Fecha: 10 de marzo del 2022
Version: 1.0
Autor: Espinoza Bautista Daniel
'''

# Importamos la libreria Numpy y Time
import sys
import msvcrt
import numpy as np
from time import time

# Inicializamos el arreglo de numeros
numeros = []

# Leemos los numeros del archivo, y lo agregamos a un arreglo
arch = np.loadtxt("D:\\Documentos\\ESCOM\\7moSemestre\\Analisis\\Practica 1\\numeros.txt", dtype="str", delimiter=" ")

# Inicializamos la variable para el ciclo
i=0

# Mediante el ciclo convertimos el arreglo a enteros para
# poder trabajar de una manera mas eficiente con el
while i<len(arch)-1:
    aux = int(arch[i])
    numeros.append(aux)
    i+=1

# Solicitamos al usuario que nos diga la posicion que
# quiere buscar dentro del arreglo y a esta le restamos
# un 1 para que coincida con el arreglo
print("Posicion del elemento que deseas buscar")
pos = input()
pos = int(pos)
pos = pos - 1 

# Inicializamos la variable tiempo_in que nos ayudara a
# contar el tiempo de ejecucion del programa
tiempo_in = time()

# Realizamos la busqueda binaria
def busqueda_binaria(lista, pos):
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        punto_medio = (izq + der) // 2
        if lista[punto_medio] == lista[pos]:
            aux = lista[punto_medio]
            aux2 = pos+1
            return "Valor {} encontrado en la posicion {}".format(aux,aux2)
        if lista[punto_medio] > pos:
            der = punto_medio - 1
        if lista[punto_medio] < pos:
            izq = punto_medio + 1
    return "Elemento no encontrado"

# Ordenamos el arreglo de menor a mayor
numeros.sort()

# Imprimimos el mensaje que nos arroja la funcion de busqueda
mensaje = busqueda_binaria(numeros,pos)
print(mensaje)

# Calculamos el tiempo que tardo en encontrarlo
# y lo imprimimos
tiempo_fin = time() - tiempo_in
print("\nTiempo de ejecucion: %.10f segundos." % tiempo_fin)

# Presionar enter para salir
while True:
    print("\nPresione enter para salir ")
    m= str(msvcrt.getch(),'utf -8')
    if m == "\r":
        sys.exit()