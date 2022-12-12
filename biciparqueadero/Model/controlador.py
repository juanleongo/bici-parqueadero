import qrcode
from Estudiante import *
from conexionBD import conexion


def buscar_estudiante(n_documento,codigo):

	conec=conexion()  
	cursor = conec.cursor()
	sentencia = f"SELECT NumeroDocumento,Codigo FROM persona WHERE NumeroDocumento={n_documento} AND Codigo={codigo}"
	resultado= cursor.execute(sentencia)
	usuario=""
	password=""
	
	"""
	for fila in resultado:
		usuario=fila[0]
		password=fila[1]

		
	if usuario==n_documento and password==codigo:
		
		return 1
	else:
		return 0	

	"""
	return resultado

def login(n_documento,codigo):

	usuario = n_documento
	password=codigo
	validacion=buscar_estudiante(usuario,password)	

	return validacion

def ultima_persona():
	conec=conexion()  
	cursor = conec.cursor()	
	sentencia =  ' SELECT * FROM persona WHERE ID_persona = (SELECT MAX(ID_persona) FROM persona) '
	resultado = cursor.execute(sentencia)
	
	return resultado

def actualizar_bici(id,bici):
	conec=conexion()  
	cursor = conec.cursor()	
	sentencia = f"UPDATE persona set id_bicicleta='{bici}' WHERE ID_persona= {id}"
	cursor.execute(sentencia)
	
	conec.commit
	
	return True

def ultima_bici():
	
	conec=conexion()  
	cursor = conec.cursor()
	sentencia =  f"SELECT * FROM bicicleta WHERE IDBicicleta = (SELECT MAX(IDBicicleta) FROM bicicleta)"
	resltado = cursor.execute(sentencia)
	
	return resltado

def crearQR():
	bici=ultima_bici()
	person=ultima_persona()
	for i in bici:
		Idbici=i[1]
	for j in person:
		idp=j[0]
		nombre=j[1]	
		codigo= j[2]
	idperson=str(idp)
	input = (nombre,codigo,Idbici)
	qr = qrcode.QRCode(version=1,box_size=10,border=5)
	qr.add_data(input)
	qr.make(fit=True)
	img = qr.make_image(fill='black',back_color='white')
	img.save('qrs/qr_estudiante'+idperson+'.png')	





