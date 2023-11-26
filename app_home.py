import streamlit as st

def app_run_home() :
    st.header("데이터를 이용한 암 유무 예측")
    st.markdown("\n")
    st.markdown("\n")
    st.info("이 데이터는 10,000명의 의사 환자로 구성되며, 각 환자는 성별, 연령, 흡연, 피로, 알레르기 등\n\n5가지 고유한 매개변수와 암의 유무를 나타내는 이진 지표를 특징으로 합니다.")
    st.info("이 데이터는 완전히 합성된 것이며 실제 임상 기록에서 파생된 것이 아니라는 점을 알려드립니다.\n\n이 데이터는 탐색 목적, 모델 개발 및 알고리즘 테스트를 위해 사용하는 것이 좋습니다.\n\n이 데이터에서 얻은 결과는 실제 임상 데이터에 대한 검증 없이 실제 의료 시나리오로 추정되어서는 안 된다는 점에 유의해야 합니다.")
    st.markdown("\n")
    st.markdown("\n")
    st.write("데이터 출처)\n\nhttps://www.kaggle.com/datasets/ohinhaque/synthetic-cancer-prediction-dataset-for-research/")
    st.image("https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/5nbC/image/y7jc2Z2kI5tPyi3vouKQTa5IZxY")