from abc import ABCMeta, abstractmethod

from _weakrefset import WeakSet

class Operacion:
    __metaclass__ = ABCMeta

    @abstractmethod
    def opereciones(self, parametro1, parametro2):
        return

class Suma(Operacion):
    def __init__(self):
        Operacion.__init__(self)

    def opereciones(self, numero1, numero2):
        return numero1+numero2

class Resta(Operacion):
    def __init__(self):
        Operacion.__init__(self)

    def opereciones(self, numero1, numero2):
        return numero1-numero2


class Division(Operacion):
    def __init__(self):
        Operacion.__init__(self)

    def opereciones(self, numero1, numero2):
        return numero1/numero2


class Multiplicacion(Operacion):
    def __init__(self):
        Operacion.__init__(self)

    def opereciones(self, numero1, numero2):
        return numero1 *numero2

class Primo(Operacion):
    def __init__(self):
        Operacion.__init__(self)

    def opereciones(self, numero):
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

class Potencias(Operacion):

    def __init__(self):
        Operacion.__init__(self)

    def calculo_de_potencias(self,numero1, numero2):
        numero_final =numero1
        for contador in range(0, numero2):
            numero_final = numero_final * numero1
        return numero_final


class Pitagoras (Operacion):
    def __init__(self):
        Operacion.__init__(self)

    def calcular_hipotenusa(self, numero1, numero2):
        clase_calculo_de_potencias = Potencias();
        cateto1_potencia = clase_calculo_de_potencias.calculo_de_potencias(numero1,2)
        cateto2_potencia = clase_calculo_de_potencias.calculo_de_potencias(numero2,2)

        hipotenusa = cateto1_potencia+cateto2_potencia
        #raiz=math.sqrt(numero)
        return hipotenusa


    def calcular_catetos(self, numero1, numero2):
        clase_calculo_de_potencias = Potencias();
        cateto1_potencia = clase_calculo_de_potencias.calculo_de_potencias(numero1, 2)
        hipotenusa_potencia = clase_calculo_de_potencias.calculo_de_potencias(numero2, 2)
        cateto = hipotenusa_potencia- cateto1_potencia
        # raiz=math.sqrt(numero)
        return cateto


