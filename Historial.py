# ----- Librerías ---- #
import numpy as np
import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
import pytz
import plotly.graph_objects as go
import plotly.express as px
from urllib.parse import urlparse
uri=st.secrets.db_credentials.URI
import Procesos,Capacitacion,Otros_Registros,Bonos,Salir

def Historial(usuario,puesto):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_7= st.sidebar.empty()
  titulo= placeholder1_7.title("Menú")

  placeholder2_7 = st.sidebar.empty()
  procesos_7 = placeholder2_7.button("Procesos",key="procesos_7")

  placeholder3_7 = st.sidebar.empty()
  capacitacion_7 = placeholder3_7.button("Capacitaciones",key="capacitacion_7")

  placeholder4_7 = st.sidebar.empty()
  otros_registros_7 = placeholder4_7.button("Otros Registros",key="otros_registros_7")

  placeholder5_7 = st.sidebar.empty()
  bonos_7 = placeholder5_7.button("Bonos",key="bonos_7")

  placeholder6_7 = st.sidebar.empty()
  salir_7 = placeholder6_7.button("Salir",key="salir_7")

  placeholder7_7 = st.empty()
  historial_7 = placeholder7_7.title("Historial")

  default_date_7 = datetime.now(pytz.timezone('America/Guatemala'))

  placeholder8_7 = st.empty()
  fecha_de__inicio_7 = placeholder8_7.date_input("Fecha de Inicio",value=default_date_7,key="fecha_de_inicio_7")

  placeholder9_7 = st.empty()
  fecha_de__finalizacion_7 = placeholder9_7.date_input("Fecha de Finalización",value=default_date_7,key="fecha_de_finalizacion_7")
  
  nombre_7= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
  nombre_7 = nombre_7.loc[0,'nombre']

  # ----- Supervisor y Coordinador ---- #

  if puesto=="Supervisor" or puesto=="Coordinador":    

    placeholder10_7 = st.empty()
    personal_7 = placeholder10_7.selectbox("Personal", options=("Todos","Operarios","Propio","Personal Asignado"), key="filtro_7")

    placeholder11_7 = st.empty()
    proceso_7_s = placeholder11_7.selectbox("Proceso", options=("Todos","Conformación","Control de Calidad Conformación","Información Final I","Control de Calidad IF I","Información Final II","Información Final III","Digitalización de Planos","Sectores Circulares"), key="proceso_7_s")
    
    placeholder12_7 = st.empty()
    tipo_7_s = placeholder12_7.selectbox("Tipo", options=("Todos","Ordinario","Corrección Georreferenciación","Corrección Primera Revisión","Corrección Primera Reinspección"), key="tipo_7_s")

    if personal_7=="Todos" and proceso_7_s=="Todos" and tipo_7_s=="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      data_1_c = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,tema,cast(horas as float),reporte from capacitaciones where fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_c = data_1_c.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

      data_1_o = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,cast(horas as float),observaciones,reporte from otros_registros where fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_o = data_1_o.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

    elif personal_7=="Todos" and proceso_7_s=="Todos" and tipo_7_s!="Todos":
        
      if tipo_7_s=="Ordinario":
        
        data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where (tipo='Ordinario' or tipo='Georreferenciación' or tipo='Afectados' or tipo='No Aplica') and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        
      else:

        data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where tipo='{tipo_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      data_1_c = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,tema,cast(horas as float),reporte from capacitaciones where fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_c = data_1_c.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

      data_1_o = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,cast(horas as float),observaciones,reporte from otros_registros where fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_o = data_1_o.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

    elif personal_7=="Todos" and proceso_7_s !="Todos" and tipo_7_s=="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      data_1_c = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,tema,cast(horas as float),reporte from capacitaciones where fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_c = data_1_c.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

      data_1_o = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,cast(horas as float),observaciones,reporte from otros_registros where fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_o = data_1_o.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

    elif personal_7=="Todos" and proceso_7_s !="Todos" and tipo_7_s!="Todos":

      if tipo_7_s=="Ordinario":

        data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where proceso='{proceso_7_s}' and (tipo='Ordinario' or tipo='Georreferenciación' or tipo='Afectados' or tipo='No Aplica') and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
    
      else:

        data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where proceso='{proceso_7_s}' and tipo='{tipo_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      data_1_c = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,tema,cast(horas as float),reporte from capacitaciones where fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_c = data_1_c.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

      data_1_o = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,cast(horas as float),observaciones,reporte from otros_registros where fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_o = data_1_o.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

    elif personal_7=="Operarios" and proceso_7_s =="Todos" and tipo_7_s=="Todos":
       
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where puesto='Operario Catastral' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      data_1_c = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,tema,cast(horas as float),reporte from capacitaciones where puesto='Operario Catastral' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_c = data_1_c.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

      data_1_o = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,cast(horas as float),observaciones,reporte from otros_registros where puesto='Operario Catastral' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_o = data_1_o.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

    elif personal_7=="Operarios" and proceso_7_s =="Todos" and tipo_7_s!="Todos":
        
      if tipo_7_s=="Ordinario":

        data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where puesto='Operario Catastral' and (tipo='Ordinario' or tipo='Georreferenciación' or tipo='Afectados' or tipo='No Aplica') and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      else:

        data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where puesto='Operario Catastral' and tipo='{tipo_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      data_1_c = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,tema,cast(horas as float),reporte from capacitaciones where puesto='Operario Catastral' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_c = data_1_c.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

      data_1_o = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,cast(horas as float),observaciones,reporte from otros_registros where puesto='Operario Catastral' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_o = data_1_o.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

    elif personal_7=="Operarios" and proceso_7_s !="Todos" and tipo_7_s=="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where puesto='Operario Catastral' and proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      data_1_c = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,tema,cast(horas as float),reporte from capacitaciones where puesto='Operario Catastral' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_c = data_1_c.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

      data_1_o = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,cast(horas as float),observaciones,reporte from otros_registros where puesto='Operario Catastral' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_o = data_1_o.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

    elif personal_7=="Operarios" and proceso_7_s !="Todos" and tipo_7_s!="Todos":
        
      if tipo_7_s=="Ordinario":

        data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where puesto='Operario Catastral' and (tipo='Ordinario' or tipo='Georreferenciación' or tipo='Afectados' or tipo='No Aplica') and proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      else:
    
        data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where puesto='Operario Catastral' and tipo='{tipo_7_s}' and proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      data_1_c = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,tema,cast(horas as float),reporte from capacitaciones where puesto='Operario Catastral' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_c = data_1_c.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

      data_1_o = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,cast(horas as float),observaciones,reporte from otros_registros where puesto='Operario Catastral' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_o = data_1_o.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

    elif personal_7=="Propio" and proceso_7_s=="Todos" and tipo_7_s=="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      data_1_c = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,tema,cast(horas as float),reporte from capacitaciones where usuario='{usuario}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_c = data_1_c.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

      data_1_o = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,cast(horas as float),observaciones,reporte from otros_registros where usuario='{usuario}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_o = data_1_o.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

    elif personal_7=="Propio" and proceso_7_s=="Todos" and tipo_7_s!="Todos":
        
      if tipo_7_s=="Ordinario":

        data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and (tipo='Ordinario' or tipo='Georreferenciación' or tipo='Afectados' or tipo='No Aplica') and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      else:
        
        data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and tipo='{tipo_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      data_1_c = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,tema,cast(horas as float),reporte from capacitaciones where usuario='{usuario}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_c = data_1_c.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

      data_1_o = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,cast(horas as float),observaciones,reporte from otros_registros where usuario='{usuario}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_o = data_1_o.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

    elif personal_7=="Propio" and proceso_7_s !="Todos" and tipo_7_s=="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      data_1_c = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,tema,cast(horas as float),reporte from capacitaciones where usuario='{usuario}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_c = data_1_c.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

      data_1_o = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,cast(horas as float),observaciones,reporte from otros_registros where usuario='{usuario}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_o = data_1_o.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

    elif personal_7=="Propio" and proceso_7_s !="Todos" and tipo_7_s!="Todos":
        
      if tipo_7_s=="Ordinario":
           
        data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and (tipo='Ordinario' or tipo='Georreferenciación' or tipo='Afectados' or tipo='No Aplica') and proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      else:
        
        data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and tipo='{tipo_7_s}' and proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      data_1_c = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,tema,cast(horas as float),reporte from capacitaciones where usuario='{usuario}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_c = data_1_c.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

      data_1_o = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,cast(horas as float),observaciones,reporte from otros_registros where usuario='{usuario}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_o = data_1_o.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

    elif personal_7=="Personal Asignado" and proceso_7_s =="Todos" and tipo_7_s=="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where supervisor='{nombre_7}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        
      data_1_c = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,tema,cast(horas as float),reporte from capacitaciones where supervisor='{nombre_7}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_c = data_1_c.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

      data_1_o = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,cast(horas as float),observaciones,reporte from otros_registros where supervisor='{nombre_7}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_o = data_1_o.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

    elif personal_7=="Personal Asignado" and proceso_7_s =="Todos" and tipo_7_s!="Todos":
        
      if tipo_7_s=="Ordinario":
           
        data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and (tipo='Ordinario' or tipo='Georreferenciación' or tipo='Afectados' or tipo='No Aplica') and proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      else:
        
        data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where supervisor='{nombre_7}' and tipo='{tipo_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      data_1_c = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,tema,cast(horas as float),reporte from capacitaciones where supervisor='{nombre_7}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_c = data_1_c.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

      data_1_o = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,cast(horas as float),observaciones,reporte from otros_registros where supervisor='{nombre_7}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_o = data_1_o.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

    elif personal_7=="Personal Asignado" and proceso_7_s !="Todos" and tipo_7_s=="Todos":
       
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where supervisor='{nombre_7}' and proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
    
      data_1_c = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,tema,cast(horas as float),reporte from capacitaciones where supervisor='{nombre_7}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_c = data_1_c.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

      data_1_o = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,cast(horas as float),observaciones,reporte from otros_registros where supervisor='{nombre_7}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_o = data_1_o.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

    elif personal_7=="Personal Asignado" and proceso_7_s !="Todos" and tipo_7_s!="Todos":
        
      if tipo_7_s=="Ordinario":

        data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where supervisor='{nombre_7}' and (tipo='Ordinario' or tipo='Georreferenciación' or tipo='Afectados' or tipo='No Aplica') and proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      else:
     
        data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where supervisor='{nombre_7}' and tipo='{tipo_7_s}' and proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      data_1_c = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,tema,cast(horas as float),reporte from capacitaciones where supervisor='{nombre_7}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_c = data_1_c.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

      data_1_o = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,cast(horas as float),observaciones,reporte from otros_registros where supervisor='{nombre_7}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_o = data_1_o.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

    # ----- Reportes ---- #

    placeholder13_7 = st.empty()
    reportes_7=placeholder13_7.subheader("Reportes")   

    pivot_reportes=len(data_1_r.iloc[:,0])

    if pivot_reportes==0:
       
      placeholder14_7 = st.empty()
      error_reportes= placeholder14_7.error('No existen reportes para mostrar')

    else:

      placeholder15_7 = st.empty()
      historial_7_reportes=placeholder15_7.dataframe(data=data_1_r)

      placeholder16_7 = st.empty()
      descarga_7_reportes = placeholder16_7.download_button("Decargar CSV",data=data_1_r.to_csv(),mime="text/csv",key="descarga_7_reportes")

    # ----- Resumen de Horas ---- #

    placeholder17_7 = st.empty()
    horas_7=placeholder17_7.subheader("Resumen de Horas")  

    data_2_r = data_1_r.groupby(["nombre", "fecha"], as_index=False)[["predios","horas"]].agg(np.sum)
  
    pivot_r=len(data_2_r.iloc[:,0])
    pivot_c=len(data_2_c.iloc[:,0])
    pivot_o=len(data_2_o.iloc[:,0])
    
    if pivot_r==0 and pivot_c==0 and pivot_o==0:
       
      placeholder18_7 = st.empty()
      error_horas= placeholder18_7.error('No existen horas para mostrar')

    else:
      
      nombre_r=data_2_r.iloc[:,0]
      nombre_c=data_2_c.iloc[:,0]
      nombre_o=data_2_o.iloc[:,0]

      nombre_horas= pd.concat([nombre_r,nombre_c])
      nombre_horas= pd.concat([nombre_horas,nombre_o])

      fecha_r=data_2_r.iloc[:,1]
      fecha_c=data_2_c.iloc[:,1]
      fecha_o=data_2_o.iloc[:,1]

      fecha_horas=pd.concat([fecha_r,fecha_c])
      fecha_horas=pd.concat([fecha_horas,fecha_o])

      datos_horas = pd.DataFrame(data={"Nombre":nombre_horas,"Fecha":fecha_horas}).groupby(["Nombre","Fecha"],as_index=False).size()

      datos_horas["Horas_Producción"] = 0.0000
      datos_horas["Horas_Capacitación"] = 0.0000
      datos_horas["Horas_Otros_Registros"] = 0.0000

      for i in range(len(datos_horas)):
          
          for j in range(len(data_2_r)):
              if datos_horas.iloc[i,0] == data_2_r.iloc[j,0] and datos_horas.iloc[i,1] == data_2_r.iloc[j,1]:
                  datos_horas.iloc[i,3] = data_2_r.iloc[j,3]

          for l in range(len(data_2_c)):
              if datos_horas.iloc[i,0] == data_2_c.iloc[l,0] and datos_horas.iloc[i,1] == data_2_c.iloc[l,1]:
                  datos_horas.iloc[i,4] = data_2_c.iloc[l,2]

          for n in range(len(data_2_o)):
              if datos_horas.iloc[i,0] == data_2_o.iloc[n,0] and datos_horas.iloc[i,1] == data_2_o.iloc[n,1]:
                  datos_horas.iloc[i,5] = data_2_o.iloc[n,2]

      datos_horas["Total"]= datos_horas.iloc[:,3:6].sum(axis=1)

      placeholder19_7 = st.empty()
      historial_7_horas= placeholder19_7.dataframe(data=datos_horas)

      placeholder20_7 = st.empty()
      descarga_7_horas = placeholder20_7.download_button("Decargar CSV",data=datos_horas.to_csv(),mime="text/csv",key="descarga_7_horas")

    # ----- Resumen de Producción ---- #

    placeholder21_7 = st.empty()
    producción_7=placeholder21_7.subheader("Resumen de Producción")  

    data_2_r = data_1_r.groupby(["nombre", "fecha"], as_index=False)[["predios","horas"]].agg(np.sum)

    if pivot_r==0:  

      placeholder22_7 = st.empty()
      error_producción= placeholder22_7.error('No existe producción para mostrar')

    else:
         
      placeholder23_7 = st.empty()
      historial_7_producción= placeholder23_7.dataframe(data=data_2_r)

      placeholder24_7 = st.empty()
      descarga_7_producción = placeholder24_7.download_button("Decargar CSV",data=data_2_r.to_csv(),mime="text/csv",key="descarga_7_producción")
    
      nombre_producción=data_2_r.iloc[:,0]
      fecha_producción=data_2_r.iloc[:,1]
      predio_producción=data_2_r.iloc[:,2]
      datos_producción = pd.DataFrame(data={'Nombre':nombre_producción, 'Fecha':fecha_producción,'Producción':predio_producción})
      lista_nombres = datos_producción["Nombre"].unique().tolist()

      placeholder25_7 = st.empty()
      nombres= placeholder25_7.multiselect("Seleccionar",lista_nombres)

      datos_producción_pivot = {nombre: datos_producción[datos_producción["Nombre"] == nombre] for nombre in nombres}
      fig_producción = go.Figure()
      for nombre, datos_producción in datos_producción_pivot.items():
        fig_producción = fig_producción.add_trace(go.Scatter(x=datos_producción["Fecha"], y=datos_producción["Producción"], name=nombre))

      placeholder26_7 = st.empty()
      grafico_producción= placeholder26_7.plotly_chart(fig_producción)
      
    # ----- Total ---- #

    data_3_r= data_1_r.groupby(["fecha","proceso"], as_index=False)["predios"].agg(np.sum)

    placeholder27_7 = st.empty()
    total_7=placeholder27_7.subheader("Totales")

    if pivot_r==0:
         
      placeholder28_7 = st.empty()
      error_total_producción= placeholder28_7.error('No existe producción para mostrar')

    else:
         
      fig_producción_total = px.bar(data_3_r, x="fecha", y="predios", text="predios", color="proceso", barmode="group")
      fig_producción_total.update_traces(textposition="outside")
      placeholder29_7 = st.empty()
      grafico_producción_total= placeholder29_7.plotly_chart(fig_producción_total)

    if pivot_r==0 and pivot_c==0 and pivot_o==0:
       
      placeholder30_7 = st.empty()
      error_horas_total = placeholder30_7.error('No existen horas para mostrar')

    else:
         
      fig_horas_total_1=px.bar(datos_horas,x="Fecha", y=["Horas_Producción","Horas_Capacitación","Horas_Otros_Registros"],barmode="group")
      placeholder31_7 = st.empty()
      grafico_horas_total_1= placeholder31_7.plotly_chart(fig_horas_total_1)
      
      fig_horas_total_2=px.bar(datos_horas,x="Fecha", y=["Horas_Producción","Horas_Capacitación","Horas_Otros_Registros"])

      placeholder32_7 = st.empty()
      grafico_horas_total_2 = placeholder32_7.plotly_chart(fig_horas_total_2)

  # ----- Operario Catastral ---- #

  elif puesto=="Operario Catastral":

    placeholder33_7 = st.empty()
    proceso_7_o= placeholder33_7.selectbox("Proceso", options=("Todos","Conformación","Control de Calidad Conformación","Información Final I","Control de Calidad IF I","Información Final II","Información Final III","Digitalización de Planos","Sectores Circulares"), key="proceso_7_o")

    placeholder34_7 = st.empty()
    tipo_7_o = placeholder34_7.selectbox("Tipo", options=("Todos","Ordinario","Corrección Primera Revisión","Corrección Primera Reinspección"), key="tipo_7_o")    

    if proceso_7_o =="Todos" and tipo_7_o=="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      
      data_1_c = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,tema,cast(horas as float),reporte from capacitaciones where usuario='{usuario}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_c = data_1_c.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

      data_1_o = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,cast(horas as float),observaciones,reporte from otros_registros where usuario='{usuario}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_o = data_1_o.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

    elif proceso_7_o =="Todos" and tipo_7_o!="Todos":

      if tipo_7_o=="Ordinario":

        data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and (tipo='Ordinario' or tipo='Georreferenciación' or tipo='Afectados' or tipo='No Aplica') and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      else:
        
        data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and tipo='{tipo_7_o}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      data_1_c = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,tema,cast(horas as float),reporte from capacitaciones where usuario='{usuario}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_c = data_1_c.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

      data_1_o = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,cast(horas as float),observaciones,reporte from otros_registros where usuario='{usuario}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_o = data_1_o.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

    elif proceso_7_o !="Todos" and tipo_7_o=="Todos":
        
      data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and proceso='{proceso_7_o}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      data_1_c = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,tema,cast(horas as float),reporte from capacitaciones where usuario='{usuario}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_c = data_1_c.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

      data_1_o = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,cast(horas as float),observaciones,reporte from otros_registros where usuario='{usuario}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_o = data_1_o.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

    elif proceso_7_o !="Todos" and tipo_7_o!="Todos":

      if tipo_7_o=="Ordinario":

        data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and proceso='{proceso_7_o}' and (tipo='Ordinario' or tipo='Georreferenciación' or tipo='Afectados' or tipo='No Aplica') and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      else:
        
        data_1_r=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and proceso='{proceso_7_o}' and tipo='{tipo_7_o}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

      data_1_c = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,tema,cast(horas as float),reporte from capacitaciones where usuario='{usuario}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_c = data_1_c.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

      data_1_o = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,cast(horas as float),observaciones,reporte from otros_registros where usuario='{usuario}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2_o = data_1_o.groupby(["nombre", "fecha"], as_index=False)["horas"].agg(np.sum)

    # ----- Reportes ---- #

    placeholder35_7 = st.empty()
    reportes_7=placeholder35_7.subheader("Reportes")   

    pivot_reportes=len(data_1_r.iloc[:,0])

    if pivot_reportes==0:
       
      placeholder36_7 = st.empty()
      error_reportes= placeholder36_7.error('No existen reportes para mostrar')

    else:

      placeholder37_7 = st.empty()
      historial_7_reportes=placeholder37_7.dataframe(data=data_1_r)

      placeholder38_7 = st.empty()
      descarga_7_reportes = placeholder38_7.download_button("Decargar CSV",data=data_1_r.to_csv(),mime="text/csv",key="descarga_7_reportes")

    # ----- Resumen de Horas ---- #

    placeholder39_7 = st.empty()
    horas_7=placeholder39_7.subheader("Resumen de Horas")  

    data_2_r = data_1_r.groupby(["nombre", "fecha"], as_index=False)[["predios","horas"]].agg(np.sum)
  
    pivot_r=len(data_2_r.iloc[:,0])
    pivot_c=len(data_2_c.iloc[:,0])
    pivot_o=len(data_2_o.iloc[:,0])
    
    if pivot_r==0 and pivot_c==0 and pivot_o==0:
       
      placeholder40_7 = st.empty()
      error_horas= placeholder40_7.error('No existen horas para mostrar')

    else:

      nombre_r=data_2_r.iloc[:,0]
      nombre_c=data_2_c.iloc[:,0]
      nombre_o=data_2_o.iloc[:,0]

      nombre_horas= pd.concat([nombre_r,nombre_c])
      nombre_horas= pd.concat([nombre_horas,nombre_o])

      fecha_r=data_2_r.iloc[:,1]
      fecha_c=data_2_c.iloc[:,1]
      fecha_o=data_2_o.iloc[:,1]

      fecha_horas=pd.concat([fecha_r,fecha_c])
      fecha_horas=pd.concat([fecha_horas,fecha_o])

      datos_horas = pd.DataFrame(data={"Nombre":nombre_horas,"Fecha":fecha_horas}).groupby(["Nombre","Fecha"],as_index=False).size()

      datos_horas["Horas_Producción"] = 0.0000
      datos_horas["Horas_Capacitación"] = 0.0000
      datos_horas["Horas_Otros_Registros"] = 0.0000

      for i in range(len(datos_horas)):
          
          for j in range(len(data_2_r)):
              if datos_horas.iloc[i,0] == data_2_r.iloc[j,0] and datos_horas.iloc[i,1] == data_2_r.iloc[j,1]:
                  datos_horas.iloc[i,3] = data_2_r.iloc[j,3]

          for l in range(len(data_2_c)):
              if datos_horas.iloc[i,0] == data_2_c.iloc[l,0] and datos_horas.iloc[i,1] == data_2_c.iloc[l,1]:
                  datos_horas.iloc[i,4] = data_2_c.iloc[l,2]

          for n in range(len(data_2_o)):
              if datos_horas.iloc[i,0] == data_2_o.iloc[n,0] and datos_horas.iloc[i,1] == data_2_o.iloc[n,1]:
                  datos_horas.iloc[i,5] = data_2_o.iloc[n,2]

      datos_horas["Total"]= datos_horas.iloc[:,3:6].sum(axis=1)

      placeholder41_7 = st.empty()
      historial_7_horas= placeholder41_7.dataframe(data=datos_horas)

      placeholder42_7 = st.empty()
      descarga_7_horas = placeholder42_7.download_button("Decargar CSV",data=datos_horas.to_csv(),mime="text/csv",key="descarga_7_horas")

    # ----- Resumen de Producción ---- #

    placeholder43_7 = st.empty()
    producción_7=placeholder43_7.subheader("Resumen de Producción")  

    data_2_r = data_1_r.groupby(["nombre", "fecha"], as_index=False)[["predios","horas"]].agg(np.sum)

    if pivot_r==0:  

      placeholder44_7 = st.empty()
      error_producción= placeholder44_7.error('No existe producción para mostrar')

    else:
         
      placeholder45_7 = st.empty()
      historial_7_producción= placeholder45_7.dataframe(data=data_2_r)

      placeholder46_7 = st.empty()
      descarga_7_producción = placeholder46_7.download_button("Decargar CSV",data=data_2_r.to_csv(),mime="text/csv",key="descarga_7_producción")
    
      nombre_producción=data_2_r.iloc[:,0]
      fecha_producción=data_2_r.iloc[:,1]
      predio_producción=data_2_r.iloc[:,2]
      datos_producción = pd.DataFrame(data={'Nombre':nombre_producción, 'Fecha':fecha_producción,'Producción':predio_producción})
      lista_nombres = datos_producción["Nombre"].unique().tolist()

      placeholder47_7 = st.empty()
      nombres= placeholder47_7.multiselect("Seleccionar",lista_nombres)

      datos_producción_pivot = {nombre: datos_producción[datos_producción["Nombre"] == nombre] for nombre in nombres}
      fig_producción = go.Figure()
      for nombre, datos_producción in datos_producción_pivot.items():
        fig_producción = fig_producción.add_trace(go.Scatter(x=datos_producción["Fecha"], y=datos_producción["Producción"], name=nombre))

      placeholder48_7 = st.empty()
      grafico_producción= placeholder48_7.plotly_chart(fig_producción)


    # ----- Total ---- #

    data_3_r= data_1_r.groupby(["fecha","proceso"], as_index=False)["predios"].agg(np.sum)

    placeholder49_7 = st.empty()
    total_7=placeholder49_7.subheader("Totales")

    if pivot_r==0:
         
      placeholder50_7 = st.empty()
      error_total_producción= placeholder50_7.error('No existe producción para mostrar')

    else:
         
      fig_producción_total = px.bar(data_3_r, x="fecha", y="predios", text="predios", color="proceso", barmode="group")
      fig_producción_total.update_traces(textposition="outside")
      placeholder51_7 = st.empty()
      grafico_producción_total= placeholder51_7.plotly_chart(fig_producción_total)

    if pivot_r==0 and pivot_c==0 and pivot_o==0:
       
      placeholder52_7 = st.empty()
      error_horas_total = placeholder52_7.error('No existen horas para mostrar')

    else:
         
      fig_horas_total_1=px.bar(datos_horas,x="Fecha", y=["Horas_Producción","Horas_Capacitación","Horas_Otros_Registros"],barmode="group")
      placeholder53_7 = st.empty()
      grafico_horas_total_1= placeholder53_7.plotly_chart(fig_horas_total_1)
      
      fig_horas_total_2=px.bar(datos_horas,x="Fecha", y=["Horas_Producción","Horas_Capacitación","Horas_Otros_Registros"])

      placeholder54_7 = st.empty()
      grafico_horas_total_2 = placeholder54_7.plotly_chart(fig_horas_total_2)

  # ----- Proceso ---- #
  
  if procesos_7:
    placeholder1_7.empty()
    placeholder2_7.empty()
    placeholder3_7.empty()
    placeholder4_7.empty()
    placeholder5_7.empty()   
    placeholder6_7.empty()
    placeholder7_7.empty()
    placeholder8_7.empty()
    placeholder9_7.empty()
    
    if puesto=="Supervisor" or puesto=="Coordinador":  
      placeholder10_7.empty()
      placeholder11_7.empty()
      placeholder12_7.empty()
      placeholder13_7.empty()
      placeholder17_7.empty()
      placeholder21_7.empty()
      placeholder27_7.empty()
    
      if pivot_reportes==0:
        placeholder14_7.empty()
      
      else:
        placeholder15_7.empty()
        placeholder16_7.empty()
         
      if pivot_r==0 and pivot_c==0 and pivot_o==0:
        placeholder18_7.empty()
        placeholder30_7.empty()
        
      else:
        placeholder19_7.empty()
        placeholder20_7.empty()
        placeholder31_7.empty()
        placeholder32_7.empty()
      
      if pivot_r==0:
        placeholder22_7.empty()
        placeholder28_7.empty()

      else:
        placeholder23_7.empty()
        placeholder24_7.empty()
        placeholder25_7.empty()
        placeholder26_7.empty()
        placeholder29_7.empty()

    elif puesto=="Operario Catastral":
      placeholder33_7.empty()
      placeholder34_7.empty()
      placeholder35_7.empty()
      placeholder39_7.empty()
      placeholder43_7.empty()
      placeholder49_7.empty()

      if pivot_reportes==0:
        placeholder36_7.empty()
      
      else:
        placeholder37_7.empty()
        placeholder38_7.empty()
         
      if pivot_r==0 and pivot_c==0 and pivot_o==0:
        placeholder40_7.empty()
        placeholder52_7.empty()
        
      else:
        placeholder41_7.empty()
        placeholder42_7.empty()
        placeholder53_7.empty()
        placeholder54_7.empty()
        
      if pivot_r==0:
        placeholder44_7.empty()
        placeholder50_7.empty()

      else:
        placeholder45_7.empty()
        placeholder46_7.empty()
        placeholder47_7.empty()
        placeholder48_7.empty()
        placeholder51_7.empty()

    st.session_state.Procesos=False
    st.session_state.Historial=False

    perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
    perfil= perfil.loc[0,'perfil']

    if perfil=="1":        
                    
      Procesos.Procesos1(usuario,puesto)
                
    elif perfil=="2":        
                    
      Procesos.Procesos2(usuario,puesto)   

    elif perfil=="3":  

      Procesos.Procesos3(usuario,puesto)

  # ----- Capacitación ---- #
    
  elif capacitacion_7:
    placeholder1_7.empty()
    placeholder2_7.empty()
    placeholder3_7.empty()
    placeholder4_7.empty()
    placeholder5_7.empty()   
    placeholder6_7.empty()
    placeholder7_7.empty()
    placeholder8_7.empty()
    placeholder9_7.empty()
    
    if puesto=="Supervisor" or puesto=="Coordinador":  
      placeholder10_7.empty()
      placeholder11_7.empty()
      placeholder12_7.empty()
      placeholder13_7.empty()
      placeholder17_7.empty()
      placeholder21_7.empty()
      placeholder27_7.empty()
    
      if pivot_reportes==0:
        placeholder14_7.empty()
      
      else:
        placeholder15_7.empty()
        placeholder16_7.empty()
         
      if pivot_r==0 and pivot_c==0 and pivot_o==0:
        placeholder18_7.empty()
        placeholder30_7.empty()
        
      else:
        placeholder19_7.empty()
        placeholder20_7.empty()
        placeholder31_7.empty()
        placeholder32_7.empty()
      
      if pivot_r==0:
        placeholder22_7.empty()
        placeholder28_7.empty()

      else:
        placeholder23_7.empty()
        placeholder24_7.empty()
        placeholder25_7.empty()
        placeholder26_7.empty()
        placeholder29_7.empty()

    elif puesto=="Operario Catastral":
      placeholder33_7.empty()
      placeholder34_7.empty()
      placeholder35_7.empty()
      placeholder39_7.empty()
      placeholder43_7.empty()
      placeholder49_7.empty()

      if pivot_reportes==0:
        placeholder36_7.empty()
      
      else:
        placeholder37_7.empty()
        placeholder38_7.empty()
         
      if pivot_r==0 and pivot_c==0 and pivot_o==0:
        placeholder40_7.empty()
        placeholder52_7.empty()
        
      else:
        placeholder41_7.empty()
        placeholder42_7.empty()
        placeholder53_7.empty()
        placeholder54_7.empty()
        
      if pivot_r==0:
        placeholder44_7.empty()
        placeholder50_7.empty()

      else:
        placeholder45_7.empty()
        placeholder46_7.empty()
        placeholder47_7.empty()
        placeholder48_7.empty()
        placeholder51_7.empty()
        
    st.session_state.Historial=False
    st.session_state.Capacitacion=True
    Capacitacion.Capacitacion(usuario,puesto)

  # ----- Otros Registros ---- #
    
  elif otros_registros_7:
    placeholder1_7.empty()
    placeholder2_7.empty()
    placeholder3_7.empty()
    placeholder4_7.empty()
    placeholder5_7.empty()   
    placeholder6_7.empty()
    placeholder7_7.empty()
    placeholder8_7.empty()
    placeholder9_7.empty()
    
    if puesto=="Supervisor" or puesto=="Coordinador":  
      placeholder10_7.empty()
      placeholder11_7.empty()
      placeholder12_7.empty()
      placeholder13_7.empty()
      placeholder17_7.empty()
      placeholder21_7.empty()
      placeholder27_7.empty()
    
      if pivot_reportes==0:
        placeholder14_7.empty()
      
      else:
        placeholder15_7.empty()
        placeholder16_7.empty()
         
      if pivot_r==0 and pivot_c==0 and pivot_o==0:
        placeholder18_7.empty()
        placeholder30_7.empty()
        
      else:
        placeholder19_7.empty()
        placeholder20_7.empty()
        placeholder31_7.empty()
        placeholder32_7.empty()
      
      if pivot_r==0:
        placeholder22_7.empty()
        placeholder28_7.empty()

      else:
        placeholder23_7.empty()
        placeholder24_7.empty()
        placeholder25_7.empty()
        placeholder26_7.empty()
        placeholder29_7.empty()

    elif puesto=="Operario Catastral":
      placeholder33_7.empty()
      placeholder34_7.empty()
      placeholder35_7.empty()
      placeholder39_7.empty()
      placeholder43_7.empty()
      placeholder49_7.empty()

      if pivot_reportes==0:
        placeholder36_7.empty()
      
      else:
        placeholder37_7.empty()
        placeholder38_7.empty()
         
      if pivot_r==0 and pivot_c==0 and pivot_o==0:
        placeholder40_7.empty()
        placeholder52_7.empty()
        
      else:
        placeholder41_7.empty()
        placeholder42_7.empty()
        placeholder53_7.empty()
        placeholder54_7.empty()
        
      if pivot_r==0:
        placeholder44_7.empty()
        placeholder50_7.empty()

      else:
        placeholder45_7.empty()
        placeholder46_7.empty()
        placeholder47_7.empty()
        placeholder48_7.empty()
        placeholder51_7.empty()

    st.session_state.Historial=False
    st.session_state.Otros_Registros=True
    Otros_Registros.Otros_Registros(usuario,puesto)

  # ----- Bonos ---- #
    
  elif bonos_7:
    placeholder1_7.empty()
    placeholder2_7.empty()
    placeholder3_7.empty()
    placeholder4_7.empty()
    placeholder5_7.empty()   
    placeholder6_7.empty()
    placeholder7_7.empty()
    placeholder8_7.empty()
    placeholder9_7.empty()
    
    if puesto=="Supervisor" or puesto=="Coordinador":  
      placeholder10_7.empty()
      placeholder11_7.empty()
      placeholder12_7.empty()
      placeholder13_7.empty()
      placeholder17_7.empty()
      placeholder21_7.empty()
      placeholder27_7.empty()
    
      if pivot_reportes==0:
        placeholder14_7.empty()
      
      else:
        placeholder15_7.empty()
        placeholder16_7.empty()
         
      if pivot_r==0 and pivot_c==0 and pivot_o==0:
        placeholder18_7.empty()
        placeholder30_7.empty()
        
      else:
        placeholder19_7.empty()
        placeholder20_7.empty()
        placeholder31_7.empty()
        placeholder32_7.empty()
      
      if pivot_r==0:
        placeholder22_7.empty()
        placeholder28_7.empty()

      else:
        placeholder23_7.empty()
        placeholder24_7.empty()
        placeholder25_7.empty()
        placeholder26_7.empty()
        placeholder29_7.empty()

    elif puesto=="Operario Catastral":
      placeholder33_7.empty()
      placeholder34_7.empty()
      placeholder35_7.empty()
      placeholder39_7.empty()
      placeholder43_7.empty()
      placeholder49_7.empty()

      if pivot_reportes==0:
        placeholder36_7.empty()
      
      else:
        placeholder37_7.empty()
        placeholder38_7.empty()
         
      if pivot_r==0 and pivot_c==0 and pivot_o==0:
        placeholder40_7.empty()
        placeholder52_7.empty()
        
      else:
        placeholder41_7.empty()
        placeholder42_7.empty()
        placeholder53_7.empty()
        placeholder54_7.empty()
        
      if pivot_r==0:
        placeholder44_7.empty()
        placeholder50_7.empty()

      else:
        placeholder45_7.empty()
        placeholder46_7.empty()
        placeholder47_7.empty()
        placeholder48_7.empty()
        placeholder51_7.empty()

    st.session_state.Historial=False
    st.session_state.Bonos=True
    Bonos.Bonos(usuario,puesto)
   
  # ----- Salir ---- #
    
  elif salir_7:
    placeholder1_7.empty()
    placeholder2_7.empty()
    placeholder3_7.empty()
    placeholder4_7.empty()
    placeholder5_7.empty()   
    placeholder6_7.empty()
    placeholder7_7.empty()
    placeholder8_7.empty()
    placeholder9_7.empty()
    
    if puesto=="Supervisor" or puesto=="Coordinador":  
      placeholder10_7.empty()
      placeholder11_7.empty()
      placeholder12_7.empty()
      placeholder13_7.empty()
      placeholder17_7.empty()
      placeholder21_7.empty()
      placeholder27_7.empty()
    
      if pivot_reportes==0:
        placeholder14_7.empty()
      
      else:
        placeholder15_7.empty()
        placeholder16_7.empty()
         
      if pivot_r==0 and pivot_c==0 and pivot_o==0:
        placeholder18_7.empty()
        placeholder30_7.empty()
        
      else:
        placeholder19_7.empty()
        placeholder20_7.empty()
        placeholder31_7.empty()
        placeholder32_7.empty()
      
      if pivot_r==0:
        placeholder22_7.empty()
        placeholder28_7.empty()

      else:
        placeholder23_7.empty()
        placeholder24_7.empty()
        placeholder25_7.empty()
        placeholder26_7.empty()
        placeholder29_7.empty()

    elif puesto=="Operario Catastral":
      placeholder33_7.empty()
      placeholder34_7.empty()
      placeholder35_7.empty()
      placeholder39_7.empty()
      placeholder43_7.empty()
      placeholder49_7.empty()

      if pivot_reportes==0:
        placeholder36_7.empty()
      
      else:
        placeholder37_7.empty()
        placeholder38_7.empty()
         
      if pivot_r==0 and pivot_c==0 and pivot_o==0:
        placeholder40_7.empty()
        placeholder52_7.empty()
        
      else:
        placeholder41_7.empty()
        placeholder42_7.empty()
        placeholder53_7.empty()
        placeholder54_7.empty()
        
      if pivot_r==0:
        placeholder44_7.empty()
        placeholder50_7.empty()

      else:
        placeholder45_7.empty()
        placeholder46_7.empty()
        placeholder47_7.empty()
        placeholder48_7.empty()
        placeholder51_7.empty()

    st.session_state.Ingreso = False
    st.session_state.Historial=False
    st.session_state.Salir=True
    Salir.Salir()
