class Memoria:

    matriz = []
    ultima_linea=0
    ultima_columna = 0

    def __init__(self, id_conocimiento):
        self.matriz = self.matriz
        return

    def Agrega_linea(self):
        self.matriz.append([])

    def Agrega_columna(self, valor_de_linea):
        self.matriz[valor_de_linea].append()

    def Agregar(self):
        for lineas in range(self.matriz):
            self.Agrega_linea()
            for columna in range(self.matriz):
                self.Agrega_columna(lineas)

    def Eliminar_conocimiento(self, linea, columna):
        self.matriz[linea,columna] = ''
        return

    def Eliminar_conocimiento(self, id_conocimiento):
        return

    def Tamaño_actual(self):
        return

    def Obtener_conocimiento(self, linea, columna):
        return