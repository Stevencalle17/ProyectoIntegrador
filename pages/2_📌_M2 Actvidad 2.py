import streamlit as st
import pandas as pd
import io

st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

df = pd.read_csv("estudiantes_colombia.csv")

st.title("Momento 2 - Actividad 2")

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

st.title("Análisis de Estudiantes en Colombia")

st.subheader("Primeras 5 filas del dataset")
st.dataframe(df.head())

st.subheader("Últimas 5 filas del dataset")
st.dataframe(df.tail())

# Convertir df.info() a un DataFrame visual
st.subheader("Información general del dataset (formato tabla)")
info_df = pd.DataFrame({
    "Columna": df.columns,
    "No. de valores no nulos": df.notnull().sum().values,
    "Tipo de dato": df.dtypes.values
})
st.dataframe(info_df)

st.subheader("Resumen estadístico (describe)")
st.dataframe(df.describe())

# Selección de columnas específicas
st.subheader("Seleccionar columnas a mostrar")
columnas_seleccionadas = st.multiselect(
    "Selecciona las columnas que quieres visualizar",
    options=df.columns.tolist(),
    default=["nombre", "edad", "promedio"]
)
st.dataframe(df[columnas_seleccionadas])

# Filtro por promedio
st.subheader("Filtrar por promedio")
umbral = st.slider("Selecciona un promedio mínimo", float(df["promedio"].min()), float(df["promedio"].max()), 4.0, step=0.1)
df_filtrado = df[df["promedio"] > umbral]
st.write(f"Estudiantes con promedio mayor a {umbral}")
st.dataframe(df_filtrado)