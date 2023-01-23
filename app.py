import streamlit as st
from streamlit_option_menu import option_menu

import numpy as np
from PIL import Image
import base64

with st.sidebar:
    page = option_menu(None, ["Notizie generali", "Calcola"], 
                           icons=["bi bi-info-circle","bi-calculator"],default_index=0, orientation="vertical",menu_icon="cast")
    

if page ==  "Notizie generali":  
    left, right = st.columns([2,1])

    with left:
        st.title('IL TEOREMA DI PITAGORA')
        """Il teorema di Pitagora è un teorema della geometria euclidea che stabilisce una relazione fondamentale tra i lati di un triangolo rettangolo."""
        """Quello che modernamente conosciamo come teorema di Pitagora viene solitamente attribuito al filosofo e matematico Pitagora. In realtà il suo enunciato (ma non la sua dimostrazione) era già noto ai Babilonesi. Viene a volte affermato che il teorema di Pitagora fosse noto agli antichi Egizi: Carl Boyer esclude questa ipotesi, basandosi sull'assenza del teorema dai papiri matematici rinvenuti. Era conosciuto anche in Cina e sicuramente in India, come dimostrano molte scritture fra cui lo Yuktibhāṣā e gli Śulbasūtra. Non sono note dimostrazioni del teorema considerate tutt'oggi valide e antecedenti o coeve a Pitagora."""
        st.subheader("Enunciato")
        """In ogni triangolo rettangolo l'area del quadrato costruito sull'ipotenusa è uguale alla somma delle aree dei quadrati costruiti sui cateti."""

        st.latex(r'''
        ipotenusa^2 = a^2 + b^2
        ''')

        st.latex(r'''
        ipotenusa = \sqrt{a^2 + b^2}
        ''')

    with right:
        image = Image.open('Pythagoras.jpg')
        st.image(image, caption='Samo, tra il 580 a.C. e il 570 a.C. – Metaponto, 495 a.C. circa')
        st.image("Pythagoras-2a.gif", caption='Animazione di una dimostrazione')
      
elif page == "Calcola":
    st.image("8e8465a55cde531b2c2a038b1e16c090.jpg")
    
    with st.sidebar: 
        
        selected =st.radio("", ("Calcola l'ipotenusa","Calcola il cateto"), index=1)
    
    if selected == "Calcola l'ipotenusa":
        cateto_1 = st.number_input("Inserisci il valore del primo cateto", min_value=0.0, max_value=None, value=0.0,label_visibility="visible")
        cateto_2 = st.number_input("Inserisci il valore del secondo cateto", min_value=0.0, max_value=None, value=0.0,label_visibility="visible")

        ipotenusa = np.sqrt(cateto_1**2 + cateto_2**2).round(2)

        st.text(f"L'ipotenusa é uguale a {ipotenusa}")

    else: 
        cateto_1 = st.number_input("Inserisci il valore di un cateto", min_value=0.0, max_value=None, value=0.0,label_visibility="visible")
        ipotenusa = st.number_input("Inserisci il valore dell' ipotenusa", min_value=0.0, max_value=None, value=0.0,label_visibility="visible")

        cateto_2 = np.sqrt(ipotenusa**2 - cateto_1**2).round(2)

        if cateto_1 > ipotenusa:
            st.error("Per definizione il cateto non puó essere maggiore dell' ipotenusa!", icon="⛔")
            st.stop()

        st.text(f"Il cateto é uguale a {cateto_2}")
    




