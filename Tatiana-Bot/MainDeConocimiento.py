from flask import Flask

app = Flask(__name__)


@app.route('/Conocimiento')
def hello_world():
    return 'Hello Tati!'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5001')




class Estado_Actual:
    def __init__(self):
        # Constructor
        return

    @app.route('/EstadoAtual', methods=['GET'])
    def estado(self):
        return 'Index'

class Lista_de_Conocimiento:

    def modulo_aritmetico(self, operacion, numero1, numero2):
        resultado =0
        if operacion is 'Suma':
           resultado= numero1 + numero2
        elif operacion is 'Resta':
            resultado= numero1 - numero2
        elif operacion is 'Division':
            resultado = numero1/numero2
        else:
            resultado = numero1*numero2
        return resultado

    def es_primo(self, numero):
        primo = False
        if numero is 2:
            primo = True
        elif numero%2 is 0:
            primo = False
        else:
            mediaRelativa = (numero-1)/2
            for contador in range(mediaRelativa):
                if numero%contador is 0:
                    primo = False
                    break

        return primo


