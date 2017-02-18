from flask import Flask, request_started

app = Flask(__name__)


@app.route('/Estado actual')
def hello_world():
    return 'Hello World!'


'''
@app.route('/Estado actual/<ID>', methods=['GET'])
def holaTati():
    return 'Hola Tati'


@app.route('/Url', methods=['GET'])
def Url():
    dato = request_started.get(app.config['0.0.0.0'] + ':' + app.config['8001'] + '/Conocimiento', auth=(app.config['ORACLE_REST_USR'], app.config['ORACLE_REST_PASS']))
    return dato
    '''

if __name__ == '_main__':
    app.run(port=5000)
