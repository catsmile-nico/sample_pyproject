import streamlit as st
from . import core_sidebar, core_body

class project:
    def __init__(self) -> None:
        self.run()

    def run(self):
        core_sidebar.display()
        core_body.display()

        