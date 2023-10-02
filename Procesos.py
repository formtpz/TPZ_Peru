# ----- Librerías ---- #

import streamlit as st
import Historial, Capacitacion, Otros_Registros, Bonos, Salir, Produccion

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
        Produccion = placeholder8_2.button("Producción",key="Produccion")

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

            st.session_state.Ingreso= False
            st.session_state.Procesos=True
            st.session_state.Salir=True
            Salir.Salir()

        # ----- Produccion ---- #

        elif Produccion:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
          
            st.session_state.Procesos=True
            st.session_state.Produccion=True
            Produccion.Produccion(usuario,puesto)

    elif st.session_state.Procesos==True:

        if st.session_state.Historial==True:
            Historial.Historial(usuario,puesto)

        elif st.session_state.Capacitacion==True:
            Capacitacion.Capacitacion(usuario,puesto)

        elif st.session_state.Otros_Registros==True:
            Otros_Registros.Otros_Registros(usuario,puesto)

        elif st.session_state.Bonos==True:
            Bonos.Bonos(usuario,puesto)

        elif st.session_state.Produccion==True:
            Produccion.Produccion(usuario,puesto)

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
        informacion_final_i_2 = placeholder8_2.button("Información Final I",key="Produccion")

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

            st.session_state.Ingreso = False
            st.session_state.Procesos=True
            st.session_state.Salir=True
            Salir.Salir()

       

    elif st.session_state.Procesos==True:

        if st.session_state.Historial==True:
            Historial.Historial(usuario,puesto)

        elif st.session_state.Capacitacion==True:
            Capacitacion.Capacitacion(usuario,puesto)

        elif st.session_state.Otros_Registros==True:
            Otros_Registros.Otros_Registros(usuario,puesto)

        elif st.session_state.Bonos==True:
            Bonos.Bonos(usuario,puesto)

        
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
        informacion_final_i_2 = placeholder8_2.button("Producción",key="Produccion")

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

            st.session_state.Procesos=True
            st.session_state.IFI=True
            IFI.IFI(usuario,puesto)

       
    elif st.session_state.Procesos==True:

        if st.session_state.Historial==True:
            Historial.Historial(usuario,puesto)       

        elif st.session_state.Capacitacion==True:
            Capacitacion.Capacitacion(usuario,puesto)

        elif st.session_state.Otros_Registros==True:
            Otros_Registros.Otros_Registros(usuario,puesto)

        elif st.session_state.Bonos==True:
            Bonos.Bonos(usuario,puesto)

        elif st.session_state.Produccion==True:
            Produccion.Produccion(usuario,puesto)

