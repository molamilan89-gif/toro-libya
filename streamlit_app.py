import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(
    page_title="Toro Libya | تورو ليبيا",
    page_icon="🐂",
    layout="centered"
)

# CSS مخصص لمحاكاة التصميم الذي في الصورة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif;
        direction: rtl;
        text-align: right;
        background-color: #0e1117;
    }
    
    /* تنسيق الحاوية الرئيسية */
    .main-container {
        background-color: #0e1117;
        padding: 20px;
        border-radius: 15px;
    }

    /* تنسيق اللوجو */
    .logo-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .logo-img {
        width: 150px;
        border-radius: 20px;
        box-shadow: 0px 4px 15px rgba(0, 255, 255, 0.3);
    }

    /* شريط العنوان المتحرك */
    .scrolling-ticker {
        background: linear-gradient(90deg, #004d4d, #008080);
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 25px;
        border: 1px solid #00ffff;
        font-weight: bold;
    }

    /* بطاقات الأسعار */
    .price-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(0, 255, 255, 0.2);
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        transition: 0.3s;
    }
    .price-card:hover {
        border-color: #00ffff;
        transform: translateY(-5px);
    }
    .price-label { color: #888; font-size: 0.8rem; }
    .price-value { color: #ffffff; font-size: 1.5rem; font-weight: bold; }

    /* صندوق نبض السوق */
    .market-pulse-card {
        background: rgba(0, 20, 30, 0.6);
        border: 2px solid #00ffff;
        border-radius: 20px;
        padding: 20px;
        margin-top: 30px;
    }
    
    /* شريط الاستقرار */
    .st-progress-bar > div > div {
        background-color: #00ffff;
    }

    </style>
    """, unsafe_allow_html=True)

# --- الهيدر واللوجو ---
st.markdown(f"""
    <div class="logo-container">
        <img src="https://i.ibb.co/XfXfXfX/toro-logo.png" class="logo-img"> 
    </div>
    <div class="scrolling-ticker">
        📢 تورو ليبيا: وجهتك الاقتصادية الأولى والوحيدة لمتابعة سوق المشير لحظة بلحظة ..
    </div>
    <div style="text-align: center; color: #555; font-size: 0.7rem; letter-spacing: 2px; margin-bottom: 20px;">
        THE LEGEND OF LIBYAN MARKET
    </div>
    """, unsafe_allow_html=True)

# --- عرض الأسعار ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="price-card"><div class="price-label">USD</div><div class="price-value">8.61</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="price-card"><div class="price-label">GOLD 18</div><div class="price-value">415.5</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="price-card"><div class="price-label">BTC</div><div class="price-value">96.5K</div></div>', unsafe_allow_html=True)

# --- نبض السوق والتوصيات ---
st.markdown('<div class="market-pulse-card">', unsafe_allow_html=True)
st.markdown("<h3 style='color:#00ffff;'>🌟 | نبض السوق والتوصيات</h3>", unsafe_allow_html=True)

col_info1, col_info2 = st.columns([1, 1])
with col_info1:
    st.write("حالة الاستقرار")
with col_info2:
    st.markdown("<p style='color:#00ffff; text-align:left;'>75% مستقر</p>", unsafe_allow
                
