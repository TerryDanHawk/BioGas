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

st.header("新项目")

tab1,tab2,tab3,tab4,tab5,tab6,tab7=st.tabs(["基本信息","进料","工艺流程","产品利用","投资和资金来源","运行费用","收入"])

class ProjectInfor:
    #基本信息
    ProjectName=""
    Area=""
    EnvEstimateTime=""
    AuditTime=""
    ConstructionTime=""
    CompleteTime=""
    TrailRunTime=""
    SOPTime=""
    LifeTime=""

    PlantArea=0
    GrassArea=0
    OtherArea=0
    TotalArea=0

    #进料
    Mats=pd.DataFrame(
        [
            {"原料种类": "牛粪", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0,
             "可挥发性干物质含量（t）": 0, "沼气产量（NM3/t FM）": 300, "甲烷含量（%）": 60, "甲烷产量（NM3/t VS）": 0,
             "沼气潜力（Nm3）": 0, "甲烷潜力（Nm3）": 0},
            {"原料种类": "猪粪", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0,
             "可挥发性干物质含量（t）": 0, "沼气产量（NM3/t FM）": 0, "甲烷含量（%）": 65, "甲烷产量（NM3/t VS）": 0,
             "沼气潜力（Nm3）": 0, "甲烷潜力（Nm3）": 0},
            {"原料种类": "羊粪", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0,
             "可挥发性干物质含量（t）": 0, "沼气产量（NM3/t FM）": 0, "甲烷含量（%）": 0, "甲烷产量（NM3/t VS）": 0,
             "沼气潜力（Nm3）": 0, "甲烷潜力（Nm3）": 0},
            {"原料种类": "马粪", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0,
             "可挥发性干物质含量（t）": 0, "沼气产量（NM3/t FM）": 0, "甲烷含量（%）": 65, "甲烷产量（NM3/t VS）": 0,
             "沼气潜力（Nm3）": 0, "甲烷潜力（Nm3）": 0},
            {"原料种类": "鸡粪", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0,
             "可挥发性干物质含量（t）": 0, "沼气产量（NM3/t FM）": 0, "甲烷含量（%）": 0, "甲烷产量（NM3/t VS）": 0,
             "沼气潜力（Nm3）": 0, "甲烷潜力（Nm3）": 0},
            {"原料种类": "鸭粪", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0,
             "可挥发性干物质含量（t）": 0, "沼气产量（NM3/t FM）": 0, "甲烷含量（%）": 0, "甲烷产量（NM3/t VS）": 0,
             "沼气潜力（Nm3）": 0, "甲烷潜力（Nm3）": 0},
            {"原料种类": "鹅粪", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0,
             "可挥发性干物质含量（t）": 0, "沼气产量（NM3/t FM）": 0, "甲烷含量（%）": 0, "甲烷产量（NM3/t VS）": 0,
             "沼气潜力（Nm3）": 0, "甲烷潜力（Nm3）": 0},
            {"原料种类": "其他粪", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0,
             "可挥发性干物质含量（t）": 0, "沼气产量（NM3/t FM）": 0, "甲烷含量（%）": 0, "甲烷产量（NM3/t VS）": 0,
             "沼气潜力（Nm3）": 0, "甲烷潜力（Nm3）": 0},
            {"原料种类": "玉米青贮", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0,
             "可挥发性干物质含量（t）": 0, "沼气产量（NM3/t FM）": 0, "甲烷含量（%）": 50, "甲烷产量（NM3/t VS）": 0,
             "沼气潜力（Nm3）": 0, "甲烷潜力（Nm3）": 0},
            {"原料种类": "能源草", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0,
             "可挥发性干物质含量（t）": 0, "沼气产量（NM3/t FM）": 0, "甲烷含量（%）": 65, "甲烷产量（NM3/t VS）": 0,
             "沼气潜力（Nm3）": 0, "甲烷潜力（Nm3）": 0},
            {"原料种类": "粮食残渣", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0,
             "可挥发性干物质含量（t）": 0, "沼气产量（NM3/t FM）": 0, "甲烷含量（%）": 0, "甲烷产量（NM3/t VS）": 0,
             "沼气潜力（Nm3）": 0, "甲烷潜力（Nm3）": 0},
            {"原料种类": "甜菜", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0,
             "可挥发性干物质含量（t）": 0, "沼气产量（NM3/t FM）": 0, "甲烷含量（%）": 0, "甲烷产量（NM3/t VS）": 0,
             "沼气潜力（Nm3）": 0, "甲烷潜力（Nm3）": 0},
            {"原料种类": "饲料残渣", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0,
             "可挥发性干物质含量（t）": 0, "沼气产量（NM3/t FM）": 0, "甲烷含量（%）": 0, "甲烷产量（NM3/t VS）": 0,
             "沼气潜力（Nm3）": 0, "甲烷潜力（Nm3）": 0},
            {"原料种类": "水", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0,
             "可挥发性干物质含量（t）": 0, "沼气产量（NM3/t FM）": 0, "甲烷含量（%）": 0, "甲烷产量（NM3/t VS）": 0,
             "沼气潜力（Nm3）": 0, "甲烷潜力（Nm3）": 0},
        ]
    )
    #总日进料量
    TotalDailyInput=0
    #总可挥发性干物质含量
    TotalVS=0
    #总沼气产量
    TotalBiogasYield=0
    #总甲烷含量
    TotalMethane=0
    #总沼气潜力
    TotalSBY=0
    #总甲烷潜力
    TotalSMY=0

    #投资和资金来源
    Construction=0
    Equipment=0
    Equipment_Pure=0
    Equipment_Power=0
    Equipment_Other=0
    DesignAndManagementCost=0
    FinancialCost=0
    WorkingCapital=0
    TotalInvestment=0

    Loan=0
    YearlyInterestRate=0
    RepaymentPeriod=0
    GracePeriod=0
    GovermentContribution=0
    OwnedFund=0
    OtherFund=0
    TotalFund=0

    #年收入
    GasPrice=0
    GasQuantity=0
    GasSales=0

    PowerPrice=0
    PowerQuantity=0
    PowerSales=0

    SelfPowerPrice=0
    SelfPowerQuantity=0
    SelfPowerSales=0

    BioGasLiquidPrice=0
    BioGasLiquidQuantity=0
    BioGasLiquidSales=0

    BioGasSolidPrice=0
    BioGasSolidQuantity=0
    BioGasSolidSales=0

    PureBioGasPrice=0
    PureBioGasQuantity=0
    PureBioGasSales=0

    GovermentSubsidies=0

    OtherPrice=0
    OtherQuantity=0
    OtherSales=0

    TotalSales=0







data=ProjectInfor()

with tab1:
    st.subheader("项目信息")
    data.ProjectName=st.text_input('*项目名称', '')
    data.Area=st.text_input('占地面积【亩】', '')
    data.EnvEstimateTime = st.text_input('环评批复时间【月/年】', '')
    data.AuditTime = st.text_input('可研批复时间【月/年】', '')
    data.ConstructionTime = st.text_input('开工建设时间【月/年】', '')
    data.CompleteTime = st.text_input('完工时间【月/年】', '')
    data.TrailRunTime = st.text_input('试运行时间【月/年】', '')
    data.SOPTime = st.text_input('正式投产时间【月/年】', '')
    data.LifeTime = st.text_input('设计使用年限【月/年】', '')

    st.subheader("养殖场信息（与沼气工程关联）")
    df = pd.DataFrame(
        [
            {"养殖牲畜": "牛", "年出栏量【头、只/年】": 0, "日清粪量【吨/日】": 0},
            {"养殖牲畜": "猪", "年出栏量【头、只/年】": 0, "日清粪量【吨/日】": 0},
            {"养殖牲畜": "羊", "年出栏量【头、只/年】": 0, "日清粪量【吨/日】": 0},
            {"养殖牲畜": "马", "年出栏量【头、只/年】": 0, "日清粪量【吨/日】": 0},
            {"养殖牲畜": "鸡", "年出栏量【头、只/年】": 0, "日清粪量【吨/日】": 0},
            {"养殖牲畜": "鸭", "年出栏量【头、只/年】": 0, "日清粪量【吨/日】": 0},
            {"养殖牲畜": "鹅", "年出栏量【头、只/年】": 0, "日清粪量【吨/日】": 0},
            {"养殖牲畜": "其他", "年出栏量【头、只/年】": 0, "日清粪量【吨/日】": 0},

        ]
    )
    edited_df = st.experimental_data_editor(df)

    st.subheader("配套农田信息（涉及沼液施用）")
    data.PlantArea = st.number_input('农作物种植面积【亩】', 0)
    data.GrassArea = st.number_input('草地面积【亩】', 0)
    data.OtherArea = st.number_input('其他作物面积【亩】', 0)
    data.TotalArea=data.PlantArea+data.GrassArea+data.OtherArea
    st.write("总农地面积 ",data.TotalArea," 亩")

with tab2:
    st.subheader("进料参数")

    df = pd.DataFrame(
        [
            {"原料种类": "牛粪", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0},
            {"原料种类": "猪粪", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0},
            {"原料种类": "羊粪", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0},
            {"原料种类": "马粪", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0},
            {"原料种类": "鸡粪", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0},
            {"原料种类": "鸭粪", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0},
            {"原料种类": "鹅粪", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0},
            {"原料种类": "其他粪", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0},
            {"原料种类": "玉米青贮", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0},
            {"原料种类": "能源草", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0},
            {"原料种类": "粮食残渣", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0},
            {"原料种类": "甜菜", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0},
            {"原料种类": "饲料残渣", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0},
            {"原料种类": "水", "进料量FM（吨/天）": 0, "干物质含量（%）": 0, "可挥发性干物质含量（%）": 0},


        ]
    )
    edited_df = st.experimental_data_editor(df)

    st.subheader("效率分析")

    for index in edited_df.index:
        data.Mats.loc[index,"进料量FM（吨/天）"]=edited_df.loc[index]["进料量FM（吨/天）"]
        data.Mats.loc[index,"干物质含量（%）"] = edited_df.loc[index]["干物质含量（%）"]
        data.Mats.loc[index,"可挥发性干物质含量（%）"] = edited_df.loc[index]["可挥发性干物质含量（%）"]
        data.Mats.loc[index,"可挥发性干物质含量（t）"] = edited_df.loc[index]["可挥发性干物质含量（%）"]*edited_df.loc[index]["进料量FM（吨/天）"]
        data.Mats.loc[index,"甲烷产量（NM3/t VS）"]= data.Mats.loc[index]["沼气产量（NM3/t FM）"]*data.Mats.loc[index]["甲烷含量（%）"]/100
        data.TotalDailyInput+= edited_df.loc[index]["进料量FM（吨/天）"]
        data.TotalVS+= data.Mats.loc[index]["可挥发性干物质含量（t）"]
        data.TotalBiogasYield += data.Mats.loc[index]["沼气产量（NM3/t FM）"]
        data.TotalMethane += data.Mats.loc[index]["甲烷产量（NM3/t VS）"]
        data.TotalSBY += data.Mats.loc[index]["沼气潜力（Nm3）"]
        data.TotalSMY += data.Mats.loc[index]["甲烷潜力（Nm3）"]

    st.table(data.Mats)


    st.write("日进料量：", data.TotalDailyInput)
    st.write("日可挥发干物质总量", data.TotalVS)
    st.write("日沼气产量", data.TotalBiogasYield)
    st.write("日甲烷产量", data.TotalMethane)
    st.write("日沼气潜力", data.TotalSBY)
    st.write("日甲烷潜力", data.TotalSMY)

with tab3:
    st.header("工艺流程")

with tab4:
    st.header("产品利用")

with tab5:
    st.subheader("总投资")
    data.Construction = st.number_input('土建【万元】', 0)
    data.Equipment_Pure  = st.number_input('提纯设备【万元】', 0)
    data.Equipment_Power = st.number_input('发电机组【万元】', 0)
    data.Equipment_Other = st.number_input('其他设备【万元】', 0)
    data.Equipment = data.Equipment_Power + data.Equipment_Power + data.Equipment_Other
    st.write("设备【万元】: ", data.Equipment)
    data.DesignAndManagementCost = st.number_input('设计和工程监理等项目管理费【万元】', 0)
    data.DesignAndManagementCost = st.number_input('财务费用【利息，万元】', 0)
    data.DesignAndManagementCost = st.number_input('流动资金【万元】', 0)
    data.DesignAndManagementCost = st.number_input('其他费用【万元】', 0)
    data.TotalInvestment=data.Construction+data.Equipment+data.DesignAndManagementCost+data.FinancialCost+data.WorkingCapital+data.OtherFund
    st.write("总投资【万元】: " , data.TotalInvestment)
    st.subheader("资金来源")
    data.Loan = st.number_input('银行贷款【万元】', 0)
    data.YearlyInterestRate = st.number_input('┗年利率【%】', 0)
    data.RepaymentPeriod = st.number_input('┗还款年限【年】', 0)
    data.GracePeriod = st.number_input('┗宽限期【年】', 0)
    data.GovermentContribution = st.number_input('政府赠款【万元】', 0)
    data.OwnedFund = st.number_input('企业自有资金【万元】', 0)
    data.OtherFund = st.number_input('其他资金来源【万元】', 0)
    data.TotalFund=data.Loan+data.GovermentContribution+data.OwnedFund+data.OtherFund
    st.write("总计【万元】： ",data.TotalFund)
with tab6:
    st.header("运行费用")

with tab7:
    st.subheader("年收入")
    st.caption("供气")
    data.GasPrice = st.number_input('单价【元/m3】', 0)
    data.GasQuantity = st.number_input('供气量【m3/天】', 0)
    data.GasSales = st.number_input('盈利额【万元/天】', 0)

    data.PowerPrice = st.number_input('单价【元/度】', 0)
    data.PowerQuantity= st.number_input('售出量【m3/天】', 0)


