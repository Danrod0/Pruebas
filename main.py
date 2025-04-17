import streamlit as st
import base64

# Configurar la página
st.set_page_config(page_title="Simulador de WhatsApp Psicológico", layout="wide")

# Fondo estilo WhatsApp en base64
def set_background():
    with open("https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?fit=crop&w=600&q=80", "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data).decode()
        css = f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)

# Aplicar fondo
# set_background()  # (No aplicable en entorno restringido, solo funciona en Streamlit Cloud con archivos locales o URLs directas)

# Simular datos de pruebas
pruebas = {
    "WAIS": {
        "avatar": "🧠",
        "mensaje": "¿Querés saber más sobre inteligencia?",
        "hora": "4:20 PM",
        "leido": False
    },
    "NEUROPSI": {
        "avatar": "🧬",
        "mensaje": "¿Tenés problemas de memoria o atención?",
        "hora": "4:35 PM",
        "leido": False
    },
    "MMPI-2-R": {
        "avatar": "🕵️",
        "mensaje": "Puedo ayudarte a entender tu personalidad.",
        "hora": "5:01 PM",
        "leido": False
    },
    "PAI": {
        "avatar": "📊",
        "mensaje": "Tengo escalas clínicas para vos.",
        "hora": "5:15 PM",
        "leido": False
    },
    "NEO-PI-R": {
        "avatar": "🌈",
        "mensaje": "¿Querés conocer tus rasgos de personalidad?",
        "hora": "5:45 PM",
        "leido": False
    }
}

if "pantalla" not in st.session_state:
    st.session_state.pantalla = "inicio"
if "chat_actual" not in st.session_state:
    st.session_state.chat_actual = ""
if "leidos" not in st.session_state:
    st.session_state.leidos = {k: False for k in pruebas}
if "wais_step" not in st.session_state:
    st.session_state.wais_step = 0

def volver_al_menu():
    st.session_state.pantalla = "inicio"
    st.session_state.chat_actual = ""

# INICIO
if st.session_state.pantalla == "inicio":
    st.markdown("<h2 style='color:white;'>Chats</h2>", unsafe_allow_html=True)
    for nombre, datos in pruebas.items():
        col1, col2 = st.columns([0.85, 0.15])
        with col1:
            if st.button(f"{datos['avatar']}  {nombre}\n{datos['mensaje']}", key=nombre):
                st.session_state.pantalla = "chat"
                st.session_state.chat_actual = nombre
                st.session_state.leidos[nombre] = True
        with col2:
            if not st.session_state.leidos[nombre]:
                st.markdown("<span style='color:lime;font-size:20px;'>●</span>", unsafe_allow_html=True)

# CHAT
elif st.session_state.pantalla == "chat":
    prueba = st.session_state.chat_actual
    st.markdown(f"<h3 style='color:white;'>{prueba} {pruebas[prueba]['avatar']}</h3>", unsafe_allow_html=True)
    st.markdown("---")

    if prueba == "WAIS":
        if st.session_state.wais_step == 0:
            st.chat_message("assistant").markdown("Hola, soy WAIS. ¿Querés saber más sobre inteligencia?")
            if st.button("Sí, contame"):
                st.session_state.wais_step = 1

        elif st.session_state.wais_step == 1:
            st.chat_message("assistant").markdown("Sirvo para evaluar la inteligencia general en personas mayores de 16 años.")
            st.chat_message("user").markdown("¿Y cómo lo hacés?")
            st.session_state.wais_step = 2

        elif st.session_state.wais_step == 2:
            st.chat_message("assistant").markdown("""Mis escalas incluyen:
- Comprensión Verbal
- Razonamiento Perceptual
- Memoria de Trabajo
- Velocidad de Procesamiento""")
            st.chat_message("user").markdown("¿Y cómo se aplica?")
            st.session_state.wais_step = 3

        elif st.session_state.wais_step == 3:
            st.chat_message("assistant").markdown("Se aplica en sesiones individuales de 60 a 90 minutos. ¡Gracias por hablar conmigo!")
            if st.button("Volver al menú"):
                volver_al_menu()

    else:
        st.chat_message("assistant").markdown(f"Este chat con {prueba} está en construcción.")
        if st.button("Volver al menú"):
            volver_al_menu()
