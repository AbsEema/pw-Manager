import streamlit as st
from password_utils import generate_password

st.set_page_config(page_title="Password Manager", page_icon="🔐", layout="centered")
st.title("🔐 Password Manager")

st.subheader("Generar Password")

col1, col2 = st.columns(2)
with col1:
    length = st.slider("Longitud", min_value=8, max_value=32, value=16)
with col2:
    st.write("") #Espacio

use_upper = st.checkbox("Mayusculas (A-Z)", value=True)
use_lower = st.checkbox("Minusculas (a-z)", value=True)
use_digits = st.checkbox("Numeros (0-9)", value=True)
use_symbols = st.checkbox("Simbolos(!@#$...)", value=True)

if st.button("Generar Password", type="primary"):
    pwd = generate_password(length, use_upper,use_lower,use_digits,use_symbols)

    if pwd:
        st.success("Password Generada:")
        st.code(pwd, language=None)
    else:
        st.error("Selecciona al menur un tipo de caracter.")