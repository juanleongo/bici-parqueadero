from io import  open
from Estudiante import *
import pickle


ARCHIVO = "Estudiantes.pickle"



ESTUDIANTES=[]

def menu():
	print("Menu Principal")
	print("1. resgistro estudiante")
	print("2. ingrese al sistema")
	print("6. salir")

def agregar():
	with open(ARCHIVO,"wb") as f:
		
		nombre_e = input("ingrese el nombre:")
		apellido_e = input("ingrese la apellido:")
		edad_e = input("ingrese la edad:")
		tipo_de_documento = input("ingrese el tipo de documento:")
		numero_de_documento = input("ingrese el numero de documento:")
		codigo_estudiante=input("ingrese su codigo:")
		estudiante = Estudiante(nombre_e,apellido_e,edad_e,tipo_de_documento,numero_de_documento,codigo_estudiante) 
		ESTUDIANTES.append(estudiante)
		pickle.dump(ESTUDIANTES,f)


def buscar_estudiante(n_documento,codigo):
	with open(ARCHIVO, "rb") as f:
		estu = pickle.load(f)
		for alumno in estu:		
			if alumno.numero_documento == n_documento and alumno.codigo==codigo:
				print("ingreso con exito")
			else:
				print("no se encontro")


	#for alumno in ESTUDIANTES:
	#	if alumno.numero_documento == n_documento and alumno.codigo==codigo:
	#		print("ingreso con exito")
	#	else:
	#		print("no se encontro")

def login(n_documento,codigo):
	usuario = n_documento
	password=codigo
	buscar_estudiante(usuario,password)	

def mostar_lista():
	with open(ARCHIVO, "rb") as f:
		obj = pickle.load(f)
		print(obj)
