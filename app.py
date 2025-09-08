import tkinter as tk
class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana principal")
        self.geometry("300x200")
        tk.Label(self, text= "Esta es la ventana principal").pack(pady=10)


if __name__=="__main__":
    app = Main()
    app.mainloop()
