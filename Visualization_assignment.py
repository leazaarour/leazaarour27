#Start by importing
import streamlit as st
import numpy as np
import pandas as pd
import plotly as plt
import plotly.figure_factory as ff
import plotly.graph_objects as go
from plotly.offline import iplot
import plotly as plt
import plotly.express as px
import chart_studio.plotly as py
import plotly.offline as py  
from asyncore import write
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim
import geopy
import geocoder
st.title('Lea Zaarour')
st.title('Streamlit Assignment') 

#title
st.title('Suicide rate')
#Design
col1, col2=st.columns([3,1])
with col1:
    st.markdown('This application is meant to study the number of suicide in several countries, in order to open an NGO to help people that have suicidal thoughts')
with col2:
    st.image('thumbs_b_c_aa3ee04afb9b4a1071bc0821fcb7cbb6.jpeg')
df= pd.read_csv('who_suicide_statistics.csv')

@st.cache(allow_output_mutation= True)
def load_data(nrows):
    df= pd.read_csv('who_suicide_statistics.csv', nrows= nrows)
    lowercase= lambda x: str(x).lower()
    df.rename(lowercase, axis='columns',inplace= True)
    return df



table= ff.create_table(df.head())
table01= ff.create_table(df.tail())
if st.checkbox('Show Table'):
    st.subheader('Table 1')
    st.write(table)

bar= [go.Bar(x=df['country'], y=df['suicides_no'])]

st.subheader('Now lets move to another dataset, which is about the population of several countries')
df1=pd.read_csv('us-cities-top-1k.csv')
table2= ff.create_table(df1.head())

fig = px.density_mapbox(df1, lat = "lat", lon ="lon", z = "Population", radius = 10, 
                       center = dict(lat = 9, lon =8), zoom = 1, hover_name = 'State', 
                       mapbox_style = 'open-street-map', title = 'Population')

if st.checkbox('Show Figure of population density'):
    st.subheader('Figure')
    st.write(fig)

if st.checkbox('Show table'):
    st.subheader('Table 2')
    st.write(table01)


px = px.scatter(df1, x = "City", y = "Population")
if st.checkbox('Show Scatter Plot'):
    st.subheader('Scatter Plot')
    st.write(px)

st.sidebar.title('Number of suicides worldwide')
st.sidebar.markdown('After selecting a visualization of your choice, you can realize the number of suicides which is changing in several countries')

st.sidebar.title('Graph of suicide numbers')
select= st.sidebar.selectbox('Choose the type of Graph',['Table','Bar'], key='1')
if select == 'Table':
    st.plotly_chart(table)
    st.markdown('This table shows the number of suicide in different countries')
if select == "Bar":
    st.plotly_chart(bar)
    st.markdown('This bar also illustrates the number of suicides')

st.sidebar.title('This application now shows the population density accross several countries')
st.sidebar.markdown('We can realize using several visualizations the density of several countries')

st.sidebar.title('Population density')
select= st.sidebar.selectbox('Choose the type of visualization',['Table','Figure'], key='1')

if not st.sidebar.checkbox('Hide', True, key='1'):
    st.title('Visualization Type')
    if select == 'Table':
       st.plotly_chart(table2)
       st.markdown('The above visualization shows the table of the population in different countries')
    if select == 'Figure':
        st.plotly_chart(fig)
        st.markdown('The figures also shows the density of population')



