import pandas as pd
import requests, zipfile, io

# URL del dataset
dataset_url = "https://files.grouplens.org/datasets/movielens/ml-1m.zip"
dataset_path = "ml-1m.zip"

# Descargar y extraer
response = requests.get(dataset_url)
with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_ref:
    zip_ref.extractall("ml-1m")

