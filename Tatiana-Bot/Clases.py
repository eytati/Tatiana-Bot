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
