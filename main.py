import streamlit as st

st.set_page_config(page_title="Simulador de Pruebas Psicológicas", layout="wide")

# CSS completo
st.markdown('''
<style>
.stApp {
    font-family: 'Segoe UI', sans-serif;
    background-color: #d1d1d1;
}
.header {
    background-color: #111;
    color: white;
    padding: 20px 30px 10px 30px;
    border-radius: 0 0 15px 15px;
    max-width: 600px;
    margin: auto;
}
.header h1 {
    font-size: 28px;
    margin-bottom: 10px;
}
.search-bar {
    background-color: #2c2c2c;
    color: #ccc;
    padding: 10px 15px;
    border-radius: 10px;
    margin-bottom: 15px;
}
.chip-row {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}
.chip {
    background-color: #1d3026;
    padding: 6px 12px;
    color: white;
    border-radius: 20px;
    font-size: 14px;
}
.menu-container {
    max-width: 600px;
    margin: auto;
    background-color: #2f2f2f;
    border-radius: 10px;
    overflow: hidden;
    color: white;
}
.chat-preview {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 15px;
}
.chat-preview:hover {
    background-color: #444;
    cursor: pointer;
}
.divider {
    border-bottom: 1px solid #444;
    margin: 0 15px;
}
.chat-avatar {
    display: flex;
    align-items: center;
    gap: 10px;
}
.chat-avatar img {
    width: 45px;
    height: 45px;
    border-radius: 50%;
}
.chat-info {
    line-height: 1.2;
    background-color: #3e3e3e;
    border-radius: 10px;
    padding: 5px 10px;
}
.chat-info small {
    color: #ccc;
}
.chat-time {
    font-size: 12px;
    color: #ccc;
    text-align: right;
}
.chat-unread {
    color: #25D366;
    font-size: 20px;
    margin-left: 5px;
}
.chat-box {
    background-color: #ffe6f0;
    max-width: 600px;
    margin: auto;
    margin-top: 30px;
    padding: 0;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.15);
}
.chat-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
    background-color: #075E54;
    color: white;
    padding: 10px;
    border-radius: 10px 10px 0 0;
}
.chat-header-left {
    display: flex;
    align-items: center;
    gap: 10px;
}
.chat-header img {
    width: 40px;
    height: 40px;
    border-radius: 50%;
}
.chat-body {
    padding: 15px 15px 0 15px;
}
.bubble-assistant {
    background-color: #f1f0f0;
    color: black;
    padding: 10px 14px;
    border-radius: 0 10px 10px 10px;
    margin: 8px 0;
    max-width: 80%;
}
.bubble-user {
    background-color: #f8b7c3;
    color: black;
    padding: 10px 14px;
    border-radius: 10px 0 10px 10px;
    margin: 8px 0;
    max-width: 80%;
    margin-left: auto;
}
.response-buttons {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 10px;
    margin: 15px 15px 0 15px;
}
.response-buttons button {
    background-color: #d81b60;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 20px;
    font-size: 16px;
    cursor: pointer;
}
.chat-footer {
    display: flex;
    align-items: center;
    background-color: white;
    padding: 10px 15px;
    border-radius: 0 0 10px 10px;
    gap: 10px;
}
.chat-footer input {
    flex: 1;
    padding: 10px;
    border-radius: 20px;
    border: 1px solid #ccc;
}
.icon {
    font-size: 20px;
    cursor: pointer;
}
</style>
''', unsafe_allow_html=True)

# Estado
if "pantalla" not in st.session_state:
    st.session_state.pantalla = "menu"
if "paso_wais" not in st.session_state:
    st.session_state.paso_wais = 0

# Pruebas
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

if st.session_state.pantalla == 'menu':
    # Encabezado estilo WhatsApp
    st.markdown('<div class="header">', unsafe_allow_html=True)
    st.markdown('<h1>Chats</h1>', unsafe_allow_html=True)
    st.markdown('<div class="search-bar">🔍 Ask Meta AI or Search</div>', unsafe_allow_html=True)
    st.markdown('''
    <div class="chip-row">
    <div class="chip">All</div>
    <div class="chip">Unread 16</div>
    <div class="chip">Favorites</div>
    <div class="chip">Groups 9</div>
    </div>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Menú
if st.session_state.pantalla == "menu":
    st.markdown('<div class="menu-container">', unsafe_allow_html=True)
    for i, (nombre, data) in enumerate(pruebas.items()):
        cols = st.columns([0.15, 0.7, 0.15])
        with cols[0]:
            st.image(data["avatar"], width=45)
        with cols[1]:
            st.markdown(f'<div class="chat-info"><b>{nombre}</b><br><small>{data["mensaje"]}</small></div>', unsafe_allow_html=True)
            if st.button(f"Responder a {nombre}", key=nombre):
                st.session_state.pantalla = nombre.lower()
                st.experimental_rerun()
        with cols[2]:
            st.markdown(f"<div style='text-align:right;font-size:12px;color:#ccc;'>{data['hora']}<br><span style='color:#25D366;font-size:18px;'>●</span></div>", unsafe_allow_html=True)
        if i < len(pruebas) - 1:
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Chat de WAIS
if st.session_state.pantalla == "wais":
    st.markdown('<div class="chat-box">', unsafe_allow_html=True)
    header_cols = st.columns([0.85, 0.15])
    with header_cols[0]:
        st.markdown(f'''
        <div class="chat-header">
            <div class="chat-header-left">
                <img src="{pruebas['WAIS']['avatar']}">
                <div><b>WAIS</b><br><small>en línea</small></div>
            </div>
        </div>''', unsafe_allow_html=True)
    with header_cols[1]:
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

    opciones = wais_conversacion[paso]["respuestas"] if paso < len(wais_conversacion) else []
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
