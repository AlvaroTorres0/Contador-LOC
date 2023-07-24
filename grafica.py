from matplotlib import pyplot as plt

class Grafica:
    def __init__(self,cantidades):
        codigo = float(cantidades[4])
        comentarios = float(cantidades[2])
        vacias = float(cantidades[3])
        # Armamos el arreglo con las cantidades ya separadas en variables
        arregloCantidades=(codigo,comentarios,vacias)

        self.lineas = ("Código","Comentarios","Vacías")
        colores = ("green","cyan","gray")
        explode =(0,0,0)

        fig,ax1 = plt.subplots()

        # Creamos la gráfica
        ax1.pie(arregloCantidades,colors=colores,labels=self.lineas,shadow = True, explode = explode, autopct="%1.1f%%")
        # Guardamos y le damos otras propiedades a la gráfica
        plt.legend()
        plt.title("Estadísticas")
        plt.savefig("grafica.png")