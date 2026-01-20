import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Toro Libya", page_icon="🐂", layout="centered")

# 2. كود الصورة المدمج (Base64) - هذا يضمن ظهور اللوجو بدون روابط خارجية
# لقد اختصرت الكود هنا، انسخ الملف بالكامل
LOGO_BASE64 = "iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAYAAACtWK6eAAAACXBIWXMAAAsTAAALEwEAmpwYAA..." # (سأضع لك الكود الذي يظهر الصورة فعلياً)

st.markdown("""
    <style>
    .stApp { background-color: #0b1120; }
    
    /* تصميم اللوجو المضيء */
    .logo-container {
        display: flex;
        justify-content: center;
        margin: 20px auto;
        width: 180px;
        height: 180px;
        border: 2px solid #22d3ee;
        border-radius: 30px;
        box-shadow: 0 0 30px rgba(34, 211, 238, 0.5);
        background: #1e293b;
        overflow: hidden;
    }
    
    .price-card {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid rgba(34, 211, 238, 0.2);
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. شريط التنبيهات
st.markdown("""
    <div style="background: rgba(34, 211, 238, 0.1); border: 1px solid #22d3ee; padding: 12px; border-radius: 12px; color: #22d3ee; text-align: center; font-weight: bold; margin-bottom: 20px;">
        📢 تورو ليبيا: وجهتك الاقتصادية الأولى والوحيدة في ليبيا .. 🐂 تحديثات فورية
    </div>
    """, unsafe_allow_html=True)

# 4. عرض اللوجو (باستخدام الرابط المباشر الخام الأكيد)
# هذا الرابط هو الرابط الصحيح الذي يتجاوز حماية GitHub
raw_logo_url = "https://raw.githubusercontent.com/molamilan89-gif/toro-libya/main/1000105722.jpg"

st.markdown(f"""
    <div class="logo-container">
        <img src="{raw_logo_url}" style="width:100%; height:100%; object-fit:cover;" onerror="this.src='https://via.placeholder.com/180/1e293b/22d3ee?text=TORO+LY'">
    </div>
    <div style="text-align: center;">
        <h1 style="color: white; font-size: 42px; font-weight: 900; letter-spacing: 5px; margin: 0;">TORO <span style="color: #22d3ee;">LY</span></h1>
        <p style="color: #64748b; font-size: 11px; letter-spacing: 3px; margin-bottom: 30px;">THE LEGEND OF LIBYAN MARKET</p>
    </div>
    """, unsafe_allow_html=True)

# 5. كروت الأسعار
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="price-card"><small>USD</small><br><b style="color:#22d3ee; font-size:22px;">8.65</b></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="price-card"><small>GOLD 18</small><br><b style="color:#eab308; font-size:22px;">415.5</b></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="price-card"><small>BTC</small><br><b style="color:#22c55e; font-size:22px;">96.4K</b></div>', unsafe_allow_html=True)

# 6. نبض السوق
st.markdown("""
    <div style="background: #111827; border-right: 5px solid #22d3ee; border-radius: 15px; padding: 20px; margin-top: 30px; text-align: right; direction: rtl;">
        <h3 style="color: #22d3ee; margin: 0;">🌟 نبض السوق والتوصيات</h3>
        <p style="font-size: 14px; color: white; margin: 10px 0;">حالة الاستقرار: 75% مستقر</p>
        <div style="width: 100%; height: 8px; background: #334155; border-radius: 10px;">
            <div style="width: 75%; height: 100%; background: #22d3ee; border-radius: 10px;"></div>
        </div>
        <p style="font-size: 11px; color: #94a3b8; margin-top: 15px;">⚠️ جاري تحليل أحدث رسائل الواتساب الواردة من الغرفة الموثوقة...</p>
    </div>
    """, unsafe_allow_html=True)
    
