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

    def recorre_matriz(self, nombre, parametro1, parametro2):
        existe= False
        for linea in range(len(self.matriz)):
            if existe is True:
                break
            for columna in range (len(self.matriz[linea])):
                if not self.matriz[linea][columna] is None:
                    instancia = self.matriz[linea][columna]
                    if nombre is instancia.get():
                        respuesta = instancia.opereciones(parametro1, parametro2)
                        print(respuesta)
                        existe = True
                        break


class Fuente_de_conocimiento:
    creacion_de_memoria = Memoria()

    def Aprender (self, tipo):

        if tipo is 'Suma':
            suma = Operaciones.Suma ()
            self.creacion_de_memoria.aprender(suma)

        elif tipo is 'Resta':
            self.creacion_de_memoria.aprender(Operaciones.Resta())

        elif tipo is 'Division':
            self.creacion_de_memoria.aprender(Operaciones.Division())

        elif tipo is 'Multiplicacion':
            self.creacion_de_memoria.aprender(Operaciones.Multiplicacion())

        elif tipo is 'pitagoras_cateto':
            self.creacion_de_memoria.aprender(Operaciones.piatgoras_cateto())

        elif tipo is 'pitagoras_hipotenusa':
            self.creacion_de_memoria.aprender(Operaciones.Pitagoras_hipotenusa())


        elif tipo is 'Potencias':
            self.creacion_de_memoria.aprender(Operaciones.Potencias())

        else:
            self.creacion_de_memoria.aprender(Operaciones.Primo())

        return
    def ejercer_conocimiento(self, nombre, parametro1, parametro2):
        self.creacion_de_memoria.recorre_matriz(nombre, parametro1, parametro2)
        print(self.creacion_de_memoria.matriz)

conocimiento = Fuente_de_conocimiento()
conocimiento.Aprender('Suma')
conocimiento.Aprender('Resta')
conocimiento.Aprender('Potencias')
conocimiento.Aprender('Primo')
conocimiento.Aprender('Suma')
conocimiento.ejercer_conocimiento('Primo', 6, 2)


