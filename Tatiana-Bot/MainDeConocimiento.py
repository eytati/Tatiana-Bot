from flask import Flask,render_template, request, jsonify, json
from werkzeug.security import generate_password_hash

app = Flask(__name__)

class operecion:



    def modulo_aritmetico(self, operacion, numero1, numero2):
        resultado =0
        if operacion is 1:
           resultado= numero1 + numero2
        elif operacion is 2:
            resultado= numero1 - numero2
        elif operacion is 3:
            resultado = numero1/numero2
        else:
            resultado = numero1*numero2
        return resultado


    def es_primo(self, numero):
        primo = True
        if numero is 2:
            primo = True
        elif numero%2 is 0:
            primo = False
        else:
            mediaRelativa = int((numero-1)/2)
            for contador in range(3, mediaRelativa):
                if numero%contador is 0:
                    primo = False
                    break
        return primo
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


#-------------------------------Ruta de Informacion General---------------------------------------------#
@app.route('/api/informacion_del_bot')
def informacion_del_bot():

    return render_template('Informacion.html')

#-------------------------------Ruta de Obencion de hash------------------------------------------------#
@app.route('/prueba<valor>')
def prueba(valor):
    obtener_hash = Informacion()
    return str(obtener_hash.Valor_de_hash(valor))


#-------------------------------Ruta que va al menu principal------------------------------------------#
@app.route('/api/principal')
def principal():
    return  render_template('Index2.html')


#-------------------------------Ruta del menu de aprender----------------------------------------------#
@app.route('/api/aprender')
def aprender():
    return 'hola'


#-------------------------------Ruta de aprender operaciones basicas----------------------------------#
@app.route('/api/aprender/ModuloAritmetico/<operacion>/<numero1>/<numero2>', methods=['GET','POST'])
def modulo_aritmetico(operacion, numero1, numero2):
    operacion_int = int(operacion)
    numero_int1 = int(numero1)
    numero_int2 = int(numero2)
    resultado_de_operacion = Aprender()
    return str(resultado_de_operacion.modulo_aritmetico(operacion_int, numero_int1, numero_int2))

#---------------------Ruta de aprender a identificar los numeros primos------------------------------#
@app.route('/api/aprender/primo/<numero>', methods=['GET', 'POST'])
def primo(numero):
    resultado_de_primo = Aprender()
    primo2 = int(numero)
    return str(resultado_de_primo.es_primo(primo2))


'''
class Lista_de_Conocimento:
    @app.route('/lista_actual')
    def lista_actual(slef):
        return

    def buscar_videos(self):

        return

    def toma_fotos(self):

        return
'''

#-------------------------------Donde se accede y el inicio-----------------------------------------#
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5001')