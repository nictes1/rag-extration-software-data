# Project: RAG Coding Environment Setup

Este repositorio contiene la configuración necesaria para levantar un entorno básico de RAG (Retrieval-Augmented Generation) sobre tu propio código, utilizando:

- **Neo4j** para grafo de conocimiento.
- **Qdrant** para base de datos vectorial.
- **Backend Python** con Flask para endpoints de salud y futuras integraciones.

---

## 📁 Estructura del Repositorio

```
rag-coding/
├── backend/
│   ├── Dockerfile
│   ├── entrypoint.sh      # (opcional) script de arranque
│   ├── requirements.txt
│   ├── app.py
│   └── utils/
│       ├── __init__.py
│       └── connections.py
├── code/                  # Ruta donde se monta el código a indexar
├── docker-compose.yml
└── README.md              # Este archivo
```

---

## ⚙️ Prerrequisitos

- Docker y Docker Compose instalados.
- Git para clonar este repositorio.

---

## 🚀 Instalación y Ejecución

1. Clona este repositorio:

   ```bash
   git clone https://url-de-tu-repo/tu-proyecto-rag-coding.git
   cd tu-proyecto-rag-coding
   ```

2. Compón los contenedores:

   ```bash
   docker compose up --build -d
   ```

3. Verifica que todos los servicios estén activos:

   ```bash
   docker ps
   ```

4. Comprueba el endpoint de salud:

   ```bash
   curl http://localhost:8000/health
   ```

   Deberías obtener:

   ```json
   {"neo4j":"connected","qdrant":"connected","status":"ok"}
   ```

5. Comprueba el endpoint de Qdrant y Neo4j:

   Qdrant:
   ```bash
   # Lista las colecciones (debe devolver [] si no hay colecciones aún)
   curl -X GET http://localhost:6333/collections
   ```

   Neo4j:

   ```bash
   # Ejecuta una consulta Cypher simple (devuelve 42)
   curl -u neo4j:test1234 \
     -H "Content-Type: application/json" \
     -X POST http://localhost:7474/db/neo4j/tx/commit \
     -d '{"statements":[{"statement":"RETURN 42 AS answer"}]}'
   ```
---

## 📑 Descripción de Archivos Clave

- **docker-compose.yml**: Orquesta los contenedores de Neo4j, Qdrant y el backend.
- **backend/Dockerfile**: Define la imagen Python con herramientas de compilación y dependencias.
- **backend/requirements.txt**: Lista de librerías necesarias (Flask, Neo4j driver, Qdrant client, Tree-sitter, Transformers, Torch).
- **backend/app.py**: Servicio Flask con endpoint `/health` que comprueba conexiones.
- **backend/utils/connections.py**: Lógica de conexión a Neo4j (espera activa + reintentos) y Qdrant.

---

