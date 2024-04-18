import streamlit as st
import datetime

st.header('student registration form')
my_form=st.form(key="form1")
Fname=my_form.text_input('student first name')
Lname=my_form.text_input('student last name')
Email=my_form.text_input('student email')
mobile=my_form.number_input('student mobile')
gender=my_form.radio("gender",('male','female'))
age= my_form.slider('age',1,100)
DOB=my_form.date_input('enter the DOB',min_value=datetime.date(1990,1,1))
addr=my_form.text_area("enter ur address")
resume=my_form.file_uploader("upload ur resume")

my_form.form_submit_button("submit")

st.write('Fname',Fname)
st.write('Lname',Lname)
st.write('Email',Email)
st.write('mobile',mobile)
st.write('gender',gender)
st.write('age',age)
st.write('DOB',DOB)
st.write('addr',addr)