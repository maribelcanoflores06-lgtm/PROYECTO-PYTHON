import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Proyecto 1 – Python Fundamentals",
    page_icon="🧵",
    layout="centered"
)
 
# ─────────────────────────────────────────────
# MENÚ LATERAL
# ─────────────────────────────────────────────
seccion = st.sidebar.selectbox(
    "Navegación",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)
 
# ═══════════════════════════════════════════════════════════
# HOME
# ═══════════════════════════════════════════════════════════
if seccion == "Home":
    st.title("🧵 Proyecto 1 – Python Fundamentals")
    st.subheader("Especialización en Python for Analytics")
 
    st.markdown("---")
 
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**👤 Estudiante:**")
        st.write("Maribel")
        st.markdown("**📚 Módulo:**")
        st.write("Módulo 1 – Python Fundamentals")
        st.markdown("**📅 Año:**")
        st.write("2025")
 
    with col2:
        st.markdown("**🏫 Curso:**")
        st.write("Especialización en Python for Analytics")
        st.markdown("**👨‍🏫 Docente:**")
        st.write("MSc. Carlos Carrillo Villavicencio")
 
    st.markdown("---")
    st.markdown("### 📋 Descripción del proyecto")
    st.write(
        "Esta aplicación interactiva integra los conceptos fundamentales del Módulo 1: "
        "variables, estructuras de datos, control de flujo, funciones, programación funcional "
        "y programación orientada a objetos (POO). Cada sección corresponde a un ejercicio "
        "práctico desarrollado con Streamlit."
    )
 
    st.markdown("### 🛠️ Tecnologías utilizadas")
    st.markdown(
        "- **Python 3** – lenguaje principal  \n"
        "- **Streamlit** – interfaz web interactiva  \n"
        "- **NumPy** – arreglos numéricos  \n"
        "- **Pandas** – DataFrames  \n"
        "- **Librerías externas del curso** – funciones y clases proporcionadas por el docente"
    )
 
# ═══════════════════════════════════════════════════════════
# EJERCICIO 1 – Flujo de caja con listas
# ═══════════════════════════════════════════════════════════
elif seccion == "Ejercicio 1":
    st.title("📊 Ejercicio 1 – Flujo de caja con listas")
 
    st.markdown("""
    Módulo para registrar movimientos financieros en una lista.  
    Ingresa el concepto, tipo de movimiento y valor. Al presionar **Agregar movimiento**,  
    el registro se guarda y se actualiza el resumen del flujo de caja.
    """)
 
    # Inicializar lista en session_state
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []
 
    st.markdown("---")
    st.subheader("Registrar movimiento")
 
    col1, col2, col3 = st.columns(3)
    with col1:
        concepto = st.text_input("Concepto", placeholder="Ej: Venta de producto")
    with col2:
        tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    with col3:
        valor = st.number_input("Valor (S/)", min_value=0.01, step=0.01, format="%.2f")
 
    if st.button("➕ Agregar movimiento"):
        if concepto.strip() == "":
            st.error("El concepto no puede estar vacío.")
        else:
            st.session_state.movimientos.append({
                "Concepto": concepto.strip(),
                "Tipo": tipo,
                "Valor (S/)": round(valor, 2)
            })
            st.success(f"Movimiento '{concepto}' agregado correctamente.")
 
    st.markdown("---")
    st.subheader("Movimientos registrados")
 
    if len(st.session_state.movimientos) == 0:
        st.info("Aún no hay movimientos registrados.")
    else:
        df_mov = pd.DataFrame(st.session_state.movimientos)
        st.dataframe(df_mov, use_container_width=True)
 
        total_ingresos = sum(
            m["Valor (S/)"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso"
        )
        total_gastos = sum(
            m["Valor (S/)"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto"
        )
        saldo = total_ingresos - total_gastos
 
        st.markdown("---")
        st.subheader("Resumen del flujo de caja")
 
        col1, col2, col3 = st.columns(3)
        col1.metric("✅ Total ingresos", f"S/ {total_ingresos:,.2f}")
        col2.metric("❌ Total gastos", f"S/ {total_gastos:,.2f}")
        col3.metric("💰 Saldo final", f"S/ {saldo:,.2f}")
 
        if saldo > 0:
            st.success(f"✅ El flujo de caja está **a favor** con un saldo de S/ {saldo:,.2f}")
        elif saldo < 0:
            st.error(f"⚠️ El flujo de caja está **en contra** con un déficit de S/ {abs(saldo):,.2f}")
        else:
            st.warning("⚖️ El flujo de caja está **en equilibrio** (saldo = 0).")
 
    if st.button("🗑️ Limpiar todos los movimientos"):
        st.session_state.movimientos = []
        st.info("Lista de movimientos reiniciada.")
 
# ═══════════════════════════════════════════════════════════
# EJERCICIO 2 – Registro con NumPy, arrays y DataFrame
# ═══════════════════════════════════════════════════════════
elif seccion == "Ejercicio 2":
    st.title("🏭 Ejercicio 2 – Registro de producción textil con NumPy")
 
    st.markdown("""
    Formulario para registrar la producción en kilogramos por turno en la hilandería.  
    Los datos se almacenan en **arrays de NumPy** y se convierten en un **DataFrame** actualizado.
    """)
 
    # Inicializar arrays en session_state
    if "arr_maquina" not in st.session_state:
        st.session_state.arr_maquina   = np.array([], dtype=str)
        st.session_state.arr_tipo_hilo = np.array([], dtype=str)
        st.session_state.arr_turno     = np.array([], dtype=str)
        st.session_state.arr_kg        = np.array([], dtype=float)
 
    st.markdown("---")
    st.subheader("Nuevo registro de producción")
 
    col1, col2 = st.columns(2)
    with col1:
        maquina   = st.text_input("Máquina / sección", placeholder="Ej: Máquina 3 – Sección A")
        tipo_hilo = st.selectbox("Tipo de hilo", ["Acrílico", "Algodón", "Poliéster", "Lana", "Mezcla"])
    with col2:
        turno         = st.selectbox("Turno", ["T1 – Mañana", "T2 – Tarde", "T3 – Noche"])
        kg_producidos = st.number_input("Kg producidos", min_value=0.0, step=0.1, format="%.1f")
 
    if st.button("➕ Agregar registro"):
        if maquina.strip() == "":
            st.error("El nombre de la máquina no puede estar vacío.")
        else:
            st.session_state.arr_maquina   = np.append(st.session_state.arr_maquina,   maquina.strip())
            st.session_state.arr_tipo_hilo = np.append(st.session_state.arr_tipo_hilo, tipo_hilo)
            st.session_state.arr_turno     = np.append(st.session_state.arr_turno,     turno)
            st.session_state.arr_kg        = np.append(st.session_state.arr_kg,        float(kg_producidos))
            st.success("Registro agregado correctamente.")
 
    st.markdown("---")
    st.subheader("Tabla de producción registrada")
 
    if len(st.session_state.arr_maquina) == 0:
        st.info("Aún no hay registros de producción.")
    else:
        df_prod = pd.DataFrame({
            "Máquina / Sección": st.session_state.arr_maquina,
            "Tipo de hilo":      st.session_state.arr_tipo_hilo,
            "Turno":             st.session_state.arr_turno,
            "Kg producidos":     st.session_state.arr_kg
        })
        st.dataframe(df_prod, use_container_width=True)
 
        total_kg = float(np.sum(st.session_state.arr_kg))
        prom_kg  = float(np.mean(st.session_state.arr_kg))
        max_kg   = float(np.max(st.session_state.arr_kg))
 
        col1, col2, col3 = st.columns(3)
        col1.metric("⚖️ Total kg", f"{total_kg:,.1f} kg")
        col2.metric("📊 Promedio kg/registro", f"{prom_kg:,.1f} kg")
        col3.metric("🏆 Máximo kg en un registro", f"{max_kg:,.1f} kg")
 
    if st.button("🗑️ Limpiar registros"):
        st.session_state.arr_maquina   = np.array([], dtype=str)
        st.session_state.arr_tipo_hilo = np.array([], dtype=str)
        st.session_state.arr_turno     = np.array([], dtype=str)
        st.session_state.arr_kg        = np.array([], dtype=float)
        st.info("Registros limpiados.")
 
# ═══════════════════════════════════════════════════════════
# EJERCICIO 3 – Función externa: calcular_ticket_promedio
# ═══════════════════════════════════════════════════════════
elif seccion == "Ejercicio 3":
    from libreria_funciones_proyecto1 import calcular_ticket_promedio
    st.title("🛒 Ejercicio 3 – Ticket promedio (función externa)")
 
    st.markdown("""
    Usa la función **`calcular_ticket_promedio`** de la librería del curso.  
    Ingresa las ventas totales y el número de clientes para obtener el ticket promedio por cliente.  
    Cada resultado se guarda en un historial tipo DataFrame.
    """)
 
    # Inicializar historial
    if "historial_ticket" not in st.session_state:
        st.session_state.historial_ticket = []
 
    st.markdown("---")
    st.subheader("Parámetros de cálculo")
 
    descripcion   = st.text_input("Descripción", placeholder="Ej: Semana 1 – Mayo")
    col1, col2    = st.columns(2)
    with col1:
        ventas_totales  = st.number_input("Ventas totales (S/)", min_value=0.01, step=1.0, value=1000.0)
    with col2:
        numero_clientes = st.number_input("Número de clientes", min_value=1, step=1, value=10)
 
    if st.button("▶️ Calcular ticket promedio"):
        if descripcion.strip() == "":
            st.error("Ingresa una descripción para identificar el cálculo.")
        else:
            try:
                resultado = calcular_ticket_promedio(
                    ventas_totales   = float(ventas_totales),
                    numero_clientes  = int(numero_clientes)
                )
                ticket = resultado["ticket_promedio"]
 
                st.markdown("---")
                st.subheader("Resultado")
                st.metric("🎫 Ticket promedio por cliente", f"S/ {ticket:,.2f}")
 
                st.session_state.historial_ticket.append({
                    "Descripción":         descripcion.strip(),
                    "Ventas totales (S/)": float(ventas_totales),
                    "N° clientes":         int(numero_clientes),
                    "Ticket promedio (S/)": ticket
                })
                st.success("Resultado guardado en el historial.")
 
            except ValueError as e:
                st.error(f"Error: {e}")
 
    st.markdown("---")
    st.subheader("Historial de resultados")
 
    if len(st.session_state.historial_ticket) == 0:
        st.info("Aún no hay cálculos registrados.")
    else:
        df_hist = pd.DataFrame(st.session_state.historial_ticket)
        st.dataframe(df_hist, use_container_width=True)
 
    if st.button("🗑️ Limpiar historial"):
        st.session_state.historial_ticket = []
        st.info("Historial limpiado.")
 
# ═══════════════════════════════════════════════════════════
# EJERCICIO 4 – CRUD con clase EquipoMantenimiento
# ═══════════════════════════════════════════════════════════
elif seccion == "Ejercicio 4":
    from libreria_clases_proyecto1 import EquipoMantenimiento
    st.title("🔧 Ejercicio 4 – Gestión de equipos con CRUD")
 
    st.markdown("""
    Usa la clase **`EquipoMantenimiento`** de la librería del curso.  
    Registra equipos industriales, consulta sus indicadores (MTBF, MTTR, disponibilidad)  
    y administra los registros con operaciones **Crear, Leer, Actualizar y Eliminar**.
    """)
 
    # Inicializar registros CRUD
    if "equipos" not in st.session_state:
        st.session_state.equipos = {}
    if "eq_contador" not in st.session_state:
        st.session_state.eq_contador = 1
 
    # ── CREAR ─────────────────────────────────────────────
    st.markdown("---")
    st.subheader("➕ Crear nuevo equipo")
 
    col1, col2 = st.columns(2)
    with col1:
        eq_nombre   = st.text_input("Nombre del equipo", placeholder="Ej: Huso 12 – Sección B")
        eq_horas_op = st.number_input("Horas de operación", min_value=1.0, step=1.0, value=720.0)
    with col2:
        eq_fallas   = st.number_input("Número de fallas", min_value=1, step=1, value=3)
        eq_h_rep    = st.number_input("Horas de reparación total", min_value=0.0, step=0.5, value=6.0)
 
    if st.button("💾 Registrar equipo"):
        if eq_nombre.strip() == "":
            st.error("El nombre del equipo no puede estar vacío.")
        else:
            try:
                equipo_obj = EquipoMantenimiento(
                    nombre_equipo    = eq_nombre.strip(),
                    horas_operacion  = float(eq_horas_op),
                    numero_fallas    = int(eq_fallas),
                    horas_reparacion = float(eq_h_rep)
                )
                resumen = equipo_obj.resumen()
                eq_id = st.session_state.eq_contador
                st.session_state.equipos[eq_id] = {
                    "nombre":           eq_nombre.strip(),
                    "horas_operacion":  float(eq_horas_op),
                    "numero_fallas":    int(eq_fallas),
                    "horas_reparacion": float(eq_h_rep),
                    "MTBF (h)":         resumen["mtbf_h"],
                    "MTTR (h)":         resumen["mttr_h"],
                    "Disponibilidad %": resumen["disponibilidad_pct"]
                }
                st.session_state.eq_contador += 1
                st.success(f"Equipo '{eq_nombre}' registrado con ID {eq_id}.")
            except ValueError as e:
                st.error(f"Error: {e}")
 
    # ── LEER ──────────────────────────────────────────────
    st.markdown("---")
    st.subheader("📋 Equipos registrados")
 
    if len(st.session_state.equipos) == 0:
        st.info("No hay equipos registrados aún.")
    else:
        filas = []
        for eq_id, datos in st.session_state.equipos.items():
            filas.append({
                "ID":               eq_id,
                "Equipo":           datos["nombre"],
                "Horas operación":  datos["horas_operacion"],
                "Fallas":           datos["numero_fallas"],
                "Horas reparación": datos["horas_reparacion"],
                "MTBF (h)":         datos["MTBF (h)"],
                "MTTR (h)":         datos["MTTR (h)"],
                "Disponibilidad %": datos["Disponibilidad %"]
            })
        df_equipos = pd.DataFrame(filas)
        st.dataframe(df_equipos, use_container_width=True)
 
        # ── ACTUALIZAR ────────────────────────────────────
        st.markdown("---")
        st.subheader("✏️ Actualizar equipo")
 
        ids_disponibles = list(st.session_state.equipos.keys())
        id_actualizar = st.selectbox(
            "Selecciona el ID del equipo a actualizar",
            ids_disponibles,
            key="sel_actualizar"
        )
 
        datos_sel = st.session_state.equipos[id_actualizar]
        col1, col2 = st.columns(2)
        with col1:
            nuevo_nombre  = st.text_input("Nuevo nombre", value=datos_sel["nombre"], key="upd_nombre")
            nuevas_horas  = st.number_input("Horas de operación", value=datos_sel["horas_operacion"], min_value=1.0, step=1.0, key="upd_horas")
        with col2:
            nuevas_fallas = st.number_input("Número de fallas", value=datos_sel["numero_fallas"], min_value=1, step=1, key="upd_fallas")
            nuevas_h_rep  = st.number_input("Horas de reparación", value=datos_sel["horas_reparacion"], min_value=0.0, step=0.5, key="upd_hrep")
 
        if st.button("🔄 Guardar cambios"):
            if nuevo_nombre.strip() == "":
                st.error("El nombre no puede estar vacío.")
            else:
                try:
                    equipo_upd = EquipoMantenimiento(
                        nombre_equipo    = nuevo_nombre.strip(),
                        horas_operacion  = float(nuevas_horas),
                        numero_fallas    = int(nuevas_fallas),
                        horas_reparacion = float(nuevas_h_rep)
                    )
                    resumen_upd = equipo_upd.resumen()
                    st.session_state.equipos[id_actualizar] = {
                        "nombre":           nuevo_nombre.strip(),
                        "horas_operacion":  float(nuevas_horas),
                        "numero_fallas":    int(nuevas_fallas),
                        "horas_reparacion": float(nuevas_h_rep),
                        "MTBF (h)":         resumen_upd["mtbf_h"],
                        "MTTR (h)":         resumen_upd["mttr_h"],
                        "Disponibilidad %": resumen_upd["disponibilidad_pct"]
                    }
                    st.success(f"Equipo ID {id_actualizar} actualizado correctamente.")
                except ValueError as e:
                    st.error(f"Error: {e}")
 
        # ── ELIMINAR ──────────────────────────────────────
        st.markdown("---")
        st.subheader("🗑️ Eliminar equipo")
 
        id_eliminar = st.selectbox(
            "Selecciona el ID del equipo a eliminar",
            ids_disponibles,
            key="sel_eliminar"
        )
 
        nombre_a_eliminar = st.session_state.equipos[id_eliminar]["nombre"]
        st.warning(f"Se eliminará el equipo: **{nombre_a_eliminar}** (ID {id_eliminar})")
 
        if st.button("❌ Confirmar eliminación"):
            del st.session_state.equipos[id_eliminar]
            st.success(f"Equipo ID {id_eliminar} eliminado correctamente.")
            st.rerun()
