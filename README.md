<h1 align=center> <strong>PROYECTO FINAL</strong> </h1>
<h2 align="center">Data Science</h2>
<p align=center><img src="https://github.com/OlgaAcosta/Final_Project_DS_Henry/blob/main/src/Data-Solutions-Logo.png"><p>

# 📑 Índice
- [Introducción](#introduccion)
- [¿Quiénes somos?](#quienes)
- [Nuestro cliente](#cliente)
- [Propuesta de negocio](#propuestadenegocio)
- [KPI's](#kpis)
- [Alcance](#alcance)
- [Contexto de los datos](#contextodelosdatos)
- [Flujo de trabajo](#flujodetrabajo)
- [EDA-ETL](#edaetl)
- [Análisis](#analisis)
- [Modelo Machine Learning](#ml)
- [Deployment](#dep)
- [Herramientas utilizadas](#herramientas)
- [Colaboradores](#colaboradores)

# 📍  Introducción <a name="introduccion"></a>
<b>Este proyecto corresponde al Proyecto Final de la etapa de *Lab's* del programa de **Data Science** de **Henry**.</b> 

En los Estados Unidos, el rubro de los negocios gastronómicos es extremadamente diverso y dinámico, reflejando la rica mezcla cultural y étnica del país. La presencia de diversas comunidades ha tenido un impacto significativo en la industria alimentaria, llevando a la evolución de una amplia variedad de opciones culinarias para satisfacer gustos y preferencias.

Por otro lado, la creciente población latinoamericana en los Estados Unidos, especialmente en estados como California, Texas y Florida, ha impulsado la demanda de alimentos auténticos que reflejen sus raíces culturales y tradiciones culinarias. Este cambio demográfico ha sido un catalizador para la expansión y adaptación de los negocios gastronómicos, ya que los empresarios han reconocido la necesidad de ofrecer platillos que sean familiares y apreciados por la comunidad latina.

En el contexto de nuestro proyecto, esta evolución y adaptación de la industria gastronómica nos brinda una oportunidad única para ayudar a un empresario a ampliar su oferta hacia la comida mexicana, capitalizando la demanda existente y creando una propuesta culinaria atractiva para la comunidad latina y otros amantes de la comida auténtica.

Así, combinamos la gastronomía y la analítica de datos para posicionar la marca de un restaurante californiano  y  expandir su oferta hacia la comida mexicana, todo ello respaldado por el poder de las puntuaciones y reseñas en plataformas como Google Maps y Yelp.

A partir de los datos proporcionados por las reseñas de los comensales, se aplicaron técnicas de análisis de sentimiento y procesamiento de lenguaje natural para descubrir los secretos de lo que hace que la comida mexicana sea irresistible. A través de este análisis profundo, no solo buscamos entender las preferencias de los clientes, sino también identificar las áreas donde el restaurante puede superarse y destacar en un mercado competitivo. Así, con estos conocimientos, diseñamos métricas informadas y orientadas al objetivo de elevar la experiencia culinaria y capturar la esencia auténtica de la comida mexicana en cada platillo ofrecido.

Finalmente, trabajamos con Google Cloud para la obtimización del flujo de trabajo, tiempo y recursos, y la automatización de la extracción, la extracción y la carga de los datos ya limpios, así como de la alimentación de una base de datos también en la nube.

# 📍 ¿Quiénes somos? <a name="quienes"></a>
Somos la empresa de consultoría “Data Solution”, especializada en el análisis de datos para empresas y empresarios. 
Nos dedicamos a proporcionar soluciones de negocio altamente personalizadas y efectivas, respaldadas por un enfoque innovador basado en tecnologías de vanguardia, como el machine learning. Brindamos una visión profunda y fundamentada que permite identificar oportunidades de mejora, optimización de procesos y una ventaja competitiva en el mercado.

# 📍 Nuestro cliente <a name="cliente"></a>
Lure Fish House - 'Seafood restaurant' | Sta. Barbara, California) | [Website](https://www.lurefishhouse.com/)
* CGO (Chief Growth Officer): Matt Rek | [Linkedin](https://www.linkedin.com/in/matt-rek-a11a1379/)
* Cantidad de reviews: Yelp - 1202 | Google Maps- 1088
<p align=center><img src="https://github.com/OlgaAcosta/Final_Project_DS_Henry/blob/main/src/Lure_Fish_House_Logo.png"><p>


# 📍 Propuesta de negocio <a name="propuestadenegocio"></a>
### Objetivo General de Proyecto:
  1. Evaluar el estado actual del negocio para identificar oportunidades de mejora.
  2. Identificar las preferencias gastronómicas que influyen en el consumo de comida mexicana para una implementación competitiva de la nueva oferta.

### ¿Cómo lo haremos?:

#### Objetivo 1:
- Establecer un modelo de NLP que devuelva la correlación entre palabras clave y rating a partir de las reseñas para determinar mejoras a implementar en los restaurantes.
- Identificar palabras clave en los comentarios menores o igual a 3 estrellas, para detectar lo que se debe mejorar. 
- Identificar palabras clave en los comentarios mayores a 3 estrellas, para detectar lo que se debe mantener y potenciar.
- Obtener una métrica de la satisfacción del cliente respecto a la velocidad de atención a partir de la relación de los comentarios positivos y negativos respecto a esto.


#### Objetivo 2:
- Detectar los tres estados donde hay mayor porcentaje de latinos (California, Texas, Florida).
- Establecer un modelo de NLP que devuelva la correlación entre palabras clave y rating a partir de las reseñas para determinar un top N de características a implementar en la oferta.

#### Plus: 
- Identificar los lugares donde se encuentra la mayor cantidad de restaurantes.
- Predecir el crecimiento del consumo en restaurantes de comida latina (dataset externo).
- Automatizar la clasificación de los comentarios con análisis de sentimiento.

# 📍  KPI's <a name="kpis"></a>
Los cuatro primeros están orientados a la consecución del primer objetivo relacionado a la mejora del servicio: el primero consiste en:  
1. <b>Cantidad de reseñas</b>: Aumentar en 66 puntos porcentuales la tasa de nivel óptimo de reseñas, en el próximo trimestre (22 puntos porcentuales cada mes).
>> * Métrica: cantidad de reseñas del mes actual sobre cantidad máxima de reseñas alcanzadas en un mes.
>> * Objetivo: 30% en el próximo trimestre (2022-Q1).
2. <b>Retención de clientes</b>:	Aumentar en 4 puntos porcentuales la tasa de retención de clientes en el próximo año.
>> * Métrica: cantidad de clientes anual que comentaron más de una vez / cantidad total anual de clientes que comentaron.
>> * Objetivo: 10% en el 2022.
3.	<b>Insatisfacción del cliente respecto al servicio</b>: Reducir en 30 puntos porcentuales la tasa de satisfacción del cliente respecto al servicio, en el próximo trimestre.
>> * Métrica: cantidad de comentarios negativos respecto al servicio sobre cantidad de comentarios totales respecto al servicio.
>> * Objetivo: 7% en el próximo trimestre (2022-Q1).
4. <b>Usuarios elite</b>: Aumentar en 18% la tasa de reseñas de usuarios elite en el próximo trimestre.
>> * Métrica: cantidad de reseñas  de usuarios elite sobre la cantidad de reseñas  totales por trimestre.
>> * Objetivo: 40% al finalizar el periodo 2022-Q1.

Los dos últimos se orientan a la consecución del segundo objetivo relacionado a la implementación competitiva de la nueva oferta de comida mexicana:  
5. <b>Clientes de comida mexicana</b>: Aumentar en 23% la tasa de clientes de comida mexicana en el siguiente trimestre.
>> * Métrica: clientes que consuman comida mexicana sobre clientes totales.
>> * Objetivo: 45% al finalizar el próximo trimestres 2022-Q1. 
6.	<b>PLUS: Oferta-Demanda de comida mexicana</b>: A partir de la relación de la cantidad de restaurantes de comida mexicana (oferta) sobre la cantidad de reviews de comida mexicana (demanda), detectar las ciudades con menor tasa con el fin de identificar las ciudades potenciales donde abrir nuevos locales del rubro de comida mexicana. 
>> * Métrica: cantidad de restaurantes de comida mexicana sobre cantidad de reseñas de comida mexicana por estado.
>> * Objetivo: Identificar el top 3 de ciudades potenciales por estado.


# 📍  Alcance <a name="alcance"></a>
Respecto al alcance de nuestro proyecto es importante precisar en primer lugar que las métricas necesarias y el análisis general se obtendrán a partir de los datos provistos por Google Maps y Yelp, y consistirán en una aproximación / proporción que nos permita entender la cantidad de consumidores de comida mexicana, cantidad de restaurantes , etc., a partir de las reviews realizadas. Por lo que no serán datos reales en cuanto a cifra exacta pero sí datos que brinden información  valiosa que represente a esa realidad. 
* El alcance temporal comprende las reviews a partir del año 2018 al 2022; esto porque consideramos importante que, ya que uno de los objetivos es la mejora del servicio, se debe trabajar a partir de los datos más recientes; si tomáramos años anteriores es muy probable que la información ya esté desactualizada ya que sabemos que los restaurantes realizan cambios de infraestructura, oferta , servicios, métodos de pago incorporando nuevos medios.
* El alcance geográfico se basa en tres estados: California, Florida y Texas , ya que en estos tres estados se encuentra la mayor población latina de Estados Unidos, lo cual es un punto de interés en el cual enfocar la nueva oferta de comida mexicana.

# 📍  Contexto de los datos <a name="contextodelosdatos"></a>
Los datos en bruto se adquirieron de la carpeta de googgle drive proporcionada por Henry y corresponden a Google Maps y Yelp, de los cuales se sleccionaron los datasets relevantes con respecto a los objetivos del proyecto. Los formatos son json, parquet y pickle. A partir de ellos se realizaron los procesos de EDA/ETL para obtener nuevos dataset limpios, trasformados, normalizados y listos para su ingesta en una base de datos.
A continuación, se brindan los enlaces correspondientes a la data original.
## 📁  Data
- [Google Maps - original](https://drive.google.com/drive/folders/1Wf7YkxA0aHI3GpoHc9Nh8_scf5BbD4DA?usp=drive_link)
- [Yelps - original](https://drive.google.com/drive/folders/1yP5gKRrJmlng-44zHeOGkmLozZCR3yze?usp=drive_link)
>>>[Diccionario de datos](https://docs.google.com/spreadsheets/d/14G-V0MYpDUzjEogw37VsYo75ure0puJb/edit#gid=754630663)
- [POST EDA-ETL](https://drive.google.com/drive/folders/1yP5gKRrJmlng-44zHeOGkmLozZCR3yze?usp=drive_link)

# 📍  Flujo de trabajo <a name="flujodetrabajo"></a>
<p align=center><img src="https://github.com/OlgaAcosta/Final_Project_DS_Henry/blob/main/src/Work%20flow.jpeg"><p>

# 📍  EDA - ETL <a name="edaetl"></a> : [Notebook](https://drive.google.com/file/d/1WEXVs5lHsXclyavWLYiscu9OxmLr1TAf/view?usp=sharing) 
Se realizaron los siguientes pasos en los procedimientos de EDA-ETL:

#### 1. Proceso de Google Maps Metadata:

* Extracción:
>> - Se leyeron archivos JSON que contenían metadatos de Google Maps y se cargaron en DataFrames.
* Transformación:
>> - Se normalizó la columna 'state' cambiando nombres completos de estados por códigos ISO.
>> - Se filtraron registros por estados específicos: California (CA), Florida (FL) y Texas (TX).
>> - Se identificaron palabras clave en la columna 'category' para determinar si un establecimiento es un restaurante.
>> - Se eliminaron duplicados basados en la columna 'gmap_id'.
>> - Se eliminaron columnas innecesarias ('description', 'hours', 'price', 'url' y 'relative_results').
>> - Se creó una nueva tabla 'states' para mapear estados con códigos ISO y nombres.
>> - Se asignaron identificadores 'state_id' a cada registro en función de su estado.
>> - Se reordenaron las columnas en el DataFrame resultante.
* Carga:
>> - Se guardaron los resultados en archivos CSV ('gm_restaurants.csv' y 'states.csv').

#### 2. Proceso de Google Maps Revisiones:

* Extracción:
>> - Se leyeron archivos JSON que contenían revisiones de Google Maps y se cargaron en DataFrames.
* Transformación:
>> - Se convirtió el tipo de dato de la columna 'time' a formato de fecha.
>> - Se filtraron revisiones por año, manteniendo solo aquellas a partir de 2018.
>> - Se filtraron revisiones por establecimientos previamente seleccionados ('gmap_id').
>> - Se eliminaron columnas innecesarias ('name' y 'pics').
>> - Se creó la columna 'state_id' basada en el estado al que pertenece la revisión.
>> - Se cambió el nombre de la columna 'time' a 'date'.
>> - Se eliminaron revisiones duplicadas basadas en todas las columnas excepto 'resp'.
>> - Se generó un identificador único 'review_id' para cada revisión.
>> - Se reordenaron las columnas en el DataFrame resultante.
* Carga:
>> - Se guardaron los resultados en un archivo CSV ('gm_reviews.csv').

#### 3. Proceso de Yelp Metadata:

* Extracción:
>> - Se leyó un archivo Parquet llamado 'business.pkl' que contenía metadatos de Yelp y se cargaron en un DataFrame.
* Transformación:
>> - Se seleccionaron las columnas relevantes del DataFrame ('business_id', 'name', 'postal_code', 'city', 'state', 'categories').
>> - Se filtraron los registros basados en códigos postales que correspondían a California, Florida y Texas.
>> - Se filtraron los establecimientos que eran restaurantes y tenían categorías relevantes.
>> - Se convirtió la columna 'categories' en listas de categorías.
>> - Se imputaron valores nulos en columnas específicas.
>> - Se normalizó la columna 'city' a formato de título.
>> - Se generó un DataFrame adicional llamado 'cities' con identificadores únicos para ciudades y estados.
>> - Se asignaron identificadores únicos para ciudades en el DataFrame principal.
>> - Se eliminaron columnas redundantes.
* Carga:
>> - Se guardaron los resultados en archivos CSV ('yelp_restaurants.csv' y 'cities.csv').

#### 4. Proceso de Yelp Revisiones:

* Extracción:
>> - Se leyó un archivo JSON de revisiones de Yelp en trozos y se cargaron en DataFrames.
* Transformación:
>> - Se eliminaron columnas innecesarias ('useful', 'funny' y 'cool').
>> - Se convirtió el tipo de dato de la columna 'date' a formato de fecha.
>> - Se filtraron revisiones por establecimientos previamente seleccionados ('business_id').
>> - Se filtraron revisiones por año, manteniendo solo aquellas a partir de 2018.
* Carga:
>> - Se guardaron los resultados en un archivo CSV ('yelp_reviews.csv').

#### 5. Proceso de Yelp Usuarios:

* Extracción:
>> - Se leyó un archivo Parquet que contenía datos de usuarios de Yelp y se cargaron en DataFrames.
* Transformación:
>> - Se filtraron usuarios en función de los identificadores únicos de revisores en el DataFrame de revisiones.
>> - Se imputaron valores vacíos en la columna 'elite'.
* Carga:
>> - Se guardaron los resultados en un archivo CSV ('yelp_users.csv').

En resumen, estos procedimientos de EDA-ETL abordaron la extracción, transformación y carga de datos desde varios formatos de archivo, incluyendo JSON, Parquet y PKL, para generar archivos CSV que contienen datos normalizados y relevantes de acuerdo a los objetivos propuestos.

A partir de estas transformaciones, se construyeron las siguientes funciones para automatizar el proceso:
1. process_gm_metadata_files: Extrae y transforma metadatos de Google Maps.
2. process_gm_reviews_files: Extrae, transforma y filtra revisiones de Google Maps.
3. process_yelp_metadata: Extrae y transforma metadatos de Yelp.
4. process_yelp_reviews_file: Extrae, transforma y filtra revisiones de Yelp en trozos.
5. process_yelp_users: Extrae y transforma usuarios de Yelp.

<b>Puede observarse el paso a paso en el notebook provisto, o en el archivo *EDA-ETL* que se encuentra en este repositorio.</b>


# 📍  Análisis e insights: <a name="analisis"></a> [Notebook](https://drive.google.com/file/d/1pypyJQlzKG_iaCaHJ3cdk-Ye_kGFHTOi/view?usp=sharing)
A partir del objetivo planteado, se analizó el comportamiento y evolución de los usuarios a partir de sus reviews en cuánto a los siguientes aspectos:
* Evolución de la cantidad de reviews de manera general, de los restaurantes marinos y de Lure Fish House.
* Evolución de la tasa de retención de clientes por mes y año de Lure Fish House.
* Contenido de las reviews de Lure y, en específico, las relacionadas al mal servicio.
* Cantidad de reviews realizadas por usuarios elite.
* Cantidad de reviews realizadas a restaurantes de comida mexicana.

De lo anterior, se halló, entre otras cosas, que:
* La cantidad máxima a la que ha llegado ha sido de 30, mientras que la cantidad máxima del top 1 ha sido del doble, 60.
* Actualmente, nuestro cliente se encuentra al nivel de los últimos puestos del top 5 de restaurantes marinos con más reseñas por mes, teniendo menos del 50% de cantidad de reviews respecto al restaurante que tiene más reviews.
* Todos los restaurantes del top 5 han disminuido su cantidad de reseñas respecto a la evolución general.
* Es conveniente poner el foco en aumentar la cantidad actual para que vuelva a llegar a 30, ya que esta sería una cantidad óptima a partir de la cual seguir creciendo.
  
* En general, los clientes suelen estar satisfechos con su experiencia en Lure Fish House y con los platos ofrecidos: más del 80% de comentarios relacionados a la atención de los meseros son buenos, teniendo 4 o 5 estrellas. Sin embargo, el 16% de comentarios totales respecto al servicio son o neutros o negativos (d 1 a 3 estrellas). Esto muestra que hay un aspecto importante que mejorar relacionado a la atención de los meseros y al tiempo, ya que las palabras *service*, *server*, *waiter*, *table*, *order*, *time* y *minute* destacan en el wordcloud. Además, esto puede tener que ver con la decisión de retorno al restaurante , puesto que las palabras *back* y*never* también tienen una presencia importante.

<b>Puede observarse el paso a paso en el notebook provisto, o en el archivo *Analysis* que se encuentra en este repositorio.</b>
 
# 📍  Dashboard: <a name="analisis"></a> [Archivo Pbi](https://drive.google.com/file/d/1GFoQ7qi4O1usQHHR4Ss4CCDubPafkB1t/view?usp=sharing)
El dashboard se realizó en Power BI. 
<b>Puede observarse en el link del archivo pbi provisto, o en el archivo *Dashboard* que se encuentra en este repositorio.</b>

# 📍 Modelo Machine Learning <a name="ml"></a>
Se realizaron los siguientes pasos para el entrenamiento de nuestro modelo de análisis de sentimiento:
* Extracción:
>> -Se leyeron archivos CSVs desde Google Cloud Storage que contenían metadatos de Google Maps y YELP y se cargaron en DataFrames.

* Transformación:
>> -Se eliminaron las columnas que no se utilizarían en el modelo dejando la estructura: 'review_id','stars','text'
>> -Se consideraron sólo reviews que tengan una longitud mayor a 2 y menor de 500 caracteres.
>> -Se realizó el preprocesamiento de los reviews quitando los números, signos de puntuación, y volviendo minúsculas, esto se guardo en una nueva columna: 'cleaned_text'
>> -Se realizó el mapeado de sentimiento considerando la información de la columna 'starts' de la siguiente manera: calificación 1 y 2 sentimiento negativo, calificiación 3 como sentimiento neutral, y calificación 4 y 5 como positivo.
* Modelos utilizados:
>> -SVM (support vector machine)
>> -BERT (Bidirectional Encoder Representations from Transformers)
* Entrenamiento:
>> -La representación de los reviews se realizó mediante el TF-IDF considerando 1000 feautures.
>> -El entrenamiento se realizó de utilizando el 80% de la data para el entranmiento y el 20% para las pruebas de validación
* Carga:
>> -Se guardaron las matrices TF-IDF como: tfidf_vectorizer.pkl  y también los pesos ajustados de nuestro modelos: svm_model.pkl y bert_model.pkl para ser utilizados en streamlit todo esto desde Google Cloud Storage

# 📍  Deployment <a name="dep"></a>
El funcionamiento del modelo realizado se desarrolló a través de *Streamlit* y puede visualizarse en este [link](https://app-final-project-kze5wzgats9sj7bhmjgyt4.streamlit.app/).

# 📍  Herramientas utilizadas <a name="herramientas"></a>
* Python
* Numpy
* Pandas
* Re
* pyarrow
* uuid
* Matplotlib
* Seaborn
* TensorFlow
* Sckit Learn
* NLTK
* Google Cloud
* Power BI
* Streamlit

# 📍  Colaboradores <a name="colaboradores"></a>
<p align=center><img src="https://github.com/OlgaAcosta/Final_Project_DS_Henry/blob/main/src/Team.jpeg"><p>
 @OlgaAcosta | @FGC97 | @Roberto4129 | @juanjolopez28 | @HernAle

