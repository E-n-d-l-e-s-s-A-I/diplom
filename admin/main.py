import streamlit as st
from routers.term.router import term_tab_page


def main_page():
    term_tab, extract_tabs = st.tabs(
        [
            "Медицинские термины",
            "Извлечение терминов",
        ]
    )
    term_tab_page(term_tab)



main_page()