
import streamlit as st

st.set_page_config(page_title="Chat WAIS", layout="wide")

# Estilos
st.markdown('''
    <style>
    .stApp {
        background-color: #ffe6f0;
        font-family: 'Segoe UI', sans-serif;
    }
    .chat-container {
        background-color: #fff;
        max-width: 600px;
        margin: auto;
        padding: 10px 20px;
        border-radius: 10px;
        margin-top: 30px;
        box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
    }
    .chat-header {
        display: flex;
        align-items: center;
        gap: 10px;
        background-color: #d81b60;
        color: white;
        padding: 10px;
        border-radius: 10px 10px 0 0;
    }
    .chat-header img {
        width: 40px;
        height: 40px;
        border-radius: 50%;
    }
    .bubble-assistant {
        background-color: #f1f0f0;
        color: black;
        padding: 10px 14px;
        border-radius: 0 10px 10px 10px;
        margin: 8px 0;
        width: fit-content;
        max-width: 80%;
    }
    .bubble-user {
        background-color: #ffcdd2;
        color: black;
        padding: 10px 14px;
        border-radius: 10px 0 10px 10px;
        margin: 8px 0;
        width: fit-content;
        max-width: 80%;
        margin-left: auto;
    }
    .response-buttons {
        display: flex;
        flex-direction: column;
        gap: 10px;
        margin-top: 15px;
    }
    button {
        background-color: #d81b60 !important;
        color: white !important;
        border: none;
        padding: 10px;
        border-radius: 20px;
        font-size: 16px !important;
        cursor: pointer;
    }
    </style>
''', unsafe_allow_html=True)

# Flujo de conversaciÃ³n
wais_conversacion = [
    {
        "pregunta": "Hola, soy WAIS. Â¿QuerÃ©s saber mÃ¡s sobre inteligencia?",
        "respuestas": ["SÃ­, contame"],
        "respuesta_usuario": "SÃ­, contame"
    },
    {
        "pregunta": "Sirvo para evaluar la inteligencia general en personas mayores de 16 aÃ±os.",
        "respuestas": ["Â¿Y cÃ³mo lo hacÃ©s?"],
        "respuesta_usuario": "Â¿Y cÃ³mo lo hacÃ©s?"
    },
    {
        "pregunta": "Mis escalas incluyen: ComprensiÃ³n Verbal, Razonamiento Perceptual, Memoria de Trabajo y Velocidad de Procesamiento.",
        "respuestas": ["Â¿Y cÃ³mo se aplica?"],
        "respuesta_usuario": "Â¿Y cÃ³mo se aplica?"
    },
    {
        "pregunta": "Se aplica en sesiones individuales de 60 a 90 minutos. Â¡Gracias por hablar conmigo!",
        "respuestas": [],
        "respuesta_usuario": ""
    }
]

# Estado inicial
if "pantalla" not in st.session_state:
    st.session_state.pantalla = "menu"
if "paso_wais" not in st.session_state:
    st.session_state.paso_wais = 0

# MenÃº inicial
if st.session_state.pantalla == "menu":
    st.markdown("<h2 style='text-align:center;'>Simulador de conversaciÃ³n</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>SeleccionÃ¡ con quÃ© prueba querÃ©s chatear:</p>", unsafe_allow_html=True)
    if st.button("Chat con WAIS"):
        st.session_state.pantalla = "wais"

# Chat WAIS
if st.session_state.pantalla == "wais":
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    # Encabezado
    st.markdown('''
    <div class="chat-header">
        <img src="https://cdn-icons-png.flaticon.com/512/4333/4333609.png">
        <div>
            <b>WAIS</b><br><small>en lÃ­nea</small>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    paso = st.session_state.paso_wais

    # Mostrar mensajes anteriores
    for i in range(paso + 1):
        mensaje = wais_conversacion[i]
        st.markdown(f'<div class="bubble-assistant">{mensaje["pregunta"]}</div>', unsafe_allow_html=True)
        if i < paso:
            st.markdown(f'<div class="bubble-user">{mensaje["respuesta_usuario"]}</div>', unsafe_allow_html=True)

    # Mostrar opciones actuales
    if paso < len(wais_conversacion):
        opciones = wais_conversacion[paso]["respuestas"]
        if opciones:
            for opcion in opciones:
                if st.button(opcion):
                    st.session_state.paso_wais += 1
                    st.experimental_rerun()
        else:
            if st.button("Volver al menÃº"):
                st.session_state.pantalla = "menu"
                st.session_state.paso_wais = 0

    st.markdown('</div>', unsafe_allow_html=True)
