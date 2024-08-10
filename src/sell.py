import streamlit as st
import sqlstock
import pandas as pd
import buy
import mail

corporate = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\ip project\\project\\corporate.csv",encoding='latin1')

def getfullname(company_symbol):
    company_list = list(corporate['symbol'])
    company_index = company_list.index(company_symbol)
    company_symbol = corporate['company'][company_index]
    return company_symbol

def cont(a):
        ipin_value = a[0][3]
        st.subheader('***YOUR STOCK***')
        b = sqlstock.my_stocks(a[0][0])
        
        l={}
        if b==[]:
            st.write('YOU HAVE NOT BOUGHT ANY STOCKS')
        else:
            for i in range (len(b)):
                qty1=sqlstock.my_stocks_quantity(a[0][0],b[i][0])
                if len(qty1)==1:
                    ns1 = int(qty1[0][0])
                else:
                    ns1 = int(qty1[0][0] - qty1[1][0])
                if ns1 != 0 :
                    l[b[i][0]]=ns1
            st.write('INVESTING ON STOCKS IS BETTER THAN OWNING A HOUSE!!')
            l2 = []
            for i in l.keys():
                l2.append(getfullname(i))
            choice = st.selectbox('Companies you hold stocks in',l2) 
            data = buy.getdata(choice)
            st.write('***TODAYS RATE FOR ',choice,'is ***', round(data['High'][-1]))
            bb = sqlstock.my_stocks_quantity(a[0][0],buy.getsymbol(choice))
            if len(bb)==1:
                ns = int(bb[0][0])
            else:
                ns = int(bb[0][0] - bb[1][0])
            st.write('YOU OWN ',ns,'STOCKS ')
            y = st.slider('NO. OF STOCKS TO SELL',1,ns)
            sell_stock = st.checkbox('SELL')
            li=list(data['Close'])
            if sell_stock :
                ipin=st.text_input('enter ipin')
                do = int(y*data['High'][-1]*0.9)
                c = st.button('SELL '+ str(y) +' stocks for a total of $'+str(do))
                
                
                if ipin == ipin_value and c :
                    sqlstock.remove_stock(a[0][0],buy.getsymbol(choice),y,li[-1])
                    
                    sqlstock.add_money(a[0][0],do)
                    st.success("STOCK SOLD")
                    mail.sell(a,do,choice,y)
                elif c and ipin != ipin_value:
                    st.warning('INCORRECT IPIN')
            
