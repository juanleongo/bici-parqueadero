import tkinter as tk
from tkinter import ttk,messagebox
from Registro import *
from Login import *
import sqlite3

class Inicio(tk.Tk):

    def __init__(self):
        super().__init__() 
        self.geometry('800x600')
        self.title('BICI-PARKING')
        self.configure(bg = 'beige')
        self.resizable(0,0)

        self.rowconfigure(0,weight=5)
        self.rowconfigure(1,weight=1)
        self.rowconfigure(2,weight=1)
        self.columnconfigure(0,weight=1)        
        self.columnconfigure(1,weight=1)
        
        self._crear_componentes()
        


    def _crear_componentes(self):

        letrero = tk.Label(self,text="BIENVENIDOS A BICI-PARKING\nUD",font=("Helvetica",14))
        letrero.grid(row=0,column=0,columnspan=3)

        def registrar():
            ventana_resgistro = Registro()
            self.destroy()
            

        registro = ttk.Button(self,text='REGISTRAR', command=registrar)
        registro.grid(row=1,column=0 ,sticky='NWES',padx=10)

        def ingresar():
            ventana_login= Login()
            self.destroy()
            

        ingreso = ttk.Button(self,text='INICIAR SESION', command=ingresar)
        ingreso.grid(row=1,column=1 ,sticky='NWES',padx=10)


if __name__ == '__main__':
    principal = Inicio()
    principal.mainloop()