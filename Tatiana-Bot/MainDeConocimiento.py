from flask import Flask,render_template, request, jsonify, json
from werkzeug.security import generate_password_hash
from Funciones import Gestion_de_conocimiento

app = Flask(__name__)


class Informacion():

    def JSON_informacion_general(self, nombre, id, fecha_de_creacion):
        json_valor= {"informacion":
                   {
                       "Nombre": nombre,
                       "ID": id,
                       "Creador": "Eylen Fernandez",
                       "FechaDeCreacion": fecha_de_creacion
                   }
              }
        return json.dump(json_valor)

    def Valor_de_hash(self, palabra_clave):
        return generate_password_hash(palabra_clave)


#----------------------------------------Ruta de Informacion General---------------------------------------------------#
@app.route('/api/informacion_del_bot')
def informacion_del_bot():

    return render_template('Informacion.html')

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
        Gestion_de_conocimiento.Fuente_de_conocimiento.Aprender(tipo)
        

#--------------------------------Aprender, rutas generales-------------------------------------------------------------#

#--------------------------------Ruta General de Aprender--------------------------------------------------------------#
@app.route('/api/aprender_menu')
def aprender_menu():
    return 'Hola' #Retorna hola por que aun no hay menu

#----------------------------------Ruta para suma----------------------------------------------------------------------#
@app.route('/api/aprender_menu/suma>')
def suma():
    return solicitar_instancia('Suma') #LLama instancia de un metodo de aprender

#--------------------------------Ruta para resta-----------------------------------------------------------------------#
@app.route('/api/aprender_menu/resta')
def resta():
    return solicitar_instancia('Resta') #LLama instancia de un metodo de aprender

#--------------------------------Ruta para division--------------------------------------------------------------------#
@app.route('/api/aprender_menu/division')
def division():
    return solicitar_instancia('Division') #LLama instancia de un metodo de aprender

#--------------------------------Ruta para multiplicacion--------------------------------------------------------------#
@app.route('/api/aprender_menu/multiplicacion')
def multiplicacion():
    return solicitar_instancia('Multiplicacion') #LLama instancia de un metodo de aprender

#-------------------------------------Ruta para pitagoras--------------------------------------------------------------#
@app.route('/api/aprender_menu/pitagoras')
def pitagoras():
    return solicitar_instancia('Pitagoras') #LLama instancia de un metodo de aprender

#-------------------------------------Ruta para potencias--------------------------------------------------------------#
@app.route('/api/aprender_menu/potencias')
def potencias():
    return solicitar_instancia('Potencias') #LLama instancia de un metodo de aprender

#-------------------------------------Ruta para potencias--------------------------------------------------------------#
@app.route('/api/aprender_menu/prima')
def primo():
    return solicitar_instancia('Primo') #LLama instancia de un metodo de aprender

#---------------------------------------Fin de las rutas de aprender---------------------------------------------------#


#----------------------------------------Lista de conocimiento---------------------------------------------------------#





#-------------------------------Donde se accede y el inicio-----------------------------------------#
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5001')
