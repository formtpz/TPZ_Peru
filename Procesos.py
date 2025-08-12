# ----- Librerías ---- #

import streamlit as st
import Historial, Capacitacion, Otros_Registros, Bonos_Extras, Salir, FMI, Consulta_Campo,Restitucion_Tierras,Revision_Segregados,Estado_UIT_Hito,Precampo, CC_Precampo, Preparacion_Insumos, Revision_Campo, Validacion, CC_Validacion

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
        fmi_2 = placeholder8_2.button("Procesos Jurídico", key="fmi_2")

        placeholder9_2 = st.empty()
        consulta_campo_2 = placeholder9_2.button("Consultas de Campo",key="consulta_campo_2")

        placeholder10_2 = st.empty()
        precampo_2 = placeholder10_2.button("Precampo",key="precampo_2")

        placeholder11_2 = st.empty()
        cc_precampo_2 = placeholder11_2.button("Control de Calidad Precampo",key="cc_precampo_2")
        
        placeholder12_2 = st.empty()
        preparacion_insumos_2 = placeholder12_2.button("Preparación de Insumos",key="preparacion_insumos_2") 
        
        placeholder13_2 = st.empty()
        revision_campo_2 = placeholder13_2.button("Revisión de Campo",key="revision_campo_2")

        placeholder14_2 = st.empty()
        validacion_2 = placeholder14_2.button(":blue[Postcampo]",key="validacion_2")

        placeholder15_2 = st.empty()
        cc_validacion_2 = placeholder15_2.button(":blue[Control de Calidad Postcampo]",key="cc_validacion_2")

        placeholder16_2 = st.empty()
        restitucion_tierras_2 = placeholder16_2.button("Restitución de Tierras",key="restitucion_tierras_2")

        placeholder17_2 = st.empty()
        revision_segregados_2 = placeholder17_2.button("Revisión de Predios Segregados",key="revision_segregados_2")

        placeholder18_2 = st.empty()
        estado_uit_hito_2 = placeholder18_2.button("Calidad Externa XTF",key="estado_uit_hito_2")

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
            placeholder15_2.empty()
            placeholder16_2.empty()
            placeholder17_2.empty()
            placeholder18_2.empty()
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
            placeholder15_2.empty()
            placeholder16_2.empty()
            placeholder17_2.empty()
            placeholder18_2.empty()
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
            placeholder15_2.empty()
            placeholder16_2.empty()
            placeholder17_2.empty()
            placeholder18_2.empty()
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
            placeholder15_2.empty()
            placeholder16_2.empty()
            placeholder17_2.empty()
            placeholder18_2.empty()
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
            placeholder15_2.empty()
            placeholder16_2.empty()
            placeholder17_2.empty()
            placeholder18_2.empty()
            st.session_state.Ingreso= False
            st.session_state.Procesos=True
            st.session_state.Salir=True
            Salir.Salir()
            
             # -----  FMI ---- #

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
            placeholder15_2.empty()
            placeholder16_2.empty()
            placeholder17_2.empty()
            placeholder18_2.empty()
            st.session_state.Procesos=True
            st.session_state.FMI=True
            FMI.FMI(usuario,puesto)
                
                  
               
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
            placeholder15_2.empty()
            placeholder16_2.empty()
            placeholder17_2.empty()
            placeholder18_2.empty()
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
            placeholder15_2.empty()
            placeholder16_2.empty()
            placeholder17_2.empty()
            placeholder18_2.empty()
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
            placeholder15_2.empty()
            placeholder16_2.empty()
            placeholder17_2.empty()
            placeholder18_2.empty()
            st.session_state.Procesos=True
            st.session_state.CC_Precampo=True
            CC_Precampo.CC_Precampo(usuario,puesto)
            
        # ----- Preparación de Insumos ---- #

        elif preparacion_insumos_2:

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
            placeholder15_2.empty()
            placeholder16_2.empty()
            placeholder17_2.empty()
            placeholder18_2.empty()
            st.session_state.Procesos=True
            st.session_state.Preparacion_Insumos=True
            Preparacion_Insumos.Preparacion_Insumos(usuario,puesto)

          # ----- Revisión de Campo ---- #

        elif revision_campo_2:

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
            placeholder15_2.empty()
            placeholder16_2.empty()
            placeholder17_2.empty()
            placeholder18_2.empty()
            st.session_state.Procesos=True
            st.session_state.Revision_Campo=True
            Revision_Campo.Revision_Campo(usuario,puesto)

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
            placeholder15_2.empty()
            placeholder16_2.empty()
            placeholder17_2.empty()
            placeholder18_2.empty()
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
            placeholder15_2.empty()
            placeholder16_2.empty()
            placeholder17_2.empty()
            placeholder18_2.empty()
            st.session_state.Procesos=True
            st.session_state.CC_Validacion=True
            CC_Validacion.CC_Validacion(usuario,puesto)

        # ----- Restitución de Tierras ---- #

        elif restitucion_tierras_2:

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
            placeholder15_2.empty()
            placeholder16_2.empty()
            placeholder17_2.empty()
            placeholder18_2.empty()
            st.session_state.Procesos=True
            st.session_state.Restitucion_Tierras=True
            Restitucion_Tierras.Restitucion_Tierras(usuario,puesto)

        # ----- Revisión de Predios Segredados ---- #

        elif revision_segregados_2:

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
            placeholder15_2.empty()
            placeholder16_2.empty()
            placeholder17_2.empty()
            placeholder18_2.empty()
            st.session_state.Procesos=True
            st.session_state.Revision_Segregados=True
            Revision_Segregados.Revision_Segregados(usuario,puesto)
                   
        # ----- Estado UIT Hito ---- #

        elif estado_uit_hito_2:

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
            placeholder15_2.empty()
            placeholder16_2.empty()
            placeholder17_2.empty()
            placeholder18_2.empty()
            st.session_state.Procesos=True
            st.session_state.Estado_UIT_Hito=True
            Estado_UIT_Hito.Estado_UIT_Hito(usuario,puesto)

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
           
        elif st.session_state.Postcampo_FMI==True:
            Postcampo_FMI.Postcampo_FMI(usuario,puesto)

        elif st.session_state.Consulta_Campo==True:
            Consulta_Campo.Consulta_Campo(usuario,puesto)

        elif st.session_state.Precampo==True:
            Precampo.Precampo(usuario,puesto)

        elif st.session_state.CC_Precampo==True:
            CC_Precampo.CC_Precampo(usuario,puesto)

        elif st.session_state.Preparacion_Insumos==True:
            Preparacion_Insumos.Preparacion_Insumos(usuario,puesto)
            
        elif st.session_state.Revision_Campo==True:
            Revision_Campo.Revision_Campo(usuario,puesto)

        elif st.session_state.Validacion==True:
            Validacion.Validacion(usuario,puesto)

        elif st.session_state.CC_Validacion==True:
            CC_Validacion.CC_Validacion(usuario,puesto)

        elif st.session_state.Restitucion_Tierras==True:
            Restitucion_Tierras.Restitucion_Tierras(usuario,puesto)

        elif st.session_state.Revision_Segregados==True:
            Revision_Segregados.Revision_Segregados(usuario,puesto)
            
        elif st.session_state.Estado_UIT_Hito==True:
            Estado_UIT_Hito.Estado_UIT_Hito(usuario,puesto)
            
# ----- Procesos 2 (Gabinete) ---- #

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
        preparacion_insumos_2 = placeholder10_2.button("Preparación de Insumos",key="preparacion_insumos_2")

        placeholder11_2 = st.empty()
        revision_campo_2 = placeholder11_2.button("Revisión de Campo",key="revision_campo_2")

        placeholder12_2 = st.empty()
        validacion_2 = placeholder12_2.button("Postcampo",key="validacion_2")

        placeholder13_2 = st.empty()
        cc_validacion_2 = placeholder13_2.button("Control de Calidad Postcampo",key="cc_validacion_2")
       
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
            placeholder12_2.empty()
            placeholder13_2.empty()
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
            placeholder12_2.empty()
            placeholder13_2.empty()
            st.session_state.Procesos=True
            st.session_state.CC_Precampo=True
            CC_Precampo.CC_Precampo(usuario,puesto)

        # ----- Preparación de Insumos ---- #

        elif preparacion_insumos_2:

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
            st.session_state.Procesos=True
            st.session_state.Preparacion_Insumos=True
            Preparacion_Insumos.Preparacion_Insumos(usuario,puesto)

         # ----- Revisión de Campo ---- #

        elif revision_campo_2:

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
            st.session_state.Procesos=True
            st.session_state.Revision_Campo=True
            Revision_Campo.Revision_Campo(usuario,puesto)

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
            placeholder12_2.empty()
            placeholder13_2.empty()
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
            placeholder12_2.empty()
            placeholder13_2.empty()
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

        elif st.session_state.Preparacion_Insumos==True:
            Preparacion_Insumos.Preparacion_Insumos(usuario,puesto)
        
        elif st.session_state.Revision_Campo==True:
            Revision_Campo.Revision_Campo(usuario,puesto)

        elif st.session_state.Validacion==True:
            Validacion.Validacion(usuario,puesto)

        elif st.session_state.CC_Validacion==True:
            CC_Validacion.CC_Validacion(usuario,puesto)

# ----- Procesos 3 (Jurídicos) ---- #

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
        consulta_campo_2 = placeholder9_2.button("Consultas de Campo",key="consulta_campo_2")

        placeholder10_2 = st.empty()
        restitucion_tierras_2 = placeholder10_2.button("Restitución de Tierras",key="restitucion_tierras_2")

        placeholder11_2 = st.empty()
        revision_segregados_2 = placeholder11_2.button("Revisión de Predios Segregados",key="revision_segregados_2")
              
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
            placeholder11_2.empty()
            st.session_state.Procesos=True
            st.session_state.FMI=True
            FMI.FMI(usuario,puesto)

      
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
            placeholder11_2.empty()
            st.session_state.Procesos=True
            st.session_state.Consulta_Campo=True
            Consulta_Campo.Consulta_Campo(usuario,puesto)
        
        # ----- Restitución de Tierras ---- #

        elif restitucion_tierras_2:

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
            st.session_state.Restitucion_Tierras=True
            Restitucion_Tierras.Restitucion_Tierras(usuario,puesto)

        # ----- Revisión de Predios Segredados ---- #

        elif revision_segregados_2:

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
            st.session_state.Revision_Segregados=True
            Revision_Segregados.Revision_Segregados(usuario,puesto)
    
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
        
        elif st.session_state.Consulta_Campo==True:
            Consulta_Campo.Consulta_Campo(usuario,puesto)

        elif st.session_state.Restitucion_Tierras==True:
            Restitucion_Tierras.Restitucion_Tierras(usuario,puesto)

        elif st.session_state.Revision_Segregados==True:
            Revision_Segregados.Revision_Segregados(usuario,puesto)
