import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import random 

def app_run_eda() :
    st.info("데이터를 분석하고 차트화 시키는 페이지 입니다.")

    df = pd.read_csv("./data/cancer_prediction_dataset.csv")

    st.text_area("각 컬럼에 대한 설명", "Gender : '성별'은 이진 값으로 0은 남성, 1은 여성에 해당합니다.\n\n"
                 "Age : '나이'는 18세부터 100세까지의 범위를 가집니다.\n\n"
                 "Smoking : '흡연'은 이진 속성으로 0은 비흡연자, 1은 흡연자를 나타냅니다.\n\n"
                 "Fatigue : '피로'는 이진 값으로 0은 피로가 없음, 1은 피로가 있음을 나타냅니다.\n\n"
                 "Allergy : '알레르기'는 이진 값으로 0은 알레르기가 없음, 1은 알레르기가 있음을 나타냅니다.\n\n"
                 "Cancer : '암'은 주요 대상 변수로써, 0은 암이 없음을 나타내고 1은 있음을 나타냅니다.", height=280)
    
    if st.checkbox("데이터 보기") :
        st.dataframe(df)

    st.markdown("\n")    
    
    if st.checkbox("기초통계데이터 보기") :
        st.info("전체 데이터 중 NaN값을 가진 데이터는 없으며, 총 데이터의 개수는 10000개 입니다.")
        st.write(df.describe())

    st.markdown("\n")    

    if st.checkbox("컬럼들의 빈도수 보기") :
        st.info("색상은 선택마다 랜덤으로 나오게 됩니다.")
        column_select = st.selectbox("궁금한 컬럼을 골라주세요.", df.columns)
        
        message = df[column_select].value_counts().sort_index().values
        
        def select_chart(column_select) :
            fig = plt.figure()
            colors = random.sample(sb.color_palette(), 2)
            sb.countplot(data=df , x=column_select, palette=[colors[0],colors[1]])
            return fig
        
        if column_select == df.columns[1] :
            fig_age = plt.figure()
            plt.hist(data=df , x=column_select, rwidth=0.8)
            plt.title("Person by Age")
            plt.xlabel("Age")
            plt.ylabel("Person")
            st.pyplot(fig_age)
            st.info("최소 나이는 18세, 최대 나이는 100세, 평균 나이는 59세 입니다. ")
        elif column_select == df.columns[0] :
            st.pyplot(select_chart(column_select))
            st.info(f"0은 남성, 1은 여성을 의미합니다.\n\n0은 {message[0]}개 , 1은 {message[1]}개 입니다.")
        else :                              
            st.pyplot(select_chart(column_select))
            st.info(f"0은 {column_select}이(가) 없음, 1은 있음을 의미합니다.\n\n0은 {message[0]}개 , 1은 {message[1]}개 입니다.")

    st.markdown("\n")    

    if st.checkbox("상관계수와 차트 보기") :
        st.info("상관계수란 변수들간의 관련성을 의미하며 -1 ~ 1 사이 숫자로 나타납니다.")
        st.write(df.corr())

        fig = plt.figure(figsize=(10,8))
        sb.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5)
        plt.title("각 컬럼들의 상관관계")
        plt.rc('font', family='Malgun Gothic')
        st.pyplot(fig)
        
    else : st.text("")
