import streamlit as st
import numpy as np

cateto_1 = st.number_input("Inserisci il valore del primo cateto", min_value=None, max_value=None, value=0,label_visibility="visible")
cateto_2 = st.number_input("Inserisci il valore del secondo cateto", min_value=None, max_value=None, value=0,label_visibility="visible")

ipotenusa = np.sqrt(cateto_1**2 + cateto_2**2)

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.text(f"L'ipotenusa é {ipotenusa}")
