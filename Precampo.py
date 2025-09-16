# ----- Librerías ---- #

import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
import pytz
from urllib.parse import urlparse
import Procesos,Historial,Capacitacion,Otros_Registros,Bonos_Extras,Salir

def Precampo(usuario,puesto):

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
  bonos_extras_3 = placeholder6_3.button("Bonos y Horas Extras",key="bonos_extras_3")

  placeholder7_3 = st.sidebar.empty()
  salir_3 = placeholder7_3.button("Salir",key="salir_3")

  placeholder8_3 = st.empty()
  precampo_3 = placeholder8_3.title("Precampo")

  default_date_3 = datetime.now(pytz.timezone('America/Guatemala'))

  placeholder9_3= st.empty()
  fecha_3= placeholder9_3.date_input("Fecha",value=default_date_3,key="fecha_3")
  
  placeholder10_3= st.empty()
  distrito_3= placeholder10_3.selectbox("Distrito", options=("Chorrillos","San Juan De Miraflores","Villa el Salvador"),key="distrito_3")
  
  placeholder11_3= st.empty()
  sector_3= placeholder11_3.selectbox("Sector", options=("01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100","101","102","103","104","105","106","107","108","109","110","111","112","113","114","115","116","117","118","119","120"),key="sector_3")

  placeholder12_3= st.empty()
  manzana_3= placeholder12_3.selectbox("Manzana", options=("001","002","003","004","005","006","007","008","009","010","011","012","013","014","015","016","017","018","019","020","021","022","023","024","025","026","027","028","029","030","031","032","033","034","035","036","037","038","039","040","041","042","043","044","045","046","047","048","049","050","051","052","053","054","055","056","057","058","058","059","060","061","062","063","064","065","066","067","068","069","070","071","072","073","074","075","076","077","078","079","080","081","082","083","084","085","086","087","088","089","090","091","092","093","094","095","096","097","098","099","100","101","102","103","104","105","106","107","108","109","110","111","112","113","114","115","116","117","118","119","120"),key="manzana_3")

  #placeholder13_3= st.empty()
  #zona_3= placeholder13_3.selectbox("Zona",options=("Urbano","Rural","Sin Geometría"),key="zona_3")
  
  placeholder14_3= st.empty()
  tipo_3= placeholder14_3.selectbox("Tipo", options=("Ordinario","Reproceso Ordinario","Corrección de Calidad"),key="tipo_3")
  
  placeholder15_3= st.empty()
  estado_3= placeholder15_3.selectbox("Estado" , options=("Finalizado", "En conflicto"),key="estado_3")
  
  placeholder16_3= st.empty()
  lotes_3= placeholder16_3.number_input("Cantidad Total de Lotes Producidos",min_value=0,key="lotes_3")

  placeholder17_3= st.empty()
  edficas_3= placeholder17_3.number_input("Cantidad de Edficas",min_value=0,key="edficas_3")
  
  #placeholder18_3= st.empty()
  #efes_3= placeholder18_3.number_input("Cantidad de Construcciones",min_value=0,key="efes_3")
  
  placeholder19_3= st.empty()
  horas_3= placeholder19_3.number_input("Cantidad de Horas Trabajadas en el Proceso",min_value=0.0,key="horas_3")

  placeholder20_3= st.empty()
  observaciones_3= placeholder20_3.text_input("Observaciones", max_chars=60, key="observaciones_3")

  placeholder21_3 = st.empty()
  reporte_3 = placeholder21_3.button("Generar Reporte",key="reporte_3")

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
    #placeholder13_3.empty()
    placeholder14_3.empty()
    placeholder15_3.empty()
    placeholder16_3.empty()
    placeholder17_3.empty()
    #placeholder18_3.empty()
    placeholder19_3.empty()
    placeholder20_3.empty()
    placeholder21_3.empty()
    st.session_state.Procesos=False
    st.session_state.Precampo=False

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
    #placeholder13_3.empty()
    placeholder14_3.empty()
    placeholder15_3.empty()
    placeholder16_3.empty()
    placeholder17_3.empty()
    #placeholder18_3.empty()
    placeholder19_3.empty()
    placeholder20_3.empty()
    placeholder21_3.empty()
    st.session_state.Precampo=False
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
    #placeholder13_3.empty()
    placeholder14_3.empty()
    placeholder15_3.empty()
    placeholder16_3.empty()
    placeholder17_3.empty()
    #placeholder18_3.empty()
    placeholder19_3.empty()
    placeholder20_3.empty()
    placeholder21_3.empty()
    st.session_state.Precampo=False
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
    #placeholder13_3.empty()
    placeholder14_3.empty()
    placeholder15_3.empty()
    placeholder16_3.empty()
    placeholder17_3.empty()
    #placeholder18_3.empty()
    placeholder19_3.empty()
    placeholder20_3.empty()
    placeholder21_3.empty()
    st.session_state.Precampo=False
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
    #placeholder13_3.empty()
    placeholder14_3.empty()
    placeholder15_3.empty()
    placeholder16_3.empty()
    placeholder17_3.empty()
    #placeholder18_3.empty()
    placeholder19_3.empty()
    placeholder20_3.empty()
    placeholder21_3.empty()
    st.session_state.Precampo=False
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
    #placeholder13_3.empty()
    placeholder14_3.empty()
    placeholder15_3.empty()
    placeholder16_3.empty()
    placeholder17_3.empty()
    #placeholder18_3.empty()
    placeholder19_3.empty()
    placeholder20_3.empty()
    placeholder21_3.empty()
    st.session_state.Ingreso = False
    st.session_state.Precampo=False
    st.session_state.Salir=True
    Salir.Salir()

  elif reporte_3:

    cursor01=con.cursor()

    marca_3= datetime.now(pytz.timezone('America/Guatemala')).strftime("%Y-%m-%d %H:%M:%S")
    
    nombre_3= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
    nombre_3 = nombre_3.loc[0,'nombre']
      
    supervisor_3= pd.read_sql(f"select supervisor from usuarios where usuario ='{usuario}'",uri)
    supervisor_3 = supervisor_3.loc[0,'supervisor']
 
    semana_3 = fecha_3.isocalendar()[1]

    año_3 = fecha_3.isocalendar()[0]



      # ----- Almacenar Lote_3 según municipio seleccionado ---- #
    
    #lote_3_municipios = {"Cabuyaro", "Colombia", "San Luis de Cubarral"}
    #lote_2_municipios = {"Trinidad", "Iza", "Cuítiva"}
   
    #if municipio_3 in lote_3_municipios:
      #lote_3 = '3'
    #elif municipio_3 in lote_2_municipios:
      #lote_3 = '2'
    #else:
      #lote_3 = '1'
      # ----- Fin del script ---- #
    
    horas_bi = float(horas_3)
    area_bi = float(0.0)

    
    cursor01.execute(f"INSERT INTO registro (marca,usuario,nombre,puesto,supervisor,proceso,fecha,semana,año,distrito,tipo,lote,aprobados,rechazados,horas,manzana,sector,lote,estado,area,efes,edificas,paquete,con_fmi,sin_fmi,observaciones,zona,tipo_calidad,horas_bi,area_bi,operador_cc,total_de_errores,errores_por_excepciones,tipo_de_errores,conteo_de_errores)VALUES('{marca_3}','{usuario}','{nombre_3}','{puesto}','{supervisor_3}','Precampo','{fecha_3}','{semana_3}','{año_3}','{distrito_3}','{tipo_3}','{lotes_3}','0','0','{horas_3}','{manzana_3}','{sector_3}','0','{estado_3}','0.0','0','{edficas_3}','P0','0','0','{observaciones_3}','N/A','N/A','{horas_bi}','{area_bi}','N/A','0','0','N/A','0')")
    con.commit()                                                                                                                                 
    st.success('Reporte enviado correctamente')
