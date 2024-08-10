import streamlit as st
from PIL import Image
import sqlstock


def cont(b):
    if b[0][6] == 'no pro':
        
        image=Image.open("C:\\Users\\Lenovo\\Desktop\\ip project\\project\\prologo.png")
        st.write('**GET LOADS OF BENIFITS BY UPGRADING TO ADDIS TRADES PRO!!**' )
        st.write('')
        col1, col2 = st.beta_columns([2,1])
        with col1:
            st.write("**GET EARLY ACCESS TO IPO's**")
            st.write("**UNLIMITED WATCH LIST**")
            st.write("**HAVE A MINIMUM ACCOUNT BALANCE OF JUST $500**")
            st.write("**SAVE 20% MONEY YOU SPEND ON BROKERAGE**")
            st.write("**CONTAIN UPTO $40000 PER TRANSACTION**")
            st.write("**GET GUIDANCE ON THE STOCK MARKET FROM OUR EXPERTS**")
            st.write("**EARN UPTO $10000 A YEAR**")
        with col2:
            st.image(image,use_column_width='True')
        st.write("all of this and much more at just $99 per year")
    
        a=st.checkbox("BECOME PRO MEMBER BY PAYING $99")
        c = b[0][3]
        if a :
            pin = st.text_input("enter IPIN")
            b2 = st.button ('confirm') 
        
            if b2:
        
                if pin == c:
                    sqlstock.become_pro(b[0][0])
                    st.success("congratulations! you are now a pro member")
                    sqlstock.take_money(b[0][0],99)
                else:
                    st.warning("incorrect IPIN")
    else:
        st.title('You are already a pro member')
        image=Image.open("C:\\Users\\Lenovo\\Desktop\\ip project\\project\\prologo.png")
        st.write('**ENJOY LOADS OF BENIFITS AS ADDIS TRADES PRO!!**' )
        st.write('')
        col1, col2 = st.beta_columns([2,1])
        with col1:
            st.write("**GET EARLY ACCESS TO IPO's**")
            st.write("**YOU HAVE UNLIMITED WATCH LIST **")
            st.write("**SAVE 20% MONEY YOU SPEND ON BROKERAGE**")
            st.write("**EARN UPTO $10000 A YEAR**")
            st.write("**COMPLETE TRANSACTIONS UPTO $40000**")
        with col2:
            st.image(image,use_column_width='True')
            