import tkinter as tk
from tkinter import ttk,messagebox
from Inicio import *


class Registro(tk.Tk):

	def __init__(self):
		super().__init__()

		self.geometry('800x600')

		self.title('Registro')
		self.configure(bg = 'beige')
		self.resizable(0,0)

		self.rowconfigure(0,weight=20)
		self.rowconfigure(1,weight=1)
		self.rowconfigure(2,weight=20)
		self.rowconfigure(3,weight=1)
		self.rowconfigure(4,weight=20)
		self.rowconfigure(5,weight=1)
		self.rowconfigure(6,weight=20)
		self.rowconfigure(7,weight=10)
		self.columnconfigure(0,weight=1)
		self.columnconfigure(1,weight=1)
		ESTUDIANTES=[]
		self._crear_componentes()


	def _crear_componentes(self):	
		letrero = tk.Label(self,text="Registro estudiante",font=("Helvetica",14))
		letrero.grid(row=0,column=0,columnspan=2)

		nombre=tk.StringVar(value="")
		self.in_nombre=ttk.Entry(self,width=20,justify=tk.CENTER, textvariable=nombre)
		self.in_nombre.grid(row=2,column=0)

		lt_nombre = tk.Label(self,text="Nombre:",font=("Helvetica",12))
		lt_nombre.grid(row=1,column=0)

		apellido=tk.StringVar(value="")
		self.in_apellido=ttk.Entry(self,width=20,justify=tk.CENTER, textvariable=apellido)
		self.in_apellido.grid(row=2,column=1)

		lt_apellido = tk.Label(self,text="Apellido:",font=("Helvetica",12))
		lt_apellido.grid(row=1,column=1)

		edad=tk.StringVar(value="")
		self.in_edad=ttk.Entry(self,width=20,justify=tk.CENTER, textvariable=edad)
		self.in_edad.grid(row=4,column=0)

		lt_edad = tk.Label(self,text="Edad:",font=("Helvetica",12))
		lt_edad.grid(row=3,column=0)

		tp_documento=tk.StringVar(value="")
		self.in_tp_documento=ttk.Entry(self,width=20,justify=tk.CENTER, textvariable=tp_documento)
		self.in_tp_documento.grid(row=4,column=1)

		lt_tp_documento = tk.Label(self,text="Tipo de documento:",font=("Helvetica",12))
		lt_tp_documento.grid(row=3,column=1)

		num_documento=tk.StringVar(value="")
		self.in_num_documento=ttk.Entry(self,width=20,justify=tk.CENTER, textvariable=num_documento)
		self.in_num_documento.grid(row=6,column=0)

		lt_num_documento = tk.Label(self,text="Numero de documento:",font=("Helvetica",12))
		lt_num_documento.grid(row=5,column=0)

		codigo=tk.StringVar(value="")
		self.in_codigo=ttk.Entry(self,width=20,justify=tk.CENTER, textvariable=codigo)
		self.in_codigo.grid(row=6,column=1)

		lt_codigo = tk.Label(self,text="codigo",font=("Helvetica",12))
		lt_codigo.grid(row=5,column=1)

		def enviar():
			with open(ARCHIVO,"wb") as f:
		
				nombre_e = self.in_nombre.get()
				apellido_e = self.in_apellido.get()
				edad_e = self.in_edad.get()
				tipo_de_documento = self.in_tp_documento.get()
				numero_de_documento = self.in_num_documento.get()
				codigo_estudiante=self.in_codigo.get()
				estudiante = Estudiante(nombre_e,apellido_e,edad_e,tipo_de_documento,numero_de_documento,codigo_estudiante) 
				ESTUDIANTES.append(estudiante)
				pickle.dump(ESTUDIANTES,f)	

			messagebox.showinfo('Registro',"Registro exitoso")

		def atras():
			ventana_inicio=Inicio()
			self.destroy()	

		def salir():
			self.destroy()	
			
		btn_enviar = ttk.Button(self,text='ENVIAR', command=enviar)
		btn_enviar.grid(row=7,column=0 , columnspan=2)

		btn_atras = ttk.Button(self,text='ATRAS', command=atras)
		btn_atras.grid(row=7,column=0 , columnspan=1)

		btn_salir = ttk.Button(self,text='SALIR', command=salir)
		btn_salir.grid(row=7,column=1 , columnspan=1)

	
	



#if __name__ == '__main__':
#	registro= Registro()
#	registro.mainloop()