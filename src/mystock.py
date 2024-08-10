import streamlit as st
import sqlstock
import pandas as pd
import view
import buy



corporate = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\ip project\\project\\corporate.csv",encoding='latin1')

def getfullname(company_symbol):
    company_list = list(corporate['symbol'])
    company_index = company_list.index(company_symbol)
    company_symbol = corporate['company'][company_index]
    return company_symbol

def cont(a):
    st.write('***YOUR STOCK***')
    
    pp = sqlstock.total_spend(a[0][0])
    
    d={}
    for j in pp:
        d[j[0]]=j[1]
    
    df = pd.Series(d)
    st.header('TOTAL INVESTMENTS MADE IN STOCKS :  $'+str(sum(df)))
    d2={}
    l1 = list(d.keys())
    for i in range (len(pp)):
        abb=l1[i]
        bb = sqlstock.my_stocks_quantity(a[0][0],abb)
        if len(bb)==2:
            d2[abb] = int(bb[0][0] - bb[1][0])
        else:
            d2[abb] = int(bb[0][0])
    b = sqlstock.my_stocks(a[0][0])
    if b==[]:
        st.write('YOU HAVE NOT BOUGHT ANY STOCKS')
    else:
        st.write('INVESTING ON STOCKS IS THE MOST VERSATILE WAY OF INVESTING WITH HIGH RETURNS!!')
        l = []
        for i in range (len(b)):
            l.append(getfullname(b[i][0]))
        choice = st.selectbox('Companies you hold stocks in',l) 
        ab = sqlstock.my_stocks_quantity(a[0][0],buy.getsymbol(choice))
        data = view.getdata(choice)
        st.write('***TODAYS RATE FOR ',choice,'is ***', round(data['High'][-1]))
        if len(ab) == 2:
            ns = ab[0][0]-ab[1][0]
            st.write('***YOU OWN ',ab[0][0]-ab[1][0],'***STOCKS ')
        else:
            ns = ab[0][0]
            st.write('***YOU OWN ',ab[0][0],'***STOCKS ')
        x=buy.getsymbol(choice)
        y=df[x]
        c1,c2,c3=st.beta_columns(3)
        with c1:
            st.title('')
            st.subheader('TOTAL INVESTMENTS IN   '+choice)
            st.title('$'+str(y))
        with c2:
            st.title('')
            coo = 0
            xo=0
            vall = sqlstock.sell_value(a[0][0])
            if len(ab) == 2:
                coo = vall
                l={}
                for i in coo:
                    l[i[0]]=i[1]
                st.subheader('VALUE OF STOCKS SOLD IN '+choice)
                xo=l[buy.getsymbol(choice)]
                st.title('$'+str(xo))
            else:
                st.subheader('VALUE OF STOCKS SOLD IN '+choice)
                st.title('$0')
                st.write('***YOU HAVE NOT SOLD ANY STOCKS IN ***'+choice)
        with c3:
            st.title('')
            st.subheader('VALUE OF STOCKS YOU HOLD IN '+choice)
            st.title('$'+str(int(data['High'][-1])*int(ns)))
        sp = (int(data['High'][-1])*int(ns))+xo
        cp = y
        profit=sp-cp
        if profit<0:
            loss=0-profit
            c1,c2,c3 = st.beta_columns([1.5,1,1.5])
            with c1:
                st.header('')
                st.error('NET LOSS : $ '+str(loss))
                
            with c3:
                st.header('')
                st.error('PERCENTAGE :'+str(round(loss*100/cp,2))+'% ')
        elif profit>0:
            loss=profit
            c1,c2,c3 = st.beta_columns([1.5,1,1.5])
            with c1:
                st.header('')
                st.success('NET PROFIT : $ '+str(loss))
                
            with c3:
                st.header('')
                st.success('PERCENTAGE :'+str(round(loss*100/cp,2))+'% ')
            
            
        elif profit == 0:
            st.header('NO PROFIT OR LOSS')
            st.header('NET PROFIT: 0%')
            
            
            
            
                
            