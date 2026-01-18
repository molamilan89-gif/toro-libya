import streamlit as st

# إعدادات الصفحة الاحترافية لـ Toro Libya
st.set_page_config(page_title="Toro Libya - النسخة الأسطورية", page_icon="🐂", layout="centered")

# الكود الشامل - تم دمج كافة الأقسام ورسم الشعار برمجياً
full_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Tajawal', sans-serif; background: #0b1120; color: white; margin: 0; padding: 0; overflow-x: hidden; }
        .glass { background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; margin-bottom: 20px; }
        .section-title { border-right: 4px solid #22d3ee; padding-right: 12px; margin-bottom: 15px; font-weight: 900; color: #22d3ee; display: flex; align-items: center; gap: 8px; }
        
        /* شريط الأخبار العلوي */
        .marquee-wrapper { width: 100%; position: fixed; top: 0; left: 0; background: rgba(8, 51, 68, 0.95); border-bottom: 2px solid #22d3ee; z-index: 9999; padding: 10px 0; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
        .animate-marquee { display: inline-block; white-space: nowrap; animation: marquee 25s linear infinite; font-size: 14px; font-weight: bold; color: #22d3ee; }
        
        .main-container { padding: 140px 20px 50px 20px; display: flex; flex-direction: column; items: center; }
        
        /* 🔥 رسم الشعار برمجياً (SVG) لضمان الظهور 100% */
        .logo-box { width: 160px; height: 160px; border-radius: 45px; background: linear-gradient(135deg, #1e293b 0%, #0891b2 100%); border: 4px solid #22d3ee; box-shadow: 0 0 50px rgba(34, 211, 238, 0.6); display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; }
        .bull-svg { width: 100px; height: 100px; fill: #22d3ee; filter: drop-shadow(0 0 8px white); }

        .logo-text { font-size: 3rem; font-weight: 900; letter-spacing: 6px; text-transform: uppercase; color: white; line-height: 1; text-align: center; }
        
        /* تصميم الأقسام والأسعار */
        .price-item { display: flex; justify-content: space-between; align-items: center; padding: 14px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
        .price-val { font-family: 'Verdana', sans-serif; font-weight: 900; font-size: 18px; color: #22d3ee; }

        /* 🔄 حاسبة Toro الاحترافية (أرقام دولية) */
        .calc-box { width: 100%; background: #0f172a; border: 2px solid #334155; border-radius: 15px; padding: 20px; text-align: center; margin-bottom: 15px; }
        .calc-input { width: 100%; background: transparent; border: none; text-align: center; font-size: 30px; font-weight: 900; color: #22d3ee; outline: none; font-family: 'Verdana', sans-serif; }
        .calc-label { font-size: 12px; color: #94a3b8; text-transform: uppercase; margin-bottom: 10px; display: block; font-weight: bold; }
    </style>
</head>
<body>
    <div class="marquee-wrapper">
        <div class="animate-marquee">
            📢 Toro Libya: تم تفعيل الشعار وكافة الأقسام بنجاح .. الدولار 8.65 .. ذهب كسر 415.5 .. الإسمنت 45.00 .. 🐂
        </div>
    </div>

    <div class="main-container">
        <div class="logo-box">
            <svg class="bull-svg" viewBox="0 0 24 24">
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm4.59-12.42L10 14.17l-2.59-2.58L6 13l4 4 8-8z"/>
            </svg>
        </div>
        <h1 class="logo-text">TORO <span class="text-cyan-400">LY</span></h1>
        <p class="text-gray-500 text-[11px] tracking-[0.5em] uppercase font-black mt-4">The Legend of Libyan Market</p>

        <div class="w-full max-w-md mt-10">
            <div class="glass p-6">
                <h2 class="section-title">💵 أسعار العملات الموازية</h2>
                <div class="price-item"><span>🇺🇸 دولار موازي</span><span class="price-val">8.65</span></div>
                <div class="price-item"><span>🇪🇺 يورو موازي</span><span class="price-val">9.12</span></div>
                <div class="price-item"><span>🇹🇷 ليرة تركية</span><span class="price-val">0.27</span></div>
                <div class="price-item"><span>🇹🇳 دينار تونسي</span><span class="price-val">2.65</span></div>
            </div>

            <div class="glass p-6">
                <h2 class="section-title">✨ الذهب والمعادن</h2>
                <div class="price-item"><span>💍 ذهب كسر (18)</span><span class="price-val text-yellow-400">415.50</span></div>
                <div class="price-item"><span>💍 ذهب جديد (21)</span><span class="price-val">485.00</span></div>
                <div class="price-item"><span>🥈 فضة (جرام)</span><span class="price-val text-gray-400">5.40</span></div>
            </div>

            <div class="glass p-6">
                <h2 class="section-title">🏗️ مواد البناء</h2>
                <div class="price-item"><span>🧱 إسمنت (قنطار)</span><span class="price-val">45.00</span></div>
                <div class="price-item"><span>⛓️ حديد (الطن)</span><span class="price-val">4100</span></div>
            </div>

            <div class="glass border-2 border-cyan-500/30 p-8">
                <h3 class="text-center text-cyan-400 text-xs font-bold mb-6 uppercase tracking-widest">🔄 حاسبة Toro الأسطورية</h3>
                <div class="calc-box">
                    <span class="calc-label">الدينار الليبي (LYD)</span>
                    <input type="number" id="inp-lyd" oninput="runCalc('lyd')" class="calc-input" placeholder="0.00">
                </div>
                <div class="grid grid-cols-2 gap-4">
                    <div class="calc-box">
                        <span class="calc-label">الدولار ($)</span>
                        <input type="number" id="inp-usd" oninput="runCalc('usd')" class="calc-input !text-[20px]" placeholder="0.00">
                    </div>
                    <div class="calc-box">
                        <span class="calc-label">اليورو (€)</span>
                        <input type="number" id="inp-eur" oninput="runCalc('eur')" class="calc-input !text-[20px]" placeholder="0.00">
                    </div>
                </div>
            </div>
        </div>
        <p class="text-center text-gray-600 text-[10px] mt-12">TORO LY LEGEND © 2026</p>
    </div>

    <script>
        const rateUsd = 8.65;
        const rateEur = 9.12;

        function runCalc(source) {
            const l = document.getElementById('inp-lyd');
            const u = document.getElementById('inp-usd');
            const e = document.getElementById('inp-eur');

            if(source === 'lyd') {
                u.value = (l.value / rateUsd).toFixed(2);
                e.value = (l.value / rateEur).toFixed(2);
            } else if(source === 'usd') {
                l.value = (u.value * rateUsd).toFixed(2);
                e.value = ((u.value * rateUsd) / rateEur).toFixed(2);
            } else if(source === 'eur') {
                l.value = (e.value * rateEur).toFixed(2);
                u.value = ((e.value * rateEur) / rateUsd).toFixed(2);
            }
        }
    </script>
</body>
</html>
"""

# عرض التطبيق النهائي
st.components.v1.html(full_code, height=3500, scrolling=True)
