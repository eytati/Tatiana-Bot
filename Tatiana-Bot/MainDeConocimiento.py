from flask import Flask, render_template, request, jsonify, json
from werkzeug.security import generate_password_hash
from Funciones import Gestion_de_conocimiento
import logging
from logging.handlers import RotatingFileHandler
from  datetime import datetime

app = Flask(__name__)


class Informacion():
    # ----------------------------------Creacion de Hash--------------------------------------------------------------------#
    def Valor_de_hash(self, palabra_clave):
        return generate_password_hash(palabra_clave)

    # -------------------------------------Fin de creacion de hash----------------------------------------------------------#

    def Informacion_general(self):
        identificador = self.Valor_de_hash("Tati-bot")
        informacion = "Nombre: Tati-bot \n ID: " + identificador + "\nCreador: Eylen Fernandez" \
                                                                   "\n FechaDeCreacion: " + str(datetime.now())
        app.logger.info('Informacion General del bot')
        return informacion


# ----------------------------------------Ruta de Informacion General---------------------------------------------------#
@app.route('/api/informacion_del_bot')
def informacion_del_bot():
    obtener_informacion = Informacion()
    app.logger.info(str(datetime.now()) + 'Informacion del bot')
    return obtener_informacion.Informacion_general()


# -----------------------------------------Ruta que va al menu principal------------------------------------------------#
@app.route('/api/principal')
def principal():
    return render_template('Index2.html')


# --------------------------------Ruta General de Aprender--------------------------------------------------------------#
@app.route('/api/aprender_menu/<tipo>')
def aprender_aprender_menu(tipo):
    instancia = Gestion_de_conocimiento.Fuente_de_conocimiento()
    app.logger.info(str(datetime.now()) + 'Aprende calcula el valor de ' + tipo)
    return str(instancia.Aprender(tipo))


# --------------------------------Ruta General de Aprender--------------------------------------------------------------#
@app.route('/api/conocimiento_menu/<tipo>/<numero1>/<numero2>')
def conocimieto_menu(tipo, numero1, numero2):
    instancia = Gestion_de_conocimiento.Fuente_de_conocimiento()
    numero1_int = int(numero1)
    numero2_int = int(numero2)
    app.logger.info(str(datetime.now()) + 'La accion a realizar es'+tipo)
    return str(instancia.ejercer_conocimiento(tipo, numero1_int, numero2_int))

# --------------------------------Ruta General de desaprender-----------------------------------------------------------#
@app.route('/api/desaprender_menu/<tipo>')
def aprender_desaprender_menu(tipo):
    instancia_de_olvidar = Gestion_de_conocimiento.Fuente_de_conocimiento()
    return str(instancia_de_olvidar.olvidar(tipo))


# ----------------------------------------Donde se accede y el inicio---------------------------------------------------#
if __name__ == '__main__':
    handler = RotatingFileHandler('tatizilla2.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host='127.0.0.1', port='5001')
