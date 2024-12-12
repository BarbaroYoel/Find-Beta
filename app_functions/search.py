import pandas as pd
from datetime import datetime


def restaurantes_por_municipio(data_frame,municipio):
    restaurantes_filtrados = data_frame[data_frame['municipality'] == municipio]
    if len(restaurantes_filtrados)==0:
        print(f"No se encontraron restaurantes en el municipio '{municipio}'.")
        return pd.DataFrame()
    else:
        return restaurantes_filtrados
    

def restaurantes_por_nombre(data_frame,nombre):
    restaurantes_filtrados = data_frame[data_frame['name'] == nombre]
    if len(restaurantes_filtrados)==0:
        print(f"No se encontraron restaurantes con el nombre  '{nombre}'.")
        return pd.DataFrame()
    else:
        return restaurantes_filtrados
    
def restaurantes_por_tipo(data_frame,tipo):
    restaurantes_filtrados = data_frame['type']=tipo
    if len(restaurantes_filtrados)==0:
        print(f"No se encontraron restauentes con ese tipo de dueño '{tipo}'")    
        return pd.DataFrame()
    else:
        return restaurantes_filtrados

def restaurantes_por_especialidad(data_frame,especialidad):
    restaurantes_filtrados = data_frame['specialty']=especialidad
    if len(restaurantes_filtrados)==0:
        print(f"No se encontraron restauentes con esa especialidad '{especialidad}'")    
        return pd.DataFrame()
    else:
        return restaurantes_filtrados
    

def restaurantes_por_tipo_dueño(data_frame,owner):
    restaurantes_filtrados = data_frame['owner']=owner
    if len(restaurantes_filtrados)==0:
        print(f"No se encontraron restauentes con ese tipo de dueño '{owner}'")    
        return pd.DataFrame()
    else:
        return restaurantes_filtrados
    
def restaurantes_por_calificaciones(data_frame, calificacion):
    def obtener_calificacion_mas_alta(ratings:dict):
        if ratings:
            return max(ratings.values())
        return 0

    data_frame['top_rating'] = data_frame['ratings'].apply(obtener_calificacion_mas_alta)
    return data_frame[data_frame['top_rating'] >= calificacion]
   

def restaurantes_abiertos(data_frame, dia=None, hora=None):
    if dia is None:
        dia = datetime.now().strftime("%A").lower() 
    if hora is None:
        hora = datetime.now().strftime("%H%M")

    def esta_abierto(horarios):
        horario = horarios.get(dia, "")
        if not horario or horario == "off":
            return False
        apertura, cierre = map(int, horario.split('_'))
        return apertura <= int(hora) < cierre

    return data_frame[data_frame['hours'].apply(esta_abierto)]
   
    
def restaurantes_por_servio(data_frame,horario):
    pass
   
   
   
   
   
   

def restaurantes_por_metodo_de_pago(data_frame,metodos_de_pago):
    pass
    
def restaurantes_por_plato(data_frame,plato):
    pass
    
def restaurantes_por_precio_promedio_entrantes(data_frame,precio):
    pass

def restaurantes_por_precio_promedio_plato_principal(data_frame,precio):
    pass

def restaurantes_por_precio_promedio_postres(data_frame,precio):
    pass

def restaurantes_por_precio_promedio_bebidas(data_frame,precio):
    pass 
    
def restaurantes_por_precio_promedio_comida(data_frame,precio):
    pass
    
def restaurantes_por_precio_plato_inferiores(data_frame,plato,precio):
    pass
def restaurantes_por_rango_de_precios(data_frame,precio_min,precio_max):
   pass