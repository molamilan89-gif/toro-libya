import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="Toro Libya", page_icon="🐂", layout="centered")

# 2. تصميم CSS احترافي (لتحسين المظهر العام وإخفاء عناصر Streamlit الزائدة)
st.markdown("""
    <style>
    .main { background-color: #0b1120; }
    /* تنسيق اللوجو ليكون في المنتصف وبحدود مضيئة */
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
        border: 2px solid #22d3ee;
        border-radius: 30px;
        box-shadow: 0 0 25px rgba(34, 211, 238, 0.4);
        margin: 20px auto;
        width: 180px;
        padding: 0;
        background: #1e293b;
    }
    img { border-radius: 28px; }
    
    /* تنسيق كروت الأسعار */
    .price-box {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        margin: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. شريط الإعلانات العلوي
st.info("📢 تورو ليبيا: وجهتك الاقتصادية الأولى والوحيدة في ليبيا .. 🐂 تحديثات فورية")

# 4. عرض اللوجو (استخدام الرابط المباشر الخام لضمان التوافق)
# تأكد أن اسم الملف في GitHub هو 1000105722.jpg تماماً
logo_url = "https://raw.githubusercontent.com/molamilan89-gif/toro-libya/main/1000105722.jpg"
st.image(logo_url, width=180)

# 5. اسم البراند والشعار اللفظي
st.markdown("""
    <div style="text-align: center; margin-top: -10px;">
        <h1 style="color: white; font-size: 42px; font-weight: 900; letter-spacing: 4px; margin: 0;">TORO <span style="color: #22d3ee;">LY</span></h1>
        <p style="color: #64748b; font-size: 11px; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 30px;">THE LEGEND OF LIBYAN MARKET</p>
    </div>
    """, unsafe_allow_html=True)

# 6. شبكة الأسعار (3 أعمدة متساوية)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="price-box"><span style="color: #94a3b8; font-size: 12px;">USD</span><br><span style="color: #22d3ee; font-size: 22px; font-weight: bold;">8.65</span></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="price-box"><span style="color: #94a3b8; font-size: 12px;">GOLD 18</span><br><span style="color: #eab308; font-size: 22px; font-weight: bold;">415.5</span></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="price-box"><span style="color: #94a3b8; font-size: 12px;">BTC</span><br><span style="color: #22c55e; font-size: 22px; font-weight: bold;">96.4K</span></div>', unsafe_allow_html=True)

# 7. قسم نبض السوق والتوصيات
st.markdown("""
    <div style="background: #111827; border: 1px solid #22d3ee; border-radius: 20px; padding: 25px; margin-top: 30px; text-align: right; direction: rtl;">
        <h3 style="color: #22d3ee; margin-top: 0; font-size: 20px;">🌟 نبض السوق والتوصيات</h3>
        <p style="color: white; font-size: 15px; margin-bottom: 12px;">حالة الاستقرار: <span style="color: #22d3ee; font-weight: bold;">75% مستقر</span></p>
        <div style="width: 100%; height: 8px; background: #334155; border-radius: 10px; margin-bottom: 20px;">
            <div style="width: 75%; height: 100%; background: linear-gradient(90deg, #22d3ee, #06b6d4); border-radius: 10px;"></div>
        </div>
        <p style="font-size: 12px; color: #94a3b8;">⚠️ يتم الآن تحليل أحدث البيانات الواردة من غرف الواتساب الموثوقة للتحديث اللحظي...</p>
        <hr style="border: 0.5px solid rgba(34, 211, 238, 0.2); margin: 20px 0;">
        <div style="text-align: center;">
            <a href="https://wa.me/218XXXXXXXXX" style="text-decoration: none; background: rgba(34, 211, 238, 0.1); color: #22d3ee; border: 1px solid #22d3ee; padding: 10px 30px; border-radius: 10px; font-weight: bold;">تواصل مع الإدارة 💬</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<p style="text-align: center; color: #475569; font-size: 10px; margin-top: 60px; letter-spacing: 2px;">TORO LIBYA © 2026 | ALL RIGHTS RESERVED</p>', unsafe_allow_html=True)
