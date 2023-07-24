import subprocess
from tkinter import messagebox
from tkinter import filedialog
import ntpath

class Operaciones:
    def __init__(self):
        self.arregloDatos=[]

    def abrirVSCODE(self):
        comando="code"
        subprocess.check_output(comando,shell=True)

    # Todo empieza seleccionando el archivo, de aquí derivan los demás métodos
    def seleccionarArchivo(self):
        # Vaciamos de nuevo el arreglo grande ya que si no los datos se van almacenando
        self.arregloDatos = []
        ruta = filedialog.askopenfilename(title="Seleccionar Archivo")
        self.identificarNombre(ruta)


    def identificarNombre(self,ruta):
        # Sacamos el nombre del archivo
        nombreArchivo=ntpath.basename(ruta)
        self.arregloDatos.append(nombreArchivo)
        self.calcularLineas(ruta)

    def calcularLineas(self,ruta):
        lineasTotales = 0
        lineasVacias = 0
        lineasComentarios = 0
        lineasVaciasComentarios = 0

        self.comentarioMultilinea = False

        # Abrimos el Archivo y lo leemos con el for
        archivo = open(ruta,"r")

        for linea in archivo:
            # Este método elimina los espacios y tabulaciones del inicio de la línea
            lineaLeida = linea.lstrip()

            # Calculamos las líneas totales
            lineasTotales += 1

            # Validamos si la línea está vacía pero está dentro de un código multilinea la mandamos a vacías
            if linea.isspace() and self.comentarioMultilinea:
                lineasVaciasComentarios += 1

            # Calculamos las líneas vacías
            if linea.isspace():
                lineasVacias += 1

            # Validamos si hay un cometarioMultilinea abierto
            if self.comentarioMultilinea == True:
                lineasComentarios+=1

            # Validamos si la línea comienza con "'''" y si el comentario multilinea está falso, entonces significa que se está abriendo un nuevo comentario
            if lineaLeida.startswith("'''") and self.comentarioMultilinea==False:
                lineasComentarios+=1
                self.comentarioMultilinea=True

            # Hacemos elif ya que si se cumple la de arriba como que se cicla y hace un desmadre
            # También validamos si ya hay un comentarioMultilinea abierto y se topa de nuevo con "'''" significa que cierra
            elif self.comentarioMultilinea==True and lineaLeida.startswith("'''"):
                self.comentarioMultilinea=False

            # Calculamos comentarios de una línea
            if lineaLeida.startswith("#"):
                lineasComentarios+=1

        archivo.close()

        # Hacemos la resta si es que hay líneas vacías dentro de comentarios
        # LineasComentarios -= lineasVaciasComentarios


        # Calculamos las líneas de código puro
        lineasCodigoPuro = lineasTotales - lineasComentarios - lineasVacias + lineasVaciasComentarios

        self.arregloDatos.append(lineasTotales)
        self.arregloDatos.append(lineasComentarios)
        self.arregloDatos.append(lineasVacias)
        self.arregloDatos.append(lineasCodigoPuro)

    # Nos devuelve todos los datos del archivo
    def retornarDatos(self):
        # Validamos si es que hay un error de cierre en los comentarios multilineas
        if self.comentarioMultilinea == True:
            messagebox.showerror(title="Error", message="Su código presenta errores en los comentarios")
            self.arregloDatos = [0,0,0,0,0]
        return self.arregloDatos