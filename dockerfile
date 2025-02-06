# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de tu proyecto al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto que usará la aplicación Flask
EXPOSE 5000

# Define el comando para iniciar la aplicación Flask
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app.app:app"]
