# Usamos una imagen base ligera de Python
FROM python:3.10-slim

# Instalamos las herramientas de compilación necesarias (gcc, build-essential)
RUN apt-get update && \
    apt-get install -y gcc build-essential && \
    rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos el archivo de requerimientos y actualizamos pip
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código fuente de la aplicación
COPY . .

# Exponemos el puerto que usará la aplicación (8000)
EXPOSE 8000

# Comando de inicio del servicio
CMD ["python", "app.py"]
