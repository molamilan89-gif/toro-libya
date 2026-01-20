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

# 2. التنسيق الجمالي (CSS) لمحاكاة التصميم المطلوب
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif;
        direction: rtl;
        text-align: right;
        background-color: #0e1621;
    }

    .logo-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .logo-img {
        width: 250px;
        border-radius: 15px;
        border: 2px solid #00ffff;
        box-shadow: 0px 4px 20px rgba(0, 255, 255, 0.3);
    }

    .sub-title {
        text-align: center;
        color: #00ffff;
        background: rgba(0, 255, 255, 0.05);
        padding: 10px;
        border-radius: 10px;
        border: 1px solid rgba(0, 255, 255, 0.2);
        margin-bottom: 5px;
    }

    .legend-text {
        text-align: center;
        color: #55606e;
        font-size: 0.7rem;
        letter-spacing: 2px;
        margin-bottom: 25px;
    }

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
        border-bottom: 3px solid #00ffff;
    }
    .label { color: #808d9a; font-size: 0.8rem; }
    .value { color: #ffffff; font-size: 1.3rem; font-weight: bold; margin-top: 5px; }

    .market-container {
        background: #17212b;
        border: 1px solid #00ffff;
        border-radius: 20px;
        padding: 20px;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. عرض اللوجو الرئيسي (تم تصحيح الرابط)
st.markdown(f"""
    <div class="logo-container">
        <img src="https://raw.githubusercontent.com/molamilan89-gif/toro-libya/main/1000105722.jpg" class="logo-img">
    </div>
    <div class="sub-title">
        أ .. 🐂 تورو ليبيا: وجهتك الاقتصادية الأولى والوحيدة ..
    </div>
    <div class="legend-text">THE LEGEND OF LIBYAN MARKET</div>
    """, unsafe_allow_html=True)

# 4. شبكة الأسعار
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
st.markdown("<h3 style='color:#00ffff; text-align:right;'>🌟 | نبض السوق والتوصيات</h3>", unsafe_allow_html=True)

col_a, col_b = st.columns([1, 1])
with col_a: st.write("حالة الاستقرار")
with col_b: st.markdown("<p style='color:#00ffff; text-align:left;'>75% مستقر</p>", unsafe_allow_html=True)
st.progress(75)

# 6. الرسم البياني (تم تصحيح الخطأ البرمجي هنا)
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5, 6, 7],
    'y': [10, 15, 13, 20, 25, 40, 65]
})

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df['x'], 
    y=df['y'],
    mode='lines+markers',
    line=dict(color='#00ffff', width=3),
    fill='tozeroy',
    fillcolor='rgba(0, 255, 255, 0.1)'
))

fig.update_layout(
    title={"text": "USD/LYD Price Trend", "font": {"color": "white", "size": 14}},
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font={"color": "#55606e"},
    margin=dict(l=0, r=0, t=40, b=0),
    height=250,
    xaxis=dict(showgrid=False, visible=False),
    yaxis=dict(showgrid=True, gridcolor='#242f3d')
)

st.plotly_chart(fig, use_container_width=True)

# 7. زر التواصل
if st.button("💬 تواصل مع الإدارة عبر واتساب"):
    st.write("جاري التحويل...")

st.markdown('</div>', unsafe_allow_html=True)
