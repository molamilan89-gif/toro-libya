import streamlit as st
import datetime

# إعدادات الواجهة
st.set_page_config(page_title="TORO LY", page_icon="📊", layout="centered")

# تصميم مطابق للفيديو
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; direction: rtl; }
    .card {
        background-color: #1a1c24; padding: 20px; border-radius: 15px;
        border-right: 5px solid #00d4ff; margin-bottom: 10px;
    }
    .price-val { color: #4caf50; float: left; font-weight: bold; font-size: 1.2em; }
    .title-text { text-align: center; font-size: 2.5em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='title-text'>TORO <span style='color:#00d4ff'>LY</span></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>المؤشر الاقتصادي الليبي المتكامل</p>", unsafe_allow_html=True)

# دالة لإنشاء البطاقات
def make_card(name, items):
    st.markdown(f'<div class="card"><h3>{name}</h3>', unsafe_allow_html=True)
    for label, price in items.items():
        st.markdown(f'<div>{label} <span class="price-val">{price}</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# عرض البيانات
make_card("💵 العملات والذهب", {"دولار موازي": "8.65", "يورو موازي": "9.12", "ذهب كسر (18)": "415.5"})
make_card("⛽ الطاقة والنفط", {"خام برنت": "$78.40", "غاز الطهي": "5.00 LYD"})

# حاسبة بسيطة
st.markdown("<br>", unsafe_allow_html=True)
val = st.number_input("أدخل القيمة بالدولار لنحولها لك بالدينار:", value=1.0)
st.success(f"تساوي حالياً: {val * 8.65:.2f} دينار ليبي")

st.write(f"آخر تحديث: {datetime.datetime.now().strftime('%H:%M')}")

