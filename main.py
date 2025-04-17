import streamlit as st

st.set_page_config(page_title="Simulador de Chats Psicológicos", layout="centered")

# Datos de las pruebas
pruebas = {
    "WAIS": {"mensaje": "Hola, soy WAIS.", "leido": False},
    "NEUROPSI": {"mensaje": "Hola, soy NEUROPSI.", "leido": False},
    "MMPI-2-R": {"mensaje": "Hola, soy MMPI-2-R.", "leido": False},
    "PAI": {"mensaje": "Hola, soy PAI.", "leido": False},
    "NEO-PI-R": {"mensaje": "Hola, soy NEO-PI-R.", "leido": False}
}

# Inicializar estados
if "pantalla" not in st.session_state:
    st.session_state.pantalla = "inicio"
if "leidos" not in st.session_state:
    st.session_state.leidos = {k: False for k in pruebas}
if "chat_actual" not in st.session_state:
    st.session_state.chat_actual = ""

# Función para volver al inicio
def volver_al_inicio():
    st.session_state.pantalla = "inicio"
    st.session_state.chat_actual = ""

# Pantalla principal: lista de chats
if st.session_state.pantalla == "inicio":
    st.title("Chats")
    st.markdown("Simulador de conversación con pruebas psicológicas")
    for nombre, data in pruebas.items():
        col1, col2 = st.columns([0.9, 0.1])
        with col1:
            if st.button(f"{nombre}: {data['mensaje']}", key=nombre):
                st.session_state.pantalla = "chat"
                st.session_state.chat_actual = nombre
                st.session_state.leidos[nombre] = True
        with col2:
            if not st.session_state.leidos[nombre]:
                st.markdown("🟢")

# Chat individual (solo WAIS funcional por ahora)
elif st.session_state.pantalla == "chat":
    prueba = st.session_state.chat_actual
    st.markdown(f"### Chat con {prueba}")
    st.markdown("---")

    if prueba == "WAIS":
        if "wais_step" not in st.session_state:
            st.session_state.wais_step = 0

        if st.session_state.wais_step == 0:
            st.chat_message("assistant").markdown("Hola, soy WAIS, la Escala Wechsler de Inteligencia para Adultos.")
            if st.button("¿Para qué servís?"):
                st.session_state.wais_step = 1

        elif st.session_state.wais_step == 1:
            st.chat_message("assistant").markdown("Sirvo para evaluar la inteligencia general en personas mayores de 16 años.")
            if st.button("¿Qué escalas usás?"):
                st.session_state.wais_step = 2

        elif st.session_state.wais_step == 2:
            st.chat_message("assistant").markdown("""Mis escalas principales son:
- Comprensión Verbal
- Razonamiento Perceptual
- Memoria de Trabajo
- Velocidad de Procesamiento""")
            if st.button("¿Cómo se aplica?"):
                st.session_state.wais_step = 3

        elif st.session_state.wais_step == 3:
            st.chat_message("assistant").markdown("Se aplica individualmente, en una sesión de entre 60 y 90 minutos.")
            st.success("¡Gracias por conversar conmigo!")
            if st.button("Volver al menú"):
                volver_al_inicio()

    else:
        st.info(f"El chat de {prueba} está en construcción.")
        if st.button("Volver al menú"):
            volver_al_inicio()
