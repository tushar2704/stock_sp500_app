# S&P 500 Application by Tushar Aggarwal

# Importing required libraries
import streamlit as st
import pandas as pd
import numpy as np
import base64
import matplotlib.pyplot as plt
#import yfinance as yf
import seaborn as sns
# Application title and body
st.set_page_config(page_title="Supermarket Sales Dashboard",
                   page_icon=":📈:",
                   layout='wide')
# Title of application
st.title("S&P 500 Application")
st.markdown( '### by Tushar Aggarwal')

st.markdown("""This app retrives the list of **S&P 500** from Wikipedia and its corresponding **closing stock proce**(ytd)
* **Data Source:**  [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
""")

# Sidebar
st.sidebar.header("Please choose: ")

# Webscraping of S&P500 data

#@st.cache_data(persist=True)