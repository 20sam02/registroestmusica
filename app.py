import tkinter as tk
import sys
import getpass
import tkinter.messagebox
from tkinter import messagebox
class Main(tk.Tk):
    #en la siguiente funcion establecemos la GUI del programa
    def __init__(self):
        super().__init__()
        self.title("LOGIN ADMIN")
        self.geometry("300x300")
        tk.Label(self, text= "Esta es la ventana principal").pack(pady=10)
        boton1 = tk.Button(self, text="Entrar", cursor="hand2", bg="#00f4fc", width=10, relief="flat", command=lambda:valiusuario)
        boton1.place(x=200, y=100) 

        pwd_login = tk.StringVar()


        #entradas de información: parte de la interfaz grafica:


        entradapwd = tk.Entry(self, textvar=pwd_login, width=30, 
                                  font = ("Roboto", 13), relief="flat", bg="#1bf7da", show="*")
        entradapwd.place(x= 170, y = 170)
        

#en esta nueva funcion implementaremos la logica para validar el usuario
        #LOGICA
        def valiusuario():
            pwd_ = "123"
            passLogin = entradapwd.get()
            
            if pwd_ == passLogin:
                messagebox.showinfo("Login Successful", "Welcome, Admin!")
                abrirVentana2
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")
                
                #sys.exit()
         
        
           
        #LOGICA

        #en esta línea pediremos al usuario ingresar la contraseña
        #Contraseña = tk.Entry(self,)
        #Contraseña.pack
        #Contraseña.get()
        
            def abrirVentana2(self):
                    #self.withdraw
                Ventana2(self)
                    #Ventana2(self)
                    #self.mainloop()

class Ventana2(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("LOGIN ADMIN")
        self.geometry("500x300")
        tk.Label(self, text= "Esta es la ventana secundaria").pack(pady=100)
        #LOGICA

        #LOGICA
        boton1 = tk.Button(self, text="Entrar", cursor="hand2", bg="#00f4fc", width=10, relief="flat", command=self.abrirVentana3)
        boton1.place(x=200, y=100) 
    def abrirVentana3(self):
        Ventana3(self)



class Ventana3(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("LOGIN ADMIN")
        self.geometry("500x300")
        tk.Label(self, text= "Esta es la ventana secundaria").pack(pady=100)
        #LOGICA
        #LOGICA
        boton1 = tk.Button(self, text="salir", cursor="hand2", bg="#00f4fc", width=10, relief="flat", command=exit)
        boton1.place(x=200, y=100) 

#if __name__=="__main__":
    app = Main()
    app.mainloop()
