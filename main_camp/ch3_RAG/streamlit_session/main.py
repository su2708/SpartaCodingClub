import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import altair as alt
import seaborn as sns

# 파일 업로드
uploaded_file = st.file_uploader("CSV 파일 업로드", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("데이터 미리보기:")
    st.dataframe(df)

if uploaded_file:
    st.write("컬럼별 데이터 요약:")
    st.write(df.describe())

# 데이터 필터링
if uploaded_file:
    column = st.selectbox("필터링할 컬럼 선택", df.columns)
    value = st.text_input(f"{column}의 값을 입력하세요")
    if value:
        filtered_df = df[df[column].astype(str).str.contains(value)]
        # df라는 데이터프레임 안에서
        # df[column](예를 들면, df["이름"], df["학점"], df["학과"])에서
        # df[column] 값을 문자열(str)로 변경한 다음에
        # 문자열에서 쓰이는 함수만 쓸거야.
        # contains라는 함수를 쓸게.
        # value가 포함된 값만 뽑아줘.
        st.write("필터링된 데이터:")
        st.dataframe(filtered_df)

if uploaded_file:
    fig = px.scatter(df, x=df.columns[0], y=df.columns[1], title="Scatter Plot")
    st.plotly_chart(fig)

if uploaded_file:
    plt.figure(figsize=(10, 5))
    plt.hist(df[df.columns[3]], bins=20)  # hist = 히스토그램 = 분포를 나타내는 그림
    st.pyplot(plt)

if uploaded_file:
    chart = alt.Chart(df).mark_bar().encode(
        x=df.columns[0],
        y=df.columns[1]
    )  
    # mark_bar() => 막대그래프 mark_line() => 꺾은선 그래프
    # encode => 알테어에 데이터를 입력해라
    st.altair_chart(chart, use_container_width=True)
    # use_container_width = 웹사이트 가로 길이랑 같아야 하니?

if uploaded_file:
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots()
    # ax : x랑 y의 축(axis) 값
    sns.boxplot(data=df, ax=ax)  # 주식의 캔들 형태
    st.pyplot(fig)