import streamlit as st

st.set_page_config(page_title="Simulador de Pruebas Psicológicas", layout="wide")

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
    }
}

# Conversación WAIS con toda la info que compartiste
wais_conversacion = [
    {"pregunta": "Hola, soy WAIS-IV. ¿Querés saber más sobre inteligencia?", "respuestas": ["Sí, contame"], "respuesta_usuario": "Sí, contame"},
    {"pregunta": "Mi nombre completo es: Escala de Inteligencia para Adultos de Wechsler, Cuarta Edición.", "respuestas": ["¿Qué es lo que mido?"], "respuesta_usuario": "¿Qué es lo que mides?"},
    {"pregunta": "Mido la inteligencia general (CI) en adultos.", "respuestas": ["¿Y para qué se usa?"], "respuesta_usuario": "¿Y para qué se usa?"},
    {"pregunta": "Me usan para:
- Diagnóstico de discapacidad intelectual o superdotación
- Evaluación de deterioro cognitivo (como demencia)
- Apoyo clínico, neuropsicológico y forense", "respuestas": ["¿Cuáles son tus escalas?"], "respuesta_usuario": "¿Cuáles son tus escalas?"},
    {"pregunta": "Tengo 4 escalas principales:

1. Comprensión Verbal (ICV):
• Semejanzas
• Vocabulario
• Información
• (Complementaria: Comprensión)", "respuestas": ["¿Y las otras?"], "respuesta_usuario": "¿Y las otras?"},
    {"pregunta": "2. Razonamiento Perceptivo (IRP):
• Diseño con cubos
• Matrices
• Puzzles visuales
• (Complementarias: Peso de figuras, Figuras incompletas)", "respuestas": ["¿Y la siguiente?"], "respuesta_usuario": "¿Y la siguiente?"},
    {"pregunta": "3. Memoria de Trabajo (IMT):
• Retención de dígitos
• Aritmética
• (Complementaria: Secuencia de letras y números)", "respuestas": ["¿Falta alguna más?"], "respuesta_usuario": "¿Falta alguna más?"},
    {"pregunta": "4. Velocidad de Procesamiento (IVP):
• Claves
• Búsqueda de símbolos
• (Complementaria: Cancelación)", "respuestas": ["¿Algo más importante que deba saber?"], "respuesta_usuario": "¿Algo más importante que deba saber?"},
    {"pregunta": "Sí. También tengo un resultado general: el Cociente Intelectual Total (CIT), que resume tu desempeño global. ¡Gracias por conversar conmigo!", "respuestas": [], "respuesta_usuario": ""}
]

# Menú
if st.session_state.pantalla == "menu":
    st.write("Encabezado y diseño del menú (ya incluido en versiones anteriores)")

# Chat WAIS
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
