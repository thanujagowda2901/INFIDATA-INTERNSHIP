import streamlit as st

if'clicked1' not in st.session_state:
    st.session_state.clicked1=False


if'clicked2' not in st.session_state:
    st.session_state.clicked2=False

def click_button1():
    st.session_state.clicked1=True
    st.write("button clicked!")

def click_button2():
    st.session_state.clicked2=True
    st.write("button clicked!")

st.button('ADD',on_click=click_button1)
st.button('SUB',on_click=click_button2)

if(st.session_state.clicked1):
    # The message and nested widget will remain on the page
    st.title('Addition program')
    n1=st.number_input('enter n1')
    n2=st.number_input('enter n2')
    sum=n1+n2
    st.info('Addition of 2 int numbers')
    st.success(sum)

if(st.session_state.clicked2):
    # The message and nested widget will remain on the page
    st.title('Substraction program')
    n1=st.number_input('enter n1 ')
    n2=st.number_input('enter n2 ')
    sub=n1-n2
    st.info('Substraction of 2 int numbers')
    st.success(sub)