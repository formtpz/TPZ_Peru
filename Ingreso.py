# ----- Librerías ---- #

import streamlit as st
import pandas as pd
from PIL import Image
import Autenticacion, Procesos

# Estilos CSS personalizados
custom_css = """
<style>
.custom-button {
    background-color: #B5CBD3; /* Cambia este color al color deseado para el botón */
    color: #FFFFFF; /* Cambia este color al color deseado para el texto del botón */
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}
</style>
"""

# Estilo para ocultar el menú
hide_menu_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility:visible;}
footer:after{
    content:'V.1.1 Copyrigth @ 2023 Telespazio Argentina S.A.';
    display: block;
    position: relative;
    color: tomato;
}
</style>
"""

# Combinar estilos CSS y ocultar menú
combined_styles = hide_menu_style + custom_css

# Insertar estilos combinados
st.markdown(combined_styles, unsafe_allow_html=True)

# ----- Formato General ---- #

img=Image.open('logoicon.png')

st.set_page_config(page_title="Formularios TPZ",page_icon=img,layout="wide")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility:visible;}
        footer:after{
            content:'V.1.1 Copyrigth @ 2023 Telespazio Argentina S.A.';
            display: block;
            position: relative;
            color: tomato;
        }
        </style>
        """

st.markdown(hide_menu_style, unsafe_allow_html=True)

# ----- Conexión, Botones y Memoria ---- #

uri=st.secrets.db_credentials.URI

pivot=0 # Se requiere para mantener las indicaciones generales en caso de errores de ingreso

placeholder1_1= st.sidebar.empty()
titulo_1= placeholder1_1.title("Ingreso")

placeholder2_1= st.sidebar.empty()
usuario=placeholder2_1.text_input("Usuario",key="usuario")

placeholder3_1= st.sidebar.empty()
contraseña_1 = placeholder3_1.text_input("Contraseña", type = 'password', key="contraseña_1")

placeholder4_1 = st.sidebar.empty()
iniciar_sesion_1 = placeholder4_1.button("Iniciar sesión",key="iniciar_sesion_1", class="custom-button")

if "Ingreso" not in st.session_state:
     st.session_state.Ingreso = False

if st.session_state.Ingreso:

    st.session_state.Ingreso=True
    placeholder1_1.empty()
    placeholder2_1.empty()
    placeholder3_1.empty()
    placeholder4_1.empty()
    
    puesto=pd.read_sql(f"select puesto from usuarios where usuario ='{usuario}'",uri)
    puesto= puesto.loc[0,'puesto']

    perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
    perfil= perfil.loc[0,'perfil']

    if perfil=="1":        
        
        Procesos.Procesos1(usuario,puesto)
    
    elif perfil=="2":        
        
        Procesos.Procesos2(usuario,puesto)   

    elif perfil=="3":        
        
        Procesos.Procesos3(usuario,puesto)   

    pivot=pivot + 1

# ----- Validación ---- #

if iniciar_sesion_1:

    if usuario == '' or contraseña_1 == '':
        st.error('Favor ingresar sus credenciales')

    else:
        
        contraseña= Autenticacion.contraseña(usuario)

        if contraseña.empty:
            st.error('El usuario no existe, intente de nuevo')

        else:

            contraseña = contraseña.loc[0,'contraseña']

            if contraseña == contraseña_1:

                nombre_1=pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
                nombre_1 = nombre_1.loc[0,'nombre']
                st.success(f'¡Bienvenido {nombre_1}!')

                placeholder1_1.empty()
                placeholder2_1.empty()
                placeholder3_1.empty()
                placeholder4_1.empty()

                st.session_state.Procesos=False
                st.session_state.Historial=False
                st.session_state.Capacitacion=False
                st.session_state.Otros_Registros=False
                st.session_state.Bonos=False
                st.session_state.Salir=False
                st.session_state.IFI=False

                puesto=pd.read_sql(f"select puesto from usuarios where usuario ='{usuario}'",uri)
                puesto= puesto.loc[0,'puesto']
                   
                perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
                perfil= perfil.loc[0,'perfil']

                if perfil=="1":        
                    
                    Procesos.Procesos1(usuario,puesto)
                
                elif perfil=="2":        
                    
                    Procesos.Procesos2(usuario,puesto)   

                elif perfil=="3":  

                    Procesos.Procesos3(usuario,puesto)       

                pivot= pivot + 1
                                
            else:
                st.error('Contraseña incorrecta, intente de nuevo')

# ----- Mensajes Generales ---- #
     
if pivot!=1:
    
     st.image(Image.open("logo.png"))

     st.title("Telespazio Argentina S.A.")

     st.header("Aplicación de uso exclusivo para el personal de Telespazio Argentina S.A.")

     st.subheader("Para soporte técnico favor escribir a luis.hidalgo@telespazio.pe")
