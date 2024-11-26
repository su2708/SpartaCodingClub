import streamlit as st 
import pandas as pd
from streamlit_chat import message
from sklearn.linear_model import LinearRegression
import requests
import numpy as np
import time

@st.cache_data(ttl=600) # 10분 동안 캐시 유지 (ttl: time to live의 약자, 단위: 초)
def fetch_data():
    # 데이터 로딩 예시 
    return {"data": [1, 2, 3, 4]} 

st.write(fetch_data())

if "user_name" not in st.session_state:
    st.session_state.user_name = "Guest"
name = st.text_input("Your Name:", st.session_state.user_name)
        
if st.button("Save Name"):
    st.session_state.user_name = name
st.write(f"Hello, {st.session_state.user_name}!")

@st.cache_data  # 기본 ttl = 600 (10분)
def load_file(file):
    return pd.read_csv(file)

file = st.file_uploader("Upload a CSV File", type=["csv"])
if file:
    df = load_file(file)
    st.dataframe(df)

    # 필터링 기능 추가
    filter_value = st.text_input("Filter by column value")
    filtered_df = df[df.iloc[:, 0].astype(str).str.contains(filter_value, na=False)]
    st.write("Filtered Data:", filtered_df)
    
st.markdown(
    """
    <style>
    .custom-title {
        color: #4CAF50;
        font-size: 30px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="custom-title">Customized Title</p>', unsafe_allow_html=True)

st.components.v1.html(
    """
    <button onclick="alert('Button clicked!')">Click Me</button>
    """
)

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("Content for Tab 1")
with tab2:
    st.write("Content for Tab 2")
    
df = pd.read_csv("test.csv")  # 어제 받으셨던 파일

selected_columns = st.multiselect("Select columns to display", df.columns)
if selected_columns:
    st.write(df[selected_columns])
    
message("My message")
message("Hello bot!", is_user=True)

placeholder = st.empty()

for i in range(10):
    placeholder.write(f"Iteration {i}")
    time.sleep(1)

        
# 모델 학습
model = LinearRegression()
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])
model.fit(X, y)

# 사용자 입력
user_input = st.number_input("Enter a value for prediction:")
if st.button("Predict"):
    prediction = model.predict([[user_input]])
    st.write(f"Prediction: {prediction[0]:.2f}")
    
# response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=YOUR_API_KEY")
# if response.status_code == 200:
#     data = response.json()
#     st.write(f"Temperature: {data['main'][temp']}K")