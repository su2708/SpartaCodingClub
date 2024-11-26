import streamlit as st 

@st.cache_data(ttl=600) # 10분 동안 캐시 유지 (ttl: time to live의 약자, 단위: 초)
def fetch_data():
    # 데이터 로딩 예시 
    return {"data": [1, 2, 3, 4]} 

st.write(fetch_data())