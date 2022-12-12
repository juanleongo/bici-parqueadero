from Persona import *

class Profesor (Persona):
	def __init__(self,nombre,apellido,fecha_nacimiento,tipo_documento,numero_documento,carrera):
		super().__init__(nombre,apellido,fecha_nacimiento,tipo_documento,numero_documento)
		self._carrera = carrera


	@property
	def carrera(self):
		return self._carrera

	@carrera.setter
	def carrera(self,carrera):
		self._carrera=carrera

	def __str__(self):
		return f'Profesor : {self._carrera}, {super().__str__()}'

persona1 = Persona('Juan', 'su papa ',2020,' cc ',214525)
print(persona1)

empleado1 = Profesor('Karla ',' ssss ',2020,' yi ',4252142,"sistemas")
print(empleado1)						