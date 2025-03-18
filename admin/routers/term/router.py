import streamlit as st
from routers.term.schemas import TermBase
from routers.core_api import med_base_api
from routers.utils import error_to_readable_view


def term_tab_page(term_tab):
    """Логика вкладки медицинских терминов."""

    with term_tab:
        terms = med_base_api.term.get_terms()
        term_name_to_id = {term.name: term.id for term in terms}
        terms_inner_ids = (term.name for term in terms)

        term_widget = st.multiselect(
            "Выбрать медицинский термин", terms_inner_ids, default=None, max_selections=1
        )

        st.divider()
        if not term_widget:
            st.subheader("Создать медицинский термин")

        if term_widget:
            term_id = term_name_to_id[term_widget[0]]
            term = med_base_api.term.get_term(term_id)

            term_id = st.text_input("ID", value=term.id, disabled=True, key="term_id")
            term_name = st.text_input("Название", value=term.name, key="term_name")
            term_description = st.text_input("Описание", value=term.description, key="term_description")

            col1, col2, _, _, _, _ = st.columns(6, gap="small")

            change_clicked = col1.button("Изменить", key="term_update_btn")
            if change_clicked:
                term_data = TermBase(name=term_name, description=term_description)
                try:
                    med_base_api.term.update_term(term_id, term_data)
                except Exception as error:
                    st.error(f"Медицинский термин не обновлен по причине: {error_to_readable_view(error)}")
                else:
                    st.success("Медицинский термин обновлен")

            delete_clicked = col2.button("Удалить", key="term_delete_btn")
            if delete_clicked:
                try:
                    med_base_api.term.delete_term(term_id)
                except Exception as error:
                    st.error(f"Медицинский термин не удален по причине: {error_to_readable_view(error)}")
                else:
                    st.success("Медицинский термин удален")

        else:
            term_name = st.text_input("Название", key="term_name")
            term_description = st.text_input("Описание", key="term_description")
            term_data = TermBase(name=term_name, description=term_description)

            add_clicked = st.button("Добавить", key="term_create_btn")
            if add_clicked:
                try:
                    med_base_api.term.create_term(term_data)
                except Exception as error:
                    st.error(f"Медицинский термин не создан по причине: {error_to_readable_view(error)}")
                else:
                    st.success("Медицинский термин создан")