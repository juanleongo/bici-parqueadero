from Persona import *

class Funcionario(Persona):
	def __init__(self,nombre,apellido,fecha_nacimiento,tipo_documento,numero_documento,codigo):
		super().__init__(nombre,apellido,fecha_nacimiento,tipo_documento,numero_documento)
		self._codigo = codigo


	@property
	def codigo(self):
		return self._codigo

	@codigo.setter
	def codigo(self,codigo):
		self._codigo=codigo

	def __str__(self):
		return f'Funcionario: {self._codigo}, {super().__str__()}'

persona1 = Persona('Juan', 'su papa ',2020,' cc ',214525)
print(persona1)

empleado1 = Funcionario('jaime',' ssss ',2001,' yi ',4252142,"guachiman")
print(empleado1)						