from flask import Flask, render_template, request, jsonify
import Pyro5.api
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

def obtener_calculadora():
    try:
        return Pyro5.api.Proxy("PYRO:calculadora@localhost:9090")
    except Exception as e:
        print(f"Error: {e}")
        return None

def probar_conexion():
    try:
        calc = obtener_calculadora()
        return calc is not None and calc.obtener_info()
    except:
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/suma', methods=['POST'])
def suma():
    try:
        calc = obtener_calculadora()
        if not calc:
            return jsonify({'resultado': None, 'error': 'No conectado al servidor'})
        data = request.json
        a = float(data['a'])
        b = float(data['b'])
        resultado = calc.suma(a, b)
        return jsonify({'resultado': resultado, 'error': None})
    except Exception as e:
        return jsonify({'resultado': None, 'error': str(e)})

@app.route('/api/resta', methods=['POST'])
def resta():
    try:
        calc = obtener_calculadora()
        if not calc:
            return jsonify({'resultado': None, 'error': 'No conectado al servidor'})
        data = request.json
        a = float(data['a'])
        b = float(data['b'])
        resultado = calc.resta(a, b)
        return jsonify({'resultado': resultado, 'error': None})
    except Exception as e:
        return jsonify({'resultado': None, 'error': str(e)})

@app.route('/api/multiplicacion', methods=['POST'])
def multiplicacion():
    try:
        calc = obtener_calculadora()
        if not calc:
            return jsonify({'resultado': None, 'error': 'No conectado al servidor'})
        data = request.json
        a = float(data['a'])
        b = float(data['b'])
        resultado = calc.multiplicacion(a, b)
        return jsonify({'resultado': resultado, 'error': None})
    except Exception as e:
        return jsonify({'resultado': None, 'error': str(e)})

@app.route('/api/division', methods=['POST'])
def division():
    try:
        calc = obtener_calculadora()
        if not calc:
            return jsonify({'resultado': None, 'error': 'No conectado al servidor'})
        data = request.json
        a = float(data['a'])
        b = float(data['b'])
        resultado = calc.division(a, b)
        return jsonify({'resultado': resultado, 'error': None})
    except Exception as e:
        return jsonify({'resultado': None, 'error': str(e)})

@app.route('/api/historial', methods=['GET'])
def historial():
    try:
        calc = obtener_calculadora()
        if not calc:
            return jsonify({'historial': [], 'error': 'No conectado al servidor'})
        hist = calc.obtener_historial()
        return jsonify({'historial': hist, 'error': None})
    except Exception as e:
        return jsonify({'historial': [], 'error': str(e)})

@app.route('/api/limpiar', methods=['POST'])
def limpiar():
    try:
        calc = obtener_calculadora()
        if not calc:
            return jsonify({'error': 'No conectado al servidor'})
        calc.limpiar_historial()
        return jsonify({'error': None})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/api/status', methods=['GET'])
def status():
    try:
        calc = obtener_calculadora()
        if not calc:
            return jsonify({'conectado': False, 'info': None})
        info = calc.obtener_info()
        return jsonify({'conectado': True, 'info': info})
    except:
        return jsonify({'conectado': False, 'info': None})

if __name__ == '__main__':
    app.run(debug=False, port=5000, threaded=True)
