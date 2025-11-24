import pandas as pd
import streamlit as st
import psycopg2
from urllib.parse import urlparse
from sqlalchemy import create_engine

uri = st.secrets.db_credentials.URI

# --- Crear engine con pool (cacheado) ---
@st.cache_resource
def get_engine():
    return create_engine(uri, pool_pre_ping=True, pool_recycle=1800)

engine = get_engine()

# --- Consulta de contraseña usando engine pool ---
def contraseña(usuario):
    query = f"""SELECT contraseña 
                FROM usuarios 
                WHERE usuario = '{usuario}' 
                  AND estado='Activo'"""
    return pd.read_sql(query, engine)
def init_connection():
    return psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

con = init_connection()

