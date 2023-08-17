# ----- Librerías ---- #

import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
import pytz
from urllib.parse import urlparse
import Procesos,Historial,Capacitacion,Otros_Registros,Bonos,Salir

def IFIII(usuario,puesto):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_5= st.sidebar.empty()
  titulo= placeholder1_5.title("Menú")

  placeholder2_5 = st.sidebar.empty()
  procesos_5 = placeholder2_5.button("Procesos",key="procesos_5")

  placeholder3_5 = st.sidebar.empty()
  historial_5 = placeholder3_5.button("Historial",key="historial_5")

  placeholder4_5 = st.sidebar.empty()
  capacitacion_5 = placeholder4_5.button("Capacitaciones",key="capacitacion_5")

  placeholder5_5 = st.sidebar.empty()
  otros_registros_5 = placeholder5_5.button("Otros Registros",key="otros_registros_5")

  placeholder6_5 = st.sidebar.empty()
  bonos_5 = placeholder6_5.button("Bonos",key="bonos_5")

  placeholder7_5 = st.sidebar.empty()
  salir_5 = placeholder7_5.button("Salir",key="salir_5")

  placeholder8_5 = st.empty()
  informacion_final_iii_5 = placeholder8_5.title("Información Final III")

  default_date_5 = datetime.now(pytz.timezone('America/Guatemala'))

  placeholder9_5= st.empty()
  fecha_5= placeholder9_5.date_input("Fecha",value=default_date_5,key="fecha_5")

  placeholder10_5= st.empty()
  bloque_5= placeholder10_5.number_input("Bloque o Distrito",min_value=10000000,max_value=99999999,step=1,key="bloque_5")
    
  placeholder11_5= st.empty()
  estado_5= placeholder11_5.selectbox("Estado", options=("En Proceso","Conflicto","Terminado"), key="estado_5")
       
  placeholder12_5= st.empty()
  tipo_5= placeholder12_5.selectbox("Tipo",options=("Ordinario","Afectados","Corrección Primera Revisión","Corrección Primera Reinspección"), key="tipo_5")
       
  placeholder13_5= st.empty()
  predios_5= placeholder13_5.number_input("Cantidad de Predios Producidos",min_value=0,step=1,key="predios_5")

  placeholder14_5= st.empty()
  horas_5= placeholder14_5.number_input("Cantidad de Horas Trabajadas en el Proceso",min_value=0.0,key="horas_5")

  placeholder15_5 = st.empty()
  reporte_5 = placeholder15_5.button("Generar Reporte",key="reporte_5")

  # ----- Procesos ---- #
    
  if procesos_5:
    placeholder1_5.empty()
    placeholder2_5.empty()
    placeholder3_5.empty()
    placeholder4_5.empty()
    placeholder5_5.empty()
    placeholder6_5.empty()
    placeholder7_5.empty()
    placeholder8_5.empty()
    placeholder9_5.empty()
    placeholder10_5.empty()
    placeholder11_5.empty()
    placeholder12_5.empty()
    placeholder13_5.empty()
    placeholder14_5.empty()
    placeholder15_5.empty()
    st.session_state.Procesos=False
    st.session_state.IFI=False

    perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
    perfil= perfil.loc[0,'perfil']

    if perfil=="1":        
                    
      Procesos.Procesos1(usuario,puesto)
                
    elif perfil=="2":        
                    
      Procesos.Procesos2(usuario,puesto)   

    elif perfil=="3":  

      Procesos.Procesos3(usuario,puesto)       


  #----- Historial ---- #
    
  elif historial_5:
    placeholder1_5.empty()
    placeholder2_5.empty()
    placeholder3_5.empty()
    placeholder4_5.empty()
    placeholder5_5.empty()
    placeholder6_5.empty()
    placeholder7_5.empty()
    placeholder8_5.empty()
    placeholder9_5.empty()
    placeholder10_5.empty()
    placeholder11_5.empty()
    placeholder12_5.empty()
    placeholder13_5.empty()
    placeholder14_5.empty()
    placeholder15_5.empty()
    st.session_state.IFI=False
    st.session_state.Historial=True
    Historial.Historial(usuario,puesto)   

  # ----- Capacitación ---- #
    
  elif capacitacion_5:

    placeholder1_5.empty()
    placeholder2_5.empty()
    placeholder3_5.empty()
    placeholder4_5.empty()
    placeholder5_5.empty()
    placeholder6_5.empty()
    placeholder7_5.empty()
    placeholder8_5.empty()
    placeholder9_5.empty()
    placeholder10_5.empty()
    placeholder11_5.empty()
    placeholder12_5.empty()
    placeholder13_5.empty()
    placeholder14_5.empty()
    placeholder15_5.empty()
    st.session_state.IFI=False
    st.session_state.Capacitacion=True
    Capacitacion.Capacitacion(usuario,puesto)

  # ----- Otros Registros ---- #
    
  elif otros_registros_5:

    placeholder1_5.empty()
    placeholder2_5.empty()
    placeholder3_5.empty()
    placeholder4_5.empty()
    placeholder5_5.empty()
    placeholder6_5.empty()
    placeholder7_5.empty()
    placeholder8_5.empty()
    placeholder9_5.empty()
    placeholder10_5.empty()
    placeholder11_5.empty()
    placeholder12_5.empty()
    placeholder13_5.empty()
    placeholder14_5.empty()
    placeholder15_5.empty()
    st.session_state.IFI=False
    st.session_state.Otros_Registros=True
    Otros_Registros.Otros_Registros(usuario,puesto)

    # ----- Bonos ---- #
    
  elif bonos_5:

    placeholder1_5.empty()
    placeholder2_5.empty()
    placeholder3_5.empty()
    placeholder4_5.empty()
    placeholder5_5.empty()
    placeholder6_5.empty()
    placeholder7_5.empty()
    placeholder8_5.empty()
    placeholder9_5.empty()
    placeholder10_5.empty()
    placeholder11_5.empty()
    placeholder12_5.empty()
    placeholder13_5.empty()
    placeholder14_5.empty()
    placeholder15_5.empty()
    st.session_state.IFI=False
    st.session_state.Bonos=True
    Bonos.Bonos(usuario,puesto)
    
    # ----- Salir ---- #
    
  elif salir_5:
    placeholder1_5.empty()
    placeholder2_5.empty()
    placeholder3_5.empty()
    placeholder4_5.empty()
    placeholder5_5.empty()
    placeholder6_5.empty()
    placeholder7_5.empty()
    placeholder8_5.empty()
    placeholder9_5.empty()
    placeholder10_5.empty()
    placeholder11_5.empty()
    placeholder12_5.empty()
    placeholder13_5.empty()
    placeholder14_5.empty()
    placeholder15_5.empty()
    st.session_state.Ingreso = False
    st.session_state.IFI=False
    st.session_state.Salir=True
    Salir.Salir()

  elif reporte_5:

    cursor01=con.cursor()

    marca_5= datetime.now(pytz.timezone('America/Guatemala')).strftime("%Y-%m-%d %H:%M:%S")
    
    nombre_5= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
    nombre_5 = nombre_5.loc[0,'nombre']
      
    horario_5= pd.read_sql(f"select horario from usuarios where usuario ='{usuario}'",uri)
    horario_5 = horario_5.loc[0,'horario']

    supervisor_5= pd.read_sql(f"select supervisor from usuarios where usuario ='{usuario}'",uri)
    supervisor_5 = supervisor_5.loc[0,'supervisor']

    cursor01.execute(f"INSERT INTO registro (marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,predios,horas)VALUES('{marca_5}','{usuario}','{nombre_5}','{horario_5}','{puesto}','{supervisor_5}','Información Final III','{fecha_5}','{bloque_5}','{estado_5}','{tipo_5}','{predios_5}','{horas_5}')")
    con.commit()
    st.success('Reporte enviado correctamente')
