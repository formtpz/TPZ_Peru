# ----- Librerías ---- #

import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
import pytz
from urllib.parse import urlparse
import Procesos,Historial,Capacitacion,Otros_Registros,Bonos,Salir

def Auxiliares(usuario,puesto):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_14= st.sidebar.empty()
  titulo= placeholder1_14.title("Menú")

  placeholder2_14 = st.sidebar.empty()
  procesos_14 = placeholder2_14.button("Procesos",key="procesos_14")

  placeholder3_14 = st.sidebar.empty()
  historial_14 = placeholder3_14.button("Historial",key="historial_14")

  placeholder4_14 = st.sidebar.empty()
  capacitacion_14 = placeholder4_14.button("Capacitaciones",key="capacitacion_14")

  placeholder5_14 = st.sidebar.empty()
  otros_registros_14 = placeholder5_14.button("Otros Registros",key="otros_registros_14")

  placeholder6_14 = st.sidebar.empty()
  bonos_14 = placeholder6_14.button("Bonos",key="bonos_14")

  placeholder7_14 = st.sidebar.empty()
  salir_14 = placeholder7_14.button("Salir",key="salir_14")

  placeholder8_14 = st.empty()
  informacion_final_iii_14 = placeholder8_14.title("Auxiliares")

  default_date_14 = datetime.now(pytz.timezone('America/Guatemala'))

  placeholder9_14= st.empty()
  fecha_14= placeholder9_14.date_input("Fecha",value=default_date_14,key="fecha_14")

  placeholder10_14= st.empty()
  proceso_14= placeholder10_14.selectbox("Proceso", options=("Digitalización de Planos","Sectores Circulares"), key="estado_14")
       
  placeholder11_14= st.empty()
  bloque_14= placeholder11_14.number_input("Bloque o Distrito",min_value=10000000,max_value=99999999,step=1,key="bloque_14")
    
  placeholder12_14= st.empty()
  predios_14= placeholder12_14.number_input("Cantidad de Planos Producidos",min_value=0,step=1,key="predios_14")

  placeholder13_14= st.empty()
  horas_14= placeholder13_14.number_input("Cantidad de Horas Trabajadas en el Proceso",min_value=0.0,key="horas_14")

  placeholder14_14 = st.empty()
  reporte_14 = placeholder14_14.button("Generar Reporte",key="reporte_14")

  # ----- Procesos ---- #
    
  if procesos_14:

    placeholder1_14.empty()
    placeholder2_14.empty()
    placeholder3_14.empty()
    placeholder4_14.empty()
    placeholder5_14.empty()
    placeholder6_14.empty()
    placeholder7_14.empty()
    placeholder8_14.empty()
    placeholder9_14.empty()
    placeholder10_14.empty()
    placeholder11_14.empty()
    placeholder12_14.empty()
    placeholder13_14.empty()
    placeholder14_14.empty()
    st.session_state.Procesos=False
    st.session_state.Auxiliares=False

    perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
    perfil= perfil.loc[0,'perfil']

    if perfil=="1":        
                    
      Procesos.Procesos1(usuario,puesto)
                
    elif perfil=="2":        
                    
      Procesos.Procesos2(usuario,puesto)   

    elif perfil=="3":  

      Procesos.Procesos3(usuario,puesto)       


  #----- Historial ---- #
    
  elif historial_14:

    placeholder1_14.empty()
    placeholder2_14.empty()
    placeholder3_14.empty()
    placeholder4_14.empty()
    placeholder5_14.empty()
    placeholder6_14.empty()
    placeholder7_14.empty()
    placeholder8_14.empty()
    placeholder9_14.empty()
    placeholder10_14.empty()
    placeholder11_14.empty()
    placeholder12_14.empty()
    placeholder13_14.empty()
    placeholder14_14.empty()
    st.session_state.Auxiliares=False
    st.session_state.Historial=True
    Historial.Historial(usuario,puesto)   

  # ----- Capacitación ---- #
    
  elif capacitacion_14:

    placeholder1_14.empty()
    placeholder2_14.empty()
    placeholder3_14.empty()
    placeholder4_14.empty()
    placeholder5_14.empty()
    placeholder6_14.empty()
    placeholder7_14.empty()
    placeholder8_14.empty()
    placeholder9_14.empty()
    placeholder10_14.empty()
    placeholder11_14.empty()
    placeholder12_14.empty()
    placeholder13_14.empty()
    placeholder14_14.empty()
    st.session_state.IFI=False
    st.session_state.Capacitacion=True
    Capacitacion.Capacitacion(usuario,puesto)

  # ----- Otros Registros ---- #
    
  elif otros_registros_14:

    placeholder1_14.empty()
    placeholder2_14.empty()
    placeholder3_14.empty()
    placeholder4_14.empty()
    placeholder5_14.empty()
    placeholder6_14.empty()
    placeholder7_14.empty()
    placeholder8_14.empty()
    placeholder9_14.empty()
    placeholder10_14.empty()
    placeholder11_14.empty()
    placeholder12_14.empty()
    placeholder13_14.empty()
    placeholder14_14.empty()
    st.session_state.Auxiliares=False
    st.session_state.Otros_Registros=True
    Otros_Registros.Otros_Registros(usuario,puesto)

    # ----- Bonos ---- #
    
  elif bonos_14:

    placeholder1_14.empty()
    placeholder2_14.empty()
    placeholder3_14.empty()
    placeholder4_14.empty()
    placeholder5_14.empty()
    placeholder6_14.empty()
    placeholder7_14.empty()
    placeholder8_14.empty()
    placeholder9_14.empty()
    placeholder10_14.empty()
    placeholder11_14.empty()
    placeholder12_14.empty()
    placeholder13_14.empty()
    placeholder14_14.empty()
    st.session_state.Auxiliares=False
    st.session_state.Bonos=True
    Bonos.Bonos(usuario,puesto)
    
    # ----- Salir ---- #
    
  elif salir_14:
    placeholder1_14.empty()
    placeholder2_14.empty()
    placeholder3_14.empty()
    placeholder4_14.empty()
    placeholder5_14.empty()
    placeholder6_14.empty()
    placeholder7_14.empty()
    placeholder8_14.empty()
    placeholder9_14.empty()
    placeholder10_14.empty()
    placeholder11_14.empty()
    placeholder12_14.empty()
    placeholder13_14.empty()
    placeholder14_14.empty()
    st.session_state.Ingreso = False
    st.session_state.Auxiliares=False
    st.session_state.Salir=True
    Salir.Salir()

  elif reporte_14:

    cursor01=con.cursor()

    marca_14= datetime.now(pytz.timezone('America/Guatemala')).strftime("%Y-%m-%d %H:%M:%S")
    
    nombre_14= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
    nombre_14 = nombre_14.loc[0,'nombre']
      
    horario_14= pd.read_sql(f"select horario from usuarios where usuario ='{usuario}'",uri)
    horario_14 = horario_14.loc[0,'horario']

    supervisor_14= pd.read_sql(f"select supervisor from usuarios where usuario ='{usuario}'",uri)
    supervisor_14 = supervisor_14.loc[0,'supervisor']

    cursor01.execute(f"INSERT INTO registro (marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,predios,horas)VALUES('{marca_14}','{usuario}','{nombre_14}','{horario_14}','{puesto}','{supervisor_14}','{proceso_14}','{fecha_14}','{bloque_14}','Terminado','Ordinario','{predios_14}','{horas_14}')")
    con.commit()
    st.success('Reporte enviado correctamente')
