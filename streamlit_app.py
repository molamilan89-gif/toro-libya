import streamlit as st
import datetime

# --- إعدادات النظام العالمي ---
st.set_page_config(page_title="TORO LY PRO | تورو ليبيا المطور", page_icon="👑", layout="centered")

# --- محرك التنسيق البصري (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Tajawal', sans-serif; direction: rtl; }
    .stApp { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); color: white; }
    
    .main-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 25px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }
    .main-card:hover { transform: translateY(-5px); border-color: #00d4ff; }
    
    .status-badge {
        padding: 5px 15px; border-radius: 50px; font-size: 0.8em; font-weight: bold;
        background: #4caf50; color: white; float: left;
    }
    
    .price-text { font-size: 1.4em; color: #00d4ff; font-weight: bold; }
    .label-text { color: #ccc; font-size: 1em; }
    .section-title { border-right: 4px solid #00d4ff; padding-right: 15px; margin-bottom: 20px; color: #fff; }
    </style>
    """, unsafe_allow_html=True)

# --- الهيدر الأسطوري ---
st.markdown("<h1 style='text-align: center; color: #00d4ff; font-size: 3.5em; margin-bottom:0;'>TORO <span style='color:#fff'>LY</span> PRO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; margin-top:0;'>الجيل القادم من المؤشرات الاقتصادية الليبية</p>", unsafe_allow_html=True)
st.markdown("---")

# --- قسم: نبض السوق (قسم غير موجود في المواقع الأخرى) ---
col_s1, col_s2, col_s3 = st.columns(3)
with col_s1:
    st.markdown("<div class='main-card' style='text-align:center;'>🌡️ نبض السوق<br><b style='color:#4caf50'>مستقر نسبياً</b></div>", unsafe_allow_html=True)
with col_s2:
    st.markdown("<div class='main-card' style='text-align:center;'>📊 الطلب<br><b style='color:#ff9800'>متوسط</b></div>", unsafe_allow_html=True)
with col_s3:
    st.markdown("<div class='main-card' style='text-align:center;'>📉 العرض<br><b style='color:#00d4ff'>وفير</b></div>", unsafe_allow_html=True)

# --- دالة صنع البطاقات الأسطورية ---
def display_pro_card(title, icon, data_dict):
    st.markdown(f"<h3 class='section-title'>{icon} {title}</h3>", unsafe_allow_html=True)
    with st.container():
        for label, price in data_dict.items():
            st.markdown(f"""
            <div class="main-card">
                <span class="label-text">{label}</span>
                <span class="price-text" style="float:left;">{price}</span>
            </div>
            """, unsafe_allow_html=True)

# --- الأقسام المبتكرة ---
col1, col2 = st.columns(2)

with col1:
    display_pro_card("العملات العالمية", "🏦", {
        "🇺🇸 دولار موازي": "8.65",
        "🇪🇺 يورو موازي": "9.12",
        "🇬🇧 استرليني": "10.45"
    })
    
    display_pro_card("الكريبتو و USDT", "🪙", {
        "₿ Bitcoin": "$96,400",
        "💎 Solana": "$210.5",
        "💵 USDT/LYD": "8.68"
    })

with col2:
    display_pro_card("المعادن والذهب", "✨", {
        "🟡 كسر 18": "415.5",
        "🟠 كسر 24": "554.0",
        "⚪ فضة خام": "5.20"
    })
    
    display_pro_card("مواد البناء", "🧱", {
        "🏗️ حديد (طن)": "4100",
        "⚪ إسمنت (قنطار)": "45.0"
    })

# --- الحاسبة المتطورة (UI التفاعلي) ---
st.markdown("<br><h3 class='section-title'>🔄 المحول الذكي (دولار ⇆ دينار)</h3>", unsafe_allow_html=True)
with st.container():
    calc_col1, calc_col2 = st.columns([2, 1])
    with calc_col1:
        val = st.number_input("أدخل المبلغ:", min_value=0.0, value=1.0, step=10.0)
    with calc_col2:
        mode = st.selectbox("النوع:", ["من دولار إلى ليبي", "من ليبي إلى دولار"])
    
    rate = 8.65
    if mode == "من دولار إلى ليبي":
        result = val * rate
        st.success(f"النتيجة: {result:,.2f} دينار ليبي")
    else:
        result = val / rate
        st.info(f"النتيجة: {result:,.2f} دولار أمريكي")

# --- الفوتر (التذييل) ---
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #555;'>تطوير أسطورة | TORO LY PRO © {datetime.datetime.now().year}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #444; font-size:0.8em;'>آخر تحديث للبيانات: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}</p>", unsafe_allow_html=True)
