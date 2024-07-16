def app() :
 import yfinance as yf
 import streamlit as st
 from datetime import date
 import plotly.graph_objects as go

 
 START = "2023-07-01"
 TODAY = date.today().strftime("%Y-%m-%d")
 
 stocks_c = st.text_input("Enter the stock" , 'GOOG ')

 
 def load_data(ticker):
     data = yf.download(ticker, START, TODAY)
     data.reset_index(inplace=True)
     return data
 stock_c = load_data(stocks_c)
 st.write(stock_c.tail())
 st.subheader("Candlestick Chart")
 fig = go.Figure(data = [ go.Candlestick(x = stock_c["Date"] ,open = stock_c['Open'], high = stock_c['High'] , low = stock_c['Low'] , close = stock_c['Close'])])
 fig.update_layout(
    width=800, height=600,
    title= stocks_c,
    yaxis_title=stocks_c+' Stock'
 )
 st.plotly_chart(fig)
 
