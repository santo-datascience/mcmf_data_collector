import streamlit as st

from .common import footer, header

    

def render():
    header.draw()
    st.write("Enter the following information:")
    st.text_input("Name:")

    footer.draw()