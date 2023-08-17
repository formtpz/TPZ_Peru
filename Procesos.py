# ----- Librerías ---- #

import streamlit as st
import Historial, Capacitacion, Otros_Registros, Bonos, Salir, IFI, IFII, IFIII, Conformacion, CC_Conformacion, CC_IFI,Auxiliares

# ----- Procesos 1 ---- #

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
        bonos_2 = placeholder5_2.button("Bonos",key="bonos_2")

        placeholder6_2 = st.sidebar.empty()
        salir_2 = placeholder6_2.button("Salir",key="salir_2")

        placeholder7_2 = st.empty()
        procesos_2 = placeholder7_2.title("Procesos")

        placeholder8_2 = st.empty()
        informacion_final_i_2 = placeholder8_2.button("Información Final I",key="informacion_final_i_2")

        placeholder9_2 = st.empty()
        informacion_final_ii_2 = placeholder9_2.button("Información Final II",key="informacion_final_ii_2")

        placeholder10_2= st.empty()
        informacion_final_iii_2 = placeholder10_2.button("Información Final III",key="informacion_final_iii_2")

        placeholder11_2= st.empty()
        conformacion_2 = placeholder11_2.button("Conformación",key="conformacion_2")

        placeholder12_2= st.empty()
        cc_conformacion_2 = placeholder12_2.button("Control de Calidad Conformación",key="cc_conformacion_2")

        placeholder13_2= st.empty()
        cc_ifi_2 = placeholder13_2.button("Control de Calidad IF I",key="cc_ifi_2")

        placeholder14_2= st.empty()
        auxiliares_2 = placeholder14_2.button("Auxiliares",key="auxiliares_2")


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

        # ----- Bonos ---- #

        elif bonos_2:

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
            st.session_state.Bonos=True
            Bonos.Bonos(usuario,puesto)

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

        # ----- IFI ---- #

        elif informacion_final_i_2:

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
            st.session_state.IFI=True
            IFI.IFI(usuario,puesto)

        # ----- IFII ---- #

        elif informacion_final_ii_2:

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
            st.session_state.IFII=True
            IFII.IFII(usuario,puesto)

        # ----- IFIII ---- #

        elif informacion_final_iii_2:

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
            st.session_state.IFIII=True
            IFIII.IFIII(usuario,puesto)

        # ----- Conformación ---- #

        elif conformacion_2:

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
            st.session_state.Conformacion=True
            Conformacion.Conformacion(usuario,puesto)

        # ----- Control de Calidad Conformación ---- #
        
        elif cc_conformacion_2:

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
            st.session_state.CC_Conformacion=True
            CC_Conformacion.CC_Conformacion(usuario,puesto)

        # ----- Control de Calidad IF I ---- #

        elif cc_ifi_2:

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
            st.session_state.CC_IFI=True
            CC_IFI.CC_IFI(usuario,puesto)

        # ----- Auxiliares ---- #

        elif auxiliares_2:

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
            st.session_state.Auxiliares=True
            Auxiliares.Auxiliares(usuario,puesto)

    elif st.session_state.Procesos==True:

        if st.session_state.Historial==True:
            Historial.Historial(usuario,puesto)

        elif st.session_state.Capacitacion==True:
            Capacitacion.Capacitacion(usuario,puesto)

        elif st.session_state.Otros_Registros==True:
            Otros_Registros.Otros_Registros(usuario,puesto)

        elif st.session_state.Bonos==True:
            Bonos.Bonos(usuario,puesto)

        elif st.session_state.IFI==True:
            IFI.IFI(usuario,puesto)

        elif st.session_state.IFII==True:
            IFII.IFII(usuario,puesto)

        elif st.session_state.IFIII==True:
            IFIII.IFIII(usuario,puesto)
        
        elif st.session_state.Conformacion==True:
            Conformacion.Conformacion(usuario,puesto)
        
        elif st.session_state.CC_Conformacion==True:
            CC_Conformacion.CC_Conformacion(usuario,puesto)
           
        elif st.session_state.CC_IFI==True:
            CC_IFI.CC_IFI(usuario,puesto)

        elif st.session_state.Auxiliares==True:
            Auxiliares.Auxiliares(usuario,puesto)

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
        bonos_2 = placeholder5_2.button("Bonos",key="bonos_2")

        placeholder6_2 = st.sidebar.empty()
        salir_2 = placeholder6_2.button("Salir",key="salir_2")

        placeholder7_2 = st.empty()
        registro_2 = placeholder7_2.title("Procesos")

        placeholder8_2 = st.empty()
        cc_conformacion_2 = placeholder8_2.button("Control de Calidad Conformación",key="cc_conformacion_2")

        placeholder9_2 = st.empty()
        cc_ifi_2 = placeholder9_2.button("Control de Calidad IF I",key="cc_ifi_2")

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
            st.session_state.Procesos=True
            st.session_state.Otros_Registros=True
            Otros_Registros.Otros_Registros(usuario,puesto)

        # ----- Bonos ---- #

        elif bonos_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.Bonos=True
            Bonos.Bonos(usuario,puesto)

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
            st.session_state.Ingreso = False
            st.session_state.Procesos=True
            st.session_state.Salir=True
            Salir.Salir()

        # ----- Control de Calidad Conformación ---- #

        elif cc_conformacion_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.CC_Conformacion=True
            Conformacion.CC_Conformacion(usuario,puesto)

        # ----- Control de Calidad IF I ---- #

        elif cc_ifi_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.CC_IFI=True
            CC_IFI.CC_IFI(usuario,puesto)

    elif st.session_state.Procesos==True:

        if st.session_state.Historial==True:
            Historial.Historial(usuario,puesto)

        elif st.session_state.Capacitacion==True:
            Capacitacion.Capacitacion(usuario,puesto)

        elif st.session_state.Otros_Registros==True:
            Otros_Registros.Otros_Registros(usuario,puesto)

        elif st.session_state.Bonos==True:
            Bonos.Bonos(usuario,puesto)

        elif st.session_state.CC_Conformacion==True:
            CC_Conformacion.CC_Conformacion(usuario,puesto)

        elif st.session_state.CC_IFI==True:
            CC_IFI.CC_IFI(usuario,puesto)
        
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
        bonos_2 = placeholder5_2.button("Bonos",key="bonos_2")

        placeholder6_2 = st.sidebar.empty()
        salir_2 = placeholder6_2.button("Salir",key="salir_2")

        placeholder7_2 = st.empty()
        registro_2 = placeholder7_2.title("Procesos")

        placeholder8_2 = st.empty()
        informacion_final_i_2 = placeholder8_2.button("Información Final I",key="informacion_final_i_2")

        placeholder9_2 = st.empty()
        informacion_final_ii_2 = placeholder9_2.button("Información Final II",key="informacion_final_ii_2")

        placeholder10_2= st.empty()
        informacion_final_iii_2 = placeholder10_2.button("Información Final III",key="informacion_final_iii_2")

        placeholder11_2= st.empty()
        conformacion_2 = placeholder11_2.button("Conformación",key="conformacion_2")

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

        # ----- Bonos ---- #

        elif bonos_2:

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
            st.session_state.Bonos=True
            Bonos.Bonos(usuario,puesto)

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

        # ----- IFI ---- #

        elif informacion_final_i_2:

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
            st.session_state.IFI=True
            IFI.IFI(usuario,puesto)

        # ----- IFII ---- #

        elif informacion_final_ii_2:

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
            st.session_state.IFII=True
            IFII.IFII(usuario,puesto)

        # ----- IFIII ---- #

        elif informacion_final_iii_2:

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
            st.session_state.IFIII=True
            IFIII.IFIII(usuario,puesto)

        # ----- Conformación ---- #

        elif conformacion_2:

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
            st.session_state.Conformacion=True
            Conformacion.Conformacion(usuario,puesto)

    elif st.session_state.Procesos==True:

        if st.session_state.Historial==True:
            Historial.Historial(usuario,puesto)       

        elif st.session_state.Capacitacion==True:
            Capacitacion.Capacitacion(usuario,puesto)

        elif st.session_state.Otros_Registros==True:
            Otros_Registros.Otros_Registros(usuario,puesto)

        elif st.session_state.Bonos==True:
            Bonos.Bonos(usuario,puesto)

        elif st.session_state.IFI==True:
            IFI.IFI(usuario,puesto)

        elif st.session_state.IFII==True:
            IFII.IFII(usuario,puesto)

        elif st.session_state.IFIII==True:
            IFIII.IFIII(usuario,puesto)
        
        elif st.session_state.Conformacion==True:
            Conformacion.Conformacion(usuario,puesto)
