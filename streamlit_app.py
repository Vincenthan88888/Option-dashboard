import streamlit as st

st.set_page_config(page_title="Options Dashboard", layout="centered")

st.title("📊 我的期权决策看板")
st.write("---")

# 侧边栏：输入标的
ticker = st.sidebar.text_input("标的代码", value="SPY").upper()

# 模拟显示你的核心模型数据
st.header(f"🎯 {ticker} 核心指标")

col1, col2 = st.columns(2)
col1.metric("Call Wall (压力位)", "675.01")
col2.metric("Put Wall (支撑位)", "660.00")

st.info(f"📈 {ticker} TD九转状态：当前第 8 根 K 线")
st.warning("⚠️ 价格尚未突破确认位，建议观望")

st.write("---")
st.caption("数据源：Unusual Whales API")
