# streamlit_first_project

# Stock Price Finder

## Overview
The Stock Price Finder is a Streamlit application that allows users to search for historical stock price data and volume for any given stock ticker. The application uses the `yfinance` library to fetch the data from Yahoo Finance.

## Features
- **Stock Ticker Input**: Users can enter the stock ticker symbol to fetch data for.
- **Date Selection**: Users can select a start and end date to retrieve historical data.
- **Data Visualization**: The application displays line charts for both closing prices and trading volume.

## Installation
To run this application, you need to have Python installed on your system. You can then install the required packages using the following command:

pip install streamlit yfinance

streamlit run main.py