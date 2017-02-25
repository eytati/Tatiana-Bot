class Memoria:
    matriz = [None, None,], [None,None]
    instance = None

    def __init__(self):
        if not Memoria.instance:
            Memoria.instance = self

    def Agregar(self):
        a= len(self.matriz)
        for lineas in range(len(self.matriz)):
           if lineas is a:
            self.matriz.append([])
            for columna in range(len(self.matriz)):
                self.Agrega_columna(lineas)

    def Aprender(self, conocimiento):
        ingreso_en_matriz = False
        for lineas in range(len(self.matriz)):
            if ingreso_en_matriz:
                break
            for columna in range(len(self.matriz)):
                if self.matriz[lineas][columna] is None:
                    self.matriz[lineas][columna]= conocimiento
                    ingreso_en_matriz = True
                    break
        if not ingreso_en_matriz:
            self.Agregar()
            self.Aprender(conocimiento)

    def __getattr__(self, conocimiento):
        return getattr(self.instance, conocimiento)


a = Memoria()
a.Aprender('HOLA')
a.Aprender('HOLA')
a.Aprender('HOLA')
a.Aprender('HOLA')
a.Aprender('HOLA')
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