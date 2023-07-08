import streamlit as st

from someproject import Modules

def display():
    st.session_state["body_title"] = st.title("hi")

    if st.session_state["sidebar_input_id"]:
        st.write(Modules.check_int(st.session_state["sidebar_input_id"]))