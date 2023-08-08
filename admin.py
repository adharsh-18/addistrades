import streamlit as st
import sqlcust
import pandas as pd
def cont(a):
    b=a[0][0]
    if b in ('Sid03','Adharsh18'):
        data = sqlcust.all_data()
        a = pd.DataFrame(data,columns=['Username','Fullname','password','IPIN','BankNo','Email','membership status','Acount Balance'])
        st.subheader('CUSTOMER DATABASE')
        st.write(a)
        data2 = sqlcust.history()
        st.subheader('ALL TRANSACTIONS')
        a2 = pd.DataFrame(data2,columns = ['Username','company code','quantity','rate','date','operation'])
        st.write(a2.loc[::-1])
        

