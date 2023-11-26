import streamlit as st

def app_run_home() :
    st.header("데이터를 이용한 암 예측하기")
    st.markdown("\n")
    st.markdown("\n")
    st.info("10,000명의 의사 환자로 구성되며, 각 환자는 성별, 연령, 흡연, 피로, 알레르기 등\n\n5가지 고유한 매개변수와 암의 유무를 나타내는 이진 지표를 특징으로 합니다.")
    st.markdown("\n")
    st.markdown("\n")
    st.write("데이터 출처)\n\nhttps://www.kaggle.com/datasets/ohinhaque/synthetic-cancer-prediction-dataset-for-research/")
    st.image("https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/5nbC/image/y7jc2Z2kI5tPyi3vouKQTa5IZxY")