from operaciones import Operaciones
from grafica import Grafica
from PIL import ImageTk
from tkinter import *
from PIL import Image
import PIL.Image

class CrearVentana:
    def __init__(self):
        # Creamos el objeto de la clase Operaciones
        self.operations = Operaciones()

        # Creamos la ventana Principal
        self.ventanaPrincipal = Tk()
        ancho_ventana = 500
        alto_ventana = 550
        x_ventana = self.ventanaPrincipal.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.ventanaPrincipal.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)

        self.ventanaPrincipal.geometry(posicion)
        self.ventanaPrincipal.title("Contador LOC")
        self.ventanaPrincipal.configure(background="#191919")
        self.ventanaPrincipal.resizable(0,0)

        # Creamos el contenedor
        self.contenedor = Frame(self.ventanaPrincipal)
        self.contenedor.configure(background="#313131", width=450, height=500)
        self.contenedor.place(x=25, y=20)

        # Creamos Label de bienvenida
        self.lblTitulo = Label(self.ventanaPrincipal, text="Contador LOC", font=("Courier", 17), fg="#fff",
                               bg="#313131")
        self.lblTitulo.place(x=165,y=50)

        # Botón VSCODE
        img = Image.open('vscode.png')
        img = ImageTk.PhotoImage(img)
        self.btnVSCODE = Button(self.ventanaPrincipal, text="Crear código fuente",image=img,bg="#313131", fg="#fff", activebackground="#313131",command=self.operations.abrirVSCODE,compound = LEFT,font=("Lucida Console", 14))
        self.btnVSCODE.place(x=120, y=120)
        self.btnVSCODE.config(bd=5)

        # Botón Archivo
        img2 = Image.open('archivo.png')
        img2 = ImageTk.PhotoImage(img2)
        self.btnArchivo = Button(self.ventanaPrincipal, text="Seleccionar archivo", image=img2, bg="#313131",
                                fg="#fff", activebackground="#313131", compound=LEFT,font=("Lucida Console", 14),command=self.datosArchivo)
        self.btnArchivo.place(x=120, y=210)
        self.btnArchivo.config(bd=5)

        # Datos del archivo
        self.lblNombreArchivo = Label(self.ventanaPrincipal, text="Nombre del Archivo: ", bg="#313131",font=("Lucida Console", 11), fg="#ffffff")
        self.lblNombreArchivo.place(x=25, y=325)
        self.entryNombreArchivo = Entry(self.ventanaPrincipal, width=20, font=("Courier", 13), bg="#313131",fg="#ffffff")
        self.entryNombreArchivo.place(x=240, y=320)

        self.lblNumeroTotal = Label(self.ventanaPrincipal, text="Total de líneas: ", bg="#313131",font=("Lucida Console", 11), fg="#ffffff")
        self.lblNumeroTotal.place(x=25, y=365)
        self.entryNumeroTotal = Entry(self.ventanaPrincipal, width=20, font=("Courier", 13), bg="#313131",fg="#ffffff")
        self.entryNumeroTotal.place(x=240, y=360)

        self.lblNumeroComentarios = Label(self.ventanaPrincipal, text="Líneas de comentarios: ", bg="#313131",font=("Lucida Console", 11), fg="#ffffff")
        self.lblNumeroComentarios.place(x=25, y=405)
        self.entryNumeroComentarios = Entry(self.ventanaPrincipal, width=20, font=("Courier", 13), bg="#313131", fg="#ffffff")
        self.entryNumeroComentarios.place(x=240, y=400)

        self.lblNumeroVacias = Label(self.ventanaPrincipal, text="Líneas vacías: ", bg="#313131", font=("Lucida Console", 11), fg="#ffffff")
        self.lblNumeroVacias.place(x=25, y=445)
        self.entryNumeroVacias = Entry(self.ventanaPrincipal, width=20, font=("Courier", 13), bg="#313131",fg="#ffffff")
        self.entryNumeroVacias.place(x=240, y=440)

        self.lblNumeroCodigo = Label(self.ventanaPrincipal, text="Líneas de código puro: ", bg="#313131",font=("Lucida Console", 11), fg="#ffffff")
        self.lblNumeroCodigo.place(x=25, y=485)
        self.entryNumeroCodigo = Entry(self.ventanaPrincipal, width=20, font=("Courier", 13), bg="#313131",fg="#ffffff")
        self.entryNumeroCodigo.place(x=240, y=480)

        self.ventanaPrincipal.mainloop()

    # Este método es el que se encarga de llamar los métodos de la clase Operaciones
    def datosArchivo(self):
        # Vaciamos las cajas por si están llenas
        self.entryNombreArchivo.delete(0, "end")
        self.entryNumeroTotal.delete(0, "end")
        self.entryNumeroComentarios.delete(0, "end")
        self.entryNumeroVacias.delete(0, "end")
        self.entryNumeroCodigo.delete(0, "end")


        self.operations.seleccionarArchivo()

        self.datos = self.operations.retornarDatos()

        # Asignamos los resultados a los entrys
        self.entryNombreArchivo.insert(0, self.datos[0])
        self.entryNumeroTotal.insert(0, self.datos[1])
        self.entryNumeroComentarios.insert(0, self.datos[2])
        self.entryNumeroVacias.insert(0, self.datos[3])
        self.entryNumeroCodigo.insert(0, self.datos[4])

        self.modificarVentanaPrincipal()

    # Creamos la ventana que se sobrepondrá a la principal
    def modificarVentanaPrincipal(self):
        ancho_ventana = 1200
        alto_ventana = 550
        x_ventana = self.ventanaPrincipal.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.ventanaPrincipal.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        # Redimencionamos la ventana
        self.ventanaPrincipal.geometry(posicion)

        self.grafica = Grafica(self.datos)

        self.colocarGrafica()


    def colocarGrafica(self):
        fp = open("grafica.png", "rb")
        img = PIL.Image.open(fp)
        img = img.resize((670, 498), Image.ANTIALIAS)
        # La mandamos a la clase para después pasarla a un label
        self.grafica = ImageTk.PhotoImage(img)

        # Creamos el label que la contendrá
        self.lblGrafica = Label(self.ventanaPrincipal, image=self.grafica, bg="#ec5353")
        self.lblGrafica.place(x=500,y=20)