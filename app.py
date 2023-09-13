import requests
import streamlit as st
from  streamlit_lottie import  st_lottie
from streamlit_option_menu import option_menu
from  PIL import  Image as Pillow

email_address= "rfullivarri22@gmail.com"
url= "https://lottie.host/67d569c8-c019-491a-856f-fec548202ca7/PbNLOBxPif.json"

#Animaciones
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie= load_lottieurl(url)

#Set up web
st.set_page_config(page_title="DOMOTICA",
                    page_icon="🏠",
                    layout="wide")


#CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/main.css")



#Menu
def on_change(key):
    selection = st.session_state[key]
    selected_url = menu_links.get(selection)
    if selected_url:
        #st.(selected_url)
        st.markdown(f"Redirigiendo a {selection}...")
        #st.markdown(f'<meta http-equiv="refresh" content="0;URL={selected_url}">')
        #st.markdown(f'<script>window.location.href = "{selected_url}";</script>', unsafe_allow_html=True)
        st.write(selected_url,unsafe_allow_html=True)

menu_links = {
    "Home": "http://localhost:8501/?section=About+Us#smart-homer-smart-life",
    "Valores": "http://localhost:8501/#nuestros-valores",
    "Products": "http://localhost:8501/?section=Valores#nuestros-productos",
    "About Us": "http://localhost:8501/#sobre-nosotros",
    "Contact Us": "http://localhost:8501/#ponte-en-contacto-con-nosotros"
}

selected5 = option_menu(None, ["Home", "Valores", "Products", 'About Us', 'Contact Us'],
                        icons=['house', 'cloud-upload', "list-task", 'gear', 'phone'],
                        on_change=on_change, key='menu_5', orientation="horizontal")




#Intro
with st.container():
     #st.header("Smart Homer, Smart Life 🦾")
     st.markdown(f"<h1 style='text-align: left; font-size: 80px;'>Smart Homer, Smart Life 🦾</h1>",
                 unsafe_allow_html=True)
     st.title("Te ayudamos a automatizar tu casa")
     st.write("Con mas de 10 años en el mercado de domotica traemos los mejores productos para hacer tu vida mas smart")
     st.write("[Saber Mas >]")

#Valores
with st.container():
    st.write("---")
    st.header("Nuestros Valores 💎")
    st.write("##")
    valor1, valor2, valor3 = st.columns((3))
    with valor1:
        st.subheader("INNOVACION👩‍💻")
        st.write("""
                ME GUSTA EL ARTE1
                 """)
    with valor2:
        st.subheader("TRANSPARENCIA✨")
        st.write("""
                ME GUSTA EL ARTE2
                 """)
    with valor3:
        st.subheader("ACOMPAÑAMIENTO🫀")
        st.write("""
                ME GUSTA EL ARTE3
                 """)


#Productos
##ALEXA
with st.container():
    st.write("---")
    st.header("Nuestros Productos 🛠")
    st.write("##")
    image_column, text_column = st.columns((1,2))

    with image_column:
        image1_path = r"imagen/alexa.png"
        image = Pillow.open(image1_path)
        st.image(image, use_column_width=True, caption="Alexa Home Assitant")
    with text_column:
        st.subheader("Home Assistant 🗿")
        st.write(""" 
         El Home Assistant es el cerebro de tu hogar inteligente. 
         Es una plataforma de código abierto que te permite controlar y automatizar todos los dispositivos conectados en tu casa
          desde un solo lugar. Con Home Assistant, puedes crear escenas personalizadas, programar rutinas y tener un control total 
         sobre la iluminación, la temperatura, la seguridad y mucho más.
         """)
        st.write("[Ver servicios >]")

##NFC TAG
with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
    with image_column:
        image1_path = r"imagen/NFC.png"
        image = Pillow.open(image1_path)
        st.image(image, use_column_width=True, caption="NFC Tag")
    with text_column:
        st.subheader("NFC Tags 🧿")
        st.write(""" 
                  Los NFC Tags son pequeños adhesivos que contienen chips NFC (Near Field Communication). 
                  Estos tags permiten la comunicación inalámbrica entre dispositivos cuando se acercan a ellos. 
                  Son herramientas versátiles para automatizar tareas y mejorar la experiencia del usuario en tu hogar inteligente.
                  """)
        st.write("[Ver servicios >]")


##SMART LIGHT
with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
    with image_column:
        image1_path = r"imagen/smartlight.jpeg"
        image = Pillow.open(image1_path)
        st.image(image, use_column_width=True, caption="Smart Lights")
    with text_column:
        st.subheader("Smarts Lights 💡")
        st.write(""" 
                 Las Smart Lights son bombillas LED inteligentes que te permiten ajustar el brillo,
                 el color y la programación de la iluminación en tu hogar. 
                 Estas bombillas son compatibles con asistentes de voz y aplicaciones móviles, 
                 lo que te da un control completo sobre la iluminación de tu hogar
                 """)
        st.write("[Ver servicios >]")
        
        
        


#About Us
with st.container():
    st.write("---")
    text_colum, image_colum = st.columns(2)
    with text_colum:
        st.header("Sobre Nosotros 🔍")
        st.write(""" 
                En [Nombre de la Startup], nuestra pasión es convertir casas en hogares inteligentes. 
                 Desde nuestro inicio en 2013, hemos estado liderando el camino en la industria de la domótica, 
                 brindando soluciones innovadoras y asesoramiento experto a nuestros clientes.
                """)
        st.write("[Saber Mas >]")
    with image_colum:
        st_lottie(lottie,height= 400)

        # image_path = r"imagen/smartcity.png"
        # image = Pillow.open(image_path)
        # st.image(image, use_column_width=True, caption="Imagen Smart City")

# contacto
with st.container():
    st.write("---")
    
    contact_form = f"""
    <form action="https://formsubmit.co/{email_address}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Tu nombre" required>
        <input type="email" name="email" placeholder="Tu email" required>
        <textarea name="message" placeholder="Tu mensaje aquí" required></textarea>
        <button type="submit">Enviar</button>
    </form>
    """
    left_column, center_column , right_column = st.columns((1,2,1))
    with center_column:
        st.header("Ponte en contacto con nosotros!")
        st.write("##")
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    with left_column:
        st.empty()

