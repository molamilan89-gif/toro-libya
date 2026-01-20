import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# 1. إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="Toro Libya | تورو ليبيا",
    page_icon="🐂",
    layout="centered"
)

# 2. التنسيق الجمالي المتقدم (CSS) لمحاكاة الصورة المطلوبة تماماً
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif;
        direction: rtl;
        text-align: right;
        background-color: #0e1621; /* لون الخلفية الداكن المماثل للصورة */
    }

    /* تنسيق حاوية اللوجو */
    .logo-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .logo-img {
        width: 220px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.5);
    }

    /* نص العنوان الفرعي */
    .sub-title {
        text-align: center;
        color: #00ffff;
        background: rgba(0, 255, 255, 0.05);
        padding: 10px;
        border-radius: 10px;
        border: 1px solid rgba(0, 255, 255, 0.2);
        font-size: 0.9rem;
        margin-bottom: 5px;
    }

    .legend-text {
        text-align: center;
        color: #55606e;
        font-size: 0.7rem;
        letter-spacing: 2px;
        margin-bottom: 25px;
    }

    /* بطاقات الأسعار */
    .price-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 10px;
        margin-bottom: 25px;
    }
    .price-box {
        background: #17212b;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        border-bottom: 3px solid #00ffff; /* الخط الملون أسفل البطاقة */
    }
    .label { color: #808d9a; font-size: 0.8rem; }
    .value { color: #ffffff; font-size: 1.3rem; font-weight: bold; margin-top: 5px; }

    /* حاوية نبض السوق */
    .market-container {
        background: #17212b;
        border: 1px solid #00ffff;
        border-radius: 20px;
        padding: 20px;
        margin-top: 10px;
    }
    .market-header {
        color: #00ffff;
        font-size: 1.2rem;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        gap: 10px;
        margin-bottom: 20px;
    }
    
    .status-row {
        display: flex;
        justify-content: space-between;
        color: #ffffff;
        margin-bottom: 10px;
        font-size: 0.9rem;
    }

    /* زر الواتساب */
    .stButton>button {
        background: linear-gradient(90deg, #0088cc, #00ffff);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 15px;
        width: 100%;
        font-weight: bold;
        transition: 0.3s;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. عرض اللوجو الرئيسي
st.markdown(f"""
    <div class="logo-container">
        <img src="https://raw.githubusercontent.com/molamilan89-gif/toro-libya/main/1000105722.jpg" class="logo-img">
    </div>
    <div class="sub-title">
        🐂 تورو ليبيا: وجهتك الاقتصادية الأولى والوحيدة في ليبيا ..
    </div>
    <div class="legend-text">THE LEGEND OF LIBYAN MARKET</div>
    """, unsafe_allow_html=True)

# 4. شبكة الأسعار (USD, GOLD, BTC)
st.markdown(f"""
    <div class="price-grid">
        <div class="price-box">
            <div class="label">USD</div>
            <div class="value">8.61</div>
        </div>
        <div class="price-box">
            <div class="label">GOLD 18</div>
            <div class="value">415.5</div>
        </div>
        <div class="price-box">
            <div class="label">BTC</div>
            <div class="value">96.5K</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 5. قسم نبض السوق والتوصيات
st.markdown('<div class="market-container">', unsafe_allow_html=True)
st.markdown('<div class="market-header">🌟 | نبض السوق والتوصيات</div>', unsafe_allow_html=True)

st.markdown("""
    <div class="status-row">
        <span>حالة الاستقرار</span>
        <span style="color:#00ffff;">75% مستقر</span>
    </div>
    """, unsafe_allow_html=True)
st.progress(75)

# 6. الرسم البياني لمؤشر السعر
df = pd.DataFrame({
    'date': ['1', '2', '3', '4', '5', '6', '7', '8'],
    'price': [15, 12, 18, 16, 25, 30, 60, 75] # بيانات تحاكي شكل الرسم في الصورة
})

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df['date'], 
    y=df['price'],
    mode='lines',
    line=dict(color='#00ffff', width=3),
    fill='tozeroy',
    fillcolor='rgba(0, 255, 255, 0.1)'
))

fig.update_layout(
    title=dict(text="USD/LYD Price Trend", font=dict(color="white", size=14)),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=0, r=0, t=30, b=0),
    height=200,
    xaxis=dict(visible=False),
    yaxis=dict(showgrid=True, gridcolor='#242f3d', font=dict(color="#55606e"))
)

st.plotly_chart(fig, use_container_width=True)

# 7. زر التواصل
st.button("💬 تواصل مع الإدارة عبر واتساب")

st.markdown('</div>', unsafe_allow_html=True)
