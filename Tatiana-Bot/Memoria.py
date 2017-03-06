class Memoria:
    matriz = []
    instance = None

    def __init__(self):
        if not Memoria.instance:
            Memoria.instance = self

    def Aumento_de_memoria(self):

       if len(self.matriz) is 0:
           self.matriz.append([])
           self.matriz[0].append(None)
       else:
           largo_matriz = len(self.matriz)
           self.matriz.append([])
           for intento2000 in range (0,largo_matriz):
                self.matriz[len(self.matriz)-1].append(None)
                '''
           for lineas in range(0,len(self.matriz)):
                for columnas in range(0, len(self.matriz[lineas])):
                    if lineas is len(self.matriz[lineas]) - 1:
                        self.matriz[lineas].append([])
'''
    def Aprender(self, conocimiento):
        ingreso_en_matriz = False
        for lineas in range(len(self.matriz)-1):
            if ingreso_en_matriz:
                break
            for columna in range(len(self.matriz[lineas])-1):
                if self.matriz[lineas][columna] is None:
                    self.matriz[lineas][columna]= conocimiento
                    ingreso_en_matriz = True
                    break
        if not ingreso_en_matriz:
            self. Aumento_de_memoria()
           # self.matriz[len(self.matriz)-1][0]= conocimiento

    def __getattr__(self, conocimiento):
        return getattr(self.instance, conocimiento)

    def imprimir(self):
        cadena_de_sring=''
        for linea in range(len(self.matriz)-1):
            for columna in range (len(self.matriz[linea])):
                cadena_de_sring += str(self.matriz[linea][columna])
            cadena_de_sring += '\n'
        return cadena_de_sring

a = Memoria()
a.Aprender(1)

print(a.imprimir())
print(a.matriz)
'''
    def Eliminar_conocimiento(self, linea, columna):
        self.matriz[linea,columna] = ''
        return

    def Eliminar_conocimiento(self, id_conocimiento):
        return

    def Tamaño_actual(self):
        return

    def Obtener_conocimiento(self, linea, columna):
        return
'''

