def app():
 import yfinance as yf
 import pandas as pd
 import numpy as np
 import streamlit as st
 import matplotlib.pyplot as plt
 

 stocks = st.text_input("stocks", 'WIPRO.NS TCS.NS INFY.NS')
 amount = st.number_input('Insert Amount')
 data = yf.download(stocks, start='2018-01-01')

 #daily returns
 data = data['Close']
 x = data.pct_change()

 p_weights = []
 p_returns = []
 p_risk = []
 p_sharpe = []
 st.set_option('deprecation.showPyplotGlobalUse', False)
 count = 5000
 for k in range(0, count):
     wts = np.random.uniform(size = len(x.columns))
     wts = wts/np.sum(wts)
     p_weights.append(wts)

     #returns
     mean_ret = (x.mean() * wts).sum()*252
     p_returns.append(mean_ret)

     #volatility
     ret = (x * wts).sum(axis = 1)
     annual_std = np.std(ret) * np.sqrt(252)
     p_risk.append(annual_std)
    
     #Sharpe ratio
     sharpe = (np.mean(ret) / np.std(ret))*np.sqrt(252)
     p_sharpe.append(sharpe)
 max_ind = np.argmax(p_sharpe)
 li = stocks.split(" ")
 
 
 weig = pd.DataFrame(p_weights[max_ind])
 weig.columns = ['Ratio']
 weig['Stock'] = li
 weig['Amount'] = p_weights[max_ind]* amount
 st.write('Weight allocation:')
 
 st.write(weig)
 st.write('GIVEN RATIO ARE BASED ON HISTORICAL DATA     USE AT OWN RISK!')
 
 plt.scatter(p_risk, p_returns, c=p_sharpe, cmap='plasma')
 plt.colorbar(label='Sharpe Ratio')
 
 plt.scatter(p_risk[max_ind], p_returns[max_ind], color='r', marker='*', s=500)
 
 st.pyplot()
 st.write("Optimal Sharpe ratio is " + str(p_sharpe[max_ind])) 
 
 