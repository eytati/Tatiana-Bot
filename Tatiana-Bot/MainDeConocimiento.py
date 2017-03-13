from flask import Flask,render_template, request, jsonify, json
from werkzeug.security import generate_password_hash
from Funciones import Gestion_de_conocimiento
import logging
from logging.handlers import RotatingFileHandler
from  datetime import datetime

app = Flask(__name__)


class Informacion():

#----------------------------------Creacion de Hash--------------------------------------------------------------------#
    def Valor_de_hash(self, palabra_clave):
        return generate_password_hash(palabra_clave)
#-------------------------------------Fin de creacion de hash----------------------------------------------------------#

    def Informacion_general(self):
        identificador = self.Valor_de_hash("Tati-bot")
        informacion = "Nombre: Tati-bot \n ID: " + identificador + "\nCreador: Eylen Fernandez" \
                                                                   "\n FechaDeCreacion: " + str(datetime.now())
        app.logger.info('Informacion General del bot')
        return informacion
#----------------------------------------Ruta de Informacion General---------------------------------------------------#
@app.route('/api/informacion_del_bot')
def informacion_del_bot():
    obtener_informacion = Informacion()
    return obtener_informacion.Informacion_general()

#---------------------------------------Ruta de Obencion de hash-------------------------------------------------------#
@app.route('/prueba<valor>')
def prueba(valor):
    obtener_hash = Informacion()
    return str(obtener_hash.Valor_de_hash(valor))


#-----------------------------------------Ruta que va al menu principal------------------------------------------------#
@app.route('/api/principal')
def principal():
    return  render_template('Index2.html')


#----------------------------------Metodo principal de instancia a Memoria---------------------------------------------#
def solicitar_instancia(tipo):
      instancia = Gestion_de_conocimiento.Fuente_de_conocimiento()
      return str(instancia.Aprender(tipo))
        

#--------------------------------Aprender, rutas generales-------------------------------------------------------------#

#--------------------------------Ruta General de Aprender--------------------------------------------------------------#
@app.route('/api/aprender_menu')
def aprender_aprender_menu():
  return 'Hola' #Retorna hola por que aun no hay menu

#----------------------------------Ruta para suma----------------------------------------------------------------------#
@app.route('/api/aprender_menu/Suma')
def aprender_suma():
    app.logger.info(str(datetime.now())+'Aprende calcula el valor de una suma')
    return solicitar_instancia('Suma') #LLama instancia de un metodo de aprender

#--------------------------------Ruta para resta-----------------------------------------------------------------------#
@app.route('/api/aprender_menu/resta')
def aprender_resta():
    app.logger.info(str(datetime.now())+'Aprende calcula el valor de una resta')
    return solicitar_instancia('Resta') #LLama instancia de un metodo de aprender

#--------------------------------Ruta para division--------------------------------------------------------------------#
@app.route('/api/aprender_menu/division')
def aprender_division():
    app.logger.info(str(datetime.now())+'Aprende calcula el valor de una division')
    return solicitar_instancia('Division') #LLama instancia de un metodo de aprender

#--------------------------------Ruta para multiplicacion--------------------------------------------------------------#
@app.route('/api/aprender_menu/multiplicacion')
def aprender_multiplicacion():
    app.logger.info(str(datetime.now())+'Aprende calcula el valor de una multiplicacion')
    return solicitar_instancia('Multiplicacion') #LLama instancia de un metodo de aprender

#-------------------------------------Ruta para pitagoras--------------------------------------------------------------#
@app.route('/api/aprender_menu/pitagoras_cateto')
def aprender_pitagoras_hipotenusa():
    app.logger.info(str(datetime.now())+'Aprende calcula el valor de cateto')

    return solicitar_instancia('pitagoras_cateto') #LLama instancia de un metodo de aprender

#-------------------------------------Ruta para pitagoras--------------------------------------------------------------#
@app.route('/api/aprender_menu/pitagoras_hipotenusa')
def aprender_pitagoras_cateto():
    app.logger.info(str(datetime.now())+'Aprende calcula el valor de un cateto')

    return solicitar_instancia('pitagoras_hipotenusa') #LLama instancia de un metodo de aprender

#-------------------------------------Ruta para potencias--------------------------------------------------------------#
@app.route('/api/aprender_menu/potencias')
def aprender_potencias():
    app.logger.info(str(datetime.now())+'Aprende calcula el valor de un cateto')
    return solicitar_instancia('Potencias') #LLama instancia de un metodo de aprender

#-------------------------------------Ruta para potencias--------------------------------------------------------------#
@app.route('/api/aprender_menu/primo')
def aprender_primo():
    app.logger.info(str(datetime.now())+'Aprende calcula si un numero es primo')
    return solicitar_instancia('Primo') #LLama instancia de un metodo de aprender

#---------------------------------------Fin de las rutas de aprender---------------------------------------------------#


#--------------------------------Accionar, rutas generales-------------------------------------------------------------------------------------------------------------------#

# ----------------------------------Metodo principal de instancia a Memoria---------------------------------------------#
def accionar_conocimeiento(nombre, numero1, numero2):
    instancia = Gestion_de_conocimiento.Fuente_de_conocimiento()
    numero1_int = int(numero1)
    numero2_int = int(numero2)
    return str(instancia.ejercer_conocimiento(nombre, numero1_int, numero2_int))

#--------------------------------Ruta General de Aprender--------------------------------------------------------------#
@app.route('/api/conocimiento_menu')
def conocimieto_menu():
    return 'Hola' #Retorna hola por que aun no hay menu


#----------------------------------Ruta para suma----------------------------------------------------------------------#
@app.route('/api/conocimiento_menu/suma/<numero1>/<numero2>')
def conocimiento_suma(numero1, numero2):
    app.logger.info(str(datetime.now())+'Calcula una suma')
    return accionar_conocimeiento('Suma',numero1, numero2),426

#--------------------------------Ruta para resta-----------------------------------------------------------------------#
@app.route('/api/conocimiento_menu/resta/<numero1>/<numero2>')
def conocimiento_resta(numero1, numero2):
    app.logger.info(str(datetime.now())+'Calcula una resta')
    return accionar_conocimeiento('Resta', numero1, numero2), 426

#--------------------------------Ruta para division--------------------------------------------------------------------#
@app.route('/api/conocimiento_menu/division/<numero1>/<numero2>')
def conocimiento_division(numero1, numero2):
    app.logger.info(str(datetime.now())+'Calcula division')
    return accionar_conocimeiento('Division', numero1, numero2), 426

#--------------------------------Ruta para multiplicacion--------------------------------------------------------------#
@app.route('/api/conocimiento_menu/multiplicacion/<numero1>/<numero2>')
def conocimiento_multiplicacion(numero1, numero2):
    app.logger.info(str(datetime.now())+'Calcula multiplicacion')
    return accionar_conocimeiento('Multiplicacion', numero1, numero2),426

#-------------------------------------Ruta para pitagoras--------------------------------------------------------------#
@app.route('/api/conocimiento_menu/pitagoras_cateto/<numero1>/<numero2>')
def conocimiento_pitagoras_hipotenusa(numero1, numero2):
    app.logger.info(str(datetime.now())+'Calcula la hipotenusa')
    return accionar_conocimeiento('pitagoras_cateto', numero1, numero2), 426
#-------------------------------------Ruta para pitagoras--------------------------------------------------------------#
@app.route('/api/conocimiento_menu/pitagoras_hipotenusa/<numero1>/<numero2>')
def conocimiento_pitagoras_cateto(numero1, numero2):
    app.logger.info(str(datetime.now())+'Calcula el cateto')
    return accionar_conocimeiento('pitagoras_hipotenusa', numero1, numero2), 426

#-------------------------------------Ruta para potencias--------------------------------------------------------------#
@app.route('/api/conocimiento_menu/potencias/<numero1>/<numero2>')
def conocimiento_potencias(numero1, numero2):
    app.logger.info(str(datetime.now())+'Calcula potencias')
    return accionar_conocimeiento('Potencias', numero1, numero2), 426

#-------------------------------------Ruta para potencias--------------------------------------------------------------#
@app.route('/api/conocimiento_menu/primo/<numero1>')
def conocimiento_primo(numero1):
    app.logger.info(str(datetime.now()) +'Calcula un numero primo')
    return accionar_conocimeiento('Primo', numero1, 0), 426

#---------------------------------------Fin de las rutas de accionar---------------------------------------------------#

#-------------------------------------------Desaprender----------------------------------------------------------------#
def desaprender(nombre):
    instancia_de_olvidar = Gestion_de_conocimiento.Fuente_de_conocimiento()
    return  str(instancia_de_olvidar.olvidar(nombre))

#-----------------------------------------Fin de desaprender-----------------------------------------------------------#


#--------------------------------Ruta General de desaprender-----------------------------------------------------------#
@app.route('/api/desaprender_menu')
def aprender_desaprender_menu():
  return 'Hola' #Retorna hola por que aun no hay menu

#----------------------------------Ruta para suma----------------------------------------------------------------------#
@app.route('/api/desaprender_menu/suma')
def desaprender_suma():
    app.logger.info(str(datetime.now())+'desaprende a calcular suma')
    return desaprender('Suma') #LLama instancia de un metodo de aprender

#--------------------------------Ruta para resta-----------------------------------------------------------------------#
@app.route('/api/desaprender_menu/resta')
def desaprender_resta():
    app.logger.info(str(datetime.now())+'desaprende a calcular resta')
    return desaprender('Resta')

#--------------------------------Ruta para division--------------------------------------------------------------------#
@app.route('/api/desaprender_menu/division')
def desaprender_division():
    app.logger.info(str(datetime.now())+'desaprende a calcular division')
    return desaprender('Division')

#--------------------------------Ruta para multiplicacion--------------------------------------------------------------#
@app.route('/api/desaprender_menu/multiplicacion')
def desaprender_multiplicacion():
    app.logger.info(str(datetime.now())+'desaprende a calcula multiplicacion')
    return desaprender('Multiplicacion')

#-------------------------------------Ruta para pitagoras--------------------------------------------------------------#
@app.route('/api/desaprender_menu/pitagoras_cateto')
def desaprender_pitagoras_hipotenusa():
    app.logger.info(str(datetime.now())+'desaprende a calcula hipotenusa')
    return desaprender('pitagoras_cateto')
#-------------------------------------Ruta para pitagoras--------------------------------------------------------------#
@app.route('/api/desaprender_menu/pitagoras_hipotenusa')
def desaprender_pitagoras_cateto():
    app.logger.info(str(datetime.now())+'desaprende a calcula cateto')
    return desaprender('pitagoras_hipotenusa')

#-------------------------------------Ruta para potencias--------------------------------------------------------------#
@app.route('/api/desaprender_menu/potencias')
def desaprender_potencias():
    app.logger.info(str(datetime.now())+'desaprende a calcula potencias')
    return desaprender('Potencias')
#-------------------------------------Ruta para potencias--------------------------------------------------------------#
@app.route('/api/desaprender_menu/primo')
def desaprender_primo():
    app.logger.info(str(datetime.now())+'desaprende a calcular un numero primo')
    return desaprender('Primo')

#---------------------------------------Fin de las rutas de aprender---------------------------------------------------#


#----------------------------------------Donde se accede y el inicio---------------------------------------------------#
if __name__ == '__main__':
    handler = RotatingFileHandler('Tati-Bot.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host='127.0.0.1', port='5001')
