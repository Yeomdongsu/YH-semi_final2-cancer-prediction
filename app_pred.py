import streamlit as st
import joblib 
import numpy as np

def app_run_pred() :
    st.header("암 유무 예측 페이지 입니다.")

    model = joblib.load("./model/model.pkl")

    gender = st.selectbox("성별을 선택해주세요.", ["남성", "여성"])
    st.success(f"성별은 {gender}입니다.")
    if gender == "남성" :
        gender = 0
    else : gender = 1    
    st.markdown("\n")

    age = st.number_input("나이를 적고 Enter를 눌러주세요", min_value=18, max_value=100)
    st.success(f"나이는 {age}세 입니다.")
    st.markdown("\n")

    smoke = st.selectbox("비흡연은 0, 흡연은 1을 선택해주세요.", [0,1])
    if smoke == 0 :
        res = "비흡연자"
    else : res = "흡연자"
    st.success(f"{res} 입니다.")
    st.markdown("\n")

    fatigue = st.selectbox("피로감이 없으면 0, 있으면 1을 선택해주세요", [0,1])
    if fatigue == 0 :
        res = "피로가 없음"
    else : res = "피로가 있음"
    st.success(f"{res}에 체크하셨습니다.")
    st.markdown("\n")

    allergy = st.selectbox("알레르기가 없으면 0, 있으면 1을 선택해주세요", [0,1])
    if allergy == 0 :
        res = "알레르기가 없음"
    else : res = "알레르기가 있음"
    st.success(f"{res}에 체크하셨습니다.")
    st.markdown("\n")

    if st.button("암 유무 예측!") :
        new_data = np.array([gender, age, smoke, fatigue, allergy]).reshape(1,-1)
        
        res = int(model.predict(new_data))
        proba = model.predict_proba(new_data) * 100
        proba = np.round(proba, decimals=2)

        # print(proba, proba[0][0] , proba[0][1])

        if res == 0 :
            st.info(f"암이 없을 확률 : {proba[0][0]}% , 있을 확률 : {proba[0][1]}% 이므로\n\n'없음' 으로 예측되었습니다.")
        elif res == 1 :
            st.info(f"암이 없을 확률 : {proba[0][0]}% , 있을 확률 : {proba[0][1]}% 이므로\n\n'있음' 으로 예측되었습니다.")
        
    else : st.text("")    