import streamlit as st 
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Plotly 시각화 웹앱", layout="wide")
st.title("📊 CSV 데이터 Plotly 시각화 웹앱")

@st.cache_data
def load_data():
    url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
    df = pd.read_csv(url)
    return df

df = load_data()

st.subheader("데이터 미리보기")
st.dataframe(df)

numeric_cols = df.select_dtypes(include='number').columns.tolist()

if len(numeric_cols) >= 2:
    st.subheader("📈 시각화 설정")

    chart_type = st.selectbox("그래프 종류 선택", ["산점도 (Scatter)", "막대그래프 (Bar)"])

    x_col = st.selectbox("X축 선택", numeric_cols, index=0)
    y_col = st.selectbox("Y축 선택", numeric_cols, index=1)

    if chart_type == "산점도 (Scatter)":
        fig = px.scatter(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col} 산점도")
    else:
        fig = px.bar(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col} 막대그래프")

    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("시각화를 위해 수치형 컬럼이 2개 이상 있어야 합니다.")
