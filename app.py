#SAMIR ANDRÉS QUINTANA VERONA
#grupo: 55
#tutor: stevens moreno osorio
#turbo, 2025
import tkinter as tk
import sys
import getpass
import tkinter.messagebox
from tkinter import messagebox
from datetime import date
import json

class Main(tk.Tk):
    #en la siguiente funcion establecemos la GUI del programa
    def __init__(self):
        super().__init__()
        self.title("LOGIN")
        self.geometry("400x300")
        tk.Label(self, text= "ACADEMIA MELODÍAS PERFECTAS").pack(pady=1)
        tk.Label(self, text= "PROGRAMA PARA EL REGISTRO Y GESTIÓN DE PARTICIPANTES").pack(pady=2)
        tk.Label(self, text= "DESARROLLADOR: SAMIR ANDRÉS QUINTANA VERONA").pack(pady=3)

        #este botón utiliza su función lambda para llamar la siguiente función valiusuario
        boton1 = tk.Button(self, text="Entrar", cursor="hand2", bg="#00f4fc", width=10, relief="flat", command=lambda:valiusuario())
        boton1.place(x=150, y=150) 

        pwd_login = tk.StringVar()


        #entradas de información: parte de la interfaz grafica:


        entradapwd = tk.Entry(self, textvar=pwd_login, width=30, 
                                  font = ("Roboto", 13), relief="flat", bg="#1bf7da", show="*")
        entradapwd.place(x= 50, y = 100)
        

#en esta nueva funcion implementaremos la logica para validar el usuario. 
        #LOGICA
        def valiusuario():
            pwd_ = "123"
            passLogin = entradapwd.get()
            #con este condicional validaremos de forma sencilla la contraseña del usuario admin
            #con el comando abrirventana2()ejecutamos la función que abre la ventana GestionParticipantes
            if pwd_ == passLogin:
                messagebox.showinfo("Login Successful", "Welcome, Admin!")
                abrirVentana2()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")
                
         
        
           
        #LOGICA

        #en esta línea pediremos al usuario ingresar la contraseña
        #Contraseña = tk.Entry(self,)
        #Contraseña.pack
        #Contraseña.get()
        #aquí abri
        def abrirVentana2():
            
            self.withdraw()
            GestionParticipantes(self)
                #Ventana2(self)
                    #Ventana2(self)
                    #self.mainloop()
        self.mainloop()

            
class GestionParticipantes(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("PROCESO DE REGISTRO PARA LOS PARTICIPANTES")
        self.geometry("1366x768")
        tk.Label(self, text= "PORFAVOR INGRESE LOS SIGUIENTES DATOS").pack(pady=1, padx=1)

        #####botones para guardar registro, mostrar reporte y salir:
        boton2 = tk.Button(self, text="GUARDAR REGISTRO", cursor="hand2", bg="#00f4fc", width=30, relief="flat", command=self.guardarRegi)
        boton2.place(x=500, y=500) 
        boton2 = tk.Button(self, text="CALCULAR COSTO/MOSTRAR REPORTE", cursor="hand2", bg="#00f4fc", width=30, relief="flat", command=self.calcCostClase)
        boton2.place(x=600, y=550) 
        boton2 = tk.Button(self, text="SALIR", cursor="hand2", bg="#00f4fc", width=10, relief="flat", command=exit)
        boton2.place(x=700, y=600) 



        #boton2 = tk.Button(self, text="SALIR", cursor="hand2", bg="#00f4fc", width=10, relief="flat", command=self.abrirVentana3)
        #boton2.place(x=700, y=500) 


        ######### codigo para ingresar los datos del usuario#########s

        #variables donde guardaremos los datos del usuario

        self.iduser=tk.StringVar()
        self.NombreUsur= tk.StringVar()
        self.GenUsr=tk.StringVar()
        #IntVar()
        #self.GenUsr.set(0)
        self.TecArt=tk.StringVar()
        self.NumClaCant=tk.IntVar()
        self.NumClaCant.set(0)
        self.cantidadClases=tk.IntVar()
        self.cantidadClases.set(0)

        

#Ventana2
        # Variable compartida por los radiobuttons
        opcion = tk.StringVar(value="")  # valor inicial vacío

############## a continuación, podremos observar las entradas de información para el registro de cada participantes
        idLabel = tk.LabelFrame(self,padx=10, pady=10)
        idLabel.pack(padx=10, pady=10)

        idText = tk.Label(idLabel, text="IDENTIFICACION: ")
        idText.pack(side=tk.LEFT) 

        idID = tk.Entry(idLabel, textvar=self.iduser, width=15, 
                                  font = ("Roboto", 13), relief="flat", bg="#ffffff")
        idID.pack(side=tk.RIGHT)



##############
        NameLabel = tk.LabelFrame(self,padx=10, pady=10)
        NameLabel.pack(padx=10, pady=15)

        NameText = tk.Label(NameLabel, text="NOMBRE COMPLETO: ")
        NameText.pack(side=tk.LEFT)

        NameEntry = tk.Entry(NameLabel, textvar=self.NombreUsur, width=25, 
                          font = ("Roboto", 13), relief="flat", bg="#ffffff")
        NameEntry.pack(side=tk.RIGHT)

###############
        idGenLabel= tk.LabelFrame(self,padx=10, pady=10)
        idGenLabel.pack(padx=10, pady=15)

        idGenoption= tk.Label(idGenLabel, text="GÉNERO: ")
        idGenoption.pack(side=tk.LEFT)

       

        print("Usted seleccionó: ", self.GenUsr.get())

        tk.Radiobutton(idGenLabel, text="Masculino", variable=self.GenUsr, value="Masculino").pack(side=tk.RIGHT)
        tk.Radiobutton(idGenLabel, text="Femenino", variable=self.GenUsr, value="Femenino").pack(side=tk.RIGHT)
        

################### la siguiente es "la tabla de precios" pero convertida en un diccionario con una clave y un valor
        

        self.opciones= {
                "Dibujo": 70000, 
                "Pintura": 85000, 
                "Escritura": 100000, 
                "Fotografía" : 90000, 
                "Grabado" : 75000 
        }


        idTecArt= tk.LabelFrame(self,padx=10, pady=10)
        idTecArt.pack(padx=10, pady=15)

        idlistTec= tk.Label(idTecArt, text="TÉCNICA ARTÍSTICA:")
        idlistTec.pack(side=tk.LEFT)

        #este menu de opciones con tiene un parametro command, con el que llamaremos a la función actualizar_costo, para poder seleccionar otra opción y que el precio cambie/se actualice
        menuTec=tk.OptionMenu(idTecArt, self.TecArt, *self.opciones.keys(), command=self.actualizar_costo)
        menuTec.pack(side=tk.RIGHT)


###################
        idCost= tk.LabelFrame(self,padx=10, pady=10)
        idCost.pack(padx=10, pady=15)
                                           
        CostoL= tk.Label(idCost, text="COSTO POR CLASE: ")  
        CostoL.pack(side=tk.LEFT)

        ValorCosto = tk.Label(idCost, textvariable=self.NumClaCant )
        ValorCosto.pack(side=tk.RIGHT)

#################
        idNumCla= tk.LabelFrame(self,padx=10, pady=10)
        idNumCla.pack(padx=10, pady=15)

        NumCla=tk.Label(idNumCla, text="NUMERO DE CLASES: " )
        NumCla.pack(side=tk.LEFT)

        NumClaEntry = tk.Entry(idNumCla, textvar=self.cantidadClases, width=10, 
                          font = ("Roboto", 13), relief="flat", bg="#ffffff")
        NumClaEntry.pack(side=tk.RIGHT)


################# funciónpara actualizar la selección en el label de costo por clase

    def actualizar_costo(self, seleccion):
        #Cuando el usuario elige una técnica, se actualiza el precio
        precio = self.opciones.get(seleccion, 0)
        self.NumClaCant.set(str(precio))


        #self.mainloop()

#funcion para calcular los costos y mostrar el reporte
    def calcCostClase(self, master=None):
        super().__init__(master)
        self.title("PROCESO DE REGISTRO PARA LOS PARTICIPANTES")
        self.geometry("400x400")
        tk.Label(self, text= "REPORTE").pack(pady=1, padx=1)

        
        self.iduser= self.iduser.get()
        self.NombreUsur= self.NombreUsur.get()
        self.GenUsr=self.GenUsr.get()
        self.TecArt=self.TecArt.get()
        self.NumClaCant=self.NumClaCant.get()
        self.cantidadClases=self.cantidadClases.get()
        self.today = date.today()

        #numcla=self.NumClaCant
        #cantcla=self.cantidadClases


        #totalPagar= numcla*cantcla
   


        repPart = tk.LabelFrame(self, padx=20, pady=80)
        repPart.pack(padx=5, pady=5)

        calcRepPart = tk.Label(repPart, text="IDENTIFICACIÓN: " + self.iduser )
        calcRepPart.pack(anchor="w")

        calcRepPart = tk.Label(repPart, text="NOMBRE COMPLETO: " + self.NombreUsur )
        calcRepPart.pack(anchor="w")

        calcRepPart = tk.Label(repPart, text="GÉNERO: " + self.GenUsr )
        calcRepPart.pack(anchor="w")

        calcRepPart = tk.Label(repPart, text="TÉCNICA ARTÍSTICA: " + self.TecArt )
        calcRepPart.pack(anchor="w")

        calcRepPart = tk.Label(repPart, text="COSTO POR CLASE: " + str(self.NumClaCant))
        calcRepPart.pack(anchor="w")

        calcRepPart = tk.Label(repPart, text="FECHA DE REGISTRO: " + str(self.today))
        calcRepPart.pack(anchor="w")

        calcRepPart = tk.Label(repPart, text="CANTIDAD DE CLASES: " + str(self.cantidadClases))
        calcRepPart.pack(anchor="w")

        #formula para calcular el numero de clases con el precio por clase
        totalPagar = self.NumClaCant * self.cantidadClases

        calcRepPart = tk.Label(repPart, text="TOTAL A PAGAR: " + str(totalPagar))
        calcRepPart.pack(anchor="w")

        
        
        self.mainloop()


        # Función para actualizar el precio cuando cambie la selección
    #                                                                                                                                                                                                                              def mostrar_precio(self):
                #opcion = NumClaCant.get()                 # obtiene lo que seleccionó el usuario
               # costo = opciones[opcion]               # busca el precio en el diccionario
               # idCost.config(text=f"COSTO POR CLASE: ${costo}")  # actualiza el Label

        # OptionMenu (lista desplegable)
        #menu = tk.OptionMenu(idCost, NumClaCant, *opciones.keys())
        #menu.pack(side)

        

        # Detectar cambios en la selección
       # opcion.trace_add("write", mostrar_precio)



###################
        

    #def reporteV(self, master=None):






##################################################################################################################################


    #con esta función, guardaremos el registro que acabamos de hacer en un archivo .json

    def guardarRegi(self):

        data = {"PARTICIPANTES":[]} #crear un diccionario base

        data["PARTICIPANTES"].append({
            "IDENTIFICACION": self.iduser.get(),
            "NOMBRE COMPLETO": self.NombreUsur.get(),
            "GENERO":self.GenUsr.get(),
            "TECNICA ARTISTICA":self.TecArt.get(),
            "COSTO DE CLASE":self.NumClaCant.get(),
            "CANTIDAD DE CLASES":self.cantidadClases.get(),
            "FECHA DE REGISTRO":str(date.today())
            })
        
        with open ("registro.json", "w") as archivo_json:
            json.dump(data, archivo_json, indent=4)

                 

##la siguiente función y la siguiente clase no las puedo eliminar porque el programa se rompe. aún no descubro el porqué
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
        







