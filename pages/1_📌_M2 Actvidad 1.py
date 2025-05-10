import streamlit as st
import pandas as pd
import sqlite3
import os
import numpy as np
# import openpyxl


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

st.write("### Productos en Inventario")
st.write("Este DataFrame se genera a partir de una lista de listas con información sobre productos.")

# Crear una lista de listas con datos de productos
productos = [
    ["Laptop", 1200, 15],
    ["Mouse", 25, 100],
    ["Teclado", 45, 50],
    ["Monitor", 300, 20]
]

# Convertir la lista de listas en un DataFrame con nombres de columnas
df_productos = pd.DataFrame(productos, columns=["Producto", "Precio (USD)", "Stock"])

# Mostrar el DataFrame en Streamlit
st.dataframe(df_productos)

# Descripción
st.write("### Datos de Personas")
st.write("Este DataFrame se genera combinando Series individuales de nombres, edades y ciudades.")

# Crear Series individuales
nombres = pd.Series(["Ana", "Carlos", "Elena", "Luis"])
edades = pd.Series([25, 32, 29, 40])
ciudades = pd.Series(["Madrid", "Bogotá", "Ciudad de México", "Buenos Aires"])

# Combinar Series en un diccionario y convertirlo en DataFrame
df_personas = pd.DataFrame({
    "Nombre": nombres,
    "Edad": edades,
    "Ciudad": ciudades
})

# Mostrar el DataFrame en Streamlit
st.dataframe(df_personas)

# Datos de ejemplo
data = {
    "id": [1, 2, 3],
    "nombre": ["Producto A", "Producto B", "Producto C"],
    "valor": [100, 200, 150]
}

# Convertir a DataFrame y guardar como CSV
df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)


st.write("### Datos desde CSV")


# Leer el archivo CSV creado anteriormente
df_csv = pd.read_csv("data.csv")
st.dataframe(df_csv)



st.write("### Datos desde Excel")

    # Datos de ejemplo
data = {
    "producto": ["Mouse", "Teclado", "Monitor"],
    "precio": [25.99, 45.50, 199.99],
    "stock": [100, 50, 20]
}

# Crear el DataFrame y guardarlo como archivo Excel
df = pd.DataFrame(data)
df.to_excel("static/data.xlsx", index=False, engine="openpyxl")

df_excel = pd.read_excel("data.xlsx", engine="openpyxl")
st.dataframe(df_excel)



st.write("### Datos de Usuarios desde JSON")

df_json = pd.read_json("data.json")
st.dataframe(df_json)  

st.write("### Datos desde URL")

csv_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"


df_url = pd.read_csv(csv_url)
st.dataframe(df_url.head(10))  # Mostrar las primeras 10 filas

st.write("### Datos desde SQLite")

# Crear conexión a la base de datos
db_name = "estudiantes.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS estudiantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        calificacion REAL NOT NULL
    )
""")

# Insertar datos si la tabla está vacía
cursor.execute("SELECT COUNT(*) FROM estudiantes")
if cursor.fetchone()[0] == 0:
    datos = [
        ("Ana", 8.5),
        ("Luis", 9.0),
        ("Carlos", 7.8)
    ]
    cursor.executemany("INSERT INTO estudiantes (nombre, calificacion) VALUES (?, ?)", datos)
    conn.commit()

# Leer datos con Pandas
df_sql = pd.read_sql("SELECT * FROM estudiantes", conn)

# Mostrar en Streamlit
st.dataframe(df_sql)

# Cerrar la conexión
conn.close()

st.write("### Datos desde Numpy")

# Crear un array 3x3 con datos numéricos
array = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Convertir el array a DataFrame
df_numpy = pd.DataFrame(array, columns=["Columna A", "Columna B", "Columna C"])

# Mostrar en Streamlit
st.dataframe(df_numpy)

