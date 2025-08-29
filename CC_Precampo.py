# ----- Librerías ---- #

import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
import pytz
from urllib.parse import urlparse
import Procesos,Historial,Capacitacion,Otros_Registros,Bonos_Extras,Salir

def CC_Precampo(usuario,puesto):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_3= st.sidebar.empty()
  titulo= placeholder1_3.title("Menú")

  placeholder2_3 = st.sidebar.empty()
  procesos_3 = placeholder2_3.button("Procesos",key="procesos_3")

  placeholder3_3 = st.sidebar.empty()
  historial_3 = placeholder3_3.button("Historial",key="historial_3")

  placeholder4_3 = st.sidebar.empty()
  capacitacion_3 = placeholder4_3.button("Capacitaciones",key="capacitacion_3")

  placeholder5_3 = st.sidebar.empty()
  otros_registros_3 = placeholder5_3.button("Otros Registros",key="otros_registros_3")

  placeholder6_3 = st.sidebar.empty()
  bonos_extras_3 = placeholder6_3.button("Bonos y Extras",key="bonos_extras_3")

  placeholder7_3 = st.sidebar.empty()
  salir_3 = placeholder7_3.button("Salir",key="salir_3")

  placeholder8_3 = st.empty()
  control_calidad_precampo_3 = placeholder8_3.title("Control de Calidad Precampo")

  default_date_3 = datetime.now(pytz.timezone('America/Guatemala'))

  placeholder9_3= st.empty()
  fecha_3= placeholder9_3.date_input("Fecha",value=default_date_3,key="fecha_3")
  
  placeholder10_3= st.empty()
  municipio_3= placeholder10_3.selectbox("Distrito", options=("Chorrillos","San Juan De Miraflores","Villa el Salvador"),key="municipio_3")
  
  placeholder11_3= st.empty()
  manzana_3= placeholder11_3.selectbox("Manzana", options=("001","002","003","004","005","006","007","008","009","010","011","012","013","014","015","016","017","018","019","020","021","022","023","024","025","026","027","028","029","030"), key="manzana_3")

  placeholder12_3= st.empty()
  operador_3= placeholder12_3.selectbox("Operador objeto de CC",options=("Estefanía Aguilar Quirós","Kevin Anchía Román","Kevin Jesús Bonilla Bonilla","María Stefannie Chavarría Barquero","Andrés Mauricio Coto Molina","Pamela  González Arce","Tatiana  Gutiérrez Rojas","Ansil Andrés Hernández Smith","Cristopher Jiménez Serrano","Daniela María Luna Salas","Verónica María Orozco Fernández","Keilor Antonio Quirós Elizondo","José Javier Rojas Arias","Brayan Jose Romero Carazo","Mariel  Sanchez Álvarez","Steve Alberto Sánchez Moreira","Daniel Alfredo Solís Hernández","Seidy Pamela Vivas Sequeira"), key="operador_3")

  placeholder13_3= st.empty()
  tipo_3= placeholder13_3.selectbox("Tipo", options=("Inspección","Primera Reinspección"), key="tipo_3")

  placeholder14_3= st.empty()
  tipo_de_errores_3= placeholder14_3.multiselect("Tipo de Errores", options=("Numeración errónea o incompleta","Errores geométricos y/o de forma","Polígonos y/o puntos duplicados","Omisión/Comisión de polígonos","Polígonos no se ajustan a ortofoto","Omisión/Comisión de puertas"), key="tipo_de_errores_3")

  placeholder15_3= st.empty()
  aprobados_3= placeholder15_3.number_input("Cantidad de Lotes Aprobados",min_value=0,step=1,key="aprobados_3")

  placeholder16_3= st.empty()
  rechazados_3= placeholder16_3.number_input("Cantidad de Lotes Rechazados",min_value=0,step=1,key="rechazados_3")
  
  placeholder17_3= st.empty()
  horas_3= placeholder17_3.number_input("Cantidad de Horas Trabajadas en el Proceso",min_value=0.0,key="horas_3")
  
  placeholder18_3= st.empty()
  sector_3= placeholder18_3.selectbox("Sector", options=("01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"),key="sector_3")
  
  placeholder19_3 = st.empty()
  reporte_3 = placeholder19_3.button("Generar Reporte",key="reporte_3")

  # ----- Procesos ---- #
    
  if procesos_3:
    placeholder1_3.empty()
    placeholder2_3.empty()
    placeholder3_3.empty()
    placeholder4_3.empty()
    placeholder5_3.empty()
    placeholder6_3.empty()
    placeholder7_3.empty()
    placeholder8_3.empty()
    placeholder9_3.empty()
    placeholder10_3.empty()
    placeholder11_3.empty()
    placeholder12_3.empty()
    placeholder13_3.empty()
    placeholder14_3.empty()
    placeholder15_3.empty()
    placeholder16_3.empty()
    placeholder17_3.empty()
    placeholder18_3.empty()#
    placeholder19_3.empty()
    st.session_state.Procesos=False
    st.session_state.CC_FMI=False

    perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
    perfil= perfil.loc[0,'perfil']

    if perfil=="1":        
                    
      Procesos.Procesos1(usuario,puesto)
                
    elif perfil=="2":        
                    
      Procesos.Procesos2(usuario,puesto)   

    elif perfil=="3":  

      Procesos.Procesos3(usuario,puesto)       
  
  #----- Historial ---- #
    
  elif historial_3:
    placeholder1_3.empty()
    placeholder2_3.empty()
    placeholder3_3.empty()
    placeholder4_3.empty()
    placeholder5_3.empty()
    placeholder6_3.empty()
    placeholder7_3.empty()
    placeholder8_3.empty()
    placeholder9_3.empty()
    placeholder10_3.empty()
    placeholder11_3.empty()
    placeholder12_3.empty()
    placeholder13_3.empty()
    placeholder14_3.empty()
    placeholder15_3.empty()
    placeholder16_3.empty()
    placeholder17_3.empty()
    placeholder18_3.empty()#
    placeholder19_3.empty()
    st.session_state.CC_FMI=False
    st.session_state.Historial=True
    Historial.Historial(usuario,puesto)   

  # ----- Capacitación ---- #
    
  elif capacitacion_3:
    placeholder1_3.empty()
    placeholder2_3.empty()
    placeholder3_3.empty()
    placeholder4_3.empty()
    placeholder5_3.empty()
    placeholder6_3.empty()
    placeholder7_3.empty()
    placeholder8_3.empty()
    placeholder9_3.empty()
    placeholder10_3.empty()
    placeholder11_3.empty()
    placeholder12_3.empty()
    placeholder13_3.empty()
    placeholder14_3.empty()
    placeholder15_3.empty()
    placeholder16_3.empty()
    placeholder17_3.empty()
    placeholder18_3.empty()#
    placeholder19_3.empty()
    st.session_state.CC_FMI=False
    st.session_state.Capacitacion=True
    Capacitacion.Capacitacion(usuario,puesto)

  # ----- Otros Registros ---- #
    
  elif otros_registros_3:
    placeholder1_3.empty()
    placeholder2_3.empty()
    placeholder3_3.empty()
    placeholder4_3.empty()
    placeholder5_3.empty()
    placeholder6_3.empty()
    placeholder7_3.empty()
    placeholder8_3.empty()
    placeholder9_3.empty()
    placeholder10_3.empty()
    placeholder11_3.empty()
    placeholder12_3.empty()
    placeholder13_3.empty()
    placeholder14_3.empty()
    placeholder15_3.empty()
    placeholder16_3.empty()
    placeholder17_3.empty()
    placeholder18_3.empty()#
    placeholder19_3.empty()
    st.session_state.CC_FMI=False
    st.session_state.Otros_Registros=True
    Otros_Registros.Otros_Registros(usuario,puesto)

  # ----- Bonos y Horas Extras ---- #
    
  elif bonos_extras_3:
    placeholder1_3.empty()
    placeholder2_3.empty()
    placeholder3_3.empty()
    placeholder4_3.empty()
    placeholder5_3.empty()
    placeholder6_3.empty()
    placeholder7_3.empty()
    placeholder8_3.empty()
    placeholder9_3.empty()
    placeholder10_3.empty()
    placeholder11_3.empty()
    placeholder12_3.empty()
    placeholder13_3.empty()
    placeholder14_3.empty()
    placeholder15_3.empty()
    placeholder16_3.empty()
    placeholder17_3.empty()
    placeholder18_3.empty()#
    placeholder19_3.empty()
    st.session_state.CC_FMI=False
    st.session_state.Bonos_Extras=True
    Bonos_Extras.Bonos_Extras(usuario,puesto)    

    # ----- Salir ---- #
    
  elif salir_3:
    placeholder1_3.empty()
    placeholder2_3.empty()
    placeholder3_3.empty()
    placeholder4_3.empty()
    placeholder5_3.empty()
    placeholder6_3.empty()
    placeholder7_3.empty()
    placeholder8_3.empty()
    placeholder9_3.empty()
    placeholder10_3.empty()
    placeholder11_3.empty()
    placeholder12_3.empty()
    placeholder13_3.empty()
    placeholder14_3.empty()
    placeholder15_3.empty()
    placeholder16_3.empty()
    placeholder17_3.empty()
    placeholder18_3.empty()#
    placeholder19_3.empty()
    st.session_state.Ingreso = False
    st.session_state.CC_FMI=False
    st.session_state.Salir=True
    Salir.Salir()

  elif reporte_3:

    cursor01=con.cursor()

    marca_3= datetime.now(pytz.timezone('America/Bogota')).strftime("%Y-%m-%d %H:%M:%S")
    
    nombre_3= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
    nombre_3 = nombre_3.loc[0,'nombre']
      
    supervisor_3= pd.read_sql(f"select supervisor from usuarios where usuario ='{usuario}'",uri)
    supervisor_3 = supervisor_3.loc[0,'supervisor']

    produccion_3 = aprobados_3 + rechazados_3

    semana_3 = fecha_3.isocalendar()[1]

    año_3 = fecha_3.isocalendar()[0]

    unidad_3=municipio_3

    horas_bi = float(horas_3)
    
    tipos_de_errores_3 = ',' .join(tipo_de_errores_3)

    conteo_3 = len(tipo_de_errores_3)

    
      # ----- Almacenar Lote_3 según municipio seleccionado ---- #
    
    #lote_3_municipios = {"Cabuyaro", "Colombia", "San Luis de Cubarral"}#
    #lote_2_municipios = {"Trinidad", "Iza", "Cuítiva"}#
   
    #if municipio_3 in lote_3_municipios:#
      #lote_3 = '3'#
    #elif municipio_3 in lote_2_municipios:#
      #lote_3 = '2'#
    #else:#
      #lote_3 = '1'#
      # ----- Fin del script ---- #
    
    cursor01.execute(f"INSERT INTO registro (marca,usuario,nombre,puesto,supervisor,proceso,fecha,semana,año,unidad_asignacion,tipo,produccion,aprobados,rechazados,horas,uit,hito,lote,estado,area,efes,informales,paquete,con_fmi,sin_fmi,observaciones,zona,tipo_calidad,horas_bi,area_bi,operador_cc,total_de_errores,errores_por_excepciones,tipo_de_errores,conteo_de_errores)VALUES('{marca_3}','{usuario}','{nombre_3}','{puesto}','{supervisor_3}','Control de Calidad Precampo','{fecha_3}','{semana_3}','{año_3}','{unidad_3}','{tipo_3}','{produccion_3}','{aprobados_3}','{rechazados_3}','{horas_3}','UIT-0','0','0','N/A','0.0','0','0','N/A','0','0','N/A','{manzana_3}','{sector_bi}','{horas_bi}','0','{operador_3}','0','0','{tipos_de_errores_3}','{conteo_3}')")
    con.commit()                                                                                                                                 
    st.success('Reporte enviado correctamente')
