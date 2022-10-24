from Estudiante import *

ARCHIVO = "agenda.txt"

ESTUDIANTES=[]

def menu():
	print("Menu Principal")
	print("1. resgistro estudiante")
	print("6. salir")

def agregar():
	nombre_e = input("ingrese el nombre:")
	apellido_e = input("ingrese la apellido:")
	edad_e = input("ingrese la edad:")
	tipo_de_documento = input("ingrese el tipo de documento:")
	numero_de_documento = input("ingrese el numero de documento:")
	codigo_estudiante=input("ingrese su codigo:")
	estudiante = Estudiante(nombre_e,apellido_e,edad_e,tipo_de_documento,numero_de_documento,codigo_estudiante) 
	ESTUDIANTES.append(estudiante)
	#datos.write(estudiante)

def buscar_estudiante(codigo,n_documento):
	for alumno in ESTUDIANTES:
		if alumno.codigo==codigo and alumno.numero_documento==n_documento:
			print("ingreso con exito")
		else:
			print("no se encontro")

def login(n_documento,codigo):
	usuario = numero_documento
	password=codigo
	buscar_estudiante(n_documento,codigo)	

def mostar_lista():
	for i in ESTUDIANTES:
		print(i)


while True:
	menu()
	opcion = input()
	if opcion == "3":
		print("Digite la información del beneficiario a agregar:")
		agregar()
		mostar_lista()
	else:
		break		
