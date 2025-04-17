
import streamlit as st

st.set_page_config(page_title="Simulador de Pruebas Psicológicas", layout="wide")

# CSS
st.markdown('''<style>
/* Todo el CSS anterior mantenido igual para estilo */
.stApp { font-family: 'Segoe UI', sans-serif; background-color: #d1d1d1; }
/* ... resto del CSS ... (omitido por espacio) ... */
</style>''', unsafe_allow_html=True)

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
        "hora": "4:21 p.m.",
        "leido": False
    },
    "NEUROPSI": {
        "avatar": "https://cdn-icons-png.flaticon.com/512/2821/2821028.png",
        "mensaje": "Hola, soy NEUROPSI. ¿Querés saber sobre funciones cognitivas?",
        "hora": "3:42 p.m.",
        "leido": False
    },
    "MMPI-2-R": {
        "avatar": "https://cdn-icons-png.flaticon.com/512/3135/3135789.png",
        "mensaje": "Hola, soy MMPI-2-R. ¿Te interesa tu perfil psicológico?",
        "hora": "3:10 p.m.",
        "leido": False
    },
    "PAI": {
        "avatar": "https://cdn-icons-png.flaticon.com/512/1048/1048949.png",
        "mensaje": "Hola, soy PAI. ¿Querés conocer tu ajuste psicológico?",
        "hora": "2:55 p.m.",
        "leido": False
    },
    "NEO-PI-R": {
        "avatar": "https://cdn-icons-png.flaticon.com/512/219/219969.png",
        "mensaje": "Hola, soy NEO-PI-R. ¿Querés conocer tus rasgos de personalidad?",
        "hora": "2:30 p.m.",
        "leido": False
    }
}

# Conversación de WAIS
wais_conversacion = [
    {"pregunta": "Hola, soy WAIS. ¿Querés saber más sobre inteligencia?", "respuestas": ["Sí, contame"], "respuesta_usuario": "Sí, contame"},
    {"pregunta": "Sirvo para evaluar la inteligencia general en personas mayores de 16 años.", "respuestas": ["¿Y cómo lo hacés?"], "respuesta_usuario": "¿Y cómo lo hacés?"},
    {"pregunta": "Mis escalas incluyen: Comprensión Verbal, Razonamiento Perceptual, Memoria de Trabajo y Velocidad de Procesamiento.", "respuestas": ["¿Y cómo se aplica?"], "respuesta_usuario": "¿Y cómo se aplica?"},
    {"pregunta": "Se aplica en sesiones individuales de 60 a 90 minutos. ¡Gracias por hablar conmigo!", "respuestas": [], "respuesta_usuario": ""}
]

# Menú
if st.session_state.pantalla == "menu":
    st.markdown('<div class="menu-container">', unsafe_allow_html=True)
    for nombre, data in pruebas.items():
        cols = st.columns([0.15, 0.7, 0.15])
        with cols[0]:
            st.image(data["avatar"], width=45)
        with cols[1]:
            st.markdown(f"<b>{nombre}</b><br><small>{data['mensaje']}</small>", unsafe_allow_html=True)
            if st.button(f"Responder a {nombre}", key=nombre):
                st.session_state.pantalla = nombre.lower()
                st.experimental_rerun()
        with cols[2]:
            st.markdown(f"<div style='text-align:right;font-size:12px;color:#ccc;'>{data['hora']}<br><span style='color:#25D366;font-size:18px;'>●</span></div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Chat de WAIS
if st.session_state.pantalla == "wais":
    st.markdown('<div class="chat-box">', unsafe_allow_html=True)

    top = st.columns([0.85, 0.15])
    with top[0]:
        st.markdown(f'''
        <div class="chat-header">
            <div class="chat-header-left">
                <img src="{pruebas['WAIS']['avatar']}">
                <div><b>WAIS</b><br><small>en línea</small></div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    with top[1]:
        if st.button("Volver"):
            st.session_state.pantalla = "menu"
            st.session_state.paso_wais = 0
            st.experimental_rerun()

    st.markdown('<div class="chat-body">', unsafe_allow_html=True)

    paso = st.session_state.paso_wais
    for i in range(paso + 1):
        mensaje = wais_conversacion[i]
        st.markdown(f'<div class="bubble-assistant">{mensaje["pregunta"]}</div>', unsafe_allow_html=True)
        if i < paso:
            st.markdown(f'<div class="bubble-user">{mensaje["respuesta_usuario"]}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    if paso < len(wais_conversacion):
        opciones = wais_conversacion[paso]["respuestas"]
        if opciones:
            st.markdown('<div class="response-buttons">', unsafe_allow_html=True)
            for opcion in opciones:
                if st.button(opcion, key=f"respuesta_{paso}"):
                    st.session_state.paso_wais += 1
                    st.experimental_rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('''
    <div class="chat-footer">
        <span class="icon">&#128206;</span>
        <span class="icon">&#128247;</span>
        <input type="text" placeholder="Escribí un mensaje" disabled>
        <span class="icon">&#127908;</span>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
