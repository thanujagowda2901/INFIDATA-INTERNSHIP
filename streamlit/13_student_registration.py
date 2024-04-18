import streamlit as st
import datetime

st.header('student registration form')
my_form=st.form(key="form1")
Fname=my_form.text_input('student first name')
Lname=my_form.text_input('student last name')
Email=my_form.text_input('student email')
mobile=my_form.number_input('student mobile')
gender=my_form.radio("gender",('male','female'))
city= my_form.text_input('city')
DOB=my_form.date_input('enter the DOB',min_value=datetime.date(1990,1,1))
addr=my_form.text_area("enter ur address")
AreaPIN=my_form.number_input("AreaPIN")
State=my_form.text_input('State')
Qualification=my_form.selectbox(
        'select Qualification',
        [None,'MCA','BCA','Bcom','BA','PUC'])

specialization=my_form.checkbox('specialization')
specialization1=my_form._checkbox('CS')
specialization2=my_form._checkbox('IT')
specialization3=my_form._checkbox('CA')
specialization4=my_form._checkbox('TC')

password=my_form.text_input('password')
my_form.form_submit_button("Registerd")

st.write('Fname',Fname)
st.write('Lname',Lname)
st.write('Email',Email)
st.write('mobile',mobile)
st.write('gender',gender)
st.write('city',city)
st.write('DOB',DOB)
st.write('addr',addr)
st.write('AreaPIN',AreaPIN)
st.write('State',State)
st.write('Qualification',Qualification)
st.write('specialization',specialization)
st.write('password',password)
