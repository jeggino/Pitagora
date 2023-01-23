import streamlit as st
# import math

cateto_1 = st.number_input("Inserisci il valore del primo cateto", min_value=None, max_value=None, value=0,label_visibility="visible")
cateto_2 = st.number_input("Inserisci il valore del secondo cateto", min_value=None, max_value=None, value=0,label_visibility="visible")

# ipotenusa = math.sqrt((cateto_1**2) + (cateto_2**2))

# st.header(f"L'ipotenusa é uguale a {ipotenusa}")
