import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 3")

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

data = {
    'nombre_completo': ['Juan Pérez', 'Ana Gómez', 'Carlos Rodríguez', 'Laura Torres', 'Pedro Díaz'],
    'edad': [25, 34, 45, 56, 33],
    'municipio': ['Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín'],
    'ingreso_mensual': [2500000, 3000000, 1000000, 5000000, 7000000],
    'ocupacion': ['Estudiante', 'Docente', 'Comerciante', 'Médico', 'Ingeniero'],
    'tipo_vivienda': ['Propia', 'Arendada', 'Propia', 'Arendada', 'Arendada'],
    'fecha_nacimiento': pd.to_datetime(['1999-03-25', '1988-07-19', '1978-02-13', '1967-11-11', '1982-05-30']),
    'acceso_internet': [True, True, False, True, True]
}

df_nuevo = pd.DataFrame(data)

# Título de la aplicación
st.title('Aplicación de Filtros Dinámicos')

# Filtro por rango de edad
st.sidebar.header('Filtros')

# Filtro de rango de edad
filtrar_edad = st.sidebar.checkbox('Filtrar por rango de edad')
if filtrar_edad:
    min_edad, max_edad = st.sidebar.slider(
        'Selecciona el rango de edad',
        min_value=15, max_value=75,
        value=(15, 75)
    )
    df_nuevo = df_nuevo[df_nuevo['edad'].between(min_edad, max_edad)]

# Filtro por municipios
filtrar_municipios = st.sidebar.checkbox('Filtrar por municipios')
if filtrar_municipios:
    municipios_seleccionados = st.sidebar.multiselect(
        'Selecciona municipio(s):',
        options=['Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín', 'Tunja', 'Manizales', 
                 'Cali', 'Quibdó', 'Buenaventura', 'Villavicencio', 'Yopal', 'Leticia', 'Puerto Inírida'],
        default=['Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín']
    )
    df_nuevo = df_nuevo[df_nuevo['municipio'].isin(municipios_seleccionados)]

# Filtro por ingreso mensual mínimo
filtrar_ingreso = st.sidebar.checkbox('Filtrar por ingreso mensual mínimo')
if filtrar_ingreso:
    ingreso_minimo = st.sidebar.slider(
        'Selecciona el ingreso mensual mínimo',
        min_value=800000, max_value=12000000,
        value=1000000
    )
    df_nuevo = df_nuevo[df_nuevo['ingreso_mensual'] > ingreso_minimo]

# Filtro por ocupación
filtrar_ocupacion = st.sidebar.checkbox('Filtrar por ocupación')
if filtrar_ocupacion:
    ocupaciones_seleccionadas = st.sidebar.multiselect(
        'Selecciona ocupación(es):',
        options=['Estudiante', 'Docente', 'Comerciante', 'Agricultor', 'Ingeniero', 'Médico', 
                 'Desempleado', 'Pensionado', 'Emprendedor', 'Obrero'],
        default=['Estudiante', 'Docente', 'Comerciante', 'Médico', 'Ingeniero']
    )
    df_nuevo = df_nuevo[df_nuevo['ocupacion'].isin(ocupaciones_seleccionadas)]

# Filtro por tipo de vivienda no propia
filtrar_vivienda = st.sidebar.checkbox('Filtrar personas sin vivienda propia')
if filtrar_vivienda:
    df_nuevo = df_nuevo[~(df_nuevo['tipo_vivienda'] == 'Propia')]

# Filtro por nombres que contienen una cadena
filtrar_nombre = st.sidebar.checkbox('Filtrar por nombre')
if filtrar_nombre:
    texto = st.sidebar.text_input('Introduce una subcadena para buscar en los nombres:')
    if texto:
        df_nuevo = df_nuevo[df_nuevo['nombre_completo'].str.contains(texto, case=False, na=False)]

# Filtro por año de nacimiento
filtrar_ano_nacimiento = st.sidebar.checkbox('Filtrar por año de nacimiento')
if filtrar_ano_nacimiento:
    año_seleccionado = st.sidebar.selectbox(
        'Selecciona el año de nacimiento:',
        options=list(range(1949, 2010))
    )
    df_nuevo = df_nuevo[df_nuevo['fecha_nacimiento'].dt.year == año_seleccionado]

# Filtro por acceso a internet
filtrar_internet = st.sidebar.checkbox('Filtrar por acceso a internet')
if filtrar_internet:
    acceso_internet = st.sidebar.radio('¿Tiene acceso a internet?', ['Sí', 'No'])
    df_nuevo = df_nuevo[df_nuevo['acceso_internet'] == (acceso_internet == 'Sí')]

# Filtro por ingresos nulos
filtrar_ingresos_nulos = st.sidebar.checkbox('Filtrar por ingresos nulos')
if filtrar_ingresos_nulos:
    df_nuevo = df_nuevo[df_nuevo['ingreso_mensual'].isnull()]

# Filtro por rango de fechas de nacimiento
filtrar_fechas_nacimiento = st.sidebar.checkbox('Filtrar por rango de fechas de nacimiento')
if filtrar_fechas_nacimiento:
    fecha_inicio = st.sidebar.date_input('Fecha de nacimiento inicial', min_value=pd.to_datetime('1949-01-01'))
    fecha_fin = st.sidebar.date_input('Fecha de nacimiento final', max_value=pd.to_datetime('2009-12-31'))
    df_nuevo = df_nuevo[df_nuevo['fecha_nacimiento'].between(fecha_inicio, fecha_fin)]

# Mostrar los datos filtrados
st.write('Datos filtrados:')
st.dataframe(df_nuevo)