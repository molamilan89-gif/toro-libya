import streamlit as st
import datetime

# --- إعدادات النظام ---
st.set_page_config(page_title="TORO LY PRO", page_icon="🐂", layout="centered")

# --- محرك التنسيق البصري (الألوان كما في الصور السابقة) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Tajawal', sans-serif; direction: rtl; }
    .stApp { background-color: #0e1117; color: white; }
    
    /* شريط الأخبار المتحرك */
    .ticker-wrapper {
        width: 100%; overflow: hidden; background-color: #1a1c24; 
        border-bottom: 2px solid #00d4ff; padding: 10px 0; margin-bottom: 20px;
    }
    .ticker-text {
        display: inline-block; white-space: nowrap; animation: ticker 25s linear infinite;
        font-size: 1.1em; color: #00d4ff; font-weight: bold;
    }
    @keyframes ticker {
        0% { transform: translateX(100%); }
        100% { transform: translateX(-100%); }
    }

    .main-card {
        background: #1a1c24; border-radius: 20px; padding: 20px;
        border-right: 6px solid #00d4ff; margin-bottom: 15px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.4);
    }
    .price-row { display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #2d3139; }
    .price-val { color: #4caf50; font-weight: bold; font-size: 1.2em; }
    
    /* الحاسبة المبسطة جداً */
    .simple-calc {
        background: #1a1c24; padding: 20px; border-radius: 20px;
        border: 1px solid #444; margin-top: 20px; text-align: center;
    }
    .res-box { font-size: 2.5em; color: #00d4ff; font-weight: bold; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. شريط الأخبار المباشر ---
st.markdown("""
    <div class="ticker-wrapper">
        <div class="ticker-text">
            ⚠️ عاجل: استقرار في سعر صرف الدولار الموازي اليوم في طرابلس وبنغازي .. 📉 هبوط طفيف في أسعار الذهب الكسر عيار 18 .. 🧱 استقرار أسعار مواد البناء في المنطقة الغربية .. ⛽ توفر غاز الطهي في معظم مراكز التوزيع ..
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 2. الهيدر ---
st.markdown("<h1 style='text-align: center; color: #00d4ff;'>TORO <span style='color:white'>LY</span> PRO 🐂</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>المؤشر الاقتصادي الليبي الشامل</p>", unsafe_allow_html=True)

# --- 3. عرض الأقسام (كما طلبتها) ---
def create_section(title, icon, items):
    st.markdown(f"<div class='main-card'><h3>{icon} {title}</h3>", unsafe_allow_html=True)
    for label, val in items.items():
        st.markdown(f"<div class='price-row'><span>{label}</span><span class='price-val'>{val}</span></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    create_section("العملات", "💵", {"دولار موازي": "8.65", "يورو موازي": "9.12", "دولار رسمي": "4.85"})
    create_section("مواد البناء", "🏗️", {"إسمنت (قنطار)": "45.00", "حديد 12 (طن)": "4100"})
with col2:
    create_section("الذهب", "✨", {"كسر 18": "415.5", "كسر 24": "554.0", "ليرة ذهب": "3340"})
    create_section("الطاقة", "⛽", {"خام برنت": "$78.40", "غاز طهي": "5.00"})

# --- 4. الحاسبة الأسطورية المبسطة ---
st.markdown("---")
st.markdown("<h2 style='text-align: center;'>🔄 المحول السريع</h2>", unsafe_allow_html=True)
st.markdown('<div class="simple-calc">', unsafe_allow_html=True)

# اختيار بسيط للمستخدم
mode = st.radio("اختر نوع التحويل:", ["من دولار إلى ليبي", "من ليبي إلى دولار"], horizontal=True)
amount = st.number_input("أدخل المبلغ:", min_value=0.0, value=1.0, step=1.0)

rate = 8.65
if "إلى ليبي" in mode:
    result = amount * rate
    st.markdown(f'<div class="res-box">{result:,.2f} ل.د</div>', unsafe_allow_html=True)
else:
    result = amount / rate
    st.markdown(f'<div class="res-box">${result:,.2f}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- الفوتر ---
st.markdown(f"<p style='text-align: center; color: #555; margin-top: 40px;'>آخر تحديث: {datetime.datetime.now().strftime('%H:%M')} | TORO LY</p>", unsafe_allow_html=True)
