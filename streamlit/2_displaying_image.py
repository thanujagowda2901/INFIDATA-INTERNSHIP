import streamlit as st
from PIL import Image
img=Image.open('ima.jpg')
st.title('DISPLAYING IMAGE')
st.image(img,width=450)


st.header('THIS IS HEADER')
img=Image.open('thanuja.jpg')
st.title('DISPLAYING IMAGE')
st.image(img,width=450)

st.subheader('THIS IS SUBHEADER')
img1=Image.open('logo.jpg')
st.title('DISPLAYING IMAGE')
st.image(img1,width=450)



