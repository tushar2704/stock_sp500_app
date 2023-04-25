# S&P 500 Application by Tushar Aggarwal

# Importing required libraries
import streamlit as st
import pandas as pd
import numpy as np
import base64
import matplotlib.pyplot as plt
import yfinance as yf
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

@st.cache_data(persist=True)
def load_data():
    url='https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html =pd.read_html(url, header=0)
    df=html[0]
    return df

df = load_data()
sector = df.groupby('GICS Sector')

# Sidebar for Sector selection

sorted_secotr_unique = sorted(df['GICS Sector'].unique())
selected_sector = st.sidebar.multiselect("Sector", sorted_secotr_unique, sorted_secotr_unique)

# Filtering data
df_selected_sector = df[df['GICS Sector'].isin(selected_sector)]


st.header("Display Compaines in Selected Sector")
st.write('Data Dimension: ' + str(df_selected_sector.shape[0]) + ' rows and ' + str(df_selected_sector.shape[1]) + ' columns.')
st.dataframe(df_selected_sector)

# Download S&P 500 data

def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_sector), unsafe_allow_html=True)

data = yf.download(
    tickers= list(df_selected_sector[:10].Symbol),
    period='ytd',
    interval='1d',
    group_by='ticker',
    auto_adjust=True,
    prepost=True,
    threads=True,
    proxy=None
)

# Plotting Closing Price of Query Symbol
st.set_option('deprecation.showPyplotGlobalUse', False)
def price_plot(symbol):
    df= pd.DataFrame(data[symbol].Close)
    df['Date'] = df.index
    plt.fill_between(df.Date, df.Close, color='skyblue', alpha=0.3)
    plt.plot(df.Date, df.Close, color='skyblue', alpha=0.8)
    plt.xticks(rotation=90)
    plt.title(symbol, fontweight='bold')
    plt.xlabel("Date", fontweight='bold')
    plt.ylabel("Closing Price", fontweight='bold')
    return st.pyplot()

num_company = st.sidebar.slider("Number of Companies", 1,5)

if st.button("Show Plots"):
    st.header("Stock Closing Price")
    for i in list(df_selected_sector.Symbol)[:num_company]:
        price_plot(i)
# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)




