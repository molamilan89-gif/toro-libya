import streamlit as st
import base64
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="Toro Libya", page_icon="🐂", layout="centered")

# 2. وظيفة لجلب الصورة وتحويلها لنص (Base64) لضمان الظهور
def get_image_base64(url):
    try:
        res = requests.get(url)
        return base64.b64encode(res.content).decode()
    except:
        return None

# رابط الصورة من مستودعك
img_url = "https://raw.githubusercontent.com/molamilan89-gif/toro-libya/main/1000105722.jpg"
encoded_img = get_image_base64(img_url)

# 3. تصميم الموقع بالكامل (HTML & CSS)
html_content = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Tajawal', sans-serif; background-color: #0b1120; color: white; text-align: center; margin: 0; padding: 0; }}
        
        /* إطار اللوجو المضيء */
        .logo-container {{
            margin: 40px auto 20px;
            width: 180px;
            height: 180px;
            border-radius: 30px;
            border: 2px solid #22d3ee;
            box-shadow: 0 0 30px rgba(34, 211, 238, 0.4);
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #1e293b;
        }}
        .logo-container img {{ width: 100%; height: 100%; object-fit: cover; }}

        .brand-name {{ font-size: 38px; font-weight: 900; letter-spacing: 4px; margin: 5px 0; }}
        .brand-sub {{ color: #64748b; font-size: 11px; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 30px; }}
        
        .price-grid {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; padding: 0 15px; }}
        .card {{ background: rgba(30, 41, 59, 0.6); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 15px; padding: 15px; }}
        .card-val {{ font-size: 22px; font-weight: bold; color: #22d3ee; display: block; }}
        .card-label {{ font-size: 12px; color: #94a3b8; }}

        .news-bar {{ background: rgba(34, 211, 238, 0.1); border: 1px solid #22d3ee; padding: 8px; border-radius: 10px; margin: 20px 15px; font-size: 13px; }}
        
        .pulse-box {{ background: #111827; border: 1px solid #22d3ee; border-radius: 20px; padding: 20px; margin: 20px 15px; text-align: right; }}
    </style>
</head>
<body>

    <div class="news-bar">
        <marquee>📢 تورو ليبيا: وجهتك الاقتصادية الأولى والوحيدة في ليبيا .. 🐂 تحديثات فورية من قلب سوق المشير ..</marquee>
    </div>

    <div class="logo-container">
        {f'<img src="data:image/jpeg;base64,{encoded_img}">' if encoded_img else '<p>Loading...</p>'}
    </div>

    <div class="brand-name">TORO <span style="color: #22d3ee;">LY</span></div>
    <div class="brand-sub">THE LEGEND OF LIBYAN MARKET</div>

    <div class="price-grid">
        <div class="card"><span class="card-label">USD</span><span class="card-val">8.65</span></div>
        <div class="card"><span class="card-label">GOLD 18</span><span class="card-val">415.5</span></div>
        <div class="card"><span class="card-label">BTC</span><span class="card-val">96.4K</span></div>
    </div>

    <div class="pulse-box">
        <h3 style="color: #22d3ee; margin-top: 0;">🌟 نبض السوق والتوصيات</h3>
        <p style="font-size: 14px; margin-bottom: 5px;">حالة الاستقرار: <span style="color: #22d3ee;">75% مستقر</span></p>
        <div style="width: 100%; height: 6px; background: #334155; border-radius: 10px;">
            <div style="width: 75%; height: 100%; background: #22d3ee; border-radius: 10px;"></div>
        </div>
        <p style="font-size: 11px; color: #94a3b8; margin-top: 15px;">⚠️ جاري تحليل أحدث رسائل الواتساب الواردة من الغرفة الموثوقة...</p>
    </div>

</body>
</html>
"""

st.components.v1.html(html_content, height=1000, scrolling=True)
