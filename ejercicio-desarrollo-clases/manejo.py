# Clases

import codecs

# Creando una clase estudiante
class Estudiante():


	# Construcotr
	def __init__(self, name, n1, n2, n3):
		self.name = name
		self.n1 = n1
		self.n2 = n2
		self.n3 = n3
		
	def obtener_nombre(self):
		return self.name

	# Metodo para retornar el promedio del estudiante
	def obtener_promedio(self):
		self.promedio = (self.n1 + self.n2 + self.n3) / 3
		return self.promedio



# Creando la clase para abrir el archivo y obtener informacion
class MiArchivo:

    # Construcotr
    def __init__(self):
        self.archivo = codecs.open("informacion.csv", "r")

    # Metoodo que devuelve una lista de en la cual cada elemento es una linea
    def obtener_informacion(self):
        return self.archivo.readlines()

    # Metodo para cerrar el archivo
    def cerrar_archivo(self):
        self.archivo.close()


# Crendo la calse para poder escribir en el archivo
class MiArchivoEscribir:
    # Constructor que abre un nuevo archivo o ya existente llamado promedio.csv
    def __init__(self):
        self.archivo = codecs.open("promedios.csv", "a")

    # Metodo para agregar informacion al archivo
    def agregar_informacion(self, p):
        self.archivo.write("%s tiene un promedio de: %.2f\n" % (p.obtener_nombre(), p.obtener_promedio()))

    # Metodo para cerrar el archivo
    def cerrar_archivo(self):
        self.archivo.close()




