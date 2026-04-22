# ----- Librerías -----
import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime, timedelta
import pytz
from urllib.parse import urlparse
from pandas.tseries.offsets import BDay
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

    # Utilidad numpy → python
    def to_python(v):
        return v.item() if hasattr(v, "item") else v

    # =============================
    # Menú lateral
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
            st.write("Aquí puedes visualizar tus reportes recientes y solicitar correcciones o eliminaciones (solo últimos 3 días hábiles).")

            # -------------------------------------------------
            # Obtener nombre del usuario
            # -------------------------------------------------
            df_nombre = pd.read_sql(
                f"SELECT nombre FROM usuarios WHERE usuario = '{usuario}'",
                con
            )
            nombre = df_nombre.loc[0, "nombre"]

            # -------------------------------------------------
            # Calcular fecha límite (3 días hábiles hacia atrás)
            # -------------------------------------------------
            hoy = datetime.now().date()
            fecha_limite = (datetime.now() - BDay(3)).date()
            st.caption(f"Se muestran reportes desde el **{fecha_limite.strftime('%d/%m/%Y')}** (3 días hábiles atrás).")

            # -------------------------------------------------
            # Consultar reportes de los últimos 3 días hábiles
            # -------------------------------------------------
            # Nota: las tablas tienen columna "fecha". Si es timestamp se convertirá al leer.
            query_registro = f"""
                SELECT *
                FROM registro
                WHERE usuario = '{usuario}'
                  AND fecha::date >= '{fecha_limite}'
                ORDER BY fecha DESC
            """
            query_otros = f"""
                SELECT *
                FROM otros_registros
                WHERE usuario = '{usuario}'
                  AND fecha::date >= '{fecha_limite}'
                ORDER BY fecha DESC
            """
            query_capacitacion = f"""
                SELECT *
                FROM capacitaciones
                WHERE usuario = '{usuario}'
                  AND fecha::date >= '{fecha_limite}'
                ORDER BY fecha DESC
            """

            df_registro = pd.read_sql(query_registro, con)
            df_otros = pd.read_sql(query_otros, con)
            df_capacitaciones = pd.read_sql(query_capacitacion, con)

            for df in (df_registro, df_otros, df_capacitaciones):
                if "id" in df.columns:
                    df["id"] = df["id"].astype(str)

            # ---------- Filtro para mostrar una sola tabla ----------
            st.subheader("📋 Mis reportes recientes (últimos 3 días hábiles)")
            tabla_viz = st.radio(
                "Selecciona la tabla que deseas visualizar:",
                ("Registro", "Otros Registros", "Capacitaciones"),
                horizontal=True
            )
            if tabla_viz == "Registro":
                st.dataframe(df_registro, use_container_width=True)
            elif tabla_viz == "Otros Registros":
                st.dataframe(df_otros, use_container_width=True)
            else:
                st.dataframe(df_capacitaciones, use_container_width=True)

            # ---------- Nueva solicitud de corrección ----------
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
                        # Verificar que el ID exista y pertenezca al usuario
                        cursor.execute(
                            f"SELECT usuario, fecha FROM {tabla} WHERE id = %s",
                            (id_reporte,)
                        )
                        resultado = cursor.fetchone()
                        if resultado is None:
                            st.error(f"No existe el ID {id_reporte} en la tabla {tabla}.")
                        elif resultado[0] != usuario:
                            st.error("No puedes solicitar corrección de un reporte que no te pertenece.")
                        else:
                            # Validación de fecha: máximo 3 días hábiles de antigüedad
                            fecha_reporte = resultado[1]
                            if hasattr(fecha_reporte, 'date'):
                                fecha_reporte = fecha_reporte.date()
                            # Reutilizamos la misma fecha_limite (3 días hábiles)
                            if fecha_reporte < fecha_limite:
                                st.error(f"No se pueden solicitar correcciones para reportes con más de 3 días hábiles de antigüedad. Este reporte es del {fecha_reporte.strftime('%d/%m/%Y')}.")
                                st.stop()

                            # Verificar que no exista ya una corrección para ese ID en esa tabla
                            cursor.execute("""
                                SELECT 1 FROM correcciones
                                WHERE tabla = %s AND id_asociado = %s
                            """, (tabla, id_reporte))
                            if cursor.fetchone() is not None:
                                st.error("Ya existe una solicitud para este ID en esta tabla.")
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
                                    usuario, nombre, "Pendiente de detalle", id_reporte,
                                    marca, solucion, tabla, "", "", "Pendiente"
                                ))
                                con.commit()
                                st.success("Solicitud registrada. Ahora puedes editar los detalles abajo.")
                                st.rerun()

            # -------------------------------------------------
            # EDICIÓN DE SOLICITUDES PENDIENTES (data_editor nativo)
            # -------------------------------------------------
            st.subheader("✏️ Editar detalles de mis solicitudes pendientes")

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
                # Definir las columnas editables por tabla (según lo que indicaste)
                COLUMNAS_EDITABLES = {
                    "registro": [
                        "fecha", "horas", "observaciones",
                        "distrito", "tipo", "lotes", "aprobados", "rechazados",
                        "manzana", "sector", "numero_lote", "estado", "area",
                        "edificas", "partida", "zona", "tipo_calidad",
                        "total_de_errores", "errores_por_excepcion",
                        "tipo_de_errores", "conteo_de_errores"
                    ],
                    "otros_registros": ["fecha", "horas", "observaciones"],
                    "capacitaciones": ["fecha", "horas", "observaciones"]
                }

                # Unir todas las opciones posibles para el dropdown de "columna"
                todas_columnas = sorted(set(
                    COLUMNAS_EDITABLES["registro"] +
                    COLUMNAS_EDITABLES["otros_registros"] +
                    COLUMNAS_EDITABLES["capacitaciones"]
                ))

                st.caption("✏️ Haz doble clic en 'Solución' para cambiar entre Eliminar/Modificar.")
                st.caption("📂 Haz doble clic en 'Columna' y elige de la lista desplegable (incluye columnas de todas las tablas).")
                st.caption("⚠️ Asegúrate de elegir una columna válida para la tabla indicada en cada fila.")
                st.info(f"Columnas válidas por tabla:\n\n"
                        f"**Registro**: {', '.join(COLUMNAS_EDITABLES['registro'])}\n\n"
                        f"**Otros Registros**: {', '.join(COLUMNAS_EDITABLES['otros_registros'])}\n\n"
                        f"**Capacitaciones**: {', '.join(COLUMNAS_EDITABLES['capacitaciones'])}")

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
                    "columna": st.column_config.SelectboxColumn(
                        "Columna a modificar",
                        options=todas_columnas,
                        required=False
                    ),
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
                        errores = []
                        for idx in cambios.index.get_level_values(0).unique():
                            fila_nueva = df_editado.loc[idx]
                            fila_original = df_pendientes.loc[idx]

                            # Validar que la columna elegida sea válida para la tabla
                            tabla_actual = fila_nueva["tabla"]
                            columna_elegida = fila_nueva["columna"]
                            if fila_nueva["solucion"] == "Modificar":
                                if columna_elegida not in COLUMNAS_EDITABLES.get(tabla_actual, []):
                                    errores.append(f"Fila ID {fila_nueva['id']}: La columna '{columna_elegida}' no es editable en la tabla '{tabla_actual}'.")
                                    continue

                            # Actualizar solo si hubo cambios en solucion, columna o nuevo_valor
                            if (fila_nueva["solucion"] == fila_original["solucion"] and
                                fila_nueva["columna"] == fila_original["columna"] and
                                fila_nueva["nuevo_valor"] == fila_original["nuevo_valor"]):
                                continue

                            cursor.execute("""
                                UPDATE correcciones
                                SET solucion = %s,
                                    columna = %s,
                                    nuevo_valor = %s
                                WHERE id = %s
                            """, (
                                fila_nueva["solucion"],
                                fila_nueva["columna"],
                                fila_nueva["nuevo_valor"],
                                fila_nueva["id"]
                            ))

                        if errores:
                            for err in errores:
                                st.error(err)
                            st.warning("Corrige los errores antes de guardar.")
                        else:
                            con.commit()
                            st.success("Cambios guardados correctamente.")
                            st.rerun()

            # ---------- Ver todas mis solicitudes ----------
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
    # COORDINADOR
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

        # Obtener perfil usando la conexión activa
        perfil = pd.read_sql(
            f"SELECT perfil FROM usuarios WHERE usuario = '{usuario}'",
            con
        ).loc[0, "perfil"]

        if perfil == "1":
            Procesos.Procesos1(usuario, puesto)
        elif perfil == "2":
            Procesos.Procesos2(usuario, puesto)
        elif perfil == "3":
            Procesos.Procesos3(usuario, puesto)

    # Cerrar cursor
    cursor.close()
