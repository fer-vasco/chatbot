import streamlit as st

st.title("💬 Prueba!")
st.write(
    "Prueba de input y control"
)

clave = str(123)

text_input = st.text_input("Clave 👇")

if text_input:
    st.write("You entered: ", text_input)
    st.write("You entered: ", str(text_input) == clave)

