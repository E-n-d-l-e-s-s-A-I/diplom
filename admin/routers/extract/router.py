import streamlit as st
from routers.core_api import med_base_api, model_api
import logging

def split_terms(terms: list[str]) -> tuple[str, str]:
    all_terms = [term.name.lower() for term in med_base_api.term.get_terms()]
    existing_terms = [term for term in terms  if term in all_terms]
    not_existing_terms = [term for term in terms  if term not in all_terms]
    return existing_terms, not_existing_terms
    
terms_to_add = []  
ex_terms = []  

def extract_tab_page(term_tab):
    """Логика вкладки медицинских терминов."""
    
    with term_tab:
        global terms_to_add
        global ex_terms


        terms = med_base_api.term.get_terms()
        
        input_text = st.text_area("Текст для извлечения терминов", key="input_text",)
        
        if input_text:
            extract_clicked = st.button("Извлечь", key="extract_btn")
        else:
            extract_clicked = st.button("Извлечь", key="extract_btn", disabled=True)
        
        if extract_clicked:
            terms_to_add = []
            ex_terms = []
            placeholder = st.empty()
            with placeholder:
                st.subheader("Идет извлечение...")
    
            terms = model_api.extract.extract_terms(input_text)
            # terms= ["кашель", "ломота в суставах", "одышка"]
            existing_terms, not_existing_terms = split_terms(terms)
            placeholder.empty()
            terms_to_add = not_existing_terms
            ex_terms = existing_terms

        if ex_terms:
            st.subheader("Термины, которые есть в базе знаний")
            st.text_area(label="", key="existing_terms", value="\n".join(ex_terms))
            
        if terms_to_add:
            st.subheader("Термины, которые можно добавить в базу знаний")
            st.text_area(label="", key="not_existing_terms", value="\n".join(terms_to_add))
            
         
