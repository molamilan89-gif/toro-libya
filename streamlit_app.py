import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="Toro Libya - منصة وول ستريت ليبيا", page_icon="🐂", layout="centered")

# 2. تنسيق الألوان والتصميم (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap');
    
    html, body, [class*="css"] { font-family: 'Tajawal', sans-serif; direction: rtl; }
    .stApp { background: #0b1120; color: white; }
    
    /* شريط الأخبار المباشر */
    .ticker-wrap {
        width: 100%; background: rgba(8, 51, 68, 0.9); border-bottom: 1px solid #22d3ee;
        padding: 10px 0; position: fixed; top: 0; left: 0; z-index: 999;
    }
    .ticker { display: inline-block; white-space: nowrap; animation: marquee 30s linear infinite; color: #22d3ee; font-weight: bold; }
    @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

    .glass-card {
        background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px;
        padding: 20px; margin-bottom: 20px;
    }
    .section-title { border-right: 4px solid #22d3ee; padding-right: 12px; margin-bottom: 15px; font-weight: 900; color: #22d3ee; }
    .price-item { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
    .price-val { font-weight: bold; color: #22d3ee; }
    
    /* تعديل خانات الإدخال لتظهر الأرقام إنجليزية */
    input { font-family: sans-serif !important; text-align: center !important; font-size: 1.2rem !important; }
    </style>
    
    <div class="ticker-wrap">
        <div class="ticker">
            📢 عاجل: Toro Libya يطلق التحديث الشامل لأسعار الذهب والعملات .. 🛢️ خام برنت مستقر عند 78.40$ .. 🏗️ أسعار الإسمنت والحديد اليوم في ليبيا .. 🐂 منصة تورو ليبيا: المؤشر الاقتصادي الأول في البلاد ..
        </div>
    </div>
    """, unsafe_allow_html=True)

# 3. الهيدر واللوجو
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 3.5rem; font-weight: 900; margin-bottom:0;'>TORO <span style='color: #22d3ee;'>LY</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.8rem; letter-spacing: 2px;'>المؤشر الاقتصادي الليبي المتكامل</p>", unsafe_allow_html=True)

# 4. عرض الأقسام بجمالية الـ Glassmorphism
def display_section(title, icon, data):
    st.markdown(f"""
    <div class="glass-card">
        <h2 class="section-title">{icon} {title}</h2>
    """, unsafe_allow_html=True)
    for label, val in data.items():
        st.markdown(f"""
        <div class="price-item">
            <span>{label}</span>
            <span class="price-val">{val}</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# توزيع الأقسام
display_section("العملات والذهب", "💵", {"🇺🇸 دولار موازي": "8.65", "🇪🇺 يورو موازي": "9.12", "✨ ذهب كسر (18)": "415.5"})
display_section("العملات الرقمية", "🪙", {"₿ Bitcoin": "$96,430", "💠 Solana": "$195.20"})
display_section("الطاقة ومواد البناء", "🏗️", {"🛢️ خام برنت": "$78.40", "🧱 إسمنت": "45.00", "⛓️ حديد": "4100"})
display_section("السلع الأساسية", "🛒", {"🌻 زيت": "7.50", "🍚 أرز": "5.00"})

# 5. الحاسبة الذكية (بايثون 100% - بدون أخطاء)
st.markdown("<div class='glass-card' style='border: 2px solid #22d3ee;'>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #22d3ee; font-size: 0.9rem;'>🔄 محول العملات الذكي</h3>", unsafe_allow_html=True)

rate_usd = 8.65
rate_eur = 9.12

# استخدام أعمدة الحاسبة
col_lyd = st.number_input("المبلغ بالدينار الليبي:", min_value=0.0, step=1.0, key="lyd_input", format="%.2f")

c1, c2 = st.columns(2)
with c1:
    res_usd = col_lyd / rate_usd if col_lyd > 0 else 0.0
    st.metric("يعادل بالدولار $", f"{res_usd:,.2f}")
with c2:
    res_eur = col_lyd / rate_eur if col_lyd > 0 else 0.0
    st.metric("يعادل باليورو €", f"{res_eur:,.2f}")

st.markdown("</div>", unsafe_allow_html=True)

# الفوتر
st.markdown("<p style='text-align: center; color: #444; margin-top: 50px;'>Toro Ly Pro © 2026</p>", unsafe_allow_html=True)
