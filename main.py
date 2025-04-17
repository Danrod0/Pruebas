import streamlit as st

st.set_page_config(page_title="Simulador de Pruebas Psicológicas", layout="wide")

# Estado inicial
if "pantalla" not in st.session_state:
    st.session_state.pantalla = "menu"
if "paso_wais" not in st.session_state:
    st.session_state.paso_wais = 0

# Diccionario de pruebas
pruebas = {
    "WAIS": {
        "avatar": "https://cdn-icons-png.flaticon.com/512/4333/4333609.png",
        "mensaje": "Hola, ¿querés saber más sobre inteligencia?",
        "hora": "4:21 p.m."
    },
    "NEUROPSI": {
        "avatar": "https://cdn-icons-png.flaticon.com/512/2821/2821028.png",
        "mensaje": "Hola, soy NEUROPSI. ¿Querés saber sobre funciones cognitivas?",
        "hora": "3:42 p.m."
    },
    "MMPI-2-R": {
        "avatar": "https://cdn-icons-png.flaticon.com/512/3135/3135789.png",
        "mensaje": "Hola, soy MMPI-2-R. ¿Te interesa tu perfil psicológico?",
        "hora": "3:10 p.m."
    },
    "PAI": {
        "avatar": "https://cdn-icons-png.flaticon.com/512/1048/1048949.png",
        "mensaje": "Hola, soy PAI. ¿Querés conocer tu ajuste psicológico?",
        "hora": "2:55 p.m."
    },
    "NEO-PI-R": {
        "avatar": "https://cdn-icons-png.flaticon.com/512/219/219969.png",
        "mensaje": "Hola, soy NEO-PI-R. ¿Querés conocer tus rasgos de personalidad?",
        "hora": "2:30 p.m."
    }
}

# Conversación WAIS
wais_conversacion = [
    {"pregunta": "Hola, soy WAIS. ¿Querés saber más sobre inteligencia?", "respuestas": ["Sí, contame"], "respuesta_usuario": "Sí, contame"},
    {"pregunta": "Sirvo para evaluar la inteligencia general en personas mayores de 16 años.", "respuestas": ["¿Y cómo lo hacés?"], "respuesta_usuario": "¿Y cómo lo hacés?"},
    {"pregunta": "Mis escalas incluyen: Comprensión Verbal, Razonamiento Perceptual, Memoria de Trabajo y Velocidad de Procesamiento.", "respuestas": ["¿Y cómo se aplica?"], "respuesta_usuario": "¿Y cómo se aplica?"},
    {"pregunta": "Se aplica en sesiones individuales de 60 a 90 minutos. ¡Gracias por hablar conmigo!", "respuestas": [], "respuesta_usuario": ""}
]

# MENÚ
if st.session_state.pantalla == "menu":
    st.title("Simulador de Pruebas Psicológicas")
    for nombre, data in pruebas.items():
        st.image(data["avatar"], width=40)
        st.markdown(f"**{nombre}**  
{data['mensaje']}  
*{data['hora']}*")
        if st.button(f"Responder a {nombre}", key=f"btn_{nombre}"):
            st.session_state.pantalla = nombre.lower()
            st.experimental_rerun()
        st.markdown("---")

# CHAT WAIS
if st.session_state.pantalla == "wais":
    st.markdown("### Chat con WAIS")
    if st.button("Volver al menú", key="volver"):
        st.session_state.pantalla = "menu"
        st.session_state.paso_wais = 0
        st.experimental_rerun()

    paso = st.session_state.paso_wais
    for i in range(paso + 1):
        mensaje = wais_conversacion[i]
        st.markdown(f"**WAIS:** {mensaje['pregunta']}")
        if i < paso:
            st.markdown(f"*Tú:* {mensaje['respuesta_usuario']}")

    if paso < len(wais_conversacion):
        for r in wais_conversacion[paso]["respuestas"]:
            if st.button(r, key=f"respuesta_{paso}"):
                st.session_state.paso_wais += 1
                st.experimental_rerun()
