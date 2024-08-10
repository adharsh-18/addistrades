import streamlit as st

import pandas as pd

import hashlib

import pandas_datareader as web

from PIL import Image

from datetime import date

import admin

import view

import buy

import promembership

import sqlcust

import signup

import watchlist

import myaccount

import mystock

import sell

import mail

import sqlstock

import random

corporate = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\ip project\\project\\corporate.csv",encoding='latin1')

data = sqlcust.all_data()


image=Image.open("C:\\Users\\Lenovo\\Desktop\\school\\logo.jpeg")


def secure(x):
    enc_word=x.encode('utf32')
    xs=hashlib.md5(enc_word.strip()).hexdigest()
    return xs



def getdata(company_name):
    company_list = list(corporate['company'])
    company_index = company_list.index(company_name)
    company_symbol = corporate['symbol'][company_index]
    return  web.DataReader(company_symbol,data_source='yahoo',start='2018-01-01',end=date.today())
st.markdown(
    """
<style>
.reportview-container .markdown-text-container {
    font-family: monospace;
    font-size:30px;
}

.sidebar .sidebar-content {
    background-image: linear-gradient(#F5F5F5,#F5F5F5);    
    color: #8B0000;
}
.Widget>label {
    color: black;
    font-family: monospace;
    font-size:25px;
}
[class^="st-b"]  {
    color: black;
    font-family: monospace;
    font-size:large;
}
footer {
    font-family: monospace;
    font-size:large;
}
.reportview-container .main footer, .reportview-container .main footer a {
    color: black;
}
""",
    unsafe_allow_html=True,
)
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://www.colorhexa.com/dcdcdc.png")
    }
   
    </style>
    """,
    unsafe_allow_html=True
)

c1,c2 = st.beta_columns([3,1])
with c1:


    st.title("WELCOME TO ADDIS TRADES INCORPORATED")
with c2:
    st.image(image,use_column_width=True)

menu = ["login","sign up"]

choice = st.sidebar.selectbox("Menu",menu)






    
    
if choice == "login":
    username=st.sidebar.text_input("USERNAME")
    info = sqlcust.get_data(username)
    password=secure(st.sidebar.text_input("PASSWORD",type='password'))
    q=st.sidebar.checkbox("login")
    if q and info != []:
    
        if username == info[0][0] and password == info[0][2]:
                
            
            st.sidebar.success("logged in as {}".format(username))
            if info[0][0] in ('Adharsh18','Sid03'):
                PAGES = { "BUY": buy,"VIEW": view,"SELL":sell,"WATCHLIST":watchlist,"YOUR STOCKS":mystock,"BECOME A PRO MEMBER":promembership,"ADMIN":admin,'MY ACCOUNT':myaccount}
                st.sidebar.title('Navigation')
                selection = st.sidebar.radio("Go to", list(PAGES.keys()))
                page = PAGES[selection]
                page.cont(info)
            else:
                PAGES = { "BUY": buy,"VIEW": view,"SELL":sell,"WATCHLIST":watchlist,"YOUR STOCKS":mystock,"BECOME A PRO MEMBER":promembership,'MY ACCOUNT':myaccount}
                st.sidebar.title('Navigation')
                selection = st.sidebar.radio("Go to", list(PAGES.keys()))
                page = PAGES[selection]
                page.cont(info)
                        
                        
       
        
       
        else:
            st.sidebar.warning("invalid password")
            if st.sidebar.checkbox('FORGOT PASSWORD'):
                username1=st.text_input("USERNAME ")
                info1 = sqlcust.get_data(username1)
                name1=st.text_input("YOUR NAME")
                ip1=st.text_input("YOUR IPIN")
                b1=st.text_input("YOUR BANK NO",max_chars=15)
                if st.checkbox('continue'):
                    
                    if name1 == info1[0][1] and ip1 == info1[0][3] and b1 == info[0][4]:
                        otp = random.randint(100000,999999)
                        st.success("check your registered email for your new password")
                        mail.password(info1,otp)
                        otp=str(otp)
                        sqlstock.change_pass(info1[0][0],secure(otp))
                    else:
                        st.warning("the given information is inadequate")
                        st.write("please write an email to ")
    elif info == [] and q:
            st.sidebar.warning('invalid username')
        
elif choice == "sign up":
    signup.sign_up(data)
    
