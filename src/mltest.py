import streamlit as st
import pandas as pd
import pandas_datareader as web
corporate = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\ip project\\project\\corporate.csv")
def getdata(company_name):
    company_list = list(corporate['company'])
    company_index = company_list.index(company_name)
    company_symbol = corporate['symbol'][company_index]
    return  web.DataReader(company_symbol,data_source='yahoo',start='2018-01-01',end='2020-01-01')
def cont():

                   
                    
                        comp=st.selectbox('COMPANY',list(corporate['company']))
                        data = getdata(comp)
                        st.write('company closing rates')
                        st.line_chart(data['Close'])
                        st.write('company volume')
                        st.line_chart(data['Volume'])
                    
            
                        
                            
                    