import streamlit as st
import pandas as pd
import pandas_datareader as web
import datetime
import sqlstock

import buy

    



corporate = buy.read()

def getdata(company_name):
    company_list = list(corporate['company'])
    company_index = company_list.index(company_name)
    company_symbol = corporate['symbol'][company_index]
    return  web.DataReader(company_symbol,data_source='yahoo',start='1990-01-01',end=datetime.date.today())


def cont(a):

                   
    tb = sqlstock.get_watchlist(a[0][0])              
    comp=st.selectbox('COMPANY',list(corporate['company']))
    data = getdata(comp)
    co = list(corporate['company'])
    no = co.index(comp)
    st.write('***'+comp+'***')
    
    st.write(corporate['description'][no])
    st.subheader('company volume')
    st.line_chart(data['Volume'])
    del data['Volume']
    dat = st.multiselect("choose datas",data.columns)
    for i in dat :
        st.write('company data :',i)
        st.line_chart(data[i])
    comps = []
    for j in tb:
        comps.append(j[0])
    if comp in comps:
        st.write('You already have watchlisted the stock')
        b = st.button('remove watchlist')
        if b:
            sqlstock.remove_watchlist(a[0][0],comp)
            st.success('STOCK REMOVED')
    else:
        b = st.button('add to watchlist')
        c = sqlstock.get_watchlist(a[0][0])
                        
        if b:
            if len(c)>4 and a[0][-1] != 'pro':
                st.warning('You have already watchlisted 5 stocks \n Become a pro member to get unlimited watchlist capacity')
            else:
                sqlstock.add_watchlist(a[0][0],comp)
                st.success('added to watchlist')
                            
            
                      
                            
                    