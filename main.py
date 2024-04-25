import streamlit as st
import yfinance as yf
from datetime import date, timedelta

# Set the title of the app
st.title('Stock Price Finder')

# User input for stock ticker
tickerSymbol = st.text_input("Enter Stock Ticker", "AAPL")

# User input for start and end date
start_date = st.date_input("Start Date", date.today() - timedelta(days=365))
end_date = st.date_input("End Date", date.today())

# Fetch stock data
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)

# Display the stock price data
st.write(f"## Closing Price for {tickerSymbol}")
st.line_chart(tickerDf.Close)

st.write(f"## Volume for {tickerSymbol}")
st.line_chart(tickerDf.Volume)