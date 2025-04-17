import streamlit as st

st.set_page_config(page_title="Chat WAIS", layout="wide")

# CSS
css = '''
<style>
.stApp {
    background-image: url('https://i.ibb.co/sQBgQXf/pastel-wa-bg.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    font-family: 'Segoe UI', sans-serif;
}
.chat-container {
    background-color: rgba(255, 255, 255, 0.9);
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
    background-color: #dcf8c6;
    color: black;
    padding: 10px 14px;
    border-radius: 10px 0 10px 10px;
    margin: 8px 0;
    width: fit-content;
    max-width: 80%;
    margin-left: auto;
}
.chat-footer {
    display: flex;
    align-items: center;
    background-color: white;
    padding: 10px;
    border-radius: 0 0 10px 10px;
    margin-top: 10px;
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
'''
st.markdown(css, unsafe_allow_html=True)

# Contenedor
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Cabecera
st.markdown('''
<div class="chat-header">
    <img src="https://cdn-icons-png.flaticon.com/512/4333/4333609.png">
    <div>
        <b>WAIS</b><br><small>en lÃ­nea</small>
    </div>
</div>
''', unsafe_allow_html=True)

# Mensajes
mensajes = [
    ("assistant", "Hola, soy WAIS. Â¿QuerÃ©s saber mÃ¡s sobre inteligencia?"),
    ("user", "SÃ­, contame"),
    ("assistant", "Sirvo para evaluar la inteligencia general en personas mayores de 16 aÃ±os."),
    ("user", "Â¿Y cÃ³mo lo hacÃ©s?"),
    ("assistant", "Mis escalas incluyen:<br>- ComprensiÃ³n Verbal<br>- Razonamiento Perceptual<br>- Memoria de Trabajo<br>- Velocidad de Procesamiento"),
    ("user", "Â¿Y cÃ³mo se aplica?"),
    ("assistant", "Se aplica en sesiones individuales de 60 a 90 minutos. Â¡Gracias por hablar conmigo!")
]

for rol, texto in mensajes:
    clase = "bubble-assistant" if rol == "assistant" else "bubble-user"
    st.markdown(f'<div class="{clase}">{texto}</div>', unsafe_allow_html=True)

# Footer
st.markdown('''
<div class="chat-footer">
    <span class="icon">&#128206;</span>
    <span class="icon">&#128247;</span>
    <input type="text" placeholder="EscribÃ­ un mensaje">
    <span class="icon">&#127908;</span>
</div>
''', unsafe_allow_html=True)

# Fin contenedor
st.markdown('</div>', unsafe_allow_html=True)
