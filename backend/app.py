"""
Módulo principal del servicio backend.
Este servicio se encargará de la indexación inicial del código, generación de embeddings y actualización de DBs.
Por el momento, se establecerá el endpoint de salud para validar la conexión a Neo4j y Qdrant.
"""

import os
from flask import Flask, jsonify
from utils.connections import test_neo4j, test_qdrant

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health_check():
    """
    Endpoint para comprobar el estado de las conexiones.
    """
    neo4j_status = test_neo4j()
    qdrant_status = test_qdrant()
    return jsonify({
        "status": "ok",
        "neo4j": neo4j_status,
        "qdrant": qdrant_status
    })

if __name__ == "__main__":
    print("Iniciando pruebas de conexión a bases de datos...")
    test_neo4j()
    test_qdrant()
    print("Conexiones establecidas. Arrancando servicio Flask...")
    app.run(host="0.0.0.0", port=8000, debug=False)
