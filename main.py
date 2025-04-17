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
    {"pregunta": "Hola, soy WAIS-IV. ¿Querés saber más sobre inteligencia?", "respuestas": ["Sí, contame"], "respuesta_usuario": "Sí, contame"},
    {"pregunta": "Mi nombre completo es: Escala de Inteligencia para Adultos de Wechsler, Cuarta Edición.", "respuestas": ["¿Qué es lo que mides?"], "respuesta_usuario": "¿Qué es lo que mides?"},
    {"pregunta": "Mido la inteligencia general (CI) en adultos.", "respuestas": ["¿Y para qué se usa?"], "respuesta_usuario": "¿Y para qué se usa?"},
    {"pregunta": "Me usan para:\n- Diagnóstico de discapacidad intelectual o superdotación\n- Evaluación de deterioro cognitivo (como demencia)\n- Apoyo clínico, neuropsicológico y forense", "respuestas": ["¿Cuáles son tus escalas?"], "respuesta_usuario": "¿Cuáles son tus escalas?"},
    {"pregunta": "1. Comprensión Verbal (ICV):\n• Semejanzas\n• Vocabulario\n• Información\n• (Complementaria: Comprensión)", "respuestas": ["¿Y las otras?"], "respuesta_usuario": "¿Y las otras?"},
    {"pregunta": "2. Razonamiento Perceptivo (IRP):\n• Diseño con cubos\n• Matrices\n• Puzzles visuales\n• (Complementarias: Peso de figuras, Figuras incompletas)", "respuestas": ["¿Y la siguiente?"], "respuesta_usuario": "¿Y la siguiente?"},
    {"pregunta": "3. Memoria de Trabajo (IMT):\n• Retención de dígitos\n• Aritmética\n• (Complementaria: Secuencia de letras y números)", "respuestas": ["¿Falta alguna más?"], "respuesta_usuario": "¿Falta alguna más?"},
    {"pregunta": "4. Velocidad de Procesamiento (IVP):\n• Claves\n• Búsqueda de símbolos\n• (Complementaria: Cancelación)", "respuestas": ["¿Algo más importante que deba saber?"], "respuesta_usuario": "¿Algo más importante que deba saber?"},
    {"pregunta": "Sí. También tengo un resultado general: el Cociente Intelectual Total (CIT), que resume tu desempeño global. ¡Gracias por conversar conmigo!", "respuestas": [], "respuesta_usuario": ""}
]

neuropsi_conversacion = [
    {"pregunta": "Hola, soy NEUROPSI. ¿Querés saber cómo funciona tu atención y memoria?", "respuestas": ["Sí, contame"], "respuesta_usuario": "Sí, contame"},
    {"pregunta": "Mi nombre completo es: NEUROPSI: Atención y Memoria.", "respuestas": ["¿Qué es lo que medís?"], "respuesta_usuario": "¿Qué es lo que medís?"},
    {"pregunta": "Mido el funcionamiento cognitivo general: atención, memoria y funciones ejecutivas.", "respuestas": ["¿Y para qué se usa?"], "respuesta_usuario": "¿Y para qué se usa?"},
    {"pregunta": "Se usa para:\n- Detectar deterioro cognitivo\n- Evaluación neuropsicológica breve\n- Apoyo diagnóstico en trastornos neurológicos y psiquiátricos", "respuestas": ["¿Cuáles son tus áreas?"], "respuesta_usuario": "¿Cuáles son tus áreas?"},
    {"pregunta": "1. Orientación:\n• Personal\n• Temporal\n• Espacial", "respuestas": ["¿Y las otras áreas?"], "respuesta_usuario": "¿Y las otras áreas?"},
    {"pregunta": "2. Atención y concentración:\n• Atención selectiva\n• Atención sostenida\n• Atención alternante\n• Cálculo mental", "respuestas": ["¿Y la memoria?"], "respuesta_usuario": "¿Y la memoria?"},
    {"pregunta": "3. Memoria:\n• Codificación\n• Evocación libre\n• Evocación diferida\n• Reconocimiento", "respuestas": ["¿Te queda alguna más?"], "respuesta_usuario": "¿Te queda alguna más?"},
    {"pregunta": "4. Funciones ejecutivas:\n• Fluidez verbal (fonológica y semántica)\n• Inhibición\n• Planeación (Torre de Hanoi)\n• Flexibilidad cognitiva", "respuestas": ["Gracias, NEUROPSI"], "respuesta_usuario": "Gracias, NEUROPSI"},
    {"pregunta": "¡Con gusto! Estoy lista para ayudarte a explorar tu mente.", "respuestas": [], "respuesta_usuario": ""}
]

mmpi_conversacion = [
    {"pregunta": "Hola, soy el MMPI-2-RF. ¿Querés descubrir más sobre tu personalidad y salud mental?", "respuestas": ["Sí, contame"], "respuesta_usuario": "Sí, contame"},
    {"pregunta": "Mi nombre completo es: Inventario Multifásico de Personalidad de Minnesota 2 – Forma Reestructurada.", "respuestas": ["¿Qué mides?"], "respuesta_usuario": "¿Qué mides?"},
    {"pregunta": "Mido rasgos clínicos, personalidad, psicopatología y estilo de respuesta.", "respuestas": ["¿Para qué se usa?"], "respuesta_usuario": "¿Para qué se usa?"},
    {"pregunta": "Se utiliza en:\n- Evaluaciones clínicas y forenses\n- Diagnóstico de trastornos psicológicos\n- Selección y orientación laboral", "respuestas": ["¿Qué escalas tenés?"], "respuesta_usuario": "¿Qué escalas tenés?"},
    {"pregunta": "A. Validez (9):\n• VRIN-r, TRIN-r, F-r, Fp-r, Fs, FBS-r, L-r, K-r, RBS", "respuestas": ["¿Y las clínicas?"], "respuesta_usuario": "¿Y las clínicas?"},
    {"pregunta": "B. Problemas emocionales/internos (9):\n• EID, RCd, RC1, RC2, RC4, RC6, RC7, RC8, RC9", "respuestas": ["¿Y las conductuales?"], "respuesta_usuario": "¿Y las conductuales?"},
    {"pregunta": "C. Problemas conductuales/externalizantes:\n• AGG-r, ACT-r, SUB-r, DISC-r", "respuestas": ["¿Y las interpersonales?"], "respuesta_usuario": "¿Y las interpersonales?"},
    {"pregunta": "D. Escalas interpersonales y de personalidad:\n• SHY-r, DSF-r, NFC-r, AXY-r, JCP-r, AGGR-r, MEC-r, SAV-r, TRT-r", "respuestas": ["Gracias MMPI"], "respuesta_usuario": "Gracias MMPI"},
    {"pregunta": "¡Gracias a vos! Estoy listo para ayudarte a comprenderte mejor.", "respuestas": [], "respuesta_usuario": ""}
]

pai_conversacion = [
    {"pregunta": "¡Hola! Soy el Inventario de Evaluación de la Personalidad, PAI. ¿Querés saber cómo evalúo los trastornos y tu forma de afrontarlos?", "respuestas": ["Sí, contame"], "respuesta_usuario": "Sí, contame"},
    {"pregunta": "Mi nombre completo es: Personality Assessment Inventory.", "respuestas": ["¿Qué mides?"], "respuesta_usuario": "¿Qué mides?"},
    {"pregunta": "Mido trastornos de personalidad, psicopatología y estilo de afrontamiento.", "respuestas": ["¿Para qué se usa?"], "respuesta_usuario": "¿Para qué se usa?"},
    {"pregunta": "Me usan para:\n- Diagnóstico clínico\n- Planificación de tratamiento\n- Evaluaciones judiciales, penitenciarias y laborales", "respuestas": ["¿Cuáles son tus escalas?"], "respuesta_usuario": "¿Cuáles son tus escalas?"},
    {"pregunta": "A. Validez (4):\n• Inconsistencia (ICN)\n• Infrecuencia (INF)\n• Impresión negativa (NIM)\n• Impresión positiva (PIM)", "respuestas": ["¿Y las clínicas?"], "respuesta_usuario": "¿Y las clínicas?"},
    {"pregunta": "B. Clínicas (11):\n• SOM, ANX, ARD, DEP, MAN, PAR, SCZ, BOR, ANT, ALC, DRG", "respuestas": ["¿Y las de tratamiento?"], "respuesta_usuario": "¿Y las de tratamiento?"},
    {"pregunta": "C. Escalas de tratamiento (5):\n• AGG, SUI, STR, RXR, NON", "respuestas": ["¿Te queda alguna más?"], "respuesta_usuario": "¿Te queda alguna más?"},
    {"pregunta": "D. Interpersonales (2):\n• Dominancia (DOM)\n• Calidez (WRM)", "respuestas": ["Gracias PAI"], "respuesta_usuario": "Gracias PAI"},
    {"pregunta": "¡A vos! Estoy lista para ayudarte a comprenderte mejor.", "respuestas": [], "respuesta_usuario": ""}
]

neo_conversacion = [
    {"pregunta": "¡Hola! Soy el Inventario de Personalidad NEO Revisado. ¿Querés conocer tus rasgos más profundos?", "respuestas": ["Sí, contame"], "respuesta_usuario": "Sí, contame"},
    {"pregunta": "Mi nombre completo es: Inventario de Personalidad NEO Revisado (NEO PI-R).", "respuestas": ["¿Qué mides?"], "respuesta_usuario": "¿Qué mides?"},
    {"pregunta": "Mido los cinco grandes factores de personalidad y sus facetas.", "respuestas": ["¿Para qué se usa?"], "respuesta_usuario": "¿Para qué se usa?"},
    {"pregunta": "Se utiliza para:\n- Evaluación de personalidad en adultos\n- Contextos clínicos, laborales, vocacionales y de investigación", "respuestas": ["¿Cuáles son esos cinco factores?"], "respuesta_usuario": "¿Cuáles son esos cinco factores?"},
    {"pregunta": "1. Neuroticismo (N):\n• Ansiedad\n• Ira-hostilidad\n• Depresión\n• Autoconsciencia\n• Impulsividad\n• Vulnerabilidad", "respuestas": ["¿Y el segundo?"], "respuesta_usuario": "¿Y el segundo?"},
    {"pregunta": "2. Extraversión (E):\n• Cordialidad\n• Gregarismo\n• Asertividad\n• Nivel de actividad\n• Búsqueda de emociones\n• Emociones positivas", "respuestas": ["¿Y el tercero?"], "respuesta_usuario": "¿Y el tercero?"},
    {"pregunta": "3. Apertura a la experiencia (O):\n• Fantasía\n• Estética\n• Sentimientos\n• Actividades\n• Ideas\n• Valores", "respuestas": ["¿Y el cuarto?"], "respuesta_usuario": "¿Y el cuarto?"},
    {"pregunta": "4. Amabilidad (A):\n• Confianza\n• Franqueza\n• Altruismo\n• Conciliación\n• Modestia\n• Sensibilidad", "respuestas": ["¿Y el último factor?"], "respuesta_usuario": "¿Y el último factor?"},
    {"pregunta": "5. Responsabilidad (C):\n• Competencia\n• Orden\n• Sentido del deber\n• Búsqueda de logros\n• Autodisciplina\n• Deliberación", "respuestas": ["Gracias NEO"], "respuesta_usuario": "Gracias NEO"},
    {"pregunta": "¡Un placer! Estoy acá para ayudarte a conocerte mejor.", "respuestas": [], "respuesta_usuario": ""}
]

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
        st.markdown(f'<div class="bubble-assistant">{mensaje["pregunta"]}</div>', unsafe_allow_html=True)
        if i < paso:
            st.markdown(f'<div class="bubble-user">{mensaje["respuesta_usuario"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if paso < len(conversacion):
        opciones = conversacion[paso]["respuestas"]
        if opciones:
            st.markdown('<div class="response-buttons">', unsafe_allow_html=True)
            for opcion in opciones:
                if st.button(opcion, key=f"{nombre}_{paso}"):
                    st.session_state[paso_key] += 1
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

# Mostrar chats
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
