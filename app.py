import streamlit as st, pandas as pd, numpy as np
st.set_page_config(page_title='AI Law Firm Dashboard', layout='wide')
st.title('AI Law Firm Dashboard')

np.random.seed(42)
df = pd.DataFrame({
    'Matter ID': np.arange(1001,1031),
    'Client': np.random.choice(['Alpha','Beta','Gamma','Delta','Epsilon'], 30),
    'Status': np.random.choice(['Open','Nearing Deadline','Closed'], 30, p=[0.55,0.15,0.30]),
    'Hours':  np.round(np.random.gamma(2.2,3.0,30),1),
    'Rate':   np.random.choice([250,325,400,475],30)
})
df['Value'] = df['Hours']*df['Rate']

st.caption('Demo data – replace with your ETL.')

c1,c2,c3 = st.columns(3)
c1.metric('Total Matters', len(df))
c2.metric('Open Matters', int((df['Status']=='Open').sum()))
c3.metric('Total Value', f'$ {df['Value'].sum():,.0f}')

col1,col2 = st.columns(2)
with col1:
    st.subheader('Value by Client')
    st.bar_chart(df.groupby('Client')['Value'].sum().sort_values(ascending=False))
with col2:
    st.subheader('Matters by Status')
    st.bar_chart(df['Status'].value_counts())

st.subheader('Matter Detail')
st.dataframe(df.sort_values('Value', ascending=False), use_container_width=True)
