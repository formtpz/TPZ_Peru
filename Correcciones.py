# ----- Librerías -----
import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime, timedelta
import pytz
from urllib.parse import urlparse
import Procesos


def Correcciones(usuario, puesto):

    # =============================
    # Conexión a la BD
    # =============================
    uri = st.secrets.db_credentials.URI
    result = urlparse(uri)

    con = psycopg2.connect(
        host=result.hostname,
        dbname=result.path[1:],
        user=result.username,
        password=result.password,
        port=result.port
    )
    cursor = con.cursor()

    # =============================
    # Utilidad numpy → python
    # =============================
    def to_python(v):
        return v.item() if hasattr(v, "item") else v

    # =============================
    # Menú lateral (placeholders)
    # =============================
    placeholder1_3 = st.sidebar.empty()
    placeholder1_3.title("Menú")

    placeholder2_3 = st.sidebar.empty()
    procesos_3 = placeholder2_3.button("Regresar", key="procesos_3")

    # =========================================================
    # USUARIO NORMAL (NO COORDINADOR)
    # =========================================================
    if puesto != "Coordinador":

        page = st.empty()
        with page.container():

            st.title("Corrección de Reportes")
            st.write("Aquí puedes visualizar tus reportes recientes y solicitar correcciones o eliminaciones.")

            # -------------------------------------------------
            # Obtener nombre del usuario
            # -------------------------------------------------
            df_nombre = pd.read_sql(
                f"SELECT nombre FROM usuarios WHERE usuario = '{usuario}'",
                con
            )
            nombre = df_nombre.loc[0, "nombre"]

            # -------------------------------------------------
            # Filtro fijo: últimos 3 días (incluye hoy)
            # -------------------------------------------------
            fecha_limite = datetime.now().date() - timedelta(days=3)

            # -------------------------------------------------
            # Consultar reportes de los últimos 3 días
            # -------------------------------------------------
            query_registro = f"""
                SELECT *
                FROM registro
                WHERE usuario = '{usuario}'
                  AND fecha >= '{fecha_limite}'
                ORDER BY fecha DESC
            """

            query_otros = f"""
                SELECT *
                FROM otros_registros
                WHERE usuario = '{usuario}'
                  AND fecha >= '{fecha_limite}'
                ORDER BY fecha DESC
            """

            query_capacitacion = f"""
                SELECT *
                FROM capacitaciones
                WHERE usuario = '{usuario}'
                  AND fecha >= '{fecha_limite}'
                ORDER BY fecha DESC
            """

            df_registro = pd.read_sql(query_registro, con)
            df_otros = pd.read_sql(query_otros, con)
            df_capacitaciones = pd.read_sql(query_capacitacion, con)

            # Convertir IDs a string
            for df in (df_registro, df_otros, df_capacitaciones):
                if "id" in df.columns:
                    df["id"] = df["id"].astype(str)

            # ========== NUEVO: Filtro para mostrar una sola tabla ==========
            st.subheader("📋 Mis reportes recientes (últimos 3 días)")
            tabla_seleccionada_visualizacion = st.radio(
                "Selecciona la tabla que deseas visualizar:",
                ("Registro", "Otros Registros", "Capacitaciones"),
                horizontal=True
            )

            if tabla_seleccionada_visualizacion == "Registro":
                st.dataframe(df_registro, use_container_width=True)
            elif tabla_seleccionada_visualizacion == "Otros Registros":
                st.dataframe(df_otros, use_container_width=True)
            else:
                st.dataframe(df_capacitaciones, use_container_width=True)

            # =================================================
            # NUEVA SOLICITUD DE CORRECCIÓN (Paso 1)
            # =================================================
            st.subheader("➕ Nueva solicitud de corrección / eliminación")

            with st.form(key="nueva_correccion_form", clear_on_submit=True):
                col1, col2 = st.columns(2)
                with col1:
                    tabla = st.selectbox(
                        "Tabla donde se encuentra el reporte",
                        ("registro", "otros_registros", "capacitaciones")
                    )
                with col2:
                    id_reporte = st.text_input("ID del reporte")

                tipo_solicitud = st.radio(
                    "Tipo de solicitud",
                    ("Eliminar reporte", "Modificar valor")
                )

                enviar = st.form_submit_button("Registrar solicitud")

                if enviar:
                    if not id_reporte:
                        st.error("Debe indicar el ID del reporte.")
                    else:
                        # ========== NUEVO: Verificar que el ID pertenezca al usuario actual ==========
                        cursor.execute(
                            f"SELECT usuario FROM {tabla} WHERE id = %s",
                            (id_reporte,)
                        )
                        resultado = cursor.fetchone()
                        if resultado is None:
                            st.error(f"No existe el ID {id_reporte} en la tabla {tabla}.")
                        elif resultado[0] != usuario:
                            st.error("No puedes solicitar corrección de un reporte que no te pertenece.")
                        else:
                            # Verificar que no exista ya una corrección para ese ID en esa tabla
                            cursor.execute("""
                                SELECT 1 FROM correcciones
                                WHERE tabla = %s AND id_asociado = %s
                            """, (tabla, id_reporte))
                            if cursor.fetchone() is not None:
                                st.error("Ya existe una solicitud de corrección para este ID en esta tabla.")
                            else:
                                marca = datetime.now(pytz.timezone("America/Guatemala")).strftime("%Y-%m-%d %H:%M:%S")
                                solucion = "Eliminar" if tipo_solicitud == "Eliminar reporte" else "Modificar"

                                cursor.execute("""
                                    INSERT INTO correcciones (
                                        usuario, nombre, tipo_error, id_asociado,
                                        fecha, solucion, tabla, columna, nuevo_valor, estado
                                    )
                                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                                """, (
                                    usuario,
                                    nombre,
                                    "Pendiente de detalle",  # tipo_error inicial
                                    id_reporte,
                                    marca,
                                    solucion,
                                    tabla,
                                    "",                   # columna se llenará después
                                    "",                   # nuevo_valor se llenará después
                                    "Pendiente"
                                ))
                                con.commit()
                                st.success("Solicitud registrada. Ahora puedes editar los detalles en la sección de abajo.")
                                st.rerun()

            # =================================================
            # EDICIÓN DE SOLICITUDES PENDIENTES (Paso 2)
            # =================================================
            st.subheader("✏️ Editar detalles de mis solicitudes pendientes")

            # Cargar solicitudes pendientes del usuario
            query_pendientes = f"""
                SELECT id, fecha, tabla, id_asociado, solucion, columna, nuevo_valor, estado
                FROM correcciones
                WHERE usuario = '{usuario}' AND estado = 'Pendiente'
                ORDER BY fecha DESC
            """
            df_pendientes = pd.read_sql(query_pendientes, con)
            if "id" in df_pendientes.columns:
                df_pendientes["id"] = df_pendientes["id"].astype(str)

            if df_pendientes.empty:
                st.info("No tienes solicitudes pendientes para editar.")
            else:
                st.caption("Haz clic en 'Editar' para modificar los detalles de cada solicitud.")

                # Mostrar cada solicitud en un expander con formulario de edición
                for idx, row in df_pendientes.iterrows():
                    with st.expander(f"Solicitud #{row['id']} - Tabla: {row['tabla']} - ID: {row['id_asociado']}"):
                        # Obtener las columnas reales de la tabla asociada
                        cursor.execute("""
                            SELECT column_name
                            FROM information_schema.columns
                            WHERE table_name = %s
                            ORDER BY ordinal_position
                        """, (row['tabla'],))
                        columnas_disponibles = [col[0] for col in cursor.fetchall()]

                        # Formulario de edición para esta fila
                        with st.form(key=f"edit_form_{row['id']}"):
                            col1, col2 = st.columns(2)
                            with col1:
                                nueva_solucion = st.selectbox(
                                    "Solución",
                                    options=["Eliminar", "Modificar"],
                                    index=0 if row['solucion'] == "Eliminar" else 1,
                                    key=f"sol_{row['id']}"
                                )
                            with col2:
                                # Dropdown dinámico de columnas (solo si la solución es Modificar)
                                if nueva_solucion == "Modificar":
                                    columna_seleccionada = st.selectbox(
                                        "Columna a modificar",
                                        options=columnas_disponibles,
                                        index=columnas_disponibles.index(row['columna']) if row['columna'] in columnas_disponibles else 0,
                                        key=f"col_{row['id']}"
                                    )
                                    nuevo_valor_input = st.text_input(
                                        "Nuevo valor",
                                        value=row['nuevo_valor'] if row['nuevo_valor'] else "",
                                        key=f"val_{row['id']}"
                                    )
                                else:
                                    columna_seleccionada = ""
                                    nuevo_valor_input = ""
                                    st.info("No se requiere columna para eliminación.")

                            guardar_cambios = st.form_submit_button("Guardar cambios")
                            if guardar_cambios:
                                # Actualizar en BD
                                cursor.execute("""
                                    UPDATE correcciones
                                    SET solucion = %s,
                                        columna = %s,
                                        nuevo_valor = %s
                                    WHERE id = %s
                                """, (
                                    nueva_solucion,
                                    columna_seleccionada,
                                    nuevo_valor_input,
                                    row['id']
                                ))
                                con.commit()
                                st.success("Cambios guardados correctamente.")
                                st.rerun()

            # =================================================
            # VISUALIZACIÓN DE TODAS MIS SOLICITUDES (opcional)
            # =================================================
            with st.expander("📋 Ver todas mis solicitudes"):
                query_todas = f"""
                    SELECT id, fecha, tabla, id_asociado, solucion, columna, nuevo_valor, estado
                    FROM correcciones
                    WHERE usuario = '{usuario}'
                    ORDER BY fecha DESC
                """
                df_todas = pd.read_sql(query_todas, con)
                if "id" in df_todas.columns:
                    df_todas["id"] = df_todas["id"].astype(str)
                st.dataframe(df_todas, use_container_width=True)

        # Fin del bloque usuario normal

    # =========================================================
    # COORDINADOR (sin cambios)
    # =========================================================
    else:
        # ... (código existente para Coordinador sin modificaciones)
        pass

    # =========================================================
    # Regresar a Procesos
    # =========================================================
    if procesos_3:
        # ... (código existente de regreso)
        pass

    # Cerrar cursor
    cursor.close()
