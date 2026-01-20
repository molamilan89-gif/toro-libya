import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Toro Libya", page_icon="🐂", layout="centered")

# 2. تنسيق الخلفية والعناصر العامة (CSS)
st.markdown("""
    <style>
    .main { background-color: #0b1120; }
    div[data-testid="stVerticalBlock"] > div:has(div.stImage) {
        text-align: center;
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    /* تحسين شكل الصورة لتظهر كلوجو احترافي */
    img {
        border-radius: 25px;
        border: 2px solid #22d3ee;
        box-shadow: 0 0 20px rgba(34, 211, 238, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. عرض شريط الإعلانات في الأعلى
st.info("📢 تورو ليبيا: وجهتك الاقتصادية الأولى والوحيدة في ليبيا .. 🐂 تحديثات فورية")

# 4. عرض اللوجو باستخدام أداة Streamlit الرسمية (لضمان الظهور 100%)
logo_url = "https://raw.githubusercontent.com/molamilan89-gif/toro-libya/main/1000105722.jpg"
st.image(logo_url, width=180)

# 5. العنوان والوصف
st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <h1 style="color: white; font-size: 40px; font-weight: 900; letter-spacing: 3px; margin: 0;">TORO <span style="color: #22d3ee;">LY</span></h1>
        <p style="color: #64748b; font-size: 11px; text-transform: uppercase; letter-spacing: 2px;">THE LEGEND OF LIBYAN MARKET</p>
    </div>
    """, unsafe_allow_html=True)

# 6. كروت الأسعار (باستخدام أعمدة Streamlit لتوافق أفضل)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div style="background: rgba(30,41,59,0.7); padding: 15px; border-radius: 15px; text-align: center; border: 1px solid rgba(255,255,255,0.05);"><span style="color: #94a3b8; font-size: 12px;">USD</span><br><span style="color: #22d3ee; font-size: 20px; font-weight: bold;">8.65</span></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div style="background: rgba(30,41,59,0.7); padding: 15px; border-radius: 15px; text-align: center; border: 1px solid rgba(255,255,255,0.05);"><span style="color: #94a3b8; font-size: 12px;">GOLD 18</span><br><span style="color: #eab308; font-size: 20px; font-weight: bold;">415.5</span></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div style="background: rgba(30,41,59,0.7); padding: 15px; border-radius: 15px; text-align: center; border: 1px solid rgba(255,255,255,0.05);"><span style="color: #94a3b8; font-size: 12px;">BTC</span><br><span style="color: #22c55e; font-size: 20px; font-weight: bold;">96.4K</span></div>', unsafe_allow_html=True)

# 7. قسم نبض السوق والتوصيات
st.markdown("""
    <div style="background: #111827; border: 1px solid #22d3ee; border-radius: 20px; padding: 20px; margin-top: 30px; text-align: right; direction: rtl;">
        <h3 style="color: #22d3ee; margin-top: 0; font-size: 18px;">🌟 نبض السوق والتوصيات</h3>
        <p style="color: white; font-size: 14px; margin-bottom: 10px;">حالة الاستقرار: <span style="color: #22d3ee;">75% مستقر</span></p>
        <div style="width: 100%; height: 6px; background: #334155; border-radius: 10px;">
            <div style="width: 75%; height: 100%; background: #22d3ee; border-radius: 10px;"></div>
        </div>
        <p style="font-size: 11px; color: #94a3b8; margin-top: 15px;">⚠️ جاري تحليل أحدث رسائل الواتساب الواردة من الغرفة الموثوقة...</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<p style="text-align: center; color: #475569; font-size: 10px; margin-top: 50px;">TORO LIBYA © 2026</p>', unsafe_allow_html=True)
