import streamlit as st


class Page():
    def __init__(self, page_id, title):
        self.page_id = page_id
        self.title = title

    def header(self,):
        st.title(self.title)

    def body(self):
        pass

    def footer(self):
        pass

    def render(self):
        self.header()
        self.body()
        self.footer()









