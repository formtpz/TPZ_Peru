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
