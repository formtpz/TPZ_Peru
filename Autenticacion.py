import pandas as pd
import streamlit as st
import psycopg2

uri=st.secrets.db_credentials.URI

def contraseña(usuario):

    contraseña= pd.read_sql(f"select contraseña from usuarios where usuario = '{usuario}' AND estado='Activo'",uri)
    return contraseña
@st.cache_resource
def init_connection():
    return psycopg2.connect(
        host="...",
        user="...",
        password="...",
        database="..."
    )

con = init_connection()
