import streamlit as st

def init_state():
    if "deck" not in st.session_state:
        st.session_state.deck = {}

    if "selected_card" not in st.session_state:
        st.session_state.selected_card = None