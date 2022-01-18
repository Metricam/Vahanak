import streamlit as st
import pandas as pd
import numpy as np
import wbgapi as wb
import plotly.express as px

##configs
country_list = ['ARM','AZE', 'GEO']
year_str = 2005
year_end = 2022
year_step = 1
app_title = 'Economic KPI Dashboard'

data_indicators = pd.DataFrame(wb.series.info().items)

##sidebar
st.sidebar.image("https://cdn.icon-icons.com/icons2/2899/PNG/512/dashboard_icon_182989.png")
selected_indicator = st.sidebar.selectbox(label="Select an Indicator", options = data_indicators.value)
selected_indicator_code = data_indicators[data_indicators.value==selected_indicator].id.values[0]
##body
st.title(app_title)

data_plot = wb.data.DataFrame(selected_indicator_code, economy=country_list, time=range(year_str,year_end,year_step)).T.reset_index().dropna()
data_plot = pd.melt(data_plot, id_vars=['index'], value_vars=country_list)
data_plot.columns = ["Year","Country",selected_indicator]
data_plot.Year = data_plot.Year.str.replace("YR","").astype(int)
plot_object = px.line(data_plot, x="Year", y=selected_indicator,color="Country")
st.plotly_chart(plot_object)
