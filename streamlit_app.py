import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="Toro Libya | تورو ليبيا",
    page_icon="🐂",
    layout="centered"
)

# 2. التنسيق الجمالي (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif;
        direction: rtl;
        text-align: right;
        background-color: #0e1117;
    }

    .logo-container {
        display: flex;
        justify-content: center;
        margin-bottom: 25px;
    }
    .logo-img {
        width: 180px;
        border-radius: 20px;
        border: 2px solid #00ffff;
        box-shadow: 0px 0px 20px rgba(0, 255, 255, 0.4);
    }

    .scrolling-ticker {
        background: linear-gradient(90deg, #004d4d, #008080);
        color: white;
        padding: 12px;
        border-radius: 10px;
        margin-bottom: 20px;
        border: 1px solid #00ffff;
        text-align: center;
        font-weight: bold;
    }

    .price-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(0, 255, 255, 0.2);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        margin-bottom: 10px;
    }
    .price-label { color: #888; font-size: 0.9rem; margin-bottom: 5px; }
    .price-value { color: #ffffff; font-size: 1.6rem; font-weight: bold; }

    .market-pulse-card {
        background: rgba(0, 20, 30, 0.7);
        border: 2px solid #00ffff;
        border-radius: 20px;
        padding: 25px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. عرض اللوجو الجديد (رأس الثور)
# تأكد أن ملف الصورة 1000105722.jpg موجود في مستودع GitHub الخاص بك
st.markdown(f"""
    <div class="logo-container">
        <img src="https://raw.githubusercontent.com/molamilan89-gif/toro-libya/main/1000105722.jpg" class="logo-img">
    </div>
    <div class="scrolling-ticker">
        🐂 تورو ليبيا: وجهتك الاقتصادية الأولى والوحيدة في ليبيا ..
    </div>
    <p style="text-align: center; color: #555; font-size: 0.8rem; letter-spacing: 2px; margin-bottom: 30px;">
        THE LEGEND OF LIBYAN MARKET
    </p>
    """, unsafe_allow_html=True)

# 4. عرض أسعار العملات
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="price-card"><div class="price-label">USD</div><div class="price-value">8.61</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="price-card"><div class="price-label">GOLD 18</div><div class="price-value">415.5</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="price-card"><div class="price-label">BTC</div><div class="price-value">96.4K</div></div>', unsafe_allow_html=True)

# 5. قسم نبض السوق
st.markdown('<div class="market-pulse-card">', unsafe_allow_html=True)
st.markdown("<h3 style='color:#00ffff; text-align:right;'>🌟 | نبض السوق والتوصيات</h3>", unsafe_allow_html=True)

c1, c2 = st.columns([1, 1])
with c1: st.write("حالة الاستقرار")
with c2: st.markdown("<p style='color:#00ffff; text-align:left;'>75% مستقر</p>", unsafe_allow_html=True)
st.progress(75)

st.warning("⚠️ جاري تحليل أحدث رسائل الواتساب الواردة من الغرفة الموثوقة...")

# 6. الرسم البياني التفاعلي
df_chart = pd.DataFrame({
    'التاريخ': ['الأحد', 'الإثنين', 'الثلاثاء', 'الأربعاء', 'الخميس'],
    'السعر': [8.45, 8.52, 8.48, 8.58, 8.61]
})

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df_chart['التاريخ'], 
    y=df_chart['السعر'],
    mode='lines+markers',
    line=dict(color='#00ffff', width=3),
    fill='tozeroy',
    fillcolor='rgba(0, 255, 255, 0.1)'
))

fig.update_layout(
    title="مؤشر سعر الدولار USD/LYD",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color="white"),
    margin=dict(l=0, r=0, t=40, b=0),
    height=300,
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False)
)

st.plotly_chart(fig, use_container_width=True)

st.button("💬 تواصل مع الإدارة عبر واتساب", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# تذييل الصفحة
st.markdown("<br><p style='text-align:center; color:#444;'>تطوير أسطورة © 2026</p>", unsafe_allow_html=True)
