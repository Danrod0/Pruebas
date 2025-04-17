import streamlit as st

st.set_page_config(page_title="Simulador de Pruebas Psicológicas", layout="wide")

# CSS general
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
.chat-button {
    background-color: #25D366;
    color: white;
    width: 100%;
    text-align: left;
    padding: 10px 15px;
    border: none;
    border-bottom: 1px solid #eee;
    font-size: 16px;
}
.chat-button:hover {
    background-color: #dcf8c6;
}
.response-buttons button {
    background-color: #d81b60;
    color: white;
    border: none;
    padding: 10px;
    border-radius: 20px;
    margin-top: 10px;
    font-size: 16px;
    cursor: pointer;
}
</style>
''', unsafe_allow_html=True)

# Estados iniciales
if "pantalla" not in st.session_state:
    st.session_state.pantalla = "menu"
if "paso_wais" not in st.session_state:
    st.session_state.paso_wais = 0

# Conversación de WAIS
wais_conversacion = [
    {
        "pregunta": "Hola, soy WAIS. &iquest;Quer&eacute;s saber m&aacute;s sobre inteligencia?",
        "respuestas": ["S&iacute;, contame"],
        "respuesta_usuario": "S&iacute;, contame"
    },
    {
        "pregunta": "Sirvo para evaluar la inteligencia general en personas mayores de 16 a&ntilde;os.",
        "respuestas": ["&iquest;Y c&oacute;mo lo hac&eacute;s?"],
        "respuesta_usuario": "&iquest;Y c&oacute;mo lo hac&eacute;s?"
    },
    {
        "pregunta": "Mis escalas incluyen: Comprensi&oacute;n Verbal, Razonamiento Perceptual, Memoria de Trabajo y Velocidad de Procesamiento.",
        "respuestas": ["&iquest;Y c&oacute;mo se aplica?"],
        "respuesta_usuario": "&iquest;Y c&oacute;mo se aplica?"
    },
    {
        "pregunta": "Se aplica en sesiones individuales de 60 a 90 minutos. &iexcl;Gracias por hablar conmigo!",
        "respuestas": [],
        "respuesta_usuario": ""
    }
]

# Menú tipo WhatsApp
if st.session_state.pantalla == "menu":
    st.markdown('<div class="menu-container">', unsafe_allow_html=True)
    st.markdown('<div class="chat-button" onclick="window.location.reload();">WAIS<br><small>Hola, &iquest;Quer&eacute;s saber m&aacute;s sobre inteligencia?</small></div>', unsafe_allow_html=True)
    if st.button("Iniciar chat con WAIS"):
        st.session_state.pantalla = "wais"
    st.markdown('</div>', unsafe_allow_html=True)

# Chat
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

    # Footer con íconos
    st.markdown('''
    <div class="chat-footer">
        <span class="icon">&#128206;</span>
        <span class="icon">&#128247;</span>
        <input type="text" placeholder="Escribí un mensaje" disabled>
        <span class="icon">&#127908;</span>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
