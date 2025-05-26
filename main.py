# streamlit_app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="Plotly 시각화 웹앱", layout="wide")

# 데이터 불러오기
@st.cache_data
def load_data():
    url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
    df = pd.read_csv(url)  # 또는 read_excel(url) 파일 형식에 따라 다르게
    return df

df = load_data()

# 데이터 보여주기
st.subheader("데이터 미리보기")
st.dataframe(df)

# 컬럼 선택
numeric_columns = df.select_dtypes(include='number').columns.tolist()
if len(numeric_columns) < 2:
    st.warning("시각화를 위해 수치형 열이 2개 이상 필요합니다.")
else:
    x_col = st._
