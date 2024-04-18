import streamlit as st

#using object notation
add_selectbox=st.sidebar.selectbox(
    "How would you like to be contacted?",
    ('Email','Home phone','Mobile phone')
)

#using "with" keyword notation
with st.sidebar:
    add_radio=st.radio(
        "Choose a shiping method",
        ('Standard(5-15 days)',"express(2-5 days)")
    )
    name=st.text_input('enter c name:')