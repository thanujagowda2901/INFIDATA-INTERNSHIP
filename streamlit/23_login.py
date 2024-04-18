import streamlit as st
import streamlit_authenticator as stauth
import yaml
from streamlit_authenticator import Authenticate
from yaml.loader import SafeLoader

with open('config.yaml') as file:
    config=yaml.load(file,Loader=SafeLoader)

authenticator= Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username= authenticator.login(fields='sidebar')

if authentication_status:
    authenticator.logout('Logout','sidebar')
    st.write(f'Welcome*{name}*')
    st.title('am in home page')

elif authentication_status==False:
    st.error('Username/password is incorrect')

elif authentication_status==None:
    st.warning('Please enter your username and password')



