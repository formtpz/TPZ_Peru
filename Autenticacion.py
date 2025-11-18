import pandas as pd
import streamlit as st
import psycopg2
from urllib.parse import urlparse

uri=st.secrets.db_credentials.URI

def contraseña(usuario):

    contraseña= pd.read_sql(f"select contraseña from usuarios where usuario = '{usuario}' AND estado='Activo'",uri)
    return contraseña


result = urlparse(uri)
hostname = result.hostname
database = result.path[1:]
username = result.username
pwd = result.password
port_id = result.port

@st.cache_resource
def init_connection():
    return psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

con = init_connection()
