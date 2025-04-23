"""
Módulo para gestionar conexiones a las bases de datos:
- Conexión a Neo4j (con reintentos para esperar que el servicio esté listo)
- Conexión a Qdrant (usando el método 'list_collections()')
"""

import os
import time
from neo4j import GraphDatabase
from qdrant_client import QdrantClient

def test_neo4j():
    """
    Prueba la conexión a la base de datos Neo4j.
    Se implementa un bucle de reintentos para manejar la demora en el arranque del contenedor.
    """
    neo4j_uri = os.getenv("NEO4J_URI", "bolt://neo4j:7687")
    neo4j_user = os.getenv("NEO4J_USER", "neo4j")
    neo4j_password = os.getenv("NEO4J_PASSWORD", "test1234")
    
    attempts = 10
    for i in range(attempts):
        try:
            driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))
            with driver.session() as session:
                result = session.run("RETURN 1 AS number")
                for record in result:
                    print("Conexión a Neo4j exitosa, retorno:", record["number"])
            driver.close()
            return "connected"
        except Exception as e:
            print(f"Intento {i+1} de {attempts} fallido al conectar con Neo4j:", e)
            time.sleep(5)
    return "error: no se pudo conectar a Neo4j"

def test_qdrant():
    """
    Prueba la conexión a la base de datos Qdrant.
    Se utiliza el método 'get_collections()' directamente sobre el cliente.
    """
    try:
        client = QdrantClient(host="qdrant", port=6333)
        collections = client.get_collections()  # Llamada directa al método
        print("Conexión a Qdrant exitosa. Colecciones disponibles:", collections)
        return "connected"
    except Exception as e:
        print("Error al conectar con Qdrant:", e)
        return f"error: {e}"
