import requests
from flask import Flask

app = Flask(__name__)


@app.route('/EstadoActual')
def hello_world():
    return 'Hello World!'

'''
@app.route('/Estado actual/<ID>', methods=['GET'])
def holaTati():
    return 'Hola Tati'
'''

@app.route('/Url', methods= ['GET'])
def Url():
    return requests.get('127.0.0.1:5001/Conocimiento').content


if __name__ == '__main__':
    app.run(port='5000')

#try exept