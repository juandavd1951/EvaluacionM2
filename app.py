import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
data = pd.read_csv('historico_resultados_pruebas_saber_11.csv')

data
data.plot.scatter(x='prestacion_servicio', y='ponderado_global')
st.pyplot()

st.header('Filtro 1: Filtrando por los establecimientos tienen un puntaje de lectura mayor e igual a 50 y mostrando las comunas a los que pertenencen')
filtro1 = data[data['puntaje_lectura']>=50]
filtro1
st.set_option('deprecation.showPyplotGlobalUse', False)
filtro1.plot.scatter(x='puntaje_lectura', y='comuna')
st.pyplot()

st.header('Filtro 2: Filtrando por los colegios que tiene un mejor un poderado global superior a 100mil y los colegios a los que pertenencen')
filtro2 = data[data['ponderado_global']>100000 ]
filtro2
st.set_option('deprecation.showPyplotGlobalUse', False)
filtro2.plot.scatter(x='ponderado_global', y='establecimiento')
st.pyplot()

st.header('Filtro 3: Filtrando por los establecimientos pertenecientes a Robledo cuyo puntaje en matematicas y sociales es mayor a 60')
filtro3 = data[(data['comuna']=="robledo") & (data['puntaje_matematicas'] >60) & (data['puntaje_naturales'] >60)]
filtro3

st.header('Filtro 4: Filtrando por los establecimientos pertenecientes a Poblado cuyo puntaje en inglés es menor a 50')
filtro4 = data[(data['comuna']=="poblado") & (data['puntaje_ingles'] < 50) ]
filtro4

st.header('Filtro 5: Filtrando por los establecimientos oficiales que tuvieron un puntaje global menor a 260')
filtro5 = data[(data['prestacion_servicio']=="oficial") & (data['punt_global_med'] < 260) ]
filtro5






 