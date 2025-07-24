from flask import Flask, jsonify
from flask_cors import CORS  # <-- importar

app = Flask(__name__)
CORS(app)  # <-- habilitar CORS para todas las rutas

@app.route('/api/message')
def message():
    return jsonify({"message": "Hola desde Flask backend :)!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
