import numpy as np
import  cv2

class Tomar_foto:
    #




    #def Disparo_de_foto(self):



    def Mostrar_una_foto(self):


        IMG = cv2.imread('patricio.png', 0)
        cv2.Imshow('Patricio', IMG)
        cv2.WhiteKey(0)
        cv2.DestroAllWindows()
        print(IMG)


print(cv2)