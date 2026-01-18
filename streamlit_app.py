import streamlit as st
import datetime

# إعدادات الصفحة الاحترافية
st.set_page_config(page_title="TORO LY | تورو ليبيا", page_icon="🐂", layout="centered")

# التنسيق البصري (CSS) ليصبح مثل التطبيقات العالمية
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; direction: rtl; }
    .main-title { text-align: center; font-size: 3em; font-weight: bold; color: #00d4ff; margin-bottom: 0px; }
    .sub-title { text-align: center; color: #888; margin-bottom: 30px; }
    .card {
        background: linear-gradient(145deg, #1a1c24, #14161d);
        padding: 25px; border-radius: 20px;
        border-right: 6px solid #00d4ff; margin-bottom: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .price-row { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #2d3139; }
    .price-label { font-size: 1.1em; color: #ddd; }
    .price-value { font-size: 1.2em; color: #4caf50; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# اللوجو والعنوان الاحترافي
st.markdown("<div class='main-title'>TORO <span style='color:white'>LY</span> 🐂</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>المؤشر الاقتصادي الليبي المتكامل</div>", unsafe_allow_html=True)

# دالة عرض البيانات في بطاقات
def create_card(title, emoji, items):
    st.markdown(f"""
    <div class="card">
        <h2 style="margin-top:0;">{emoji} {title}</h2>
    """, unsafe_allow_html=True)
    for label, price in items.items():
        st.markdown(f"""
        <div class="price-row">
            <span class="price-label">{label}</span>
            <span class="price-value">{price}</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# 1. قسم العملات والذهب
create_card("العملات والذهب", "💵", {
    "🇺🇸 دولار موازي": "8.65",
    "🇪🇺 يورو موازي": "9.12",
    "✨ ذهب كسر (18)": "415.5"
})

# 2. قسم الطاقة
create_card("الطاقة والنفط", "⛽", {
    "🛢️ خام برنت": "$78.40",
    "🔥 غاز الطهي": "5.00 LYD"
})

# 3. حاسبة تحويل العملة المتطورة
st.markdown("<br><h3 style='text-align:right;'>🔄 حاسبة تحويل العملة (دولار/دينار)</h3>", unsafe_allow_html=True)
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        usd_amount = st.number_input("المبلغ بالدولار ($):", min_value=0.0, value=1.0, step=1.0)
    with col2:
        lyd_price = 8.65  # سعر الصرف الافتراضي
        total = usd_amount * lyd_price
        st.metric(label="القيمة بالدينار الليبي", value=f"{total:,.2f} LYD")

st.markdown(f"<p style='text-align: center; color: #555; margin-top: 50px;'>آخر تحديث: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}</p>", unsafe_allow_html=True)
