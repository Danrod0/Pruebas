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
if "paso_neuropsi" not in st.session_state:
    st.session_state.paso_neuropsi = 0
if "paso_mmpi" not in st.session_state:
    st.session_state.paso_mmpi = 0
if "paso_pai" not in st.session_state:
    st.session_state.paso_pai = 0
if "paso_neo" not in st.session_state:
    st.session_state.paso_neo = 0

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
    "MMPI": {
        "avatar": "https://cdn-icons-png.flaticon.com/512/3135/3135789.png",
        "mensaje": "Hola, soy MMPI-2-R. ¿Te interesa tu perfil psicológico?",
        "hora": "3:10 p.m."
    },
    "PAI": {
        "avatar": "https://cdn-icons-png.flaticon.com/512/1048/1048949.png",
        "mensaje": "Hola, soy PAI. ¿Querés conocer tu ajuste psicológico?",
        "hora": "2:55 p.m."
    },
    "NEO": {
        "avatar": "https://cdn-icons-png.flaticon.com/512/219/219969.png",
        "mensaje": "Hola, soy NEO-PI-R. ¿Querés conocer tus rasgos de personalidad?",
        "hora": "2:30 p.m."
    }
}

# Conversaciones

wais_conversacion = [
    {"pregunta": "Mi nombre completo es: Escala de Inteligencia para Adultos de Wechsler, Cuarta Edición.", "respuestas": ["¿Qué medís?"], "respuesta_usuario": "¿Qué medís?"},
    {"pregunta": "Mido la inteligencia general (CI) en adultos.", "respuestas": ["¿Para qué se usa?"], "respuesta_usuario": "¿Para qué se usa?"},
    {"pregunta": "Se usa para:\n• Diagnóstico de discapacidad intelectual o superdotación\n• Evaluación de deterioro cognitivo (ej. demencia)\n• Apoyo en contextos clínicos, neuropsicológicos y forenses", "respuestas": ["¿Cuáles son tus escalas?"], "respuesta_usuario": "¿Cuáles son tus escalas?"},
    {"pregunta": "Comprensión Verbal (ICV):\n• Semejanzas\n• Vocabulario\n• Información\n• (Complementaria: Comprensión)", "respuestas": ["¿Y las otras escalas?"], "respuesta_usuario": "¿Y las otras escalas?"},
    {"pregunta": "Razonamiento Perceptivo (IRP):\n• Diseño con cubos\n• Matrices\n• Puzzles visuales\n• (Complementarias: Peso de figuras, Figuras incompletas)", "respuestas": ["¿Y la memoria de trabajo?"], "respuesta_usuario": "¿Y la memoria de trabajo?"},
    {"pregunta": "Memoria de Trabajo (IMT):\n• Retención de dígitos\n• Aritmética\n• (Complementaria: Secuencia de letras y números)", "respuestas": ["¿Y la velocidad de procesamiento?"], "respuesta_usuario": "¿Y la velocidad de procesamiento?"},
    {"pregunta": "Velocidad de Procesamiento (IVP):\n• Claves\n• Búsqueda de símbolos\n• (Complementaria: Cancelación)", "respuestas": ["¿Algo más importante?"], "respuesta_usuario": "¿Algo más importante?"},
    {"pregunta": "Sí. También tengo un resultado general: el Cociente Intelectual Total (CIT).", "respuestas": [], "respuesta_usuario": ""}
]

neuropsi_conversacion = [
    {"pregunta": "Mi nombre completo es: NEUROPSI: Atención y Memoria.", "respuestas": ["¿Qué medís?"], "respuesta_usuario": "¿Qué medís?"},
    {"pregunta": "Mido el funcionamiento cognitivo general: atención, memoria y funciones ejecutivas.", "respuestas": ["¿Para qué se usa?"], "respuesta_usuario": "¿Para qué se usa?"},
    {"pregunta": "Se usa para:\n• Detección de deterioro cognitivo\n• Evaluación neuropsicológica breve\n• Apoyo diagnóstico en trastornos neurológicos y psiquiátricos", "respuestas": ["¿Cuáles son tus áreas?"], "respuesta_usuario": "¿Cuáles son tus áreas?"},
    {"pregunta": "Orientación:\n• Personal\n• Temporal\n• Espacial", "respuestas": ["¿Y la atención?"], "respuesta_usuario": "¿Y la atención?"},
    {"pregunta": "Atención y concentración:\n• Selectiva\n• Sostenida\n• Alternante\n• Cálculo mental", "respuestas": ["¿Y la memoria?"], "respuesta_usuario": "¿Y la memoria?"},
    {"pregunta": "Memoria:\n• Codificación\n• Evocación libre\n• Evocación diferida\n• Reconocimiento", "respuestas": ["¿Y las funciones ejecutivas?"], "respuesta_usuario": "¿Y las funciones ejecutivas?"},
    {"pregunta": "Funciones ejecutivas:\n• Fluidez verbal (fonológica y semántica)\n• Inhibición\n• Planeación (Torre de Hanoi)\n• Flexibilidad cognitiva", "respuestas": [], "respuesta_usuario": ""}
]

mmpi_conversacion = [
    {"pregunta": "Mi nombre completo es: Inventario Multifásico de Personalidad de Minnesota 2 – Forma Reestructurada.", "respuestas": ["¿Qué medís?"], "respuesta_usuario": "¿Qué medís?"},
    {"pregunta": "Mido rasgos clínicos, personalidad, psicopatología y estilo de respuesta.", "respuestas": ["¿Para qué se usa?"], "respuesta_usuario": "¿Para qué se usa?"},
    {"pregunta": "Se usa en:\n• Evaluaciones clínicas y forenses\n• Diagnóstico de trastornos psicológicos\n• Selección y orientación laboral", "respuestas": ["¿Cuáles son tus escalas?"], "respuesta_usuario": "¿Cuáles son tus escalas?"},
    {"pregunta": "Validez (9):\n• VRIN-r\n• TRIN-r\n• F-r\n• Fp-r\n• Fs\n• FBS-r\n• L-r\n• K-r\n• RBS", "respuestas": ["¿Y las clínicas?"], "respuesta_usuario": "¿Y las clínicas?"},
    {"pregunta": "Problemas emocionales / internos (9):\n• EID\n• RCd\n• RC1\n• RC2\n• RC4\n• RC6\n• RC7\n• RC8\n• RC9", "respuestas": ["¿Y los problemas conductuales?"], "respuesta_usuario": "¿Y los problemas conductuales?"},
    {"pregunta": "Problemas conductuales / externalizantes:\n• AGG-r\n• ACT-r\n• SUB-r\n• DISC-r", "respuestas": ["¿Y las interpersonales?"], "respuesta_usuario": "¿Y las interpersonales?"},
    {"pregunta": "Escalas interpersonales y de personalidad:\n• SHY-r\n• DSF-r\n• NFC-r\n• AXY-r\n• JCP-r\n• AGGR-r\n• MEC-r\n• SAV-r\n• TRT-r", "respuestas": [], "respuesta_usuario": ""}
]

pai_conversacion = [
    {"pregunta": "Mi nombre completo es: Personality Assessment Inventory (PAI).", "respuestas": ["¿Qué medís?"], "respuesta_usuario": "¿Qué medís?"},
    {"pregunta": "Mido trastornos de personalidad, psicopatología y estilo de afrontamiento.", "respuestas": ["¿Para qué se usa?"], "respuesta_usuario": "¿Para qué se usa?"},
    {"pregunta": "Se usa en:\n• Diagnóstico clínico\n• Planificación de tratamiento\n• Evaluaciones judiciales, penitenciarias y laborales", "respuestas": ["¿Cuáles son tus escalas?"], "respuesta_usuario": "¿Cuáles son tus escalas?"},
    {"pregunta": "Validez (4):\n• ICN\n• INF\n• NIM\n• PIM", "respuestas": ["¿Y las clínicas?"], "respuesta_usuario": "¿Y las clínicas?"},
    {"pregunta": "Clínicas (11):\n• SOM\n• ANX\n• ARD\n• DEP\n• MAN\n• PAR\n• SCZ\n• BOR\n• ANT\n• ALC\n• DRG", "respuestas": ["¿Y las de tratamiento?"], "respuesta_usuario": "¿Y las de tratamiento?"},
    {"pregunta": "Escalas de tratamiento (5):\n• AGG\n• SUI\n• STR\n• RXR\n• NON", "respuestas": ["¿Y las interpersonales?"], "respuesta_usuario": "¿Y las interpersonales?"},
    {"pregunta": "Interpersonales (2):\n• DOM\n• WRM", "respuestas": [], "respuesta_usuario": ""}
]

neo_conversacion = [
    {"pregunta": "Mi nombre completo es: Inventario de Personalidad NEO Revisado (NEO PI-R).", "respuestas": ["¿Qué medís?"], "respuesta_usuario": "¿Qué medís?"},
    {"pregunta": "Mido los cinco grandes factores de personalidad y sus facetas.", "respuestas": ["¿Para qué se usa?"], "respuesta_usuario": "¿Para qué se usa?"},
    {"pregunta": "Se usa en:\n• Evaluación de personalidad en adultos\n• Contextos clínicos, laborales, vocacionales y de investigación", "respuestas": ["¿Cuáles son esos factores?"], "respuesta_usuario": "¿Cuáles son esos factores?"},
    {"pregunta": "Neuroticismo (N):\n• Ansiedad\n• Ira-hostilidad\n• Depresión\n• Autoconsciencia\n• Impulsividad\n• Vulnerabilidad", "respuestas": ["¿Y la extraversión?"], "respuesta_usuario": "¿Y la extraversión?"},
    {"pregunta": "Extraversión (E):\n• Cordialidad\n• Gregarismo\n• Asertividad\n• Nivel de actividad\n• Búsqueda de emociones\n• Emociones positivas", "respuestas": ["¿Y la apertura?"], "respuesta_usuario": "¿Y la apertura?"},
    {"pregunta": "Apertura a la experiencia (O):\n• Fantasía\n• Estética\n• Sentimientos\n• Actividades\n• Ideas\n• Valores", "respuestas": ["¿Y la amabilidad?"], "respuesta_usuario": "¿Y la amabilidad?"},
    {"pregunta": "Amabilidad (A):\n• Confianza\n• Franqueza\n• Altruismo\n• Conciliación\n• Modestia\n• Sensibilidad", "respuestas": ["¿Y la responsabilidad?"], "respuesta_usuario": "¿Y la responsabilidad?"},
    {"pregunta": "Responsabilidad (C):\n• Competencia\n• Orden\n• Sentido del deber\n• Búsqueda de logros\n• Autodisciplina\n• Deliberación", "respuestas": [], "respuesta_usuario": ""}
]


# Mostrar encabezado estético solo en menú
if st.session_state.pantalla == "menu":
    st.markdown('<div class="header">', unsafe_allow_html=True)
    st.markdown('<h1>Chats</h1>', unsafe_allow_html=True)
    st.markdown('<div class="search-bar">🔍 Ask Meta AI or Search</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="chip-row">
        <div class="chip">All</div>
        <div class="chip">Unread 16</div>
        <div class="chip">Favorites</div>
        <div class="chip">Groups 9</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Menú de chats
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

# Función para mostrar cada chat
def mostrar_chat(nombre, conversacion, paso_key):
    st.markdown('<div class="chat-box">', unsafe_allow_html=True)
    header_cols = st.columns([0.85, 0.15])
    with header_cols[0]:
        st.markdown(f'''
        <div class="chat-header">
            <div class="chat-header-left">
                <img src="{pruebas[nombre]['avatar']}">
                <div><b>{nombre}</b><br><small>en línea</small></div>
            </div>
        </div>''', unsafe_allow_html=True)
    with header_cols[1]:
        if st.button("Volver"):
            st.session_state.pantalla = "menu"
            st.session_state[paso_key] = 0
            st.experimental_rerun()

    st.markdown('<div class="chat-body">', unsafe_allow_html=True)
    paso = st.session_state[paso_key]
    for i in range(paso + 1):
        mensaje = conversacion[i]
        texto = mensaje["pregunta"].replace("\\n", "<br>").replace("\n", "<br>")
        st.markdown(f'<div class="bubble-assistant">{texto}</div>', unsafe_allow_html=True)
        if i < paso:
            st.markdown(f'<div class="bubble-user">{mensaje["respuesta_usuario"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if paso < len(conversacion):
        opciones = conversacion[paso]["respuestas"]
        if opciones:
            st.markdown('<div class="response-buttons">', unsafe_allow_html=True)
            for opcion in opciones:
                if st.button(opcion, key=f"{nombre}_{paso}_{opcion}"):
                    st.session_state[paso_key] += 1
                    st.rerun()  # Esta es la nueva forma (más segura que experimental_rerun)
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

# Mostrar los chats según el nombre
if st.session_state.pantalla == "wais":
    mostrar_chat("WAIS", wais_conversacion, "paso_wais")
elif st.session_state.pantalla == "neuropsi":
    mostrar_chat("NEUROPSI", neuropsi_conversacion, "paso_neuropsi")
elif st.session_state.pantalla == "mmpi":
    mostrar_chat("MMPI", mmpi_conversacion, "paso_mmpi")
elif st.session_state.pantalla == "pai":
    mostrar_chat("PAI", pai_conversacion, "paso_pai")
elif st.session_state.pantalla == "neo":
    mostrar_chat("NEO", neo_conversacion, "paso_neo")
