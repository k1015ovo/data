# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# st.set_page_config(page_title='Cardiac disease', page_icon='❤')

# df = pd.read_csv('he.csv')

# st.header('📈 데이터 통계', divider='red')

# tab1, tab2, tab3= st.tabs(['실제데이터', '데이터 통계', '컬럼데이터'])

# with tab1:
#     t1 = df.head(10)
#     st.write(t1)

# with tab2:
#     # td1 = df.describe()
#     # st.write(td1)
#     col = df.columns
#     scol = st.multiselect('select col', col)
#     ldf = df.loc[:, scol]
#     st.write(ldf)

# with tab3:
#     c = st.selectbox('Select column', ['age', 'a'])
#     cl = df['age'] == c
#     a_df = df.loc[cl]
#     st.write(a_df)

# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder
import streamlit as st 
import joblib #모델저장 불러올때


st.set_page_config(page_title='Cardiac disease', page_icon='❤')
st.sidebar.header("머신러닝 보고서")



df = pd.read_csv('he.csv')

st.write(df)
y = df['DEATH_EVENT']
X= df.drop(['DEATH_EVENT'], axis=1) 
    
# 연속형 입력 데이터, 범주형 입력 데이터, 출력 데이터로 구분
X_num = df[['age', 'creatinine_phosphokinase','ejection_fraction', 'platelets','serum_creatinine', 'serum_sodium']]
X_cat = df[['anaemia', 'diabetes', 'high_blood_pressure', 'sex', 'smoking']]
y = df['DEATH_EVENT']

# 수치형 입력 데이터를 전처리하고 입력 데이터 통합하기
scaler = StandardScaler()
scaler.fit(X_num)
X_scaled = scaler.transform(X_num) 
X_scaled = pd.DataFrame(data=X_scaled, index=X_num.index, columns=X_num.columns)
X = pd.concat([X_scaled, X_cat], axis=1) # 행 방향으로 조인

#학습, 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

#Logistic Regression 모델 생성
model_lr = LogisticRegression(max_iter=1000) # 학습 1000번 진행
model_lr.fit(X_train, y_train)
model_lr.score(X_test, y_test) # 0.7555555555555555

pred = model_lr.predict(X_test) # X_test 데이터를 기반으로 y값 예측

#XGBoost 모델 생성
model_xgb = XGBClassifier()
model_xgb.fit(X_train, y_train)
model_xgb.score(X_test, y_test) # 0.8

#학습한 모델을 통한 예측
pred = model_xgb.predict(X_test)
st.write(classification_report(y_test, pred))


fig=plt.figure(figsize=(10,4))
st.header("Feature_importancs Graph")
plt.bar(X.columns,model_xgb.feature_importances_)
plt.xticks(rotation=90)
st.pyplot(fig)


