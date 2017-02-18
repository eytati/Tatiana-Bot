
from flask import Flask, request

app = Flask(__name__)


@app.route('/EstadoActual')
def hello_world():
    return 'Hello World!'

'''
@app.route('/Estado actual/<ID>', methods=['GET'])
def holaTati():
    return 'Hola Tati'
'''

@app.route('/Url')
def Url():
        return requests.get('0.0.0.0:5001/Conocimiento').content


if __name__ == '__main__':
    app.run(port=5000)

#try exept