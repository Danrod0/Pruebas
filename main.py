import streamlit as st

st.set_page_config(page_title="Simulador de Pruebas Psicológicas", layout="wide")

# CSS
st.markdown('''
<style>
.stApp {
    font-family: 'Segoe UI', sans-serif;
    background-color: #ece5dd;
}
.menu-container {
    max-width: 600px;
    margin: auto;
    margin-top: 40px;
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    overflow: hidden;
}
.chat-preview {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 15px;
    border-bottom: 1px solid #eee;
}
.chat-preview:hover {
    background-color: #f5f5f5;
    cursor: pointer;
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
}
.chat-info small {
    color: gray;
}
.chat-time {
    font-size: 12px;
    color: gray;
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
    gap: 10px;
    background-color: #075E54;
    color: white;
    padding: 10px;
    border-radius: 10px 10px 0 0;
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

# Estado inicial
if "pantalla" not in st.session_state:
    st.session_state.pantalla = "menu"
if "paso_wais" not in st.session_state:
    st.session_state.paso_wais = 0
if "leido_wais" not in st.session_state:
    st.session_state.leido_wais = False

# Conversación de WAIS
wais_conversacion = [
    {
        "pregunta": "Hola, soy WAIS. ¿Querés saber más sobre inteligencia?",
        "respuestas": ["Sí, contame"],
        "respuesta_usuario": "Sí, contame"
    },
    {
        "pregunta": "Sirvo para evaluar la inteligencia general en personas mayores de 16 años.",
        "respuestas": ["¿Y cómo lo hacés?"],
        "respuesta_usuario": "¿Y cómo lo hacés?"
    },
    {
        "pregunta": "Mis escalas incluyen: Comprensión Verbal, Razonamiento Perceptual, Memoria de Trabajo y Velocidad de Procesamiento.",
        "respuestas": ["¿Y cómo se aplica?"],
        "respuesta_usuario": "¿Y cómo se aplica?"
    },
    {
        "pregunta": "Se aplica en sesiones individuales de 60 a 90 minutos. ¡Gracias por hablar conmigo!",
        "respuestas": [],
        "respuesta_usuario": ""
    }
]

# Menú estilo WhatsApp
if st.session_state.pantalla == "menu":
    st.markdown('<div class="menu-container">', unsafe_allow_html=True)
    st.markdown('''
    <div class="chat-preview" onclick="window.location.reload();">
        <div class="chat-avatar">
            <img src="https://cdn-icons-png.flaticon.com/512/4333/4333609.png">
            <div class="chat-info">
                <b>WAIS</b><br>
                <small>Hola, ¿querés saber más sobre inteligencia?</small>
            </div>
        </div>
        <div class="chat-time">
            4:21 p.m.
            <span class="chat-unread">●</span>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    if st.button("Iniciar chat con WAIS"):
        st.session_state.pantalla = "wais"
        st.session_state.leido_wais = True
    st.markdown('</div>', unsafe_allow_html=True)

# Chat estilo WhatsApp
if st.session_state.pantalla == "wais":
    st.markdown('<div class="chat-box">', unsafe_allow_html=True)

    st.markdown('''
    <div class="chat-header">
        <img src="https://cdn-icons-png.flaticon.com/512/4333/4333609.png">
        <div>
            <b>WAIS</b><br><small>en línea</small>
        </div>
    </div>
    <div class="chat-body">
    ''', unsafe_allow_html=True)

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
                if st.button(opcion):
                    st.session_state.paso_wais += 1
                    st.experimental_rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            if st.button("Volver al menú"):
                st.session_state.pantalla = "menu"
                st.session_state.paso_wais = 0

    st.markdown('''
    <div class="chat-footer">
        <span class="icon">&#128206;</span>
        <span class="icon">&#128247;</span>
        <input type="text" placeholder="Escribí un mensaje" disabled>
        <span class="icon">&#127908;</span>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
