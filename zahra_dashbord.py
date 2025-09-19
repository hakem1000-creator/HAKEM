
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config( page_title='ZAHRAT ASIR PROJECTS',page_icon=None,layout="wide",initial_sidebar_state="auto",menu_items=None )

file_path="zahra.csv"

df=pd.read_csv(file_path)

#sidebar




st.sidebar.header('ZAHRAT DASHBOARD')
zahra_image="zahra.jpg"
st.sidebar.image(zahra_image)
st.sidebar.write("Zahra is dash board is used for learning")
st.sidebar.markdown("Made by HAKEM")
st.sidebar.write("   ")
st.sidebar.write(" Filter your data")



cat_filter=st.sidebar.selectbox("categorical filtering",[None,'phase','date'])
num_filter=st.sidebar.selectbox("numerical filtering",[None,'ratio','comul_total_wihout_vat','com_Ratio','act_com_ratio','value_without_vat'])
row_filter=st.sidebar.selectbox("row filtering",[None,'phase','date'])
col_filter=st.sidebar.selectbox("columen filtering",[None,'ratio','comul_total_wihout_vat','com_Ratio','act_com_ratio','value_without_vat'])




a1,a2,a3,a4=st.columns(4)
a1.metric("max.total",df['total'].max())
a2.metric("max.value",df['value'].max())
a3.metric("min.total",df['total'].min())
a4.metric("min.value",df['value'].min())


st.subheader("Zahrat Asir Projects Billes")
fig=px.scatter(data_frame=df,x="item",y="total",color=cat_filter,size=num_filter,facet_col=col_filter,facet_row=row_filter,facet_col_spacing=0.01,height=800)


st.plotly_chart(fig,use_container_width = True)

c1,c2,c3=st.columns((4,3,3))
with c1:
    st.text("Total bill vs phase")
    fig=px.bar(data_frame=df,x="item",y="total",color=cat_filter,facet_col=col_filter,facet_row=row_filter,facet_col_spacing=0.01,height=800)
    st.plotly_chart(fig,use_container_width = True)

with c2:
    fig=px.pie(data_frame=df,names='item',values='total',color=cat_filter)
    st.plotly_chart(fig,use_container_width = True)
    
with c3:
    fig=px.pie(data_frame=df,names='item',hole=0.4,values='total',color=cat_filter)
    st.plotly_chart(fig,use_container_width = True)


