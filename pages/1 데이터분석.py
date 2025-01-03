import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Cardiac disease', page_icon='❤')
st.sidebar.header("심장병 데이터 분석")

df=pd.read_csv('he.csv')

st.header('📈 데이터 통계  & 📊 시각화 그래프', divider='red')

st.markdown('''
    앞서 언급했듯 심장병의 원인은 다양합니다. 선천적인 원인으로도 발병 하지만 후천적인 원인으로 대부분 발생하고, 사망합니다. 이후에 볼 표들은 대표적인 후천적인 원인들과 심장병에 대한 결과입니다. 
''')

tab1, tab2, tab3, tab4, tab5, tab6=st.tabs(['📋심장병 데이터 분석', '🔍 선택한 열 보기', '👵나이', '🦾크레아틴키나제', '❤심박출계수', '💊사망조인트'])

with tab1:
    st.header('심장병 데이터 분석')
    # st.markdown('''
    #     - 심장병과 후천적, 선천적 요인에 의한 상관관계
    #         * 심장병의 반발 원인은 다양하다. 
    #         * 그 중 대표적으로 나이, 크레아틴키나아제, 심박출계수, 사망 조인트를 시각화 했다. 
    #         * 아래의 그래프는 심장병 데이터 엑셀 파일을 파악하기 위함이다.
    # ''')
    st.dataframe(df)

    # df=pd.read_csv('he.csv')
    # st. subheader('나이-사망 히스토그램')
    # if st.button('AGE'):              
    #  st.write(df)

    # td1=df.describe()
    # st.write(td1)
    # col=df.columns
    # scol=st.multiselect('select col' , col)
    # ldf=df.loc[:, scol]

    # c = st.selectbox('Select column', ['age', 'a'])
    # cl = df['creatinine_phosphokinase'] == c
    # a_df = df.loc[cl]
    # st.write(a_df)

with tab2:
    st.subheader('🔍 선택한 열 보기')
    st.markdown("데이터에서 원하는 열을 선택하여 표시합니다.")
    selected_cols = st.multiselect('Select columns to display', list(df.columns))
    st.dataframe(df[selected_cols])
        
with tab3:
    fig, ax = plt.subplots()
    st.subheader("나이-사망 히스토그램")
    if st.button ('age csv'):
        st.dataframe(df.loc[ : , 'age'])
    sns.histplot(x='age', data=df, hue='DEATH_EVENT', kde=True)
    st.pyplot(fig)

with tab4:
    st.subheader("크레아티키나제-사망 히스토그램")
    if st.button ('creatinine csv'):
        st.dataframe(df.loc[ : , 'creatinine_phosphokinase'])
    fig, ax = plt.subplots(1,1,figsize=(20,10))
    sns.histplot(x='creatinine_phosphokinase', data=df, hue='DEATH_EVENT', kde=True)
    st.pyplot(fig)

with tab5:
    st.subheader("박출계수-사망 바이올린프롯")
    if st.button ('ejection fraction csv'):
        st.dataframe(df.loc[ : , 'ejection_fraction'])
    fig, ax = plt.subplots()
    sns.violinplot(x='DEATH_EVENT', y='ejection_fraction', data=df)
    st.pyplot(fig)

with tab6:
    st.subheader("박출계수-혈중 크레아틴 레벨-사망 조인트")
    if st.button ('ejection fraction, creatinine_phosphokinase csv'):
        st.dataframe(df.loc[ : , ['ejection_fraction', 'creatinine_phosphokinase']])
    fig, ax = plt.subplots()
    sns.boxplot(x='ejection_fraction', y='creatinine_phosphokinase', data=df, hue='DEATH_EVENT')
    st.pyplot(fig)

