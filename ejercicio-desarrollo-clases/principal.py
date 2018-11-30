# Principal

# Importamos
from manejo import *

# Creamos el objeto para leer el archivo
m = MiArchivo() 

# Creamos el objeto para escribir el archivo
m2 = MiArchivoEscribir() 


lista = m.obtener_informacion()  # Obtenemos una lista en la cual cada elemento es una linea

lista = lista[1:6]			# Eliminanos el primero elemento (este elemento son los titulos) y el utlimo es un salto de linea
listaNueva = []  			# Creamos una nueva lista

# Separamos cada linea como otra lista
for linea in lista:
	linea = linea.split("|")               # Separamos la linea por el caracter '|'
	linea[3] = linea[3].replace('\n', '')  # Eliminamos el caracter '\n'del ultimo elemento
	listaNueva.append(linea) 			   # Agregamos la linea a la nueva lista


# Recorremos cada linea de la lista
for linea in listaNueva:

	objeto = Estudiante(linea[0], int(linea[1]), int(linea[2]), int(linea[3]))			 # Creamos el objeto para obtener el promedio
	m2.agregar_informacion(objeto)				 # Escribimos el resultado de los promedio en el nuevo archivo

# Cerramos los archivos para que no ocupen memoria
m.cerrar_archivo()
m2.cerrar_archivo()

print("Proceso realizado con éxito")


