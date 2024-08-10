import streamlit as st
import view
import sqlstock

def cont(a):
    st.write('***WELCOME TO WATCHLIST***')
    b = sqlstock.get_watchlist(a[0][0])
    if b==[]:
        st.write('YOU HAVE NOT ADDED STOCKS TO YOUR WATCHLIST')
    else:
        l=[]
        st.write('YOUR WATCHLIST')
        for i in range (len(b)):
            l.append(b[i][0])
        c = st.selectbox('choose',l)
        st.write(c,' DATAS')
        data = view.getdata(c)
        st.write(data.loc[::-1])
        st.write(c,' volume')
        st.line_chart(data['Volume'])
        del data['Volume']
        st.write(c,' close rates')
        st.line_chart(data['Close'])
        st.write(c,' open rates')
        st.line_chart(data['Open'])
            