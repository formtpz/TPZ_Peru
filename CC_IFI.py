# ----- Librerías ---- #

import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
import pytz
from urllib.parse import urlparse
import Procesos,Historial,Capacitacion,Otros_Registros,Bonos,Salir

def CC_IFI(usuario,puesto):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_12= st.sidebar.empty()
  titulo= placeholder1_12.title("Menú")

  placeholder2_12 = st.sidebar.empty()
  procesos_12 = placeholder2_12.button("Procesos",key="procesos_12")

  placeholder3_12 = st.sidebar.empty()
  historial_12 = placeholder3_12.button("Historial",key="historial_12")

  placeholder4_12 = st.sidebar.empty()
  capacitacion_12 = placeholder4_12.button("Capacitaciones",key="capacitacion_12")

  placeholder5_12 = st.sidebar.empty()
  otros_registros_12 = placeholder5_12.button("Otros Registros",key="otros_registros_12")

  placeholder6_12 = st.sidebar.empty()
  bonos_12 = placeholder6_12.button("Bonos",key="bonos_12")

  placeholder7_12 = st.sidebar.empty()
  salir_12 = placeholder7_12.button("Salir",key="salir_12")

  placeholder8_12 = st.empty()
  conformacion_12 = placeholder8_12.title("Control de Calidad de Información Final I")

  default_date_12 = datetime.now(pytz.timezone('America/Guatemala'))

  placeholder9_12= st.empty()
  fecha_12= placeholder9_12.date_input("Fecha",value=default_date_12,key="fecha_12")

  placeholder10_12= st.empty()
  bloque_12= placeholder10_12.text_input("Bloque",key="bloque_11")
    
  placeholder11_12= st.empty()
  estado_12= placeholder11_12.selectbox("Estado", options=("En Proceso","Georreferenciación Aprobada","Georreferenciación Rechazada","Reinspección Georreferenciación Aprobada", "Reinspección Georreferenciación Rechazada","Aprobado","Rechazado","Primera Reinspección Aprobada","Primera Reinspección Rechazada","Segunda Reinspección Aprobada","Segunda Reinspección Rechazada"), key="estado_12")
              
  placeholder12_12= st.empty()
  predios_12= placeholder12_12.number_input("Cantidad de Predios Revisados",min_value=0,step=1,key="predios_12")

  placeholder13_12= st.empty()
  horas_12= placeholder13_12.number_input("Cantidad de Horas Trabajadas en el Proceso",min_value=0.0,key="horas_12")

  placeholder14_12 = st.empty()
  reporte_12 = placeholder14_12.button("Generar Reporte",key="reporte_12")

  # ----- Procesos ---- #
    
  if procesos_12:
    placeholder1_12.empty()
    placeholder2_12.empty()
    placeholder3_12.empty()
    placeholder4_12.empty()
    placeholder5_12.empty()
    placeholder6_12.empty()
    placeholder7_12.empty()
    placeholder8_12.empty()
    placeholder9_12.empty()
    placeholder10_12.empty()
    placeholder11_12.empty()
    placeholder12_12.empty()
    placeholder13_12.empty()
    placeholder14_12.empty()
    st.session_state.Procesos=False
    st.session_state.CC_IFI=False

    perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
    perfil= perfil.loc[0,'perfil']

    if perfil=="1":        
                    
      Procesos.Procesos1(usuario,puesto)
                
    elif perfil=="2":        
                    
      Procesos.Procesos2(usuario,puesto)   

    elif perfil=="3":  

      Procesos.Procesos3(usuario,puesto)       

  #----- Historial ---- #
    
  elif historial_12:
    placeholder1_12.empty()
    placeholder2_12.empty()
    placeholder3_12.empty()
    placeholder4_12.empty()
    placeholder5_12.empty()
    placeholder6_12.empty()
    placeholder7_12.empty()
    placeholder8_12.empty()
    placeholder9_12.empty()
    placeholder10_12.empty()
    placeholder11_12.empty()
    placeholder12_12.empty()
    placeholder13_12.empty()
    placeholder14_12.empty()
    st.session_state.CC_IFI=False
    st.session_state.Historial=True
    Historial.Historial(usuario,puesto)   

  # ----- Capacitación ---- #
    
  elif capacitacion_12:
    placeholder1_12.empty()
    placeholder2_12.empty()
    placeholder3_12.empty()
    placeholder4_12.empty()
    placeholder5_12.empty()
    placeholder6_12.empty()
    placeholder7_12.empty()
    placeholder8_12.empty()
    placeholder9_12.empty()
    placeholder10_12.empty()
    placeholder11_12.empty()
    placeholder12_12.empty()
    placeholder13_12.empty()
    placeholder14_12.empty()
    st.session_state.CC_IFI=False
    st.session_state.Capacitacion=True
    Capacitacion.Capacitacion(usuario,puesto)

  # ----- Otros Registros ---- #
    
  elif otros_registros_12:
    placeholder1_12.empty()
    placeholder2_12.empty()
    placeholder3_12.empty()
    placeholder4_12.empty()
    placeholder5_12.empty()
    placeholder6_12.empty()
    placeholder7_12.empty()
    placeholder8_12.empty()
    placeholder9_12.empty()
    placeholder10_12.empty()
    placeholder11_12.empty()
    placeholder12_12.empty()
    placeholder13_12.empty()
    placeholder14_12.empty()
    st.session_state.CC_IFI=False
    st.session_state.Otros_Registros=True
    Otros_Registros.Otros_Registros(usuario,puesto)

  # ----- Bonos ---- #
    
  elif bonos_12:
    placeholder1_12.empty()
    placeholder2_12.empty()
    placeholder3_12.empty()
    placeholder4_12.empty()
    placeholder5_12.empty()
    placeholder6_12.empty()
    placeholder7_12.empty()
    placeholder8_12.empty()
    placeholder9_12.empty()
    placeholder10_12.empty()
    placeholder11_12.empty()
    placeholder12_12.empty()
    placeholder13_12.empty()
    placeholder14_12.empty()
    st.session_state.CC_IFI=False
    st.session_state.Bonos=True
    Bonos.Bonos(usuario,puesto)    

  # ----- Salir ---- #
    
  elif salir_12:
    placeholder1_12.empty()
    placeholder2_12.empty()
    placeholder3_12.empty()
    placeholder4_12.empty()
    placeholder5_12.empty()
    placeholder6_12.empty()
    placeholder7_12.empty()
    placeholder8_12.empty()
    placeholder9_12.empty()
    placeholder10_12.empty()
    placeholder11_12.empty()
    placeholder12_12.empty()
    placeholder13_12.empty()
    placeholder14_12.empty()
    st.session_state.Ingreso = False
    st.session_state.CC_IFI=False
    st.session_state.Salir=True
    Salir.Salir()

  elif reporte_12:

    cursor01=con.cursor()

    marca_12=datetime.now(pytz.timezone('America/Guatemala')).strftime("%Y-%m-%d %H:%M:%S")
    nombre_12= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)

    nombre_12 = nombre_12.loc[0,'nombre']
      
    horario_12= pd.read_sql(f"select horario from usuarios where usuario ='{usuario}'",uri)
    horario_12 = horario_12.loc[0,'horario']

    supervisor_12= pd.read_sql(f"select supervisor from usuarios where usuario ='{usuario}'",uri)
    supervisor_12 = supervisor_12.loc[0,'supervisor']

    cursor01.execute(f"INSERT INTO registro (marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,predios,horas)VALUES('{marca_12}','{usuario}','{nombre_12}','{horario_12}','{puesto}','{supervisor_12}','Control de Calidad IF I','{fecha_12}','{bloque_12}','{estado_12}','No Aplica','{predios_12}','{horas_12}')")
    con.commit()
    st.success('Reporte enviado correctamente')
