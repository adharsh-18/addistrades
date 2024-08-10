import streamlit as st
import sqlstock
import pandas as pd
import hashlib
from PIL import Image



corporate = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\ip project\\project\\corporate.csv",encoding='latin1')
image=Image.open("C:\\Users\\Lenovo\\Desktop\\ip project\\project\\wallet.jpg")

def getfullname(company_symbol):
    company_list = list(corporate['symbol'])
    company_index = company_list.index(company_symbol)
    company_symbol = corporate['company'][company_index]
    return company_symbol


def secure(x):
    enc_word=x.encode('utf32')
    xs=hashlib.md5(enc_word.strip()).hexdigest()
    return xs

menu = ['wallet','my history','change password']
def cont(a):
    
    pp = st.selectbox('menu',menu)
    if pp == 'my history':
        st.write('***YOUR history***')
        b = sqlstock.my_history(a[0][0])
        st.write('INVESTING ON STOCKS IS BETTER THAN OWNING A HOUSE!!')
        df = pd.DataFrame(b,columns=['DATE','COMPANY','NO OF STOCKS','RATE','OPERATION'])
        s = list(df['COMPANY'])
        l=[]
        for i in range(len(s)):
            l.append(getfullname(s[i]))
        df['COMPANY'] = l
        df.set_index('DATE')
        st.write(df.loc[::-1])
    elif pp == 'wallet':
        c1,c2 = st.beta_columns([3,1])
        with c1:
            st.write('***YOUR WALLET***')
            b=sqlstock.show_balance(a[0][0])
            if b==[]:
                st.write('***You don t have any money in your wallet add money***' )
            else:
                st.write('BALANCE : $',b)
            conf = 1
            dic = {'pro':40000,'no pro':20000}
            maxx = dic[a[0][6]]
            st.write('how much dollars do you want to add')
            a1 = st.number_input('how many dollars do you want to add ')
            if int(a1)+int(b)>40000:
                conf = 0
            a2 = st.checkbox('confirm')
            if a2 and a1<0:
                st.warning('ENTER VALID AMOUNT')
            else:
                if a2 and conf == 1:
                    pi = st.text_input('enter your IPIN')
                    c = st.button('Confirm')
                    if pi == a[0][3] and c:
                        sqlstock.add_money(a[0][0],a1)
                        st.success('MONEY ADDED SUCESSFULLY')
                    elif pi != a[0][3] and c:
                        st.warning('INCORRECT IPIN')
                elif a2 and conf == 0:
                    st.warning('YOU CAN HOLD A MAXIMUM BALANCE OF $'+str(maxx)+'\n YOU CAN ADD A MAXIMUM OF $'+str(maxx-b))
            with c2:
                st.image(image,use_column_width=True)
            
            
                
    elif pp == 'change password':
        abi=st.text_input('enter your present password')
        p1=st.text_input('enter your new password')
        p2=st.text_input('confirm new password')
        pin = st.text_input('enter your ipin')
        if st.button('continue'):
            if p1==p2 and secure(abi)==a[0][2] and pin==a[0][3]:
                st.success('UPDATED PASSWORD SUCESSFULLY LOGIN AGAIN WITH NEW PASSWORD')
                sqlstock.change_pass(a[0][0],secure(p1))
            elif secure(abi)==a[0][2]:
                if p1!=p2:
                    st.warning('CONFIRM NEW PASSWORD PROPERLY')
                elif pin!=a[0][3]:
                    st.warning('INCORRECT IPIN')
            else:
                st.warning('INCORRECT CURRENT PASSWORD')
                    