from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

RESPUESTA_CORRECTA = 'B'
RETROALIMENTACION = {
    'A': 'Incorrecto. Eso describe la Arquitectura en Capas (Layered Architecture), no la Hexagonal.',
    'B': '¡Correcto! La Arquitectura Hexagonal (Ports & Adapters) aísla el núcleo de negocio de tecnologías externas mediante puertos y adaptadores.',
    'C': 'Incorrecto. Eso describe una arquitectura de Microservicios orientada a mensajes HTTP.',
    'D': 'Incorrecto. Eso describe el patrón Front Controller, común en frameworks MVC.',
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz', methods=['POST'])
def quiz():
    data = request.get_json()
    respuesta = data.get('respuesta', '').upper()
    correcta = respuesta == RESPUESTA_CORRECTA
    return jsonify({
        'correcta': correcta,
        'respuesta_correcta': RESPUESTA_CORRECTA,
        'retroalimentacion': RETROALIMENTACION.get(respuesta, 'Respuesta no válida.')
    })

if __name__ == '__main__':
    app.run(debug=True)