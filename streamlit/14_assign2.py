import streamlit as st

cname=st.text_input('enter the name')
cid=st.text_input('enter the id')
units=st.number_input('enter the units')

if(units<=100):
    charge=units*0
    st.write('electricity charge is:',charge)

elif(units>=100 and units<=200):
    charge=units*5
    st.write('electricity charge is:',charge)

elif( units>=200):
    charge=units*10
    st.write('electricity charge is:',charge)
    