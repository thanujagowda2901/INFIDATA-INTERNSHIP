import streamlit as st

st.bar_chart({'data':[1,5,2,6,2,1]})

with st.expander('See Explanation'):
    st.write('the chart above shows some number i picked for you.')
    st.image('ima.jpg')