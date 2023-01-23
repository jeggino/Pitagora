import streamlit as st
import numpy as np


st.title('Il teorema di Pitagora')

st.subheader("Il teorema di Pitagora è un teorema della geometria euclidea che stabilisce una relazione fondamentale tra i lati di un triangolo rettangolo.")

st.latex(r'''
    ipotenusa = \sqrt{a^2 + b^2}
    ''')

cateto_1 = st.number_input("Inserisci il valore del primo cateto", min_value=None, max_value=None, value=0,label_visibility="visible")
cateto_2 = st.number_input("Inserisci il valore del secondo cateto", min_value=None, max_value=None, value=0,label_visibility="visible")

ipotenusa = np.sqrt(cateto_1**2 + cateto_2**2)



st.text(f"L'ipotenusa é {ipotenusa}")
