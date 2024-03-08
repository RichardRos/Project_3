import requests
import pandas as pd
import streamlit as st

base_url = 'https://financialmodelingprep.com/api'
API_KEY = 'DhSKlDzkmluzGeZ4mK9mvI0lQDUDmRpa'

st.header('Stock Screener')
symbol = st.sidebar.text_input('Ticker:', value='ACLS')
finance_data = st.sidebar.selectbox('Finance Data Type',options=('income-statement', 'balance-sheet-statement',
                                                                   'cash-flow-statement', 'balance-sheet-statement-growth', 
                                                                   'income-statement-growth', 'discount-cash-flow',
                                                                   'historical-discouned-cash-flow', 'eneterprise-values',
                                                                   'ratios', 'ratings', 'Historical Price smaller intervals'))

if finance_data == 'Historical Price smaller intervals':
    interval = st.sidebar.selectbox('Interval', options=('1m', '5m', '15m', '30m', '1hour', '4hour'))
    finance_data = 'historical-chart/'+interval

transpose = st.sidebar.selectbox('Transpose', options=('Yes', 'No'))
url = f'{base_url}/v3/{finance_data}/{symbol}?apikey={API_KEY}'
response = requests.get(url)
data = response.json()

if transpose == 'Yes':
    df = pd.DataFrame(data).T
else:
    df = pd.DataFrame(data)
st.write(df)