import pandas as pd
import streamlit as st
import psycopg2
from sqlalchemy import create_engine
from urllib.parse import urlparse

@st.cache_resource
def get_uri():
    return st.secrets.db_credentials.URI

@st.cache_resource
def init_connection():
    uri = get_uri()
    result = urlparse(uri)
    return psycopg2.connect(
        host=result.hostname,
        dbname=result.path[1:],
        user=result.username,
        password=result.password,
        port=result.port
    )

con = init_connection()

@st.cache_resource
def get_engine():
    return create_engine(get_uri())

sql_engine = get_engine()
