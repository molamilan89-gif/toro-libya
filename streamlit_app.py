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
        border-radius: 20px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 15px;
    }
    
    .price-text { font-size: 1.5em; color: #00d4ff; font-weight: bold; }
    .section-title { border-right: 5px solid #00d4ff; padding-right: 15px; margin-bottom: 20px; color: #fff; }
    
    /* تنسيق الحاسبة البسيط */
    .calc-container {
        background: #1a1c24;
        padding: 25px;
        border-radius: 25px;
        border: 2px solid #00d4ff;
        text-align: center;
    }
    .result-box {
        font-size: 2.2em;
        color: #4caf50;
        font-weight: bold;
        margin-top: 15px;
        padding: 10px;
        background: rgba(76, 175, 80, 0.1);
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- الهيدر ---
st.markdown("<h1 style='text-align: center; color: #00d4ff; font-size: 3em;'>TORO <span style='color:#fff'>LY</span> PRO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>المؤشر الاقتصادي الليبي - النسخة الاحترافية</p>", unsafe_allow_html=True)

# --- عرض البيانات السريع ---
def display_simple_card(title, icon, data):
    st.markdown(f"<h3 class='section-title'>{icon} {title}</h3>", unsafe_allow_html=True)
    cols = st.columns(len(data))
    for i, (label, price) in enumerate(data.items()):
        with cols[i]:
            st.markdown(f"<div class='main-card' style='text-align:center;'><small>{label}</small><br><span class='price-text'>{price}</span></div>", unsafe_allow_html=True)

display_simple_card("العملات والذهب", "💵", {"دولار": "8.65", "يورو": "9.12", "ذهب 18": "415.5"})

# --- الحاسبة "التوربو" المبسطة (طلبك يا أسطورة) ---
st.markdown("---")
st.markdown("<h3 class='section-title'>🔄 حاسبة التحويل السريع</h3>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="calc-container">', unsafe_allow_html=True)
    
    # اختيار العملية ببساطة
    option = st.radio("ماذا تريد أن تفعل؟", ["تحويل من دولار إلى دينار", "تحويل من دينار إلى دولار"], horizontal=True)
    
    # إدخال المبلغ
    amount = st.number_input("أدخل المبلغ هنا:", min_value=0.0, value=1.0, step=1.0)
    
    # سعر الصرف الثابت (يمكنك تعديله مستقبلاً)
    rate = 8.65
    
    if option == "تحويل من دولار إلى دينار":
        total = amount * rate
        st.markdown(f'<div class="result-box">{total:,.2f} ل.د</div>', unsafe_allow_html=True)
    else:
        total = amount / rate
        st.markdown(f'<div class="result-box">${total:,.2f}</div>', unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

# --- الفوتر ---
st.markdown("<br><p style='text-align: center; color: #555; font-size: 0.8em;'>آخر تحديث: " + datetime.datetime.now().strftime('%H:%M') + "</p>", unsafe_allow_html=True)
