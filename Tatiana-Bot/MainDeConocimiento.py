from flask import Flask,render_template, request
import  cv2

app = Flask(__name__)


@app.route('/Conocimiento', methods=['GET'])
def hello_world():
    return render_template('Index2.html')


@app.route('/Cono')
def hola():
    return 'Hello World'



class Lista_de_Conocimento:
    @app.route('/lista_actual')
    def lista_actual(slef):
        return

    def buscar_videos(self):

        return

    def toma_fotos(self):

        return


class Aprender:
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



@app.route('/aprender')
def aprender():
    return 'hola'

@app.route('/aprender/primo/<numero>', methods=['GET', 'POST'])
def primo(numero):
    resultado_de_primo = Aprender()
    primo2 = int(numero)
    return str(resultado_de_primo.es_primo(primo2))

@app.route('/Aprender/ModuloAritmetico/<operacion>/<numero1>/<numero2>', methods=['GET','POST'])
def modulo_aritmetico(operacion, numero1, numero2):
    operacion_int = int(operacion)
    numero_int1 = int(numero1)
    numero_int2 = int(numero2)
    resultado_de_operacion = Aprender()
    return str(resultado_de_operacion.modulo_aritmetico(operacion_int, numero_int1, numero_int2))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5001')