import streamlit as st
st.title('online Banking')

st.sidebar.title('welcome to SBI')
account_type=st.sidebar.selectbox('create account',options=['create account','saving','current'])
option=st.sidebar.selectbox('select opration',options=['deposit','withdraw','display'])

if account_type=='create account':
    name=st.text_input('enter name:')
    customerid= st.text_input('enter cid:')
    branch=st.text_input('enter the branch')
    intial_amount=st.number_input('enter the amount')

if account_type=='saving':
    name=st.text_input('enter name:')
    customerid= st.text_input('enter cid:')
    branch=st.text_input('enter the branch')
    intial_amount=st.number_input('enter the amount')

if account_type=='current':
    name=st.text_input('enter name:')
    customerid= st.text_input('enter cid:')
    branch=st.text_input('enter the branch')
    intial_amount=st.number_input('enter the amount')

if option=='deposit':
    dep=st.number_input('enter the dep amount')
    intial_amount += dep
    st.write('updated intial_amount after dep ',intial_amount)

if option=="withdraw":
    withdraw=st.number_input('enter the withdraw amount')
    if (withdraw<= intial_amount):
        intial_amount-=withdraw
        st.write(intial_amount)
    else:
        st.write('Insufficent blance')

if option == "display":
    st.write('the name is:',name)
    st.write('the customerid:',customerid)
    st.write('the branch is:',branch)
    st.write('the intial_amount is:',intial_amount)


    #csv comma separated value


