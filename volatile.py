def app() :

 import streamlit as st
 from datetime import date

 import yfinance as yf
 import matplotlib.pyplot as plt
 
 START = "2015-01-01"
 TODAY = date.today().strftime("%Y-%m-%d")
 
 # volatility
 st.title("Percentage Increase in stocks")
 st.write('Change stocks acoording to need .')
 st.set_option('deprecation.showPyplotGlobalUse', False)
 stockv1 = st.text_input("First Stock" , 'GOOG')
 stockv2 = st.text_input("Second Stock" , 'AMZN')
 stock_v1 = yf.download(stockv1 , START , TODAY )
 stock_v2 = yf.download(stockv2 , START , TODAY )
 st.write('A percentage increase in stock value is the change in stock comparing that to the previous day. The bigger the value either positive or negative the volatile the stock is.')


 stock_v1['return'] = (stock_v1['Close']/stock_v1['Close'].shift(1)) - 1

 stock_v1['return'].hist(bins = 100, label = stockv1 , alpha = 0.5 , figsize = (15,7))
 stock_v2['return'] = (stock_v2['Close']/stock_v2['Close'].shift(1)) - 1
 stock_v2['return'].hist(bins = 100, label = stockv2 , alpha = 0.5 )
 plt.legend()

 st.pyplot()
