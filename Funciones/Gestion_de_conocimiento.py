from  Funciones import Operaciones


class Memoria:
    matriz = []
    instance = None
#-------------------------------------Inicio de constructor------------------------------------------------------------#
    def __init__(self):
        if not Memoria.instance:
            Memoria.instance = self
#----------------------------------------Fin de conocimiento-----------------------------------------------------------#


#------------------------------------Aumenta el tamaño de la memoria segun sea necesario-------------------------------#
    def aumentar_memoria(self):

        if len(self.matriz) is 0:
            self.matriz.append([])
            self.matriz[0].append(None)
        else:
            largo_matriz = len(self.matriz)
            self.matriz.append([])
            for agregar_las_columnas in range(0, largo_matriz):
                self.matriz[len(self.matriz) - 1].append(None)

            for lineas in range(0, len(self.matriz)):
                for columnas in range(0, len(self.matriz[lineas])):
                    if columnas is len(self.matriz[lineas]) - 1:
                        self.matriz[lineas].append(None)
                        break

#------------------------------------Fin de aumentar el tamaño de la memoria-------------------------------------------#



#------------------------------Es el metodo para guardar los datos en la memoria---------------------------------------#

    def aprender(self, conocimiento):
        ingreso_en_matriz = False
        for lineas in range(0, len(self.matriz)):
            if ingreso_en_matriz:
                break

            for columna in range(len(self.matriz[lineas])):
                if self.matriz[lineas][columna] is None:
                    self.matriz[lineas][columna] = conocimiento
                    ingreso_en_matriz = True
                    break
        if not ingreso_en_matriz:
            self.aumentar_memoria()
            self.matriz[0][len(self.matriz) - 1] = conocimiento

#------------------------------Fin del metodo para guardar los datos en la memoria-------------------------------------#



#------------------------------Inicio del metodo para borrar los datos en la memoria-----------------------------------#
    def desaprender(self, olvida):
        desaprede = False
        for linea in range(0, len(self.matriz)):
            if desaprede is True:
                break
            for columna in range(0, len(self.matriz[linea])):
                if self.matriz[linea][columna] is not None:
                 if olvida == self.matriz[linea][columna].get():
                    self.matriz[linea][columna] = None
                    desaprede = True
                    break
        return desaprede


#------------------------------Fin del metodo para borrar los datos en la memoria-------------------------------------#

    def imprimir(self):
        cadena_de_sring = ''
        for linea in range(len(self.matriz)):
            for columna in range(len(self.matriz[linea])):
                cadena_de_sring += str(self.matriz[linea][columna]) + ' '
            cadena_de_sring += '\n'
        return cadena_de_sring

    def nombres(self):
        cadena_de_sring = ''
        for linea in range(len(self.matriz)):
            for columna in range(len(self.matriz[linea])):
                if not self.matriz[linea][columna] is None:
                    nombre = self.matriz[linea][columna].get()
                    cadena_de_sring += str(nombre) + ' '
            cadena_de_sring += '\n'
        return cadena_de_sring
#--------------------------------------Recorre la memoria--------------------------------------------------------------#

    def recorre_matriz(self, nombre, parametro1, parametro2):
        existe = False
        respuesta= ''
        for linea in range(len(self.matriz)):
            if existe is True:
                break
            for columna in range(len(self.matriz[linea])):
                if not self.matriz[linea][columna] is None:
                    instancia = self.matriz[linea][columna]
                    if nombre == instancia.get():
                        respuesta = instancia.opereciones(parametro1, parametro2)
                        #print(respuesta)
                        existe = True
                        break
        return respuesta
#------------------------------------Fin de recorrer la memoria--------------------------------------------------------#


class Fuente_de_conocimiento:
    creacion_de_memoria = Memoria()

#------------------------------------Instanciar los datos a la memoria-------------------------------------------------#
    def Aprender(self, tipo):
        agrego = False
        a = tipo
        if tipo == 'Suma':
            suma = Operaciones.Suma()
            self.creacion_de_memoria.aprender(suma)
            agrego = True

        elif tipo == 'Resta':
            self.creacion_de_memoria.aprender(Operaciones.Resta())
            agrego = True

        elif tipo == 'Division':
            self.creacion_de_memoria.aprender(Operaciones.Division())
            agrego = True

        elif tipo == 'Multiplicacion':
            self.creacion_de_memoria.aprender(Operaciones.Multiplicacion())
            agrego = True

        elif tipo == 'Cateto':
            self.creacion_de_memoria.aprender(Operaciones.piatgoras_cateto())
            agrego = True

        elif tipo == 'Hipotenusa':
            self.creacion_de_memoria.aprender(Operaciones.Pitagoras_hipotenusa())
            agrego = True

        elif tipo == 'Potencias':
            self.creacion_de_memoria.aprender(Operaciones.Potencias())
            agrego = True

        elif tipo == 'Primo':
            self.creacion_de_memoria.aprender(Operaciones.Primo())
            agrego = True

        return agrego
#----------------------------------Fin de instanciar los datos a la memoria--------------------------------------------#


#------------------------------------Accionar los conocimientos de la memoria------------------------------------------#

    def ejercer_conocimiento(self, nombre, parametro1, parametro2):
        return self.creacion_de_memoria.recorre_matriz(nombre, parametro1, parametro2)

#------------------------------Fin de accionar los conocimientos de la memoria-----------------------------------------#

#------------------------------------Accionar los conocimientos de la memoria------------------------------------------#
    def olvidar(self, nombre):
        return self.creacion_de_memoria.desaprender(nombre)

#------------------------------Fin de accionar los conocimientos de la memoria-----------------------------------------#

    def aprender_externo(self, nomb, codi):
        return  self.creacion_de_memoria.aprender(Operaciones.aprender_externo(nomb, codi))

    def memoria(self):
        return  self.creacion_de_memoria.nombres()




'''
conocimiento = Fuente_de_conocimiento()
conocimiento.Aprender('Suma')

conocimiento.ejercer_conocimiento('Suma', 6, 2)
print(conocimiento.olvidar('Suma'))
conocimiento.ejercer_conocimiento('Suma', 6, 2)
'''

