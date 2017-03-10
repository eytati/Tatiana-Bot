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
def aprender_aprender_menu():
    return 'Hola' #Retorna hola por que aun no hay menu

#----------------------------------Ruta para suma----------------------------------------------------------------------#
@app.route('/api/aprender_menu/suma>')
def aprender_suma():
    return solicitar_instancia('Suma') #LLama instancia de un metodo de aprender

#--------------------------------Ruta para resta-----------------------------------------------------------------------#
@app.route('/api/aprender_menu/resta')
def aprender_resta():
    return solicitar_instancia('Resta') #LLama instancia de un metodo de aprender

#--------------------------------Ruta para division--------------------------------------------------------------------#
@app.route('/api/aprender_menu/division')
def aprender_division():
    return solicitar_instancia('Division') #LLama instancia de un metodo de aprender

#--------------------------------Ruta para multiplicacion--------------------------------------------------------------#
@app.route('/api/aprender_menu/multiplicacion')
def aprender_multiplicacion():
    return solicitar_instancia('Multiplicacion') #LLama instancia de un metodo de aprender

#-------------------------------------Ruta para pitagoras--------------------------------------------------------------#
@app.route('/api/aprender_menu/pitagoras_cateto')
def aprender_pitagoras_hipotenusa():
    return solicitar_instancia('pitagoras_cateto') #LLama instancia de un metodo de aprender

#-------------------------------------Ruta para pitagoras--------------------------------------------------------------#
@app.route('/api/aprender_menu/pitagoras_hipotenusa')
def aprender_pitagoras_cateto():
    return solicitar_instancia('pitagoras_hipotenusa') #LLama instancia de un metodo de aprender

#-------------------------------------Ruta para potencias--------------------------------------------------------------#
@app.route('/api/aprender_menu/potencias')
def aprender_potencias():
    return solicitar_instancia('Potencias') #LLama instancia de un metodo de aprender

#-------------------------------------Ruta para potencias--------------------------------------------------------------#
@app.route('/api/aprender_menu/prima')
def aprender_primo():
    return solicitar_instancia('Primo') #LLama instancia de un metodo de aprender

#---------------------------------------Fin de las rutas de aprender---------------------------------------------------#


#--------------------------------Accionar, rutas generales-------------------------------------------------------------------------------------------------------------------#

# ----------------------------------Metodo principal de instancia a Memoria---------------------------------------------#
def acccionar_conocimeiento(numero1, numero2):
    Gestion_de_conocimiento.Fuente_de_conocimiento.ejercer_conocimiento(numero1, numero2)

#--------------------------------Ruta General de Aprender--------------------------------------------------------------#
@app.route('/api/conocimiento_menu')
def conocimieto_menu():
    return 'Hola' #Retorna hola por que aun no hay menu


#----------------------------------Ruta para suma----------------------------------------------------------------------#
@app.route('/api/conocimiento_menu/suma>')
def conocimiento_suma():
    return solicitar_instancia('Suma') #LLama instancia de un metodo de aprender

#--------------------------------Ruta para resta-----------------------------------------------------------------------#
@app.route('/api/conocimiento_menu/resta')
def conocimiento_resta():
    return solicitar_instancia('Resta') #LLama instancia de un metodo de aprender

#--------------------------------Ruta para division--------------------------------------------------------------------#
@app.route('/api/conocimiento_menu/division')
def conocimiento_division():
    return solicitar_instancia('Division') #LLama instancia de un metodo de aprender

#--------------------------------Ruta para multiplicacion--------------------------------------------------------------#
@app.route('/api/conocimiento_menu/multiplicacion')
def conocimiento_multiplicacion():
    return solicitar_instancia('Multiplicacion') #LLama instancia de un metodo de aprender

#-------------------------------------Ruta para pitagoras--------------------------------------------------------------#
@app.route('/api/conocimiento_menu/pitagoras_cateto')
def conocimiento_pitagoras_hipotenusa():
    return solicitar_instancia('pitagoras_cateto') #LLama instancia de un metodo de aprender

#-------------------------------------Ruta para pitagoras--------------------------------------------------------------#
@app.route('/api/conocimiento_menu/pitagoras_hipotenusa')
def conocimiento_pitagoras_cateto():
    return solicitar_instancia('pitagoras_hipotenusa') #LLama instancia de un metodo de aprender

#-------------------------------------Ruta para potencias--------------------------------------------------------------#
@app.route('/api/conocimiento_menu/potencias')
def conocimiento_potencias():
    return solicitar_instancia('Potencias') #LLama instancia de un metodo de aprender

#-------------------------------------Ruta para potencias--------------------------------------------------------------#
@app.route('/api/conocimiento_menu/prima')
def conocimiento_primo():
    return solicitar_instancia('Primo') #LLama instancia de un metodo de aprender

#---------------------------------------Fin de las rutas de aprender---------------------------------------------------#


#----------------------------------------Donde se accede y el inicio---------------------------------------------------#
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5001')
