import streamlit as st
import pandas as pd
import pandas_datareader as web
import datetime 
import sqlstock
import mail
import matplotlib.pyplot as plt

def read():
    return pd.read_csv("C:\\Users\\Lenovo\\Desktop\\ip project\\project\\corporate.csv",encoding='latin1')
corporate=read()


def getsymbol(company_fullname):
    company_list = list(corporate['company'])
    company_index = company_list.index(company_fullname)
    company_symbol = corporate['symbol'][company_index]
    return company_symbol
    

def getdata(company_name):
    company_list = list(corporate['company'])
    company_index = company_list.index(company_name)
    company_symbol = corporate['symbol'][company_index]
    return  web.DataReader(company_symbol,data_source='yahoo',start='2000-01-01',end=datetime.date.today())
def cont(a):
    ipin_value = a[0][3]
    stat = sqlstock.show_balance(a[0][0])
    heat='highly recomended'
    cc1,cc2 = st.beta_columns(2)
    with cc1:
        comp=st.selectbox('COMPANY',list(corporate['company']))
    dict1 = {'one month':30,'3 months':90,'6 month':180,'1 year':365,'3 years':1000,'older':10000000}
    with cc2:
        sel = st.selectbox('VIEW GRAPH FOR',list(dict1.keys()))
    data = getdata(comp)
    mb = 1000
    if a[0][6] == 'pro':
        mb = 500
    st.line_chart(data['Close'].tail(dict1[sel]))
    
    l=list(data['Close'])
    cost2 = (data['Close'][-1])
    if (stat-mb)//cost2 > 0:
        n=st.slider('NO OF STOCKS',1,int((stat-mb)//cost2))
        cost = n*cost2
        st.write('it will cost $',round(cost))
        profit = n*(l[-1] - l[-180])
        if profit < 0:
            heat = 'not recommended'
        st.write('Recommendation: ',heat)
        buy_stock=st.checkbox('CONFIRM')
        if a[0][-1]=='pro':
            x=round(cost)*1.1
            y=str(x)
        else:
            x=round(cost)*1.2
            y=str(x)
        
        if buy_stock :
            ipin=st.text_input('enter ipin')
            c = st.button('Proceed by paying $'+ y +' including tax and brokerage')        
            if ipin == ipin_value and c and sqlstock.show_balance(a[0][0])-x > mb:
                sqlstock.add_stock(a[0][0],getsymbol(comp),n,l[-1])
                st.success("STOCK ADDED")
                mail.buy(a,y,comp,n)
                sqlstock.take_money(a[0][0],y)
            elif c and ipin != ipin_value:
                st.warning('INCORRECT IPIN')
    else:
        st.write('TODAYS RATE FOR ',comp,' IS :$',round(l[-1],2))
        st.warning('NOT ENOUGH BALANCE YOU ONLY HAVE $'+str(stat))