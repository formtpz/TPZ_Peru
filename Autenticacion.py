import pandas as pd
import streamlit as st
import psycopg2
from sqlalchemy import create_engine # <--- NUEVA IMPORTACIÓN
from urllib.parse import urlparse

uri = st.secrets.db_credentials.URI

# --- MANTENER ESTO PARA LOS INSERTS (Precampo.py, etc.) ---
result = urlparse(uri)
hostname = result.hostname
database = result.path[1:]
username = result.username
pwd = result.password
port_id = result.port

@st.cache_resource
def init_connection():
    return psycopg2.connect(host=hostname, dbname=database, user=username, password=pwd, port=port_id)

con = init_connection()

# --- AGREGAR ESTO PARA PANDAS (Historial.py, Ingreso.py) ---
@st.cache_resource
def get_engine():
    # SQLAlchemy maneja la reconexión automáticamente
    return create_engine(uri)

sql_engine = get_engine() # <--- Variable que exportaremos
