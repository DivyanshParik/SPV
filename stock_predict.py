def app():

        
  import streamlit as st
  from datetime import date

  import yfinance as yf
  from prophet import Prophet
  from prophet.plot import plot_plotly
  from plotly import graph_objs as go

  #START = "2017-01-01"
  TODAY = date.today().strftime("%Y-%m-%d")

  st.title('Stock Forecast')

  stock_name = st.text_input("Enter Stock's Ticker Symbol " , "AMZN")


  stocks = (stock_name , 'GOOG', 'AAPL', 'MSFT', 'GME')
  
  col0 , col1, = st.columns(2)
  with col0:
     selected_stock = st.selectbox('Select dataset for prediction', stocks)
  with col1:
     time_period = st.selectbox('Select time period for prediction' ,( 'Years' , 'Months', 'Weeks' , 'Days' ))   
  if time_period=='Years':
     time_period = Years = st.slider('Years of Prediction' , 1 , 4)*365
  elif time_period == 'Months':
     time_period =  Months = st.slider('Months of Prediction' , 1,12)*30
  elif time_period=='Weeks':
     time_period = Weeks = st.slider("Weeks of Prediction", 1,4)*7
  elif time_period== 'Days':
     time_period = Days = st.slider('Days to predict', 1,7)

  
  period = time_period
  col2 , col3 = st.columns(2)
  with col2:
    START = st.selectbox("Start date" ,( "2014-01-01" , "2015-01-01" , "2016-01-01" , "2017-01-01", "2018-01-01") )
  
  with col3:
     UPTO = st.selectbox("End date" ,(TODAY , "2023-01-01","2022-01-01" , "2021-01-01" , "2020-01-01" , "2019-01-01", "2018-01-01") )


  @st.cache_data
  def load_data(ticker):
     data = yf.download(ticker, START, UPTO)
     data.reset_index(inplace=True)
     return data

    
  data_load_state = st.text('Loading data...')
  data = load_data(selected_stock)
  data_load_state.text('Loading data... done!')

  st.subheader('Present Data')
  st.write(data.tail())

  # Plot raw data
  def plot_raw_data():
     fig = go.Figure()
     fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
     fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
     fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
     st.plotly_chart(fig)
    
  plot_raw_data()

  # Predict forecast with Prophet.
  df_train = data[['Date','Close']]
  df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

  m = Prophet()
  m.fit(df_train)
  future = m.make_future_dataframe(periods=period)
  forecast = m.predict(future)

  # Show and plot forecast
  st.subheader('Forecast data')
  st.write(forecast.tail())
    
  st.write(f'Forecast plot for {time_period} Days')
  fig1 = plot_plotly(m, forecast)
  st.plotly_chart(fig1)

  st.write("Forecast components")
  fig2 = m.plot_components(forecast)
  st.write(fig2)
 