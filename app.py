import tkinter as tk
class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LOGIN ADMIN")
        self.geometry("300x200")
        tk.Label(self, text= "Esta es la ventana principal").pack(pady=10)
        boton1 = tk.Button(self, text="Entrar", cursor="hand2", bg="#00f4fc", width=10, relief="flat", 
                              font=("Roboto", 13))# command=lambda: ventana2())
        boton1.place(x=200, y=100) 
        Contraseña = tk.Entry(self, textvariable=)
        Contraseña.pack
        Contraseña.get()
class Ventana2(tk.Toplevel):
    def ventana2(self):
        self.title("LOGIN ADMIN")
        self.geometry("300x200")
        tk.Label(self, text= "Esta es la ventana secundaria").pack(pady=10)


if __name__=="__main__":
    app = Main()
    app.mainloop()
