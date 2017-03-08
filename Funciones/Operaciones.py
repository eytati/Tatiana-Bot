from abc import ABCMeta, abstractmethod

import math
#------------------------------------------Clase base es Operacion-----------------------------------------------------#
class Operacion:
    __metaclass__ = ABCMeta

    @abstractmethod
    def opereciones(self, parametro1, parametro2):
        return

#------------------------------------------Fin de la claes operacion---------------------------------------------------#


#-------------------------------------------Inicio de clase suma-------------------------------------------------------#
class Suma(Operacion):

    __nombre = ''

    def __init__(self):
        Operacion.__init__(self)
        self.__nombre = 'Suma'

    def opereciones(self, numero1, numero2):
        return numero1+numero2

    def get(self):
        return self.__nombre
#---------------------------------------------Fin de la clase suma-----------------------------------------------------#


#--------------------------------------------Inicio de la claes Resta--------------------------------------------------#
class Resta(Operacion):
    __nombre=''

    def __init__(self):
        Operacion.__init__(self)
        self.__nombre = 'Resta'

    def opereciones(self, numero1, numero2):
        return numero1-numero2

    def get(self):
        return self.__nombre
#---------------------------------------------Fin de la clase resta----------------------------------------------------#


#---------------------------------------------Inicio de la clase division----------------------------------------------#

class Division(Operacion):
    __nombre = ''

    def __init__(self):
        Operacion.__init__(self)
        self.__nombre =  'Division'

    def opereciones(self, numero1, numero2):
        return numero1/numero2

#---------------------------------------------Fin de la clase division-------------------------------------------------#


#---------------------------------------------Inicio de la clase multipliacion-----------------------------------------#
class Multiplicacion(Operacion):
    def __init__(self):
        Operacion.__init__(self)

    def opereciones(self, numero1, numero2):
        return numero1 *numero2
#----------------------------------------Fin de la clase multiplicacion------------------------------------------------#


#---------------------------------------------Inicio de la clase Primo-------------------------------------------------#
class Primo(Operacion):
    def __init__(self):
        Operacion.__init__(self)

    def opereciones(self, numero, numero2=0):
        primo = True
        if numero is 2:
            primo = True
        elif numero % 2 is 0:
            primo = False
        else:
            mediaRelativa = int((numero - 1) / 2)
            for contador in range(3, mediaRelativa):
                if numero % contador is 0:
                    primo = False
                    break
        return primo
#-------------------------------------------Fin de la clase primo------------------------------------------------------#


#-------------------------------------------Inicio de la clase Potencias-----------------------------------------------#
class Potencias(Operacion):

    def __init__(self):
        Operacion.__init__(self)

    def opereciones(self, numero1, numero2):
        numero_final =numero1
        for contador in range(0, numero2):
            numero_final = numero_final * numero1
        return numero_final
#-------------------------------------------Fin de la clase potencias--------------------------------------------------#


#------------------------------------------Inicio de la clase Pitagoras------------------------------------------------#
class Pitagoras (Operacion):

    def __init__(self):
        Operacion.__init__(self)

    def calcular_hipotenusa(self, numero1, numero2):
        clase_calculo_de_potencias = Potencias()
        cateto1_potencia = clase_calculo_de_potencias.opereciones(numero1,2)
        cateto2_potencia = clase_calculo_de_potencias.opereciones(numero2,2)

        hipotenusa = cateto1_potencia+cateto2_potencia
        hipotenusa=math.sqrt(hipotenusa)
        return hipotenusa


    def calcular_catetos(self, numero1, numero2):
        clase_calculo_de_potencias = Potencias()
        cateto1_potencia = clase_calculo_de_potencias.opereciones(numero1, 2)
        hipotenusa_potencia = clase_calculo_de_potencias.opereciones(numero2, 2)
        cateto = hipotenusa_potencia- cateto1_potencia
        cateto=math.sqrt(cateto)
        return cateto

    def opereciones(self, parametro1, parametro2):
        tipo = 1

        if tipo is 1:
              respuesta =self.calcular_hipotenusa(parametro1, parametro2)
        else:
            respuesta= self.calcular_catetos(parametro1, parametro2)

        return  respuesta
#---------------------------------------Fin de la clase pitagoras------------------------------------------------------#
