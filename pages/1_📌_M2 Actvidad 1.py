import streamlit as st
import pandas as pd
# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

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

# Título de la aplicación
st.title("Actividad 1 - Creación de DataFrames")

# Descripción de la actividad
st.write("En esta actividad, aprenderemos a crear y manipular DataFrames en Streamlit usando pandas.")

# Descripción de la actividad
st.write("En esta sección, crearemos un DataFrame a partir de un diccionario con información sobre libros.")

# Crear un diccionario con datos de libros
libros = {
    "Título": ["Cien años de soledad", "El principito", "1984", "Moby Dick"],
    "Autor": ["Gabriel García Márquez", "Antoine de Saint-Exupéry", "George Orwell", "Herman Melville"],
    "Año de Publicación": [1967, 1943, 1949, 1851],
    "Género": ["Realismo mágico", "Infantil", "Distopía", "Aventura"]
}

# Convertir el diccionario en un DataFrame
df_libros = pd.DataFrame(libros)

# Mostrar texto descriptivo
st.write("### DataFrame de Libros")

# Mostrar el DataFrame en la interfaz de Streamlit
st.dataframe(df_libros)


# Descripción de la actividad
st.write("En esta sección, crearemos un DataFrame a partir de una lista de diccionarios con información sobre ciudades.")

# Crear una lista de diccionarios con datos de ciudades
ciudades = [
    {"Nombre": "Buenos Aires", "Población": 2891000, "País": "Argentina"},
    {"Nombre": "Madrid", "Población": 3266000, "País": "España"},
    {"Nombre": "Ciudad de México", "Población": 9209944, "País": "México"},
    {"Nombre": "Bogotá", "Población": 7743955, "País": "Colombia"}
]

# Convertir la lista de diccionarios en un DataFrame
df_ciudades = pd.DataFrame(ciudades)

# Mostrar texto descriptivo
st.write("### Información de Ciudades")

# Mostrar el DataFrame en la interfaz de Streamlit
st.dataframe(df_ciudades)
