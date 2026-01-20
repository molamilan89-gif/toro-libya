import streamlit as st
import requests
import base64

# 1. إعدادات الصفحة
st.set_page_config(page_title="Toro Libya", page_icon="🐂", layout="centered")

# 2. وظيفة لجلب الصورة وتحويلها لـ Base64 لضمان ظهورها
def get_base64_image(url):
    try:
        response = requests.get(url)
        return base64.b64encode(response.content).decode()
    except:
        return ""

# رابط صورتك من GitHub
logo_url = "https://raw.githubusercontent.com/molamilan89-gif/toro-libya/main/1000105722.jpg"
logo_base64 = get_base64_image(logo_url)

# 3. الكود البرمجي للموقع
full_code = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Tajawal', sans-serif; background: #0b1120; color: white; margin: 0; padding: 0; overflow-x: hidden; }}
        
        /* تصميم اللوجو ليكون تماماً مثل الصورة المطلوبة */
        .header-logo-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding-top: 50px;
            margin-bottom: 20px;
        }}
        .main-logo {{
            width: 180px;
            height: 180px;
            object-fit: cover;
            border-radius: 25px;
            border: 3px solid #22d3ee;
            box-shadow: 0px 0px 35px rgba(34, 211, 238, 0.5);
            margin-bottom: 20px;
            background: #1e293b;
        }}

        .glass {{ background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; margin-bottom: 20px; transition: 0.3s ease; }}
        .section-title {{ border-right: 4px solid #22d3ee; padding-right: 12px; margin-bottom: 15px; font-weight: 900; color: #22d3ee; }}
        
        .marquee-wrapper {{ width: 100%; position: fixed; top: 0; left: 0; background: rgba(8, 51, 68, 0.95); border-bottom: 1px solid #22d3ee; z-index: 9999; padding: 8px 0; }}
        @keyframes marquee {{ 0% {{ transform: translateX(100%); }} 100% {{ transform: translateX(-100%); }} }}
        .animate-marquee {{ display: inline-block; white-space: nowrap; animation: marquee 25s linear infinite; font-size: 13px; font-weight: bold; color: #22d3ee; }}
        
        .main-container {{ padding: 20px; display: flex; flex-direction: column; items: center; width: 100%; max-width: 500px; margin: auto; }}
        .price-item {{ display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }}
    </style>
</head>
<body>
    <div class="marquee-wrapper">
        <div class="animate-marquee">
            📢 تورو ليبيا: وجهتك الاقتصادية الأولى والوحيدة في ليبيا .. 🐂 مزامنة فورية مع سوق المشير والبورصات العالمية ..
        </div>
    </div>

    <div class="header-logo-container">
        <img src="data:image/jpeg;base64,{logo_base64}" class="main-logo" alt="Toro Logo">
        <h1 class="text-4xl font-black tracking-widest uppercase">TORO <span class="text-cyan-400">LY</span></h1>
        <p class="text-gray-500 text-[11px] mt-1 uppercase tracking-widest text-center">THE LEGEND OF LIBYAN MARKET</p>
    </div>

    <div class="main-container">
        <div class="grid grid-cols-3 gap-3 w-full mb-8">
            <div class="bg-slate-800/50 p-4 rounded-2xl border border-white/5 text-center">
                <p class="text-[10px] text-gray-400">USD</p>
                <p class="text-lg font-bold text-cyan-400">8.65</p>
            </div>
            <div class="bg-slate-800/50 p-4 rounded-2xl border border-white/5 text-center">
                <p class="text-[10px] text-gray-400">GOLD 18</p>
                <p class="text-lg font-bold text-yellow-500">415.5</p>
            </div>
            <div class="bg-slate-800/50 p-4 rounded-2xl border border-white/5 text-center">
                <p class="text-[10px] text-gray-400">BTC</p>
                <p class="text-lg font-bold text-green-400">96.4K</p>
            </div>
        </div>

        <div class="w-full">
            <div class="glass p-5 border-l-4 border-cyan-500">
                <h2 class="section-title">🌟 نبض السوق والتوصيات</h2>
                <div class="flex justify-between items-center text-xs mb-2">
                    <span>حالة الاستقرار</span>
                    <span class="text-cyan-400">75% مستقر</span>
                </div>
                <div class="h-2 w-full bg-slate-700 rounded-full overflow-hidden">
                    <div class="h-full bg-cyan-500 w-[75%]"></div>
                </div>
                <p class="text-[11px] text-gray-400 mt-3 italic text-center">⚠️ جاري تحليل أحدث رسائل الواتساب من الغرفة الموثوقة...</p>
                <button class="w-full bg-green-600/20 text-green-400 py-2 rounded-xl mt-4 border border-green-600/30 font-bold">تواصل مع الإدارة 💬</button>
            </div>
        </div>
        
        <p class="text-gray-600 text-[10px] mt-10 tracking-widest">TORO LIBYA © 2026</p>
    </div>
</body>
</html>
"""

st.components.v1.html(full_code, height=1800, scrolling=True)
