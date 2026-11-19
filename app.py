import streamlit as st
from password_utils import generate_password
from storage import load_passwords, add_passwords

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

st.divider()
st.subheader("Guardar Password")

with st.form("save_form"):
    site = st.text_input("Sitio o servicio")
    username = st.text_input("Usuario (opcional)")
    password_to_save = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Guardar")
    if submitted and site and password_to_save:
        add_passwords(site, username, password_to_save)
        st.success(f"Password de {site} guardada.")
        st.rerun()

st.divider()
st.subheader("Password guardadas")
passwords = load_passwords()
if passwords:
    for p in passwords:
        with st.expander(f"{p['site']} — {p['username'] or '(sin usuario)'}"):
            st.write(f"**Password:** {p['password']}")
else:
    st.info("Aun no hay passwords guardadas")