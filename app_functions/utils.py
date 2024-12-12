import pandas as pd
import json
import glob


def crear_data_frame():
 ruta_archivos = "/home/barbaroyoel/Documentos/Estudio/MATCOM/Data Science/1ro/Primer Semestre/IP - ICD/Proyecto ICD-IP/Find Beta/data/restaurants_bars/*.json"
 data = []
 
 for archivo in glob.glob(ruta_archivos):
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = json.load(f)
        data.append(contenido)

 df = pd.DataFrame(data)
 return df

df =crear_data_frame()