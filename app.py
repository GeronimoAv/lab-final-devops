from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

# Constantes de configuración
C_HOST = "0.0.0.0"
C_PORT = 5000
C_DEBUG = True

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # ¡Esto es lo que expone los datos!

# ... (deja el resto de tus rutas F_HOME y F_HEALTH exactamente igual) ...


@app.route("/")
def F_HOME():
    V_RESPUESTA = {
        "message": "Hola desde la app DevOps prueba uno",
        "status": "ok"
    }
    return jsonify(V_RESPUESTA)

# FUNCION: F_HEALTH
# Ruta de verificación de estado de la aplicación (usada por Kubernetes)


@app.route("/health")
def F_HEALTH():
    V_RESPUESTA = {
        "status": "healthy"
    }
    return jsonify(V_RESPUESTA)


if __name__ == "__main__":
    app.run(host=C_HOST, port=C_PORT, debug=C_DEBUG)
