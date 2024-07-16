import stock_predict as stp
import portfolio
import volatile
import compare_s
import Candlestick 
import streamlit as st
from datetime import date

START = "2019-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

PAGES = {
    "Predict": stp ,
    "Portfolio" : portfolio ,
    "Volatility": volatile , 
    "Compare" : compare_s , 
    "Candlestick" : Candlestick
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
