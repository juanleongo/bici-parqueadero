import tkinter as tk
from tkinter import ttk,messagebox
from Inicio import *
from Bicicleta import *
from conexionBD import conexion
from controlador import ultima_persona,crearQR

class Registro_bicicleta(tk.Tk):

	def __init__(self):
		super().__init__()

		self.geometry('800x600')

		self.title('Registro-bicicleta')
		self.configure(bg = 'beige')
		self.resizable(0,0)

		self.rowconfigure(0,weight=20)
		self.rowconfigure(1,weight=1)
		self.rowconfigure(2,weight=20)
		self.rowconfigure(3,weight=1)

		self.columnconfigure(0,weight=1)
		self.columnconfigure(1,weight=1)
		
		self._crear_componentes()


	def _crear_componentes(self):	

		letrero = tk.Label(self,text="Registro Bicicleta",font=("Helvetica",14))
		letrero.grid(row=0,column=0,columnspan=2)

		marca=tk.StringVar(value="")
		self.in_marca=ttk.Entry(self,width=20,justify=tk.CENTER, textvariable=marca)
		self.in_marca.grid(row=2,column=0)

		lt_marca = tk.Label(self,text="Marca: ",font=("Helvetica",12))
		lt_marca.grid(row=1,column=0)

		color=tk.StringVar(value="")
		self.in_color=ttk.Entry(self,width=20,justify=tk.CENTER, textvariable=color)
		self.in_color.grid(row=2,column=1)

		lt_marca = tk.Label(self,text="Color: ",font=("Helvetica",12))
		lt_marca.grid(row=1,column=1)

		
		
		def enviar():
			
			persona = ultima_persona()
			idPersona = 0
			for i in persona:
				idPersona= i[0]	
			marca_e = self.in_marca.get()
			color_e = self.in_color.get()
			datos=(color_e,marca_e,idPersona)
			conec=conexion()
			cursor = conec.cursor()
			sentencia = f"INSERT INTO bicicleta VALUES(NULL,?,?,?)"
			cursor.execute(sentencia,datos)
			conec.commit()	
			crearQR()		
			conec.close()
			
			messagebox.showinfo('Registro',"Registro exitoso")

		def atras():
		
			self.destroy()	

		def salir():
			self.destroy()	
			
		btn_enviar = ttk.Button(self,text='ENVIAR', command=enviar)
		btn_enviar.grid(row=7,column=0 , columnspan=2)

		btn_atras = ttk.Button(self,text='ATRAS', command=atras)
		btn_atras.grid(row=7,column=0 , columnspan=1)

		btn_salir = ttk.Button(self,text='SALIR', command=salir)
		btn_salir.grid(row=7,column=1 , columnspan=1)