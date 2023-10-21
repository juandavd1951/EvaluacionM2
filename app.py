import pandas as pd
import streamlit as st

df = pd.read_csv('historico_resultados_pruebas_saber_11.csv') 



df_comuna = df.sort_values('codigo_dane', ascending=False)[['codigo_dane', 'comuna']]


df_registros =  df.loc[(df['registros'] >= 100) & (df['registros'] < 101)]

df_puntajeglobal = df.loc[df['puntaje_global'] >= 300, ['codigo_dane', 'puntaje_global']]
df_puntajelectura = df.loc[df['puntaje_lectura'] < 50, ['codigo_dane', 'puntaje_lectura']]
df_puntajesociales = df.loc[df['puntaje_sociales'] > 55, ['codigo_dane', 'puntaje_sociales']]


st.subheader('Tabla completa')
st.dataframe(df)

st.subheader(' filtra para mostrar la comuna y el codigo del dane')
st.dataframe(df_comuna)

st.subheader('Muestra la tabla registros que sean mayores o iguales a 100')
st.dataframe(df_registros)

st.subheader('Muestra la tabla que el puntaje sea mayor a 300')
st.dataframe(df_puntajeglobal)

st.subheader('Muestra la tabla que el puntaje de lectura sea menos a 50')
st.dataframe(df_puntajelectura)

st.subheader('Muestra la tabla que el puntaje de lectura sea mayor a 55')
st.dataframe(df_puntajesociales)