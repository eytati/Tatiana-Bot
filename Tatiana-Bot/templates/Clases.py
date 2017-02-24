from abc import ABCMeta, abstractmethod
from _weakrefset import WeakSet

class Operacion:
    __metaclass__ = ABCMeta

    @abstractmethod
    def opereciones(self, numero1, numero2):
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


