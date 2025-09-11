import tkinter as tk
class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LOGIN ADMIN")
        self.geometry("300x300")
        tk.Label(self, text= "Esta es la ventana principal").pack(pady=10)
        boton1 = tk.Button(self, text="Entrar", cursor="hand2", bg="#00f4fc", width=10, relief="flat", command=self.abrirVentana2)
        boton1.place(x=200, y=100) 

        #en esta línea pediremos al usuario ingresar la contraseña
        Contraseña = tk.Entry(self)
        Contraseña.pack
        Contraseña.get()
        
    def abrirVentana2(self):
        Ventana2(self)

class Ventana2(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("LOGIN ADMIN")
        self.geometry("500x300")
        tk.Label(self, text= "Esta es la ventana secundaria").pack(pady=100)
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
        boton1 = tk.Button(self, text="salir", cursor="hand2", bg="#00f4fc", width=10, relief="flat", command=exit)
        boton1.place(x=200, y=100) 

if __name__=="__main__":
    app = Main()
    app.mainloop()
