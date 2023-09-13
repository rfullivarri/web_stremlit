import requests
import streamlit as st
from  streamlit_lottie import  st_lottie
from streamlit_option_menu import option_menu
from  PIL import  Image as Pillow

#Set up web
st.set_page_config(page_title="DOMOTICA",
                    page_icon="🏠",
                    layout="wide")

email_address= "rfullivarri22@gmail.com"
url= "https://lottie.host/67d569c8-c019-491a-856f-fec548202ca7/PbNLOBxPif.json"

#Animaciones
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie= load_lottieurl(url)



#CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/main2.css")

#Menu
def on_change(key):
    selection = st.session_state[key]

    return str(selection)

selected5 = option_menu(None, ["Home", "Values", "Products", 'About Us', 'Contact Us'],
                        icons=['house', 'cloud-upload', "list-task", 'gear', 'phone'],
                        on_change=on_change, key='menu_5', orientation="horizontal")



#HOME
def Home():
    home= st.container()
    home.title("Smart Homer, Smart Life 🦾")
    home.header("Te ayudamos a automatizar tu casa")
    home.write("Con mas de 10 años en el mercado de domotica traemos los mejores productos para hacer tu vida mas smart")
    home.write("[Saber Mas >]")
    home.write("---")
    image_path = r"imagen/smartcity.png"
    image = Pillow.open(image_path)
    home.image(image, use_column_width=True, caption="Imagen Smart City")
    
    contact=st.container()
    contact.write("---")
    
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

#VALUES
def Values():
    values =st.container()
    values.title("Nuestros Valores 💎")
    values.write("---")
    valor1, valor2, valor3 = st.columns((3))
    with valor1:
        st.header("Innovasion👩‍💻")
        st.write("""ME GUSTA EL ARTE 3""")
    with valor2:
        st.header("Transparencia✨")
        st.write("""ME GUSTA EL ARTE 3""")
    with valor3:
        st.header("Acompañamiento🤲")
        st.write("""ME GUSTA EL ARTE 3""")
    st.write("---")


#PRODUCTS
def Products():

        products= st.container()
        products.title("Nuestros Productos 🛠")
        products.write("---")
    #ALEXA
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
        st.write("---")

    #NFC TAG
        products.container()
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
        st.write("---")


    #SMART LIGHT
        products.container()
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
        st.write("---")



#ABOUT US
def About_Us():
    about = st.container()
    about.write("---")
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
    st.write("---")    


#CONTACT US
def Contact_Us():
    contact=st.container()
    contact.write("---")
    
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


if on_change("menu_5") == "Home":
    Home()
elif on_change("menu_5") == "Values":
    Values()
elif on_change("menu_5") == "Products":
    Products()  
elif on_change("menu_5") == "About Us":
    About_Us() 
elif on_change("menu_5") == "Contact Us":
    Contact_Us()         
else:
    st.empty()


