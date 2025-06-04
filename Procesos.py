# ----- Librerías ---- #

import streamlit as st
import Historial, Capacitacion, Otros_Registros, Bonos_Extras, Salir, FMI, CC_FMI, Consulta_Campo, Precampo, CC_Precampo, Validacion, CC_Validacion

def Procesos1(usuario,puesto):

    st.session_state.Ingreso=True

    if st.session_state.Procesos==False: 

        placeholder1_2= st.sidebar.empty()
        titulo= placeholder1_2.title("Menú")

        placeholder2_2= st.sidebar.empty()
        historial_2 = placeholder2_2.button("Historial",key="historial_2")

        placeholder3_2 = st.sidebar.empty()
        capacitacion_2 = placeholder3_2.button("Capacitaciones",key="capacitacion_2")

        placeholder4_2 = st.sidebar.empty()
        otros_registros_2 = placeholder4_2.button("Otros Registros",key="otros_registros_2")

        placeholder5_2 = st.sidebar.empty()
        bonos_extras_2 = placeholder5_2.button("Bonos y Horas Extras",key="bonos_extras_2")

        placeholder6_2 = st.sidebar.empty()
        salir_2 = placeholder6_2.button("Salir",key="salir_2")

        placeholder7_2 = st.empty()
        procesos_2 = placeholder7_2.title("Procesos")

        placeholder8_2 = st.empty()
        fmi_2 = placeholder8_2.button("Folios de Matricula Inmobiliaria",key="fmi_2")

        placeholder9_2 = st.empty()
        cc_fmi_2 = placeholder9_2.button("Control de Calidad Folios de Matricula Inmobiliaria",key="cc_fmi_2")

        placeholder10_2 = st.empty()
        consulta_campo_2 = placeholder10_2.button("Consultas de Campo",key="consulta_campo_2")

        placeholder11_2 = st.empty()
        precampo_2 = placeholder11_2.button("Precampo",key="precampo_2")

        placeholder12_2 = st.empty()
        cc_precampo_2 = placeholder12_2.button("Control de Calidad Precampo",key="cc_precampo_2")

        placeholder13_2 = st.empty()
        validacion_2 = placeholder13_2.button("Validación",key="validacion_2")

        placeholder14_2 = st.empty()
        cc_validacion_2 = placeholder14_2.button("Control de Calidad Validación",key="cc_validacion_2")

        # ----- Historial ---- #

        if historial_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            placeholder11_2.empty()
            placeholder12_2.empty()
            placeholder13_2.empty()
            placeholder14_2.empty()
            st.session_state.Procesos=True
            st.session_state.Historial=True
            Historial.Historial(usuario,puesto)

        # ----- Capacitación ---- #

        elif capacitacion_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            placeholder11_2.empty()
            placeholder12_2.empty()
            placeholder13_2.empty()
            placeholder14_2.empty()            
            st.session_state.Procesos=True
            st.session_state.Capacitacion=True
            Capacitacion.Capacitacion(usuario,puesto)

        # ----- Otros Registros ---- #

        elif otros_registros_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            placeholder11_2.empty()
            placeholder12_2.empty()
            placeholder13_2.empty()
            placeholder14_2.empty()        
            st.session_state.Procesos=True
            st.session_state.Otros_Registros=True
            Otros_Registros.Otros_Registros(usuario,puesto)

        # ----- Bonos y Horas Extras ---- #

        elif bonos_extras_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            placeholder11_2.empty()
            placeholder12_2.empty()
            placeholder13_2.empty()
            placeholder14_2.empty()
            st.session_state.Procesos=True
            st.session_state.Bonos_Extras=True
            Bonos_Extras.Bonos_Extras(usuario,puesto)

        # ----- Salir ---- #

        elif salir_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            placeholder11_2.empty()
            placeholder12_2.empty()
            placeholder13_2.empty()
            placeholder14_2.empty()
            st.session_state.Ingreso= False
            st.session_state.Procesos=True
            st.session_state.Salir=True
            Salir.Salir()

        # ----- FMI ---- #

        elif fmi_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            placeholder11_2.empty()
            placeholder12_2.empty()
            placeholder13_2.empty()
            placeholder14_2.empty()
            st.session_state.Procesos=True
            st.session_state.FMI=True
            FMI.FMI(usuario,puesto)
        
        # ----- Control de Calidad FMI ---- #

        elif cc_fmi_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            placeholder11_2.empty()
            placeholder12_2.empty()
            placeholder13_2.empty()
            placeholder14_2.empty()
            st.session_state.Procesos=True
            st.session_state.CC_FMI=True
            CC_FMI.CC_FMI(usuario,puesto)
            
        # ----- Consultas de Campo ---- #

        elif consulta_campo_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            placeholder11_2.empty()
            placeholder12_2.empty()
            placeholder13_2.empty()
            placeholder14_2.empty()
            st.session_state.Procesos=True
            st.session_state.Consulta_Campo=True
            Consulta_Campo.Consulta_Campo(usuario,puesto)

        # ----- Precampo ---- #

        elif precampo_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            placeholder11_2.empty()
            placeholder12_2.empty()
            placeholder13_2.empty()
            placeholder14_2.empty()
            st.session_state.Procesos=True
            st.session_state.Precampo=True
            Precampo.Precampo(usuario,puesto)

        # ----- CC_Precampo ---- #

        elif cc_precampo_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            placeholder11_2.empty()
            placeholder12_2.empty()
            placeholder13_2.empty()
            placeholder14_2.empty()
            st.session_state.Procesos=True
            st.session_state.CC_Precampo=True
            CC_Precampo.CC_Precampo(usuario,puesto)

        # ----- Validación ---- #

        elif validacion_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            placeholder11_2.empty()
            placeholder12_2.empty()
            placeholder13_2.empty()
            placeholder14_2.empty()
            st.session_state.Procesos=True
            st.session_state.Validacion=True
            Validacion.Validacion(usuario,puesto)

         # ----- CC Validación ---- #

        elif cc_validacion_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            placeholder11_2.empty()
            placeholder12_2.empty()
            placeholder13_2.empty()
            placeholder14_2.empty()
            st.session_state.Procesos=True
            st.session_state.CC_Validacion=True
            CC_Validacion.CC_Validacion(usuario,puesto)
   
    elif st.session_state.Procesos==True:

        if st.session_state.Historial==True:
            Historial.Historial(usuario,puesto)

        elif st.session_state.Capacitacion==True:
            Capacitacion.Capacitacion(usuario,puesto)

        elif st.session_state.Otros_Registros==True:
            Otros_Registros.Otros_Registros(usuario,puesto)

        elif st.session_state.Bonos_Extras==True:
            Bonos_Extras.Bonos_Extras(usuario,puesto)

        elif st.session_state.FMI==True:
            FMI.FMI(usuario,puesto)

        elif st.session_state.CC_FMI==True:
            CC_FMI.CC_FMI(usuario,puesto)

        elif st.session_state.Consulta_Campo==True:
            Consulta_Campo.Consulta_Campo(usuario,puesto)

        elif st.session_state.Precampo==True:
            Precampo.Precampo(usuario,puesto)

        elif st.session_state.CC_Precampo==True:
            CC_Precampo.CC_Precampo(usuario,puesto)

        elif st.session_state.Validacion==True:
            Validacion.Validacion(usuario,puesto)

        elif st.session_state.CC_Validacion==True:
            CC_Validacion.CC_Validacion(usuario,puesto)
            
# ----- Procesos 2 ---- #

def Procesos2(usuario,puesto):

    st.session_state.Ingreso=True

    if st.session_state.Procesos==False:

        placeholder1_2= st.sidebar.empty()
        titulo= placeholder1_2.title("Menú")

        placeholder2_2= st.sidebar.empty()
        historial_2 = placeholder2_2.button("Historial",key="historial_2")

        placeholder3_2 = st.sidebar.empty()
        capacitacion_2 = placeholder3_2.button("Capacitaciones",key="capacitacion_2")

        placeholder4_2 = st.sidebar.empty()
        otros_registros_2 = placeholder4_2.button("Otros Registros",key="otros_registros_2")

        placeholder5_2 = st.sidebar.empty()
        bonos_extras_2 = placeholder5_2.button("Bonos y Horas Extras",key="bonos_extras_2")

        placeholder6_2 = st.sidebar.empty()
        salir_2 = placeholder6_2.button("Salir",key="salir_2")

        placeholder7_2 = st.empty()
        registro_2 = placeholder7_2.title("Procesos")

        placeholder8_2 = st.empty()
        precampo_2 = placeholder8_2.button("Precampo",key="precampo_2")

        placeholder9_2 = st.empty()
        cc_precampo_2 = placeholder9_2.button("Control de Calidad Precampo",key="cc_precampo_2")

        placeholder10_2 = st.empty()
        validacion_2 = placeholder10_2.button("Validación",key="validacion_2")

        placeholder11_2 = st.empty()
        cc_validacion_2 = placeholder11_2.button("Control de Calidad Validación",key="cc_validacion_2")
       
        # ----- Historial ---- #

        if historial_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            placeholder11_2.empty()
            st.session_state.Procesos=True
            st.session_state.Historial=True
            Historial.Historial(usuario,puesto)

        # ----- Capacitación ---- #

        elif capacitacion_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            placeholder11_2.empty()
            st.session_state.Procesos=True
            st.session_state.Capacitacion=True
            Capacitacion.Capacitacion(usuario,puesto)

        # ----- Otros Registros ---- #

        elif otros_registros_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            placeholder11_2.empty()
            st.session_state.Procesos=True
            st.session_state.Otros_Registros=True
            Otros_Registros.Otros_Registros(usuario,puesto)

        # ----- Bonos y Horas Extras ---- #

        elif bonos_extras_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            placeholder11_2.empty()
            st.session_state.Procesos=True
            st.session_state.Bonos_Extras=True
            Bonos_Extras.Bonos_Extras(usuario,puesto)

        # ----- Salir ---- #

        elif salir_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            placeholder11_2.empty()
            st.session_state.Ingreso = False
            st.session_state.Procesos=True
            st.session_state.Salir=True
            Salir.Salir()

        # ----- Precampo ---- #

        elif precampo_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            placeholder11_2.empty()
            st.session_state.Procesos=True
            st.session_state.Precampo=True
            Precampo.Precampo(usuario,puesto)

        # ----- CC Precampo ---- #

        elif cc_precampo_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            placeholder11_2.empty()
            st.session_state.Procesos=True
            st.session_state.CC_Precampo=True
            CC_Precampo.CC_Precampo(usuario,puesto)

        # ----- Validacion ---- #

        elif validacion_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            placeholder11_2.empty()
            st.session_state.Procesos=True
            st.session_state.Validacion=True
            Validacion.Validacion(usuario,puesto)
            
        # ----- CC_Validacion ---- #

        elif cc_validacion_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            placeholder11_2.empty()
            st.session_state.Procesos=True
            st.session_state.CC_Validacion=True
            CC_Validacion.CC_Validacion(usuario,puesto)
            
    elif st.session_state.Procesos==True:

        if st.session_state.Historial==True:
            Historial.Historial(usuario,puesto)

        elif st.session_state.Capacitacion==True:
            Capacitacion.Capacitacion(usuario,puesto)

        elif st.session_state.Otros_Registros==True:
            Otros_Registros.Otros_Registros(usuario,puesto)

        elif st.session_state.Bonos_Extras==True:
            Bonos_Extras.Bonos_Extras(usuario,puesto)

        elif st.session_state.Precampo==True:
            Precampo.Precampo(usuario,puesto)

        elif st.session_state.CC_Precampo==True:
            CC_Precampo.CC_Precampo(usuario,puesto)

        elif st.session_state.Validacion==True:
            Validacion.Validacion(usuario,puesto)

        elif st.session_state.CC_Validacion==True:
            CC_Validacion.CC_Validacion(usuario,puesto)

# ----- Procesos 3 ---- #

def Procesos3(usuario,puesto):

    st.session_state.Ingreso=True

    if st.session_state.Procesos==False:

        placeholder1_2= st.sidebar.empty()
        titulo= placeholder1_2.title("Menú")

        placeholder2_2= st.sidebar.empty()
        historial_2 = placeholder2_2.button("Historial",key="historial_2")

        placeholder3_2 = st.sidebar.empty()
        capacitacion_2 = placeholder3_2.button("Capacitaciones",key="capacitacion_2")

        placeholder4_2 = st.sidebar.empty()
        otros_registros_2 = placeholder4_2.button("Otros Registros",key="otros_registros_2")

        placeholder5_2 = st.sidebar.empty()
        bonos_extras_2 = placeholder5_2.button("Bonos y Horas Extras",key="bonos_extras_2")

        placeholder6_2 = st.sidebar.empty()
        salir_2 = placeholder6_2.button("Salir",key="salir_2")

        placeholder7_2 = st.empty()
        registro_2 = placeholder7_2.title("Procesos")

        placeholder8_2 = st.empty()
        fmi_2 = placeholder8_2.button("Folios de Matricula Inmobiliaria",key="fmi_2")

        placeholder9_2 = st.empty()
        cc_fmi_2 = placeholder9_2.button("Control de Calidad Folios de Matricula Inmobiliaria",key="cc_fmi_2")

        placeholder10_2 = st.empty()
        consulta_campo_2 = placeholder10_2.button("Consultas de Campo",key="consulta_campo_2")
              
       # ----- Historial ---- #

        if historial_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            st.session_state.Procesos=True
            st.session_state.Historial=True
            Historial.Historial(usuario,puesto)

        # ----- Capacitación ---- #

        elif capacitacion_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            st.session_state.Procesos=True
            st.session_state.Capacitacion=True
            Capacitacion.Capacitacion(usuario,puesto)

        # ----- Otros Registros ---- #

        elif otros_registros_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            st.session_state.Procesos=True
            st.session_state.Otros_Registros=True
            Otros_Registros.Otros_Registros(usuario,puesto)

        # ----- Bonos y Horas Extras ---- #

        elif bonos_extras_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            st.session_state.Procesos=True
            st.session_state.Bonos_Extras=True
            Bonos_Extras.Bonos_Extras(usuario,puesto)

        # ----- Salir ---- #

        elif salir_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            st.session_state.Ingreso = False
            st.session_state.Procesos = True
            st.session_state.Salir=True
            Salir.Salir()

        # ----- FMI ---- #

        elif fmi_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            st.session_state.Procesos=True
            st.session_state.FMI=True
            FMI.FMI(usuario,puesto)

        # ----- CC_FMI ---- #

        elif cc_fmi_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            st.session_state.Procesos=True
            st.session_state.CC_FMI=True
            CC_FMI.CC_FMI(usuario,puesto)
            
        # ----- Consulta Campo ---- #

        elif consulta_campo_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            placeholder10_2.empty()
            st.session_state.Procesos=True
            st.session_state.Consulta_Campo=True
            Consulta_Campo.Consulta_Campo(usuario,puesto)
      
    elif st.session_state.Procesos==True:

        if st.session_state.Historial==True:
            Historial.Historial(usuario,puesto)       

        elif st.session_state.Capacitacion==True:
            Capacitacion.Capacitacion(usuario,puesto)

        elif st.session_state.Otros_Registros==True:
            Otros_Registros.Otros_Registros(usuario,puesto)

        elif st.session_state.Bonos_Extras==True:
            Bonos_Extras.Bonos_Extras(usuario,puesto)

        elif st.session_state.FMI==True:
            FMI.FMI(usuario,puesto)
        
        elif st.session_state.CC_FMI==True:
            CC_FMI.CC_FMI(usuario,puesto)

        elif st.session_state.Consulta_Campo==True:
            Consulta_Campo.Consulta_Campo(usuario,puesto)

