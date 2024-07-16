def app() :
 import yfinance as yf
 import streamlit as st
 from datetime import date
 import pandas as pd
 
 
 
 START = "2015-01-01"
 TODAY = date.today().strftime("%Y-%m-%d")
 st.title('Compare')
 
 stocks_c = st.text_input("Enter all stocks to add while using '   ' blank space." , 'GOOG AAPL TSLA')
 stock_c = yf.download(stocks_c , START , TODAY)
 st.write(stock_c.tail(n=10))
 
 h = stock_c['Close']
 st.subheader("Trend")
 st.write(stock_c['Close'].tail())
 st.line_chart(h)
 st.subheader('Volume')
 st.write(stock_c['Volume'].tail())
 st.line_chart(stock_c['Volume'])
 df = pd.DataFrame(stock_c)
 df1 = df['Close'] * df['Volume']
 st.subheader('Market Cap')
 st.write(df1.tail())
 st.line_chart(df1)
 