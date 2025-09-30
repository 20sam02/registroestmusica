import tkinter as tk
import sys
import getpass
import tkinter.messagebox
from tkinter import messagebox
class Main(tk.Tk):
    #en la siguiente funcion establecemos la GUI del programa
    def __init__(self):
        super().__init__()
        self.title("LOGIN")
        self.geometry("400x300")
        tk.Label(self, text= "ACADEMIA MELODÍAS PERFECTAS").pack(pady=1)
        tk.Label(self, text= "PROGRAMA PARA EL REGISTRO Y GESTIÓN DE PARTICIPANTES").pack(pady=2)
        tk.Label(self, text= "DESARROLLADOR: SAMIR ANDRÉS QUINTANA VERONA").pack(pady=3)
        boton1 = tk.Button(self, text="Entrar", cursor="hand2", bg="#00f4fc", width=10, relief="flat", command=lambda:valiusuario())
        boton1.place(x=150, y=150) 

        pwd_login = tk.StringVar()


        #entradas de información: parte de la interfaz grafica:


        entradapwd = tk.Entry(self, textvar=pwd_login, width=30, 
                                  font = ("Roboto", 13), relief="flat", bg="#1bf7da", show="*")
        entradapwd.place(x= 50, y = 100)
        

#en esta nueva funcion implementaremos la logica para validar el usuario
        #LOGICA
        def valiusuario():
            pwd_ = "123"
            passLogin = entradapwd.get()
            
            if pwd_ == passLogin:
                messagebox.showinfo("Login Successful", "Welcome, Admin!")
                abrirVentana2()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")
                
                #sys.exit()
         
        
           
        #LOGICA

        #en esta línea pediremos al usuario ingresar la contraseña
        #Contraseña = tk.Entry(self,)
        #Contraseña.pack
        #Contraseña.get()
        
        def abrirVentana2():
            
            self.withdraw()
            Ventana2(self)
                #Ventana2(self)
                    #Ventana2(self)
                    #self.mainloop()
        self.mainloop()

            
class Ventana2(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("PROCESO DE REGISTRO PARA LOS PARTICIPANTES")
        self.geometry("1366x768")
        tk.Label(self, text= "PORFAVOR INGRESE LOS SIGUIENTES DATOS").pack(pady=1, padx=1)

        #####botones:
        boton2 = tk.Button(self, text="GUARDAR REGISTRO", cursor="hand2", bg="#00f4fc", width=10, relief="flat", command=self.abrirVentana3)
        boton2.place(x=500, y=500) 
        boton2 = tk.Button(self, text="CALCULAR COSTO/MOSTRAR REPORTE", cursor="hand2", bg="#00f4fc", width=10, relief="flat", command=self.abrirVentana3)
        boton2.place(x=600, y=500) 
        boton2 = tk.Button(self, text="SALIR", cursor="hand2", bg="#00f4fc", width=10, relief="flat", command=self.abrirVentana3)
        boton2.place(x=700, y=500) 

        ######### codigo para ingresar los datos del usuario#########

        #variables donde guardaremos los datos del usuario

        iduser=tk.StringVar()
        NombreUsur= tk.StringVar()
        GenUsr=tk.IntVar()
        GenUsr.set(0)
        TecArt=tk.StringVar()
        NumClaCant=tk.IntVar()
        NumClaCant.set(0)


        # Variable compartida por los radiobuttons
        opcion = tk.StringVar(value="")  # valor inicial vacío

##############
        idLabel = tk.LabelFrame(self,padx=10, pady=10)
        idLabel.pack(padx=10, pady=10)

        idText = tk.Label(idLabel, text="IDENTIFICACION: ")
        idText.pack(side=tk.LEFT) 

        idID = tk.Entry(idLabel, textvar=iduser, width=15, 
                                  font = ("Roboto", 13), relief="flat", bg="#ffffff")
        idID.pack(side=tk.RIGHT)



##############
        NameLabel = tk.LabelFrame(self,padx=10, pady=10)
        NameLabel.pack(padx=10, pady=15)

        NameText = tk.Label(NameLabel, text="NOMBRE COMPLETO: ")
        NameText.pack(side=tk.LEFT)

        NameEntry = tk.Entry(NameLabel, textvar=NombreUsur, width=25, 
                          font = ("Roboto", 13), relief="flat", bg="#ffffff")
        NameEntry.pack(side=tk.RIGHT)

###############
        idGenLabel= tk.LabelFrame(self,padx=10, pady=10)
        idGenLabel.pack(padx=10, pady=15)

        idGenoption= tk.Label(idGenLabel, text="GÉNERO: ")
        idGenoption.pack(side=tk.LEFT)

       

        print("Usted seleccionó: ", GenUsr.get())

        tk.Radiobutton(idGenLabel, text="Opción 1", variable=GenUsr, value=1).pack(side=tk.RIGHT)
        tk.Radiobutton(idGenLabel, text="Opción 2", variable=GenUsr, value=2).pack(side=tk.RIGHT)
        

###################
        

        opciones= {
                "Dibujo": 70000, 
                "Pintura": 85000, 
                "Escritura": 100000, 
                "Fotografía" : 90000, 
                "Grabado" : 75000 
        }


        #idTecArt= tk.LabelFrame(self,padx=10, pady=10)
        #idTecArt.pack(padx=10, pady=15)

       # idlistTec= tk.Label(idTecArt, text="TÉCNICA ARTÍSTICA:")
        #idlistTec.pack(side=tk.LEFT)


###################
        idCost= tk.LabelFrame(self,padx=10, pady=10)
        idCost.pack(padx=10, pady=15)

        Costo= tk.Label(idCost, text="TÉCNICA ARTÍSTICA: " + str(opciones["Dibujo"]), font=("Arial",12 ))       
        Costo.pack(side=tk.LEFT)

        

        # Función para actualizar el precio cuando cambie la selección
        def mostrar_precio(*args):
                opciones = NumClaCant.get()                 # obtiene lo que seleccionó el usuario
                opcion = opciones[opciones]               # busca el precio en el diccionario
                Costo.config(text=f"COSTO POR CLASE: ${opcion}")  # actualiza el Label

        # OptionMenu (lista desplegable)
        #menu = tk.OptionMenu(idCost, NumClaCant, *opciones.keys())
        #menu.pack(side)

        menuTec=tk.OptionMenu(idCost, TecArt, *opciones.keys())
        menuTec.pack(side=tk.LEFT)

        # Detectar cambios en la selección
        opcion.trace_add("write", mostrar_precio)

        self.mainloop()

        

###################
        idNumCla= tk.LabelFrame(self,padx=10, pady=10)
        idNumCla.pack(padx=10, pady=15)

        NumCla=tk.Label(idNumCla, text="NUMERO DE CLASES:")
        NumCla.pack(side=tk.LEFT)

        NumClaEntry = tk.Entry(idNumCla, textvar=NumClaCant, width=10, 
                          font = ("Roboto", 13), relief="flat", bg="#ffffff")
        NumClaEntry.pack(side=tk.RIGHT)

    def reporteV(self, master=None):






##################################################################################################################################

    
        def reporte(self):
            Ventana31()



    def abrirVentana3(self):
        Ventana3(self)



class Ventana3(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("REPORTE")
        self.geometry("500x500")
        tk.Label(self, text= "Esta es la ventana secundaria").pack(pady=10)
        #LOGICA
        #LOGICA
        boton1 = tk.Button(self, text="salir", cursor="hand2", bg="#00f4fc", width=10, relief="flat", command=exit)
        boton1.place(x=200, y=100) 

#if __name__=="__main__":
    app = Main()
    app.mainloop()
