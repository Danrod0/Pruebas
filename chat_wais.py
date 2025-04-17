# archivo: chat_wais.py

import streamlit as st

st.set_page_config(page_title="Chat con WAIS", layout="centered")

# Título
st.title("Chat Interactivo con WAIS")
st.write("¡Bienvenido/a! Estás a punto de conversar con la prueba psicológica WAIS.")

# Inicialización de sesión
if "step" not in st.session_state:
    st.session_state.step = 0

# Flujo conversacional
if st.session_state.step == 0:
    st.markdown("**WAIS:** ¡Hola! Soy la Escala Wechsler de Inteligencia para Adultos. ¿Te interesa saber para qué sirvo?")
    if st.button("Sí, ¿para qué servís?"):
        st.session_state.step = 1
    elif st.button("No, solo pasaba"):
        st.session_state.step = 99

elif st.session_state.step == 1:
    st.markdown("**WAIS:** Evalúo la inteligencia general de personas mayores de 16 años.")
    if st.button("¿Qué escalas tenés?"):
        st.session_state.step = 2
    elif st.button("¿Cuánto dura?"):
        st.session_state.step = 3

elif st.session_state.step == 2:
    st.markdown("""
    **WAIS:** Mis escalas principales son:
    - Comprensión Verbal  
    - Razonamiento Perceptual  
    - Memoria de Trabajo  
    - Velocidad de Procesamiento
    """)
    if st.button("¿Cómo se aplica?"):
        st.session_state.step = 4

elif st.session_state.step == 3:
    st.markdown("**WAIS:** Aproximadamente 60 a 90 minutos. ¡Pero pasa volando!")
    if st.button("¿Qué escalas usás?"):
        st.session_state.step = 2

elif st.session_state.step == 4:
    st.markdown("**WAIS:** Se aplica en una sesión individual, con tareas prácticas y verbales.")
    st.success("¡Gracias por conversar conmigo!")

elif st.session_state.step == 99:
    st.warning("WAIS: Bueno... si cambiás de idea, aquí estaré.")

