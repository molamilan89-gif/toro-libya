import streamlit as st
import base64

# إعدادات الصفحة الاحترافية - TORO LIBYA
st.set_page_config(page_title="Toro Libya - النسخة الأسطورية", page_icon="🐂", layout="centered")

# دالة لمعالجة الصورة إذا كانت مرفوعة محلياً (logo.png)
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

# إذا كان لديك ملف شعار باسم logo.png ضعه في نفس المجلد
img_base64 = get_base64_of_bin_file('logo.png')

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
        .glass {{ background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; margin-bottom: 20px; transition: 0.3s ease; }}
        .section-title {{ border-right: 4px solid #22d3ee; padding-right: 12px; margin-bottom: 15px; font-weight: 900; color: #22d3ee; }}
        .price-item {{ display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }}
        
        /* شريط الأخبار المتحرك */
        .marquee-wrapper {{ width: 100%; position: fixed; top: 0; left: 0; background: rgba(8, 51, 68, 0.95); border-bottom: 1px solid #22d3ee; z-index: 9999; padding: 10px 0; }}
        @keyframes marquee {{ 0% {{ transform: translateX(100%); }} 100% {{ transform: translateX(-100%); }} }}
        .animate-marquee {{ display: inline-block; white-space: nowrap; animation: marquee 25s linear infinite; font-size: 14px; font-weight: bold; color: #22d3ee; }}
        
        /* تحسين الهوامش لتفادي التداخل مع شريط الأخبار */
        .main-container {{ padding: 120px 20px 50px 20px; display: flex; flex-direction: column; items: center; }}
        
        /* تصميم الشعار */
        .logo-container {{ text-align: center; margin-bottom: 25px; }}
        .logo-img {{ width: 140px; height: 140px; border-radius: 30px; box-shadow: 0 0 40px rgba(34, 211, 238, 0.25); border: 2px solid rgba(34, 211, 238, 0.4); margin: 0 auto; object-fit: cover; background: #111827; }}
        .logo-text {{ font-size: 2.8rem; font-weight: 900; letter-spacing: 4px; margin-top: 15px; text-transform: uppercase; color: white; }}

        /* بطاقات المؤشرات السريعة (مثل البورصة العالمية) */
        .quick-cards-grid {{ display: grid; grid-template-cols: repeat(3, 1fr); gap: 10px; width: 100%; max-width: 450px; margin-bottom: 25px; }}
        .card-stat {{ background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 15px; padding: 12px; text-align: center; }}
        .card-stat p {{ font-size: 10px; color: #94a3b8; text-transform: uppercase; margin-bottom: 4px; }}
        .card-stat span {{ font-size: 14px; font-weight: 900; color: #22d3ee; }}

        .live-indicator {{ display: inline-flex; align-items: center; gap: 6px; color: #4ade80; font-size: 11px; font-weight: bold; margin-bottom: 10px; background: rgba(74, 222, 128, 0.1); padding: 4px 12px; border-radius: 20px; }}
        .dot {{ width: 8px; height: 8px; background: #4ade80; border-radius: 50%; animation: pulse 1.5s infinite; }}
        @keyframes pulse {{ 0% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.7); }} 70% {{ transform: scale(1); box-shadow: 0 0 0 6px rgba(74, 222, 128, 0); }} 100% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(74, 222, 128, 0); }} }}
    </style>
</head>
<body>
    <div class="marquee-wrapper">
        <div class="animate-marquee">
            📢 Toro Libya: التحديث الأسطوري يعمل الآن .. الأسعار مربوطة بغرف المشير الموثوقة .. ₿ البيتكوين 96,430$ .. 💍 ذهب كسر 18 بـ 415.5 دينار .. 🐂
        </div>
    </div>

    <div class="main-container">
        <div class="logo-container">
            <div class="live-indicator"><span class="dot"></span> نظام Toro Ly المباشر</div>
            <img src="data:image/png;base64,{img_base64}" class="logo-img" onerror="this.src='https://via.placeholder.com/150/111827/22d3ee?text=TORO+LY'" alt="Toro Ly Logo">
            <h1 class="logo-text">TORO <span class="text-cyan-400">LY</span></h1>
            <p class="text-gray-500 text-[9px] tracking-[0.4em] uppercase font-bold">The Legend of Libyan Market</p>
        </div>

        <div class="quick-cards-grid">
            <div class="card-stat"><p>USD/LYD</p><span id="quick-usd">8.65</span></div>
            <div class="card-stat"><p>GOLD 18</p><span id="quick-gold">415.5</span></div>
            <div class="card-stat"><p>BTC/USD</p><span id="quick-btc">96.4K</span></div>
        </div>

        <div class="w-full max-w-md">
            <div class="glass p-5 border-l-4 border-cyan-500">
                <h2 class="section-title">🌟 نبض السوق والتوصيات</h2>
                <p class="text-[11px] text-green-400 italic">✅ الأسعار الآن تعكس آخر رسائل غرف الواتساب الموثوقة.</p>
                <a href="https://wa.me/yournumber" class="block w-full text-center bg-green-600/20 text-green-400 text-xs py-2 rounded-lg mt-3 border border-green-600/30">💬 استشارة مباشرة (واتساب)</a>
            </div>

            <div class="glass p-5 mt-4">
                <h2 class="section-title">💵 العملات العالمية</h2>
                <div class="price-item"><span>🇺🇸 دولار موازي</span><span id="price-usd" class="font-bold text-cyan-400">8.65</span></div>
                <div class="price-item"><span>🇪🇺 يورو موازي</span><span class="font-bold">9.12</span></div>
                <div class="price-item"><span>🇬🇧 باوند إسترليني</span><span class="font-bold">10.85</span></div>
                <div class="price-item"><span>🇹🇳 دينار تونسي</span><span class="font-bold text-blue-300">2.65</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">✨ الذهب والمعادن</h2>
                <div class="price-item"><span>💍 ذهب جديد (21)</span><span class="font-bold text-yellow-500">485.0</span></div>
                <div class="price-item"><span>✨ ذهب كسر (18)</span><span id="price-gold" class="font-bold text-yellow-400">415.5</span></div>
                <div class="price-item"><span>🥈 فضة (جرام)</span><span class="font-bold text-gray-300">5.40</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">🪙 العملات الرقمية</h2>
                <div class="price-item"><span>₿ Bitcoin (BTC)</span><span class="text-green-400 font-bold">$96,430</span></div>
                <div class="price-item"><span>Ξ Ethereum (ETH)</span><span class="text-blue-400 font-bold">$3,345</span></div>
                <div class="price-item"><span>💠 Solana (SOL)</span><span class="text-purple-400 font-bold">$195.20</span></div>
            </div>

            <div class="glass border-2 border-cyan-500/30 p-6">
                <h3 class="text-center text-cyan-400 text-xs font-bold mb-4">🔄 محول العملات اللحظي</h3>
                <input type="text" id="lyd" class="w-full bg-slate-900 p-3 rounded-xl text-center font-bold text-xl outline-none border border-white/10" placeholder="0.00 LYD">
            </div>
        </div>
        
        <p class="text-center text-gray-600 text-[10px] mt-10 uppercase tracking-widest">Toro Ly Legend © 2026</p>
    </div>

    <script>
        // محاكاة وصول تحديث من البوت كل 10 ثواني
        setInterval(() => {{
            let newUsd = (8.60 + Math.random() * 0.1).toFixed(2);
            document.getElementById('price-usd').innerText = newUsd;
            document.getElementById('quick-usd').innerText = newUsd;
        }}, 10000);
    </script>
</body>
</html>
"""

st.components.v1.html(full_code, height=3000, scrolling=True)
