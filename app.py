import streamlit as st
import numpy as np
from PIL import Image
import base64

left, right = st.columns([2,1])

with left:
    st.title('IL TEOREMA DI PITAGORA')
    st.caption("Il teorema di Pitagora è un teorema della geometria euclidea che stabilisce una relazione fondamentale tra i lati di un triangolo rettangolo.")
    st.caption("Quello che modernamente conosciamo come teorema di Pitagora viene solitamente attribuito al filosofo e matematico Pitagora. In realtà il suo enunciato (ma non la sua dimostrazione) era già noto ai Babilonesi. Viene a volte affermato che il teorema di Pitagora fosse noto agli antichi Egizi: Carl Boyer esclude questa ipotesi, basandosi sull'assenza del teorema dai papiri matematici rinvenuti. Era conosciuto anche in Cina e sicuramente in India, come dimostrano molte scritture fra cui lo Yuktibhāṣā e gli Śulbasūtra. Non sono note dimostrazioni del teorema considerate tutt'oggi valide e antecedenti o coeve a Pitagora.")
    st.subheader("Enunciato")
    st.caption("In ogni triangolo rettangolo l'area del quadrato costruito sull'ipotenusa è uguale alla somma delle aree dei quadrati costruiti sui cateti.")
        
    st.latex(r'''
    ipotenusa^2 = a^2 + b^2
    ''')
    
    st.latex(r'''
    ipotenusa = \sqrt{a^2 + b^2}
    ''')
    
with right:
    image = Image.open('Pythagoras.jpg')
    st.image(image, caption='Samo, tra il 580 a.C. e il 570 a.C. – Metaponto, 495 a.C. circa')
    
    file_ = open("Pythagoras-2a.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    
    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True,
    )
    
    
"---"


cateto_1 = st.number_input("Inserisci il valore del primo cateto", min_value=None, max_value=None, value=0,label_visibility="visible")
cateto_2 = st.number_input("Inserisci il valore del secondo cateto", min_value=None, max_value=None, value=0,label_visibility="visible")

ipotenusa = np.sqrt(cateto_1**2 + cateto_2**2).round(2)



st.text(f"L'ipotenusa é uguale a {ipotenusa}")
