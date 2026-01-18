import streamlit as st

# إعدادات الصفحة الاحترافية - TORO LIBYA
st.set_page_config(page_title="Toro Libya - النسخة الرسمية", page_icon="🐂", layout="centered")

# الكود الكامل مع الشعار والأقسام الشاملة
full_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Tajawal', sans-serif; background: #0b1120; color: white; margin: 0; padding: 0; overflow-x: hidden; }
        .glass { background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; margin-bottom: 20px; transition: 0.3s ease; }
        .section-title { border-right: 4px solid #22d3ee; padding-right: 12px; margin-bottom: 15px; font-weight: 900; color: #22d3ee; }
        .price-item { display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
        
        /* شريط الأخبار المتحرك */
        .marquee-wrapper { width: 100%; position: fixed; top: 0; left: 0; background: rgba(8, 51, 68, 0.95); border-bottom: 1px solid #22d3ee; z-index: 9999; padding: 8px 0; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
        .animate-marquee { display: inline-block; white-space: nowrap; animation: marquee 25s linear infinite; font-size: 13px; font-weight: bold; color: #22d3ee; }
        
        .main-container { padding: 100px 20px 50px 20px; display: flex; flex-direction: column; items: center; }
        
        /* تصميم الشعار الجديد */
        .logo-container { text-align: center; margin-bottom: 30px; position: relative; }
        .logo-img { width: 150px; height: 150px; border-radius: 20px; box-shadow: 0 0 30px rgba(34, 211, 238, 0.3); border: 2px solid rgba(34, 211, 238, 0.5); margin: 0 auto; }
        .logo-text { font-size: 2.5rem; font-weight: 900; letter-spacing: 5px; margin-top: 10px; text-transform: uppercase; }

        .live-indicator { display: inline-flex; align-items: center; gap: 5px; color: #4ade80; font-size: 10px; font-weight: bold; margin-bottom: 15px; }
        .dot { width: 8px; height: 8px; background: #4ade80; border-radius: 50%; display: inline-block; animation: pulse 1.5s infinite; }
        @keyframes pulse { 0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.7); } 70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(74, 222, 128, 0); } 100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(74, 222, 128, 0); } }
    </style>
</head>
<body>
    <div class="marquee-wrapper">
        <div class="animate-marquee">
            📢 Toro Libya: الهوية الرسمية الجديدة انطلقت .. تحديثات فورية من قلب سوق المشير .. ₿ البيتكوين والذهب والعملات في مكان واحد .. 🐂
        </div>
    </div>

    <div class="main-container">
        <div class="logo-container">
            <div class="live-indicator"><span class="dot"></span> نظام Toro Ly المباشر</div>
            <img src="https://lh3.googleusercontent.com/d/1Bf2hD0G-X_f1I6xJ4n-L4z8L9Y-tG9z-" class="logo-img" alt="Toro Ly Logo">
            <h1 class="logo-text">TORO <span class="text-cyan-400">LY</span></h1>
            <p class="text-gray-500 text-[10px] tracking-[0.3em] uppercase">The Legend of Libyan Market</p>
        </div>

        <div class="w-full max-w-md">
            <div class="glass p-5 border-l-4 border-cyan-500">
                <h2 class="section-title">🌟 نبض السوق والتوصيات</h2>
                <p class="text-[11px] text-green-400 italic">✅ الشعار الجديد يعكس قوة البيانات التي نقدمها لك من غرف الواتساب الموثوقة.</p>
                <a href="https://wa.me/yournumber" class="block w-full text-center bg-green-600/20 text-green-400 text-xs py-2 rounded-lg mt-3">💬 استشارة مباشرة</a>
            </div>

            <div class="glass p-5 mt-6">
                <h2 class="section-title">💵 العملات العالمية</h2>
                <div class="price-item"><span>🇺🇸 دولار موازي</span><span id="price-usd" class="font-bold text-cyan-400">8.65</span></div>
                <div class="price-item"><span>🇪🇺 يورو موازي</span><span class="font-bold">9.12</span></div>
                <div class="price-item"><span>🇬🇧 باوند إسترليني</span><span class="font-bold">10.85</span></div>
                <div class="price-item"><span>🇹🇳 دينار تونسي</span><span class="font-bold">2.65</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">✨ الذهب والمعادن</h2>
                <div class="price-item"><span>💍 ذهب جديد (21)</span><span class="font-bold text-yellow-500">485.0</span></div>
                <div class="price-item"><span>✨ ذهب كسر (18)</span><span class="font-bold text-yellow-400">415.5</span></div>
                <div class="price-item"><span>🥈 فضة (جرام)</span><span class="font-bold text-gray-300">5.40</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">🪙 العملات الرقمية</h2>
                <div class="price-item"><span>₿ Bitcoin (BTC)</span><span class="text-green-400 font-bold">$96,430</span></div>
                <div class="price-item"><span>Ξ Ethereum (ETH)</span><span class="text-blue-400 font-bold">$3,345</span></div>
                <div class="price-item"><span>💠 Solana (SOL)</span><span class="text-purple-400 font-bold">$195.20</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">🏗️ مواد البناء والسلع</h2>
                <div class="price-item"><span>🧱 إسمنت (قنطار)</span><span class="font-bold">45.00</span></div>
                <div class="price-item"><span>⛓️ حديد (الطن)</span><span class="font-bold">4100</span></div>
                <div class="price-item"><span>🌻 زيت (لتر)</span><span class="font-bold">7.50</span></div>
            </div>

            <div class="glass border-2 border-cyan-500/30 p-6">
                <h3 class="text-center text-cyan-400 text-xs font-bold mb-4">🔄 محول العملات اللحظي</h3>
                <input type="text" id="lyd" class="w-full bg-slate-900 p-3 rounded-lg text-center font-bold text-xl outline-none" placeholder="0.00 LYD">
            </div>
        </div>
        
        <p class="text-center text-gray-600 text-[10px] mt-10">Toro Ly Legend © 2026</p>
    </div>

    <script>
        // نظام التحديث التلقائي يحاكي البوت
        setInterval(() => {
            let fakePrice = (8.60 + Math.random() * 0.1).toFixed(2);
            document.getElementById('price-usd').innerText = fakePrice;
        }, 10000);
    </script>
</body>
</html>
"""

st.components.v1.html(full_code, height=3500, scrolling=True)
