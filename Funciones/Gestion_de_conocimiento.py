from  Funciones import Operaciones

class Memoria:
    matriz = []
    instance = None

    def __init__(self):
        if not Memoria.instance:
            Memoria.instance = self

    def aumentar_memoria(self):

       if len(self.matriz) is 0:
           self.matriz.append([])
           self.matriz[0].append(None)
       else:
           largo_matriz = len(self.matriz)
           self.matriz.append([])
           for agregar_las_columnas in range (0,largo_matriz):
               self.matriz[len(self.matriz)-1].append(None)

           for lineas in range(0,len(self.matriz)):
                for columnas in range(0, len(self.matriz[lineas])):
                    if columnas is len(self.matriz[lineas]) -1:
                        self.matriz[lineas].append(None)
                        break

    def aprender(self, conocimiento):
        ingreso_en_matriz = False
        for lineas in range(0,len(self.matriz)):
           if ingreso_en_matriz:
               break

           for columna in range(len(self.matriz[lineas])):
                if self.matriz[lineas][columna] is None:
                    self.matriz[lineas][columna]= conocimiento
                    ingreso_en_matriz = True
                    break
        if not ingreso_en_matriz:
            self. aumentar_memoria()
            self.matriz[0][len(self.matriz)-1]= conocimiento

    def desaprender(self, olvida):
        for linea in range(len(self.matriz)):
            for columna in range(len(self.matriz[linea])):
                if olvida is self.matriz[linea][columna]:
                    self.matriz[linea][columna] = None

    def imprimir(self):
        cadena_de_sring=''
        for linea in range(len(self.matriz)):
            for columna in range (len(self.matriz[linea])):
                cadena_de_sring += str(self.matriz[linea][columna])+ ' '
            cadena_de_sring += '\n'
        return cadena_de_sring


class Fuente_de_conocimiento:
    def Aprender (self, tipo):
        if tipo is 'Suma':
            self.Aprender(Operaciones.Suma())

        elif tipo is 'Resta':
            self.Aprender(Operaciones.Resta())

        elif tipo is 'Division':
            self.Aprender(Operaciones.Division())

        elif tipo is 'Multiplicacion':
            self.Aprender(Operaciones.Multiplicacion)

        elif tipo is 'Pitagoras':
            self.Aprender(Operaciones.Pitagoras)

        elif tipo is 'Potencias':
            self.Aprender(Operaciones.Potencias)

        else:
            self.Aprender(Operaciones.Primo)

    #def reproducir:



creacion_de_memoria = Memoria()