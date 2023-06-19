import streamlit as st
import time
import pandas as pd
import json

st.set_page_config(layout="wide")



st.sidebar.title("沼气学术会议")
st.sidebar.info(
    """
    中国沼气学会学术年会:     
    <http://www.biogaschina.com.cn>         
    能源系统与电气工程会议:       
    <https://www.ncsti.gov.cn>
    """
)

st.sidebar.title("友情链接")
st.sidebar.info(
    """
    国际沼气网: <http://www.biogasintel.com>       
    中国农业农村部: <http://www.moa.gov.cn>          
    香港可再生能源网: <https://re.emsd.gov.hk>

    """
)

st.header("预测")

tab1,tab2=st.tabs(["产量预测","经济预测"])


with tab1:
    st.subheader("项目选择")
    df = pd.DataFrame(
        [
            {"项目名称": "沼气工程A", "是否需要预测":True},
            {"项目名称": "沼气工程B", "是否需要预测":True},
            {"项目名称": "沼气工程C", "是否需要预测": False},



        ]
    )
    edited_df = st.experimental_data_editor(df)

    st.subheader("模型选择")

    st.selectbox(
        "请选择已训练好的预测模型",
        ('基于遗传算法优化训练的XGBoost', '基于贝叶斯参数优化训练的XGBoost', '基于机理推断优化训练的XGBoost','基于遗传算法自动参数优化训练的GBDT','基于遗传算法、线性回归融合模型的GBDT'))

    if st.button("开始预测"):
       st.subheader("预测结果")
       rf = pd.DataFrame(
            [
                {"预测项": "沼气","单位":"M3","沼气工程A":8575632.6,"沼气工程B":96521152.4},
                {"预测项": "发电量","单位":"度","沼气工程A":676231.1,"沼气工程B":7821182.3},



            ]
       )
       rf

with tab2:
    st.subheader("经济预测")