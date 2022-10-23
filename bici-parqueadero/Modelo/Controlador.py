from Estudiante import *

ARCHIVO = "agenda.txt"

ESTUDIANTES=[]

def menu():
	print("Menu Principal")
	print("3. agregar beneficiario")
	print("4. buscar beneficiario")
	print("5. borrar beneficiario")
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