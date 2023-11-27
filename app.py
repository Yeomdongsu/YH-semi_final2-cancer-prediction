import streamlit as st
from app_eda import app_run_eda
from app_home import app_run_home
from app_pred import app_run_pred
from streamlit_option_menu import option_menu

def main() :
    menu = ["프로젝트 소개","EDA (Exploratory Data Analysis)","Cancer Prediction"]

    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/2611/2611208.png",use_column_width=True)
        st.markdown("\n")

        choose = option_menu("Menu", menu ,
                            icons=['bi bi-box', 'bi bi-bar-chart-line', 'bi bi-virus'],
                            menu_icon="bi bi-arrow-down-square", default_index=0,
                            styles={
            "container": {"padding": "5!important", "background-color": "9999FF"},
            "icon": {"color": "red", "font-size": "23px"}, 
            "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px","color":"skyblue"},
            "nav-link-selected": {"background-color": "black"}
            }
        )

    if choose == menu[0] :
        app_run_home()
    elif choose == menu[1] :
        app_run_eda()
    elif choose == menu[2] :
        app_run_pred() 

if __name__ == "__main__" : main()