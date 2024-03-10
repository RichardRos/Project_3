import requests
import pandas as pd
import streamlit as st

base_url = 'https://financialmodelingprep.com/api'
API_KEY = 'FcgbccsmrU7YT91G8RMicus6iN9SsaJU'

st.header('Stock Screening Tool')
symbol = st.sidebar.text_input('Ticker:', value='ACLS')
finance_data = st.sidebar.selectbox('Finance Data Type',options=('income-statement', 'balance-sheet-statement',
                                                                   'cash-flow-statement', 'balance-sheet-statement-growth', 
                                                                   'income-statement-growth', 'discounted-cash-flow',
                                                                   'historical-discounted-cash-flow', 'enterprise-value',
                                                                   'ratios', 'rating', 'Historical Price smaller intervals'))

if finance_data == 'Historical Price smaller intervals':
    interval = st.sidebar.selectbox('Interval', options=('1hour', '4hour', '1day', '1week'))
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