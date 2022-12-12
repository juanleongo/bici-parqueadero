import tkinter as tk
from tkinter import ttk, messagebox


class Ventana_validacion(tk.Tk):
    def __init__(self):
        super().__init__()
        
        
        self.geometry('300x300')
        self.title('valdiacion')
        self.resizable(0,0)
        
        self.rowconfigure(0,weight=1)        
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.resizable(0,0)
        self._crear_componentes()
        
   
    
    def _crear_componentes(self):
        def ingresar():
            messagebox.showinfo('validacion',"ingreso")
        def salir():
            messagebox.showinfo('validacion',"salida")
        
        
        ingreso= ttk.Button(self,text='INGRESO', command=ingresar)
        ingreso.grid(row=0,column=0 ,sticky='NWES',padx=10)

        salida = ttk.Button(self,text='SALIDA', command=salir)
        salida.grid(row=0,column=1 ,sticky='NWES',padx=10)

   