import streamlit as st
from app_eda import app_run_eda
from app_home import app_run_home
from app_pred import app_run_pred

def main() :
    menu = ["프로젝트 소개","EDA (Exploratory Data Analysis)","Cancer Prediction"]
    select_menu = st.sidebar.selectbox("Menu", menu)

    if select_menu == menu[0] :
        app_run_home()
    elif select_menu == menu[1] :
        app_run_eda()  
    elif select_menu == menu[2] :
        app_run_pred()  

if __name__ == "__main__" : main()