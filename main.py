import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np



titulo = st.sidebar.title("Sevici Visualization app")
image = Image.open('bicicleta.jpg')
menu = st.sidebar.image(image)
menu = st.sidebar.selectbox("Menu", ["Home", "Problemas de negocio", "Datos", "Visualizacion","Filtrado","BONUS",])
df = pd.read_csv("sevicidist.csv", index_col=0)


if menu == "Home":
    st.title("Bienvenidos a Sevici Visualization app")
    st.subheader('Obtencion de datos')
    st.write("""Los datos vendrán extraidos a traves de la API de OpenStreetMap: OverPass

Utilizaremos la libreria request utilizando como url la api de Overpass: "https://lz4.overpass-api.de/api/interpreter"

La query que utilizaremos sera la siguiente :


overpass_query = '''
[out:json];node[amenity=bicycle_rental]
(37.3582,-7,37.4428,-5.8599);out;'''

Para investigar un poco mas sobre como construir queries para la api Overpass consultar este enlace

Los datos que nos interasan seran: Longitud, Latitud, Capacidad y el Nombre de la Calle que nos devolverá la api tal que:""")




elif menu == "Problemas de negocio":
    print("hola")

elif menu == "Datos":

    st.metric(label="Numero total de bicis Sevici en Sevilla", value=4841, delta=20,
    delta_color="inverse")
    df = pd.read_csv("sevicidist.csv", index_col=0)
    st.dataframe(df)
    st.subheader('Capacidad por distrito')

    chart_data = pd.DataFrame(
    {'Distrito 1': 1281, 'Distrito 2': 1280, 'Distrito 3': 1175, 'Distrito 4': 1105}, columns=["capacity"])

    st.bar_chart(chart_data)

elif menu == "Visualizacion":
    st.map(df)

elif menu == "Filtrado": 
    genre = st.sidebar.radio(
    "Seleccione una opción de filtro",
    ('Calle', 'Capacidad & Distrito'))

    if genre == 'Calle':
        option = st.sidebar.selectbox("Calles", df.iloc[:, [2]])
        first_row = df.iloc[:1]
        st.dataframe(first_row)
        st.map(first_row)
    if genre == 'Capacidad & Distrito':
        genre1 = st.sidebar.radio("Capacidades", ('<20', '>=20'))
        genre2 = st.sidebar.radio("Distritos", ('1', '2', '3', '4'))

        if genre1 == "<20" and genre2 =="1":
            menos_20 = df.loc[(df["CAPACITY"] < 20) & (df["Distrito"] == 1)]
            st.map(menos_20)
            st.dataframe(menos_20)
        if genre1 == "<20" and genre2 =="2":
            menos_201 = df.loc[(df["CAPACITY"] < 20) & (df["Distrito"] == 2)]
            st.map(menos_201)
            st.dataframe(menos_201)
        if genre1 == "<20" and genre2 =="3":
            menos_202 = df.loc[(df["CAPACITY"] < 20) & (df["Distrito"] == 3)]
            st.map(menos_202)
            st.dataframe(menos_202)
        if genre1 == "<20" and genre2 =="4":
            menos_203 = df.loc[(df["CAPACITY"] < 20) & (df["Distrito"] == 4)]
            st.map(menos_203)
            st.dataframe(menos_203)
        if genre1 == ">=20" and genre2 =="1":
            menos_204 = df.loc[(df["CAPACITY"] >= 20) & (df["Distrito"] == 1)]
            st.map(menos_204)
            st.dataframe(menos_204)
        if genre1 == ">=20" and genre2 =="2":
            menos_205 = df.loc[(df["CAPACITY"] >= 20) & (df["Distrito"] == 2)]
            st.map(menos_205)
            st.dataframe(menos_205)
        if genre1 == ">=20" and genre2 =="3":
            menos_206 = df.loc[(df["CAPACITY"] >= 20) & (df["Distrito"] == 3)]
            st.map(menos_206)
            st.dataframe(menos_206)
        if genre1 == ">=20" and genre2 =="4":
            menos_207 = df.loc[(df["CAPACITY"] >= 20) & (df["Distrito"] == 4)]
            st.map(menos_207)
            st.dataframe(menos_207)
        

        
elif menu == "BONUS":
    st.write("Logica de la pestaña 3")