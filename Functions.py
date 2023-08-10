import pandas as pd
import numpy as np
import re
import pyarrow.parquet as pq
import uuid

####################################################################################################################

# FUNCIÓN 1
def process_gm_metadata_files(paths):
    """Explicación"""
    result_dataframes = []
# EXTRACCIÓN
    for path in paths:
        # Leer el archivo JSON y convertirlo en DataFrame
        df = pd.read_json(path, lines=True)
        
# TRANSFORMACIÓN
        # Reemplaza la columna "state" y normalizar por el ISO del estado
        df['state'] = df['address'].str.upper()
        df['state'] = df['state'].str.replace('FLORIDA', 'FL')
        df['state'] = df['state'].str.replace('CALIFORNIA', 'CA')
        df['state'] = df['state'].str.replace('TEXAS', 'TX')

        # Revisar los registros que contienen el ISO o el nombre de los estados y reemplazar por el ISO correspondiente
        df['state'] = df.apply(lambda row: 'FL' if row['state'] is not None and ('FL' in row['state'] or 'FLORIDA' in row['state']) else row['state'], axis=1)
        df['state'] = df.apply(lambda row: 'CA' if row['state'] is not None and ('CA' in row['state'] or 'CALIFORNIA' in row['state']) else row['state'], axis=1)
        df['state'] = df.apply(lambda row: 'TX' if row['state'] is not None and ('TX' in row['state'] or 'TEXAS' in row['state']) else row['state'], axis=1)
        
        #Filtrar por los estados determinados
        df = df[df['state'].isin(['CA', 'FL', 'TX'])]
        
        # Lista de palabras clave a buscar
        palabras_clave = ['restaurant', 'cafe', 'cafeteria', 'fast food', 'fastfood', 'mexican food', 'hamburger']

        # Función para buscar coincidencias de palabras clave en la lista de strings
        def buscar_coincidencias(lista):
            if lista is None:
                return False
            else:
                texto = ' '.join(lista).lower()
                for palabra in palabras_clave:
                    if re.search(r'\b' + re.escape(palabra.lower()) + r'\b', texto):
                        return True
                return False

        # Verificar si alguna palabra clave está presente en las listas de strings de la columna 'category'
        df['contains_keyword'] = df['category'].apply(buscar_coincidencias)      
                
        # Filtrar el DataFrame para obtener solo las filas que contienen palabras clave (los que sean TRUE)
        df = df[df['contains_keyword']]

        # Eliminar la columna 'contains_keyword' si ya no es necesaria
        df.drop('contains_keyword', axis=1, inplace=True)

        # Borrar duplicados de gmap_id:
        df.drop_duplicates(subset="gmap_id", inplace=True)
        
        # Eliminar columnas innecesarias:
        columns = ["description", "hours", "price", "url", "relative_results"]
        df.drop(columns, axis=1, inplace=True)
        
        # Agregar el DataFrame final a la lista de resultados
        result_dataframes.append(df)
              
    # Une los DataFrames verticalmente
    merged_dataframe = pd.concat(result_dataframes, axis=0)
    
    # Imputo nulos en la columna "MISC"
    merged_dataframe.MISC.fillna("No data", inplace= True)

    # Reiniciar los índices 
    merged_dataframe.reset_index(drop=True, inplace=True)
    
    # Obtengo una nueva tabla states:
    states = {"state_id": [1,2,3] , "iso": merged_dataframe["state"].unique() , 'name': ['California','Florida', 'Texas']}
    states = pd.DataFrame(states)
    
    # Obtengo los valores de state_id en el df gm_metadata_1:
    merged_dataframe['state_id'] = merged_dataframe['state'].map(states.set_index('iso')['state_id'])

    # Elimino la columna "state":
    merged_dataframe.drop("state", axis=1, inplace=True)
    
    # Reordeno las columnas:
    columns= ['gmap_id', 'name', 'address', 'category', 'avg_rating', 
           'num_of_reviews', 'MISC','latitude', 'longitude','state_id']

    merged_dataframe = merged_dataframe[columns]
    

# CARGA    
    merged_dataframe.to_csv('POST_ETL_DATASETS/Google_Maps_Data/gm_restaurants.csv', index=False, encoding="utf-8")
    states.to_csv('POST_ETL_DATASETS/Google_Maps_Data/states.csv', index=False, encoding="utf-8")
    me= "Función 1: 'gm_restaurants.csv', 'states.csv' guardados con éxito."
    
    return me


# Creo variables con el path de cada archivo
path1 = "metadata-sitios/1.json"
path2= "metadata-sitios/2.json"
path3 = "metadata-sitios/3.json"
path4= "metadata-sitios/4.json"
path5 = "metadata-sitios/5.json"
path6= "metadata-sitios/6.json"
path7 = "metadata-sitios/7.json"
path8= "metadata-sitios/8.json"
path9 = "metadata-sitios/9.json"
path10= "metadata-sitios/10.json"
path11 = "metadata-sitios/11.json"

# Lista de rutas de archivos JSON
paths = [ path1,path2,path3,
          path4,path5,path6,
          path7,path8,path9,
          path10,path11 ]

# Llamo a la función
process_gm_metadata_files(paths)

#######################################################################################################################

# FUNCIÓN 2:
def process_gm_reviews_files(paths, df_metadata=None):
    """Explicación"""
    if df_metadata is None:
        df_metadata = pd.read_csv("POST_ETL_DATASETS/Google_Maps_Data/gm_restaurants.csv")
        
    states = pd.read_csv('POST_ETL_DATASETS/Google_Maps_Data/states.csv')
    
    result_dataframes = []
    
    for state_idx, state_paths in enumerate(paths):
        state_iso = states.loc[state_idx, 'iso']
        
        for path in state_paths:
            df = pd.read_json(path, lines=True)
            
            df['time'] = pd.to_datetime(df['time'], unit='ms').dt.date
            df = df[df['time'].apply(lambda x: x.year) >= 2018]
            
            lista_id_restaurantes = list(df_metadata['gmap_id'])
            df = df[df['gmap_id'].isin(lista_id_restaurantes)]
            
            df = df.drop(['name', 'pics'], axis=1)
            
            # Creo la columna 'state' 
            df['state_iso'] = state_iso
            
            # Cambio el nombre de la columna "time" a "date":
            df.rename(columns = {'time': 'date'}, inplace=True)
            
            # Agrego el df a la lista de dataframes:    
            result_dataframes.append(df)
     
    # Concatenar los DataFrames generados para CA, FL y TX    
    merged_dataframe = pd.concat(result_dataframes, axis=0)
    merged_dataframe.reset_index(drop=True, inplace=True)
    
     # Obtengo las filas duplicadas sin contar la columna "resp" ya que es un diccionario:
    duplicados = merged_dataframe.drop("resp", axis=1).duplicated(keep='first')
    indices_duplicados = duplicados[duplicados].index
    merged_dataframe.drop(indices_duplicados, inplace=True)
    merged_dataframe.reset_index(drop=True, inplace=True)
    
    # Generar una columna nueva con un identificador único para cada review:
    merged_dataframe['review_id'] = [uuid.uuid4() for _ in range(len(merged_dataframe))]
    
    # Ordeno columnas:
    columns = ['review_id', 'user_id', 'date', 'rating', 'text', 'resp', 'gmap_id', 'state_iso']
    merged_dataframe = merged_dataframe[columns]
    
    #CARGA
    load_path= "POST_ETL_DATASETS/Google_Maps_Data/gm_reviews.csv"
    merged_dataframe.to_csv(load_path, index=False, encoding="utf-8")
    me="Función 2: 'gm_reviews.csv' guardado con éxito"
    
    return me

# Defino los paths
# California
cal1 = "reviews-estados/review-California/1.json"
cal2 = "reviews-estados/review-California/2.json"
cal3 = "reviews-estados/review-California/3.json"
cal4 = "reviews-estados/review-California/4.json"
cal5 = "reviews-estados/review-California/5.json"
cal6 = "reviews-estados/review-California/6.json"
cal7 = "reviews-estados/review-California/7.json"
cal8 = "reviews-estados/review-California/8.json"
cal9 = "reviews-estados/review-California/9.json"
cal10 = "reviews-estados/review-California/10.json"
cal11 = "reviews-estados/review-California/11.json"
cal12 = "reviews-estados/review-California/12.json"
cal13 = "reviews-estados/review-California/13.json"
cal14 = "reviews-estados/review-California/14.json"
cal15 ="reviews-estados/review-California/15.json"
cal16 = "reviews-estados/review-California/16.json"
cal17 = "reviews-estados/review-California/17.json"
cal18 = "reviews-estados/review-California/18.json"

# Florida
florida1 ="reviews-estados/review-Florida/1.json"
florida2 ="reviews-estados/review-Florida/2.json"
florida3 ="reviews-estados/review-Florida/3.json"
florida4 ="reviews-estados/review-Florida/4.json"
florida5 ="reviews-estados/review-Florida/5.json"
florida6 ="reviews-estados/review-Florida/6.json"
florida7 ="reviews-estados/review-Florida/7.json"
florida8 ="reviews-estados/review-Florida/8.json"
florida9 ="reviews-estados/review-Florida/9.json"
florida10 ="reviews-estados/review-Florida/10.json"
florida11 ="reviews-estados/review-Florida/11.json"
florida12 ="reviews-estados/review-Florida/12.json"
florida13 ="reviews-estados/review-Florida/13.json"
florida14 ="reviews-estados/review-Florida/14.json"
florida15 ="reviews-estados/review-Florida/15.json"
florida16 ="reviews-estados/review-Florida/16.json"
florida17 ="reviews-estados/review-Florida/17.json"
florida18 ="reviews-estados/review-Florida/18.json"
florida19 ="reviews-estados/review-Florida/19.json"

# Texas
texas1 = "reviews-estados/review-Texas/1.json"
texas2 = "reviews-estados/review-Texas/2.json"
texas3 = "reviews-estados/review-Texas/3.json"
texas4 = "reviews-estados/review-Texas/4.json"
texas5 = "reviews-estados/review-Texas/5.json"
texas6 = "reviews-estados/review-Texas/6.json"
texas7 = "reviews-estados/review-Texas/7.json"
texas8 = "reviews-estados/review-Texas/8.json"
texas9 = "reviews-estados/review-Texas/9.json"
texas10 = "reviews-estados/review-Texas/10.json"
texas11 = "reviews-estados/review-Texas/11.json"
texas12 = "reviews-estados/review-Texas/12.json"
texas13 = "reviews-estados/review-Texas/13.json"
texas14 = "reviews-estados/review-Texas/14.json"
texas15 = "reviews-estados/review-Texas/15.json"
texas16 = "reviews-estados/review-Texas/16.json"

# Creo una lista con los paths de cada json correspondiente a los tres estados:
paths=[[cal1, cal2 , cal3, cal4, cal5, cal6, cal7, cal8, cal9, cal10, cal11 , cal12, cal13, cal14, cal15, cal16, cal17, cal18],
       [florida1, florida2, florida3, florida4, florida5, florida6, florida7, florida8,florida9, florida10,florida11, florida12, florida13, florida14, florida15, florida16, florida17, florida18, florida19],
       [ texas1, texas2, texas3, texas4, texas5, texas6, texas7, texas8,texas9, texas10, texas11, texas12, texas13, texas14, texas15, texas16]]

# Llamo a la función:
process_gm_reviews_files(paths)

#######################################################################################################################

# FUNCIÓN 3:
def process_yelp_metadata(path):
    """Explicación"""
# EXTRACCIÓN   
    # Leo el archivo .pkl
    yelp_metadata = pd.read_pickle(path)

# TRANSFORMACIÓN    
    # Elimino columnas duplicadas
    yelp_metadata = yelp_metadata.loc[:, ~yelp_metadata.columns.duplicated()]

    # Elimino columnas innecesarias
    yelp_metadata.drop(["is_open", "hours"], axis=1, inplace=True)

    # Hay registros en la columna postal_code que no pertenecen a EEUU sino a Canadá. Hay que eliminarlas:
    pattern = r'^\d{5}$'  # Expresión regular para 5 dígitos
    mask = yelp_metadata['postal_code'].str.match(pattern, na=False)
    yelp_metadata = yelp_metadata[mask] # Filtro los registros 

    # Asigno los estados correctos a las ciudades
    # Primero imputo todos los estados con "-", para después obtener solo los que nos interesan:
    yelp_metadata['state']='-'

    # CALIFORNIA
    mask_ca = (yelp_metadata['postal_code'].astype(int) >= 90001) & (yelp_metadata['postal_code'].astype(int) <= 96162)
    yelp_metadata.loc[mask_ca, 'state'] = 'CA'

    # FLORIDA           
    mask_fl = (yelp_metadata['postal_code'].astype(int) >= 32003) & (yelp_metadata['postal_code'].astype(int) <= 34997)
    yelp_metadata.loc[mask_fl, 'state'] = 'FL'

    # TEXAS
    mask_tx = (yelp_metadata['postal_code'].astype(int) >= 73301) & (yelp_metadata['postal_code'].astype(int) <= 85000)
    yelp_metadata.loc[mask_tx, 'state'] = 'TX'

    # Filtro por CA, FL, TX
    yelp_metadata= yelp_metadata[yelp_metadata['state'].isin(["CA", "FL", "TX"])]

    # Filtro las filas que contienen la palabra "Restaurants" en la columna 'categories'
    yelp_metadata = yelp_metadata[yelp_metadata['categories'].apply(lambda x: x is not None and 'Restaurants' in x)]

    # Convierto cada registro en una list
    yelp_metadata["categories"] = yelp_metadata["categories"].str.split(",")

    # Imputo nulos :
    yelp_metadata.fillna("No data", inplace=True)

    # Reiniciar los índices 
    yelp_metadata.reset_index(drop=True, inplace=True)

    # Normalizo la columna "city"
    yelp_metadata['city']= yelp_metadata['city'].str.title()

    # TABLA "cities"

    # Creo un nuevo df con los valores únicos de  'postal_code' y seleccionor las columnas 'postal_code' y 'city'
    cities = yelp_metadata.drop_duplicates(subset=['city'])[['city','state']]
    cities= cities.sort_values(by=['state', 'city'])

    # Reindexo
    cities.reset_index(drop=True, inplace=True)

    # Generar un identificador único para city-postal_code:
    cities['city_id'] = cities['city'].str[:2].str.lower() + "-" + (pd.Series(range(100, 100+cities.shape[0]))).astype(str)
    
    # Reordeno columnas
    cities= cities[['city_id', 'city', 'state']]

    #Agrego la columna "city_id" al df
    # Crear un diccionario de mapeo para la columna 'city_id'
    city_id_mapping = cities.set_index('city')['city_id']

    # Usar el método .map() para asignar los valores de 'city_id' en 'yelp_metadata'
    yelp_metadata['city_id'] = yelp_metadata['city'].map(city_id_mapping)

    # Elimino las columnas repetitivas:
    yelp_metadata.drop(['city', 'postal_code', 'state'], axis=1, inplace=True)

    # Obtengo el csv "states" para crear la columna "state_id"
    states= pd.read_csv('POST_ETL_DATASETS/Google_Maps_Data/states.csv')

    # Crear un diccionario de mapeo para la columna 'state_id'
    state_id_mapping = states.set_index('iso')['state_id']

    # Usar el método .map() para asignar los valores de 'state_id' en 'cities'
    cities['state_id'] = cities['state'].map(state_id_mapping)

    # Eliminar la columna "state"
    cities.drop('state', axis=1, inplace=True)
    
# CARGA
    yelp_metadata.to_csv('POST_ETL_DATASETS/Yelp_Data/yelp_restaurants.csv', index=False, encoding="utf-8")
    cities.to_csv('POST_ETL_DATASETS/Yelp_Data/cities.csv', index=False, encoding="utf-8")
    me="Función 3: 'yelp_restaurants.csv' , 'cities.csv' guardados con éxito."
    
    return me

# LLamo a la función:
process_yelp_metadata("business.pkl")

#####################################################################################################################

# FUNCIÓN 4:
def process_yelp_reviews_file(path, chunk_size, df_metadata=None):
    """Explicación"""
    # Extraigo el df a partir del cual se realizará un filtro luego:
    if df_metadata is None:
        df_metadata = pd.read_csv("POST_ETL_DATASETS/Yelp_Data/yelp_restaurants.csv")
    
    
    # Crear una lista para almacenar los DataFrames procesados de cada trozo
    chunks_procesados = []
    
    # Leer el archivo JSON en trozos y procesarlos por separado
    for chunk in pd.read_json(path, lines=True, chunksize=chunk_size):
        # Eliminar columnas innecesarias
        chunk.drop(['useful', 'funny', 'cool'], axis=1, inplace=True)

        # Extraer solo la fecha de la columna "date"
        chunk['date'] = pd.to_datetime(chunk['date']).dt.date
            
        # Generar lista de business_id de restaurantes del yelp_restaurants
        lista_id_restaurantes = list(df_metadata['business_id'])

        # Filtrar establecimientos que son restaurantes y están en CA, FL y TX
        chunk = chunk[chunk['business_id'].isin(lista_id_restaurantes)]
            
        # Filtrar a partir del año 2018
        chunk=chunk[chunk['date'].apply(lambda x: x.year)>=2018]
        
        # Agregar el trozo procesado a la lista de trozos procesados
        chunks_procesados.append(chunk)
     
    # Concatenar los chunks de la lista en un solo dataframe    
    df_concatenado= pd.concat(chunks_procesados)

    # Eliminar duplicados y reindexar
    df_concatenado.drop_duplicates(inplace=True)
    df_concatenado.reset_index(drop=True, inplace=True)

# CARGA
    df_concatenado.to_csv('POST_ETL_DATASETS/Yelp_Data/yelp_reviews.csv', index=False, encoding="utf-8")
    me="Función 4: 'yelp_reviews.csv' guardado con éxito."
    
    return me

# Defino los parámetros:
path = 'C:/Users/Usuario/Downloads/review.json'
chunk_size = 100000

# Llamo a la función:
process_yelp_reviews_file(path, chunk_size)

#####################################################################################################################



# FUNCIÓN 5:
def process_yelp_users(path, df_reviews=None):
    
    # Defino el df que luego se utilizará para un filtro:
    if df_reviews==None:
        df_reviews= pd.read_csv('POST_ETL_DATASETS/Yelp_Data/yelp_reviews.csv')
        
# EXTRACCIÓN
    # Obtengo el arhivo:
    parquet_file = pq.ParquetFile(path)
    
    # Seleccionar las columnas de interés:
    columns = ['user_id', 'name', 'review_count', 'elite', 'fans',
       'average_stars', 'compliment_photos']

    # Lista para almacenar los DataFrames de cada lote
    batch_dfs = []

    for batch in parquet_file.iter_batches(batch_size=100000, columns=columns):
        # Convertir el lote en un DataFrame de Pandas
        batch_df = batch.to_pandas()
        
# TRANSFORMACIÓN        
        # Obtengo en una lista los user_id únicos de df_reviews:
        lista_user_id= list(df_reviews['user_id'].unique())
        
        # Filtro los usuarios a partir de la lista generada:
        batch_df = batch_df[batch_df['user_id'].isin(lista_user_id)]    
        
        # Agregar el DataFrame del lote a la lista
        batch_dfs.append(batch_df)

    # Concatenar todos los DataFrames de los lotes en uno solo
    df_concat = pd.concat(batch_dfs)

    # Borrar duplicados:
    df_concat.drop_duplicates(inplace=True)
    
    # Imputar valores vacíos en la columna "elite":
    df_concat["elite"] = df_concat["elite"].replace("", "No elite")
    
    # Reindexar:
    df_concat.reset_index(drop=True, inplace=True)

# CARGA    
    df_concat.to_csv('POST_ETL_DATASETS/Yelp_Data/yelp_users.csv', index=False, encoding="utf-8")
    me="Función 5: 'yelp_users.csv' guardado con éxito."
    
    return me

# Llamo a la función:
yelp_users = process_yelp_users('user.parquet')