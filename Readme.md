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

---

## 📑 Descripción de Archivos Clave

- **docker-compose.yml**: Orquesta los contenedores de Neo4j, Qdrant y el backend.
- **backend/Dockerfile**: Define la imagen Python con herramientas de compilación y dependencias.
- **backend/requirements.txt**: Lista de librerías necesarias (Flask, Neo4j driver, Qdrant client, Tree-sitter, Transformers, Torch).
- **backend/app.py**: Servicio Flask con endpoint `/health` que comprueba conexiones.
- **backend/utils/connections.py**: Lógica de conexión a Neo4j (espera activa + reintentos) y Qdrant.

---

## 📈 Siguientes Pasos

1. **Parser y chunking**: Implementar `utils/parser.py` con Tree‑sitter.
2. **Generación de embeddings**: Integrar GraphCodeBERT en `utils/embeddings.py`.
3. **Grafo de conocimiento**: Cargar relaciones en Neo4j.
4. **RAG & UI**: Orquestar recuperación y respuesta con LangChain o n8n.

---

¡Listo! Este README cubre la configuración inicial (Pasos 1 y 2). Para la parte de parser y chunking (Paso 3), crea las tareas correspondientes y sigue iterando.


