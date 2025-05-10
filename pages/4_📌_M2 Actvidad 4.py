import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 4")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")

df = pd.read_csv("musica_electronica.csv") 


st.title("🎧 Explorador de Música Electrónica")
st.write("Usa los filtros y controles para explorar y modificar datos sobre canciones electrónicas.")

st.subheader("🎵 DataFrame Original")
st.dataframe(df)

st.sidebar.header("🎚️ Controles de Exploración")

# Filtro por género usando .loc
genero = st.sidebar.selectbox("Selecciona un género", df['Género'].unique())
filtrado_genero = df.loc[df['Género'] == genero]
st.write(f"Canciones del género **{genero}**")
st.dataframe(filtrado_genero)

# Filtro por año usando .loc
anio_min, anio_max = st.sidebar.slider("Rango de años", min_value=1990, max_value=2022, value=(2000, 2020))
filtrado_anio = df.loc[(df['Año'] >= anio_min) & (df['Año'] <= anio_max)]
st.write(f"Canciones entre los años {anio_min} y {anio_max}")
st.dataframe(filtrado_anio)

# Selección de fila por índice con .iloc
st.sidebar.header("🔍 Selección por Índice")
index = st.sidebar.number_input("Índice de canción", min_value=0, max_value=len(df)-1, step=1)
fila = df.iloc[index]
st.write("🎯 Canción seleccionada por índice:")
st.write(fila)

# Modificación usando .loc
st.sidebar.header("✏️ Modificación de Datos")
indice_mod = st.sidebar.number_input("Índice para modificar", min_value=0, max_value=len(df)-1, step=1)
columna_mod = st.sidebar.selectbox("Columna a modificar", df.columns)
nuevo_valor = st.sidebar.text_input("Nuevo valor")

if nuevo_valor:
    df.loc[indice_mod, columna_mod] = nuevo_valor
    st.success(f"Se actualizó la fila {indice_mod} en la columna {columna_mod}")
    st.write(df.loc[indice_mod])

# Mostrar DataFrame actualizado
st.subheader("📊 DataFrame Actualizado")
st.dataframe(df)

