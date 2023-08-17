# ----- Librerías ---- #

import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
import pytz
from urllib.parse import urlparse
import Procesos,Historial,Capacitacion,Otros_Registros,Bonos,Salir

def Conformacion(usuario,puesto):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_10= st.sidebar.empty()
  titulo= placeholder1_10.title("Menú")

  placeholder2_10 = st.sidebar.empty()
  procesos_10 = placeholder2_10.button("Procesos",key="procesos_10")

  placeholder3_10 = st.sidebar.empty()
  historial_10 = placeholder3_10.button("Historial",key="historial_10")

  placeholder4_10 = st.sidebar.empty()
  capacitacion_10 = placeholder4_10.button("Capacitaciones",key="capacitacion_10")

  placeholder5_10 = st.sidebar.empty()
  otros_registros_10 = placeholder5_10.button("Otros Registros",key="otros_registros_10")

  placeholder6_10 = st.sidebar.empty()
  bonos_10 = placeholder6_10.button("Bonos",key="bonos_10")

  placeholder7_10 = st.sidebar.empty()
  salir_10 = placeholder7_10.button("Salir",key="salir_10")

  placeholder8_10 = st.empty()
  conformacion_10 = placeholder8_10.title("Conformación")

  default_date_10 = datetime.now(pytz.timezone('America/Guatemala'))

  placeholder9_10= st.empty()
  fecha_10= placeholder9_10.date_input("Fecha",value=default_date_10,key="fecha_10")

  placeholder10_10= st.empty()
  bloque_10= placeholder10_10.number_input("Bloque",min_value=10000000,max_value=99999999,step=1,key="bloque_10")
    
  placeholder11_10= st.empty()
  estado_10= placeholder11_10.selectbox("Estado", options=("En Proceso","Conflicto","Terminado"), key="estado_10")
       
  placeholder12_10= st.empty()
  tipo_10= placeholder12_10.selectbox("Tipo", options=("Ordinario","Corrección Primera Revisión","Corrección Primera Reinspección"), key="tipo_10")
       
  placeholder13_10= st.empty()
  predios_10= placeholder13_10.number_input("Cantidad de Predios Producidos",min_value=0,step=1,key="predios_10")

  placeholder14_10= st.empty()
  horas_10= placeholder14_10.number_input("Cantidad de Horas Trabajadas en el Proceso",min_value=0.0,key="horas_10")

  placeholder15_10 = st.empty()
  reporte_10 = placeholder15_10.button("Generar Reporte",key="reporte_10")

  # ----- Procesos ---- #
    
  if procesos_10:
    placeholder1_10.empty()
    placeholder2_10.empty()
    placeholder3_10.empty()
    placeholder4_10.empty()
    placeholder5_10.empty()
    placeholder6_10.empty()
    placeholder7_10.empty()
    placeholder8_10.empty()
    placeholder9_10.empty()
    placeholder10_10.empty()
    placeholder11_10.empty()
    placeholder12_10.empty()
    placeholder13_10.empty()
    placeholder14_10.empty()
    placeholder15_10.empty()
    st.session_state.Procesos=False
    st.session_state.Conformacion=False

    perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
    perfil= perfil.loc[0,'perfil']

    if perfil=="1":        
                    
      Procesos.Procesos1(usuario,puesto)
                
    elif perfil=="2":        
                    
      Procesos.Procesos2(usuario,puesto)   

    elif perfil=="3":  

      Procesos.Procesos3(usuario,puesto)       


  #----- Historial ---- #
    
  elif historial_10:
    placeholder1_10.empty()
    placeholder2_10.empty()
    placeholder3_10.empty()
    placeholder4_10.empty()
    placeholder5_10.empty()
    placeholder6_10.empty()
    placeholder7_10.empty()
    placeholder8_10.empty()
    placeholder9_10.empty()
    placeholder10_10.empty()
    placeholder11_10.empty()
    placeholder12_10.empty()
    placeholder13_10.empty()
    placeholder14_10.empty()
    placeholder15_10.empty()
    st.session_state.Conformacion=False
    st.session_state.Historial=True
    Historial.Historial(usuario,puesto)   

  # ----- Capacitación ---- #
    
  elif capacitacion_10:
    placeholder1_10.empty()
    placeholder2_10.empty()
    placeholder3_10.empty()
    placeholder4_10.empty()
    placeholder5_10.empty()
    placeholder6_10.empty()
    placeholder7_10.empty()
    placeholder8_10.empty()
    placeholder9_10.empty()
    placeholder10_10.empty()
    placeholder11_10.empty()
    placeholder12_10.empty()
    placeholder13_10.empty()
    placeholder14_10.empty()
    placeholder15_10.empty()
    st.session_state.Conformacion=False
    st.session_state.Capacitacion=True
    Capacitacion.Capacitacion(usuario,puesto)

  # ----- Otros Registros ---- #
    
  elif otros_registros_10:
    placeholder1_10.empty()
    placeholder2_10.empty()
    placeholder3_10.empty()
    placeholder4_10.empty()
    placeholder5_10.empty()
    placeholder6_10.empty()
    placeholder7_10.empty()
    placeholder8_10.empty()
    placeholder9_10.empty()
    placeholder10_10.empty()
    placeholder11_10.empty()
    placeholder12_10.empty()
    placeholder13_10.empty()
    placeholder14_10.empty()
    placeholder15_10.empty()
    st.session_state.Conformacion=False
    st.session_state.Otros_Registros=True
    Otros_Registros.Otros_Registros(usuario,puesto)

  # ----- Bonos ---- #
    
  elif bonos_10:
    placeholder1_10.empty()
    placeholder2_10.empty()
    placeholder3_10.empty()
    placeholder4_10.empty()
    placeholder5_10.empty()
    placeholder6_10.empty()
    placeholder7_10.empty()
    placeholder8_10.empty()
    placeholder9_10.empty()
    placeholder10_10.empty()
    placeholder11_10.empty()
    placeholder12_10.empty()
    placeholder13_10.empty()
    placeholder14_10.empty()
    placeholder15_10.empty()
    st.session_state.Conformacion=False
    st.session_state.Bonos=True
    Bonos.Bonos(usuario,puesto)    

  # ----- Salir ---- #
    
  elif salir_10:
    placeholder1_10.empty()
    placeholder2_10.empty()
    placeholder3_10.empty()
    placeholder4_10.empty()
    placeholder5_10.empty()
    placeholder6_10.empty()
    placeholder7_10.empty()
    placeholder8_10.empty()
    placeholder9_10.empty()
    placeholder10_10.empty()
    placeholder11_10.empty()
    placeholder12_10.empty()
    placeholder13_10.empty()
    placeholder14_10.empty()
    placeholder15_10.empty()
    st.session_state.Ingreso = False
    st.session_state.Conformacion=False
    st.session_state.Salir=True
    Salir.Salir()

  elif reporte_10:

    cursor01=con.cursor()

    marca_10=datetime.now(pytz.timezone('America/Guatemala')).strftime("%Y-%m-%d %H:%M:%S")
    
    nombre_10= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
    nombre_10 = nombre_10.loc[0,'nombre']
      
    horario_10= pd.read_sql(f"select horario from usuarios where usuario ='{usuario}'",uri)
    horario_10 = horario_10.loc[0,'horario']

    supervisor_10= pd.read_sql(f"select supervisor from usuarios where usuario ='{usuario}'",uri)
    supervisor_10 = supervisor_10.loc[0,'supervisor']

    cursor01.execute(f"INSERT INTO registro (marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,predios,horas)VALUES('{marca_10}','{usuario}','{nombre_10}','{horario_10}','{puesto}','{supervisor_10}','Conformación','{fecha_10}','{bloque_10}','{estado_10}','{tipo_10}','{predios_10}','{horas_10}')")
    con.commit()
    st.success('Reporte enviado correctamente')
