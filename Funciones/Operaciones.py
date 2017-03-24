from abc import ABCMeta, abstractmethod
import math
#------------------------------------------Clase base es Operacion-----------------------------------------------------#
class Operacion:
    __metaclass__ = ABCMeta

    @abstractmethod
    def opereciones(self, parametro1, parametro2):
        return

    @abstractmethod
    def get(self):
        return
#------------------------------------------Fin de la claes operacion---------------------------------------------------#
class aprender_externo (Operacion):

    __nombre= ''
    __codigo= None

    def __init__(self, nombre, codigo):
        Operacion.__init__(self)
        self.__nombre = nombre
        self.__codigo = codigo

    def opereciones(self, numero1, numero2):
        exec (self.__codigo)
        return 'HOLA'

    def get(self):
        return self.__nombre

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

    def get(self):
        return self.__nombre
#---------------------------------------------Fin de la clase division-------------------------------------------------#


#---------------------------------------------Inicio de la clase multipliacion-----------------------------------------#
class Multiplicacion(Operacion):

    __nombre = ''

    def __init__(self):
        Operacion.__init__(self)
        self.__nombre = 'Multiplicacion'

    def opereciones(self, numero1, numero2):
        return numero1 *numero2

    def get(self):
        return self.__nombre
#----------------------------------------Fin de la clase multiplicacion------------------------------------------------#


#---------------------------------------------Inicio de la clase Primo-------------------------------------------------#
class Primo(Operacion):

    __nombre = ''

    def __init__(self):
        Operacion.__init__(self)
        self.__nombre = 'Primo'

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

    def get(self):
        return self.__nombre
#-------------------------------------------Fin de la clase primo------------------------------------------------------#


#-------------------------------------------Inicio de la clase Potencias-----------------------------------------------#
class Potencias(Operacion):

    __nombre = ''
    def __init__(self):
        Operacion.__init__(self)
        self.__nombre= 'Potencias'

    def opereciones(self, numero1, numero2):
        numero_final =numero1
        for contador in range(0, numero2):
            numero_final = numero_final * numero1
        return numero_final

    def get(self):
        return self.__nombre
#-------------------------------------------Fin de la clase potencias--------------------------------------------------#


#-------------------------Inicio de la clase Pitagoras calculo de hipotenusa-------------------------------------------#
class Pitagoras_hipotenusa (Operacion):

    __nombre= ''

    def __init__(self):
        Operacion.__init__(self)
        self.__nombre = 'Hipotenusa'

    def calcular_hipotenusa(self, numero1, numero2):
        clase_calculo_de_potencias = Potencias()
        cateto1_potencia = clase_calculo_de_potencias.opereciones(numero1,2)
        cateto2_potencia = clase_calculo_de_potencias.opereciones(numero2,2)

        hipotenusa = cateto1_potencia+cateto2_potencia
        hipotenusa=math.sqrt(hipotenusa)
        return hipotenusa

    def get(self):
        return self.__nombre

 #----------------------------Inicio de la clase Pitagoras calculo de cateto-------------------------------------------#

class piatgoras_cateto(Operacion):

    __nombre = ''

    def __init__(self):
        Operacion.__init__(self)
        self.__nombre = 'Cateto'

    def operaciones(self, numero1, numero2):
        clase_calculo_de_potencias = Potencias()
        cateto1_potencia = clase_calculo_de_potencias.opereciones(numero1, 2)
        hipotenusa_potencia = clase_calculo_de_potencias.opereciones(numero2, 2)
        cateto = hipotenusa_potencia- cateto1_potencia
        cateto=math.sqrt(cateto)
        return cateto

    def get(self):
        return self.__nombre
#---------------------------------------Fin de la clase pitagoras------------------------------------------------------#

