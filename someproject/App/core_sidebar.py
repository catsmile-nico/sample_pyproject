import streamlit as st

def display():
    with st.sidebar:
        st.session_state["sidebar_input_id"] = st.text_input("Input ID")