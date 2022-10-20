class Bicicleta:
	def __init__(self,color,marca,numero_serial):
		self._color=color
		self._marca=marca
		self._numero_serial=numero_serial

	@property
	def color(self):
		return self._color

	@color.setter
	def color(self, color):
		self._color = color

	@property
	def marca(self):
		return self._marca

	@marca.setter
	def marca(self, marca):
		self._marca = marca

	@property
	def numero_serial(self):
		return self._numero_serial

	@numero_serial.setter
	def numero_serial(self, numero_serial):
		self._numero_serial = numero_serial      	

	def __str__(self):
		return f'bicicleta : [{self._color},{self._marca},{self._numero_serial} ]'   


cicla = Bicicleta("amarillo","GW","545ds55")    	
print(cicla)