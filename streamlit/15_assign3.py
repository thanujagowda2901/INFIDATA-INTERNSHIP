import streamlit as st

marks=st.number_input('enter the marks')

if(marks>90):
    st.info('Grade A')

elif(marks>80 and marks<=90):
    st.info('Grade B')

elif(marks>=60 and marks<=80):
    st.info('Grade C')

elif(marks<=60):
    st.info('Grade D')
else:
    st.info('fail')

