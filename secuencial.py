'''
Titulo: Busqueda secuencial 
Descripcion: Este programa realiza la busqueda secuencial dada la posicion del elemento que el usuario quiera buscar, en este caso, los elementos se cargar
a traves de un txt
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
arch = np.loadtxt("path del documento txt", dtype="str", delimiter=" ")

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
print("Posicion que deseas buscar")
pos = input()
pos = int(pos)
pos = pos - 1

# Inicializamos las variables para el ciclo y para saber
# si el elemento existe o no
j=0
ex=0

# Inicializamos la variable tiempo_in que nos ayudara a
# contar el tiempo de ejecucion del programa
tiempo_in = time()

# Ordenamos el arreglo de menor a mayor
numeros.sort()

# Realizamos la busqueda secuencial del elemento
for j in range(len(numeros)):
    if j==(pos):
        print("Valor ",numeros[j]," encontrado en la posicion ",j+1)
        ex+=1

# Si el valor no se encuentra, se le notifica al
# usuario
if ex==0:
    print("Valor no encontrado en el arreglo")

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
