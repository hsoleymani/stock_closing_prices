import pandas as pd
import streamlit as st
import plotly.express as px
from alpha_vantage.timeseries import TimeSeries

# Side panel for streamlit
st.set_page_config(page_title="Ex-stream-ly Cool App", page_icon="🧊", layout="centered",initial_sidebar_state="expanded")

st.subheader('TDI Milestone app day 10')
st.subheader('An interactive chart of stock closing prices using Streamlit and Plotly.')

st.sidebar.title('Ticker (e.g. AAPL):')
# add a panel to enter ticker as string, this will be use later in the Api

symbol = st.sidebar.text_input("Select ticker (e.g., AAPL)", 'AAPL')

# Get the data from API
api_key = 'JWX4DUFEIKYYB7KQ'

ts = TimeSeries (key=api_key, output_format = "pandas")
data_daily, meta_data = ts.get_daily_adjusted(symbol=str(symbol), outputsize ='full')

data_daily.reset_index(level=0, inplace=True)

data_daily['year'] = pd.DatetimeIndex(data_daily['date']).year
data_daily['month'] = pd.DatetimeIndex(data_daily['date']).month
data_daily['day'] = pd.DatetimeIndex(data_daily['date']).day

# streamlit

years = pd.Series(data_daily['year']).unique()
years_list = years.tolist()
years_list = [str(x) for x in years_list]   # convert all the elements in string

month = pd.Series(data_daily['month']).unique()
month_list = month.tolist()
month_list.sort()
month_list = [str(x) for x in month_list]   # convert all the elements in string

year = st.sidebar.selectbox('Select year',(years_list))
month = st.sidebar.selectbox('Select month',(month_list))

# Manipulate, plot and vsualize
sel_data = data_daily[(data_daily.year == int(year)) & (data_daily.month == int(month))]

fig = px.line(sel_data, x="day", y="4. close")
st.plotly_chart(fig, use_container_width=True)

##------------------------------------------------------------------------------------------------------------------------------------------