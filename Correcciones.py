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

            df = pd.read_sql(query_registro, con)
            dfo = pd.read_sql(query_otros, con)
            dfc = pd.read_sql(query_capacitacion, con)

            # Convertir IDs a string para mejor visualización
            for dataframe in (df, dfo, dfc):
                if "id" in dataframe.columns:
                    dataframe["id"] = dataframe["id"].astype(str)

            st.subheader("📋 Registro (últimos 3 días)")
            st.dataframe(df, use_container_width=True)

            st.subheader("📌 Otros Registros (últimos 3 días)")
            st.dataframe(dfo, use_container_width=True)

            st.subheader("📚 Capacitaciones (últimos 3 días)")
            st.dataframe(dfc, use_container_width=True)

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

                # Si es modificación, mostrar lista de columnas disponibles para esa tabla
                columna_seleccionada = None
                if tipo_solicitud == "Modificar valor":
                    # Obtener columnas reales de la tabla seleccionada (excluyendo id y algunas de sistema)
                    cursor.execute("""
                        SELECT column_name
                        FROM information_schema.columns
                        WHERE table_name = %s
                        ORDER BY ordinal_position
                    """, (tabla,))
                    columnas_tabla = [row[0] for row in cursor.fetchall()]
                    # Excluir columnas que normalmente no se modifican
                    excluir = {'id', 'marca', 'usuario', 'nombre', 'puesto', 'supervisor',
                               'proceso', 'fecha', 'semana', 'año'}
                    columnas_disponibles = [c for c in columnas_tabla if c not in excluir]
                    if columnas_disponibles:
                        columna_seleccionada = st.selectbox(
                            "Columna a modificar",
                            columnas_disponibles
                        )
                    else:
                        st.warning("No hay columnas editables en esta tabla.")

                enviar = st.form_submit_button("Registrar solicitud")

                if enviar:
                    if not id_reporte:
                        st.error("Debe indicar el ID del reporte.")
                    else:
                        # Verificar que el ID exista en la tabla seleccionada
                        cursor.execute(f"SELECT 1 FROM {tabla} WHERE id = %s", (id_reporte,))
                        if cursor.fetchone() is None:
                            st.error(f"No existe el ID {id_reporte} en la tabla {tabla}.")
                        else:
                            # Verificar que no exista ya una corrección para ese ID en esa tabla
                            cursor.execute("""
                                SELECT 1 FROM correcciones
                                WHERE tabla = %s AND id_asociado = %s
                            """, (tabla, id_reporte))
                            if cursor.fetchone() is not None:
                                st.error("Ya existe una solicitud de corrección para este ID en esta tabla.")
                            else:
                                # Validar que si es modificación se haya seleccionado una columna
                                if tipo_solicitud == "Modificar valor" and not columna_seleccionada:
                                    st.error("Debe seleccionar una columna para modificar.")
                                else:
                                    marca = datetime.now(pytz.timezone("America/Guatemala")).strftime("%Y-%m-%d %H:%M:%S")
                                    solucion = "Eliminar" if tipo_solicitud == "Eliminar reporte" else "Modificar"
                                    columna_valor = columna_seleccionada if tipo_solicitud == "Modificar valor" else ""

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
                                        columna_valor,           # columna ya definida
                                        "",                      # nuevo_valor se llenará después
                                        "Pendiente"
                                    ))
                                    con.commit()
                                    st.success("Solicitud registrada. Ahora puedes editar el nuevo valor en la tabla de abajo.")
                                    st.rerun()

            # =================================================
            # TABLA EDITABLE DE SOLICITUDES PENDIENTES (Paso 2)
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
                st.caption("Puedes modificar 'solución' y 'nuevo valor' directamente en la tabla.")
                st.caption("La columna a modificar fue seleccionada al crear la solicitud y no puede cambiarse aquí.")

                # Configuración de columnas para el editor
                column_config = {
                    "id": st.column_config.Column(disabled=True),
                    "fecha": st.column_config.Column(disabled=True),
                    "tabla": st.column_config.Column(disabled=True),
                    "id_asociado": st.column_config.Column(disabled=True),
                    "estado": st.column_config.Column(disabled=True),
                    "solucion": st.column_config.SelectboxColumn(
                        "Solución",
                        options=["Eliminar", "Modificar"],
                        required=True
                    ),
                    "columna": st.column_config.Column(disabled=True, label="Columna a modificar"),
                    "nuevo_valor": st.column_config.TextColumn("Nuevo valor"),
                }

                df_editado = st.data_editor(
                    df_pendientes,
                    use_container_width=True,
                    num_rows="fixed",
                    column_config=column_config,
                    key="editor_pendientes"
                )

                if st.button("💾 Guardar cambios en solicitudes"):
                    cambios = df_editado.compare(df_pendientes)
                    if cambios.empty:
                        st.info("No se detectaron cambios.")
                    else:
                        for idx in cambios.index.get_level_values(0).unique():
                            fila_nueva = df_editado.loc[idx]
                            fila_original = df_pendientes.loc[idx]

                            columnas_cambiadas = [
                                col for col in ["solucion", "nuevo_valor"]
                                if fila_nueva[col] != fila_original[col]
                            ]
                            if not columnas_cambiadas:
                                continue

                            set_clause = ", ".join(f"{col} = %s" for col in columnas_cambiadas)
                            valores = [to_python(fila_nueva[col]) for col in columnas_cambiadas]
                            id_python = to_python(fila_nueva["id"])

                            sql = f"""
                                UPDATE correcciones
                                SET {set_clause}
                                WHERE id = %s
                            """
                            cursor.execute(sql, valores + [id_python])

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
    # COORDINADOR (sin cambios en la lógica actual)
    # =========================================================
    else:

        page = st.empty()
        with page.container():

            st.title("Gestión de Correcciones")

            filtro = st.selectbox("Mostrar", ("Todos", "Pendiente"))

            query_corr = "SELECT * FROM correcciones"
            if filtro == "Pendiente":
                query_corr += " WHERE estado = 'Pendiente'"

            df_corr_original = pd.read_sql(query_corr, con)

            if "id" in df_corr_original.columns:
                df_corr_original["id"] = df_corr_original["id"].astype(str)

            column_config_coord = {
                "id": st.column_config.Column(disabled=True),
                "usuario": st.column_config.Column(disabled=True),
                "nombre": st.column_config.Column(disabled=True),
                "fecha": st.column_config.Column(disabled=True),
                "tabla": st.column_config.Column(disabled=True),
                "id_asociado": st.column_config.Column(disabled=True),
            }

            df_corr_editado = st.data_editor(
                df_corr_original,
                use_container_width=True,
                num_rows="fixed",
                column_config=column_config_coord
            )

            if st.button("Guardar cambios"):
                cambios = df_corr_editado.compare(df_corr_original)

                if cambios.empty:
                    st.info("No hay cambios para guardar.")
                else:
                    for idx in cambios.index.get_level_values(0).unique():
                        fila_nueva = df_corr_editado.loc[idx]
                        fila_original = df_corr_original.loc[idx]

                        columnas_cambiadas = [
                            col for col in df_corr_original.columns
                            if fila_nueva[col] != fila_original[col]
                        ]
                        columnas_permitidas = [c for c in columnas_cambiadas if c not in ("id", "usuario", "nombre", "fecha", "tabla", "id_asociado")]
                        if not columnas_permitidas:
                            continue

                        set_clause = ", ".join(f"{col} = %s" for col in columnas_permitidas)
                        valores = [to_python(fila_nueva[col]) for col in columnas_permitidas]
                        id_python = to_python(fila_nueva["id"])

                        sql = f"""
                            UPDATE correcciones
                            SET {set_clause}
                            WHERE id = %s
                        """
                        cursor.execute(sql, valores + [id_python])

                    con.commit()
                    st.success("Cambios guardados correctamente")

        # Fin del bloque Coordinador

    # =========================================================
    # Regresar a Procesos
    # =========================================================
    if procesos_3:

        placeholder1_3.empty()
        placeholder2_3.empty()

        try:
            page.empty()
        except:
            pass

        st.session_state.Procesos = False
        st.session_state.Correcciones = False

        # Obtener perfil ANTES de cerrar la conexión
        perfil = pd.read_sql(
            f"SELECT perfil FROM usuarios WHERE usuario = '{usuario}'",
            con
        ).loc[0, "perfil"]

        # Ahora podemos cerrar la conexión, porque ya no la usaremos en esta función
        cursor.close()
        con.close()

        if perfil == "1":
            Procesos.Procesos1(usuario, puesto)
        elif perfil == "2":
            Procesos.Procesos2(usuario, puesto)
        elif perfil == "3":
            Procesos.Procesos3(usuario, puesto)
    else:
        # Si no se presionó "Regresar", cerramos la conexión normalmente al salir
        cursor.close()
        con.close()
