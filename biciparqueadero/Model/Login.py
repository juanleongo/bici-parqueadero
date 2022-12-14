
import tkinter as tk
from tkinter import ttk, messagebox
from controlador import login
from Ventana_validacion import Ventana_validacion
from Registro_bicicleta import *


class Login(tk.Tk):

    def __init__(self):
        super().__init__()
        # ventana principal
        self.geometry('300x150')
        self.title('Login')
        
        self.resizable(0,0)
        # configuración del grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        # Creamos los componentes
        self._crear_componentes()
        #self.ventana_validador()

    # Definir el método crear_componentes
    def _crear_componentes(self):
        # usuario
        usuario_etiqueta = ttk.Label(self, text='Usuario:')
        usuario_etiqueta.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.usuario_entrada = ttk.Entry(self)
        self.usuario_entrada.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        # password
        password_etiqueta = ttk.Label(self, text='Password:')
        password_etiqueta.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        self.password_entrada = ttk.Entry(self, show='*')
        self.password_entrada.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        # boton Login
        login_boton = ttk.Button(self, text='Login', command=self.login)
        login_boton.grid(row=3, column=0, columnspan=2)



    def login(self):

        resul =  login(self.usuario_entrada.get(),self.password_entrada.get())
        user=""
        contra=""
        for i in resul:
            user=i[0]
            contra=i[1]
        print(user)
        print(contra)    
        try:    
        
            if self.usuario_entrada.get() == user and self.password_entrada.get() == 0 :
                #messagebox.showinfo('validacion',"vigilante")
                Ventana_validacion()

            elif self.usuario_entrada.get()== user  and self.password_entrada.get()== contra :                
                Registro_bicicleta()
                    
            else:            
                messagebox.showinfo('validacion',"estudiante no registrado")    
        except:
              messagebox.showinfo('validacion',"datos incorrectos")  

            



# Ejecutar la ventana
#if __name__ == '__main__':
    #login_ventana = Login()
    #login_ventana.mainloop()