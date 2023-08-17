# ----- Librerías ---- #

import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
import pytz
from urllib.parse import urlparse
import Procesos,Historial,Capacitacion,Otros_Registros,Bonos,Salir

def CC_Conformacion(usuario,puesto):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_11= st.sidebar.empty()
  titulo= placeholder1_11.title("Menú")

  placeholder2_11 = st.sidebar.empty()
  procesos_11 = placeholder2_11.button("Procesos",key="procesos_11")

  placeholder3_11 = st.sidebar.empty()
  historial_11 = placeholder3_11.button("Historial",key="historial_11")

  placeholder4_11 = st.sidebar.empty()
  capacitacion_11 = placeholder4_11.button("Capacitaciones",key="capacitacion_11")

  placeholder5_11 = st.sidebar.empty()
  otros_registros_11 = placeholder5_11.button("Otros Registros",key="otros_registros_11")

  placeholder6_11 = st.sidebar.empty()
  bonos_11 = placeholder6_11.button("Bonos",key="bonos_11")

  placeholder7_11 = st.sidebar.empty()
  salir_11 = placeholder7_11.button("Salir",key="salir_11")

  placeholder8_11 = st.empty()
  conformacion_11 = placeholder8_11.title("Control de Calidad de Conformación")

  default_date_11 = datetime.now(pytz.timezone('America/Guatemala'))

  placeholder9_11= st.empty()
  fecha_11= placeholder9_11.date_input("Fecha",value=default_date_11,key="fecha_11")

  placeholder10_11= st.empty()
  bloque_11= placeholder10_11.number_input("Bloque",min_value=10000000,max_value=99999999,step=1,key="bloque_11")
    
  placeholder11_11= st.empty()
  estado_11= placeholder11_11.selectbox("Estado",options=("En Proceso","Aprobado","Rechazado","Primera Reinspección Aprobada","Primera Reinspección Rechazada","Segunda Reinspección Aprobada","Segunda Reinspección Rechazada"), key="estado_11")
              
  placeholder12_11= st.empty()
  predios_11= placeholder12_11.number_input("Cantidad de Predios Revisados",min_value=0,step=1,key="predios_11")

  placeholder13_11= st.empty()
  horas_11= placeholder13_11.number_input("Cantidad de Horas Trabajadas en el Proceso",min_value=0.0,key="horas_11")

  placeholder14_11 = st.empty()
  reporte_11 = placeholder14_11.button("Generar Reporte",key="reporte_11")
  
  # ----- Procesos ---- #
    
  if procesos_11:
    placeholder1_11.empty()
    placeholder2_11.empty()
    placeholder3_11.empty()
    placeholder4_11.empty()
    placeholder5_11.empty()
    placeholder6_11.empty()
    placeholder7_11.empty()
    placeholder8_11.empty()
    placeholder9_11.empty()
    placeholder10_11.empty()
    placeholder11_11.empty()
    placeholder12_11.empty()
    placeholder13_11.empty()
    placeholder14_11.empty()
    st.session_state.Procesos=False
    st.session_state.CC_Conformacion=False

    perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
    perfil= perfil.loc[0,'perfil']

    if perfil=="1":        
                    
      Procesos.Procesos1(usuario,puesto)
                
    elif perfil=="2":        
                    
      Procesos.Procesos2(usuario,puesto)   

    elif perfil=="3":  

      Procesos.Procesos3(usuario,puesto) 
      
  #----- Historial ---- #
    
  elif historial_11:
    placeholder1_11.empty()
    placeholder2_11.empty()
    placeholder3_11.empty()
    placeholder4_11.empty()
    placeholder5_11.empty()
    placeholder6_11.empty()
    placeholder7_11.empty()
    placeholder8_11.empty()
    placeholder9_11.empty()
    placeholder10_11.empty()
    placeholder11_11.empty()
    placeholder12_11.empty()
    placeholder13_11.empty()
    placeholder14_11.empty()
    st.session_state.CC_Conformacion=False
    st.session_state.Historial=True
    Historial.Historial(usuario,puesto)   

  # ----- Capacitación ---- #
    
  elif capacitacion_11:
    placeholder1_11.empty()
    placeholder2_11.empty()
    placeholder3_11.empty()
    placeholder4_11.empty()
    placeholder5_11.empty()
    placeholder6_11.empty()
    placeholder7_11.empty()
    placeholder8_11.empty()
    placeholder9_11.empty()
    placeholder10_11.empty()
    placeholder11_11.empty()
    placeholder12_11.empty()
    placeholder13_11.empty()
    placeholder14_11.empty()
    st.session_state.CC_Conformacion=False
    st.session_state.Capacitacion=True
    Capacitacion.Capacitacion(usuario,puesto)

  # ----- Otros Registros ---- #
    
  elif otros_registros_11:
    placeholder1_11.empty()
    placeholder2_11.empty()
    placeholder3_11.empty()
    placeholder4_11.empty()
    placeholder5_11.empty()
    placeholder6_11.empty()
    placeholder7_11.empty()
    placeholder8_11.empty()
    placeholder9_11.empty()
    placeholder10_11.empty()
    placeholder11_11.empty()
    placeholder12_11.empty()
    placeholder13_11.empty()
    placeholder14_11.empty()
    st.session_state.CC_Conformacion=False
    st.session_state.Otros_Registros=True
    Otros_Registros.Otros_Registros(usuario,puesto)

  # ----- Bonos ---- #
    
  elif bonos_11:

    placeholder1_11.empty()
    placeholder2_11.empty()
    placeholder3_11.empty()
    placeholder4_11.empty()
    placeholder5_11.empty()
    placeholder6_11.empty()
    placeholder7_11.empty()
    placeholder8_11.empty()
    placeholder9_11.empty()
    placeholder10_11.empty()
    placeholder11_11.empty()
    placeholder12_11.empty()
    placeholder13_11.empty()
    placeholder14_11.empty()
    st.session_state.CC_Conformacion=False
    st.session_state.Bonos=True
    Bonos.Bonos(usuario,puesto)    

  # ----- Salir ---- #
    
  elif salir_11:
    placeholder1_11.empty()
    placeholder2_11.empty()
    placeholder3_11.empty()
    placeholder4_11.empty()
    placeholder5_11.empty()
    placeholder6_11.empty()
    placeholder7_11.empty()
    placeholder8_11.empty()
    placeholder9_11.empty()
    placeholder10_11.empty()
    placeholder11_11.empty()
    placeholder12_11.empty()
    placeholder13_11.empty()
    placeholder14_11.empty()
    st.session_state.Ingreso = False
    st.session_state.CC_Conformacion=False
    st.session_state.Salir=True
    Salir.Salir()

  elif reporte_11:

    cursor01=con.cursor()

    marca_11=datetime.now(pytz.timezone('America/Guatemala')).strftime("%Y-%m-%d %H:%M:%S")

    nombre_11= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
    nombre_11 = nombre_11.loc[0,'nombre']
      
    horario_11= pd.read_sql(f"select horario from usuarios where usuario ='{usuario}'",uri)
    horario_11 = horario_11.loc[0,'horario']

    supervisor_11= pd.read_sql(f"select supervisor from usuarios where usuario ='{usuario}'",uri)
    supervisor_11 = supervisor_11.loc[0,'supervisor']

    cursor01.execute(f"INSERT INTO registro (marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,predios,horas)VALUES('{marca_11}','{usuario}','{nombre_11}','{horario_11}','{puesto}','{supervisor_11}','Control de Calidad Conformación','{fecha_11}','{bloque_11}','{estado_11}','No Aplica','{predios_11}','{horas_11}')")
    
    con.commit()
    st.success('Reporte enviado correctamente')
