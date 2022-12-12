class Bicicleta:
	def __init__(self,color,marca):
		self._color=color
		self._marca=marca
		

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

	      	

	def __str__(self):
		return f'bicicleta : [{self._color},{self._marca}]'   


