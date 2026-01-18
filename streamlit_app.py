import streamlit as st

# إعدادات الصفحة الاحترافية - TORO LIBYA
st.set_page_config(page_title="Toro Libya - النسخة الأسطورية", page_icon="🐂", layout="centered")

# الكود البرمجي المدمج - تم إصلاح إغلاق علامات الاقتباس
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
        
        /* شريط الأخبار العلوي */
        .marquee-wrapper { width: 100%; position: fixed; top: 0; left: 0; background: rgba(8, 51, 68, 0.95); border-bottom: 2px solid #22d3ee; z-index: 9999; padding: 10px 0; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
        .animate-marquee { display: inline-block; white-space: nowrap; animation: marquee 25s linear infinite; font-size: 14px; font-weight: bold; color: #22d3ee; }
        
        .main-container { padding: 140px 20px 50px 20px; display: flex; flex-direction: column; items: center; }
        
        /* 🔥 شعار الثور المرسوم بالكود (SVG) لضمان الظهور */
        .logo-box { width: 160px; height: 160px; border-radius: 45px; background: linear-gradient(135deg, #1e293b 0%, #0891b2 100%); border: 4px solid #22d3ee; box-shadow: 0 0 50px rgba(34, 211, 238, 0.6); display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; }
        .bull-svg { width: 100px; height: 100px; fill: white; filter: drop-shadow(0 0 10px rgba(34, 211, 238, 0.8)); }

        .logo-text { font-size: 3rem; font-weight: 900; letter-spacing: 6px; text-transform: uppercase; color: white; line-height: 1; text-align: center; }
        
        /* بطاقات الأسعار */
        .price-item { display: flex; justify-content: space-between; align-items: center; padding: 15px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
        .price-val { font-family: sans-serif; font-weight: 900; font-size: 1.2rem; color: #22d3ee; }

        /* حاسبة الأرقام الدولية */
        .calc-box { width: 100%; background: #0f172a; border: 2px solid #334155; border-radius: 15px; padding: 20px; text-align: center; margin-bottom: 15px; }
        .calc-input { width: 100%; background: transparent; border: none; text-align: center; font-size: 32px; font-weight: 900; color: #22d3ee; outline: none; font-family: sans-serif; }
        .calc-label { font-size: 12px; color: #94a3b8; text-transform: uppercase; margin-bottom: 8px; display: block; }
    </style>
</head>
<body>
    <div class="marquee-wrapper">
        <div class="animate-marquee">
            📢 Toro Libya: تم إصلاح خطأ الكود نهائياً .. الدولار 8.65 .. ذهب كسر 415.5 .. البيتكوين يتألق .. 🐂
        </div>
    </div>

    <div class="main-container">
        <div class="logo-box">
            <svg class="bull-svg" viewBox="0 0 24 24">
                <path d="M12,2C10.89,2 10,2.89 10,4V7H14V4C14,2.89 13.11,2 12,2M10,9V11H4V13H10V15H8V17H10V19H14V17H16V15H20V13H14V11H20V9H14V7H10V9M12,12A1,1 0 0,1 13,13A1,1 0 0,1 12,14A1,1 0 0,1 11,13A1,1 0 0,1 12,12Z" />
            </svg>
        </div>
        <h1 class="logo-text">TORO <span class="text-cyan-400">LY</span></h1>
        <p class="text-gray-500 text-[11px] tracking-[0.5em] uppercase font-black mt-4">The Legend of Libyan Market</p>

        <div class="w-full max-w-md mt-10">
            <div class="glass p-6">
                <h2 class="text-cyan-400 font-bold mb-4 border-r-4 border-cyan-400 pr-3">💵 أسعار العملات</h2>
                <div class="price-item"><span>🇺🇸 دولار موازي</span><span class="price-val">8.65</span></div>
                <div class="price-item"><span>🇪🇺 يورو موازي</span><span class="price-val">9.12</span></div>
                <div class="price-item"><span>🇹🇷 ليرة تركية</span><span class="price-val">0.27</span></div>
            </div>

            <div class="glass p-6 mt-4">
                <h2 class="text-yellow-400 font-bold mb-4 border-r-4 border-yellow-400 pr-3">✨ الذهب والمعادن</h2>
                <div class="price-item"><span>💍 ذهب كسر (18)</span><span class="price-val text-yellow-400">415.50</span></div>
                <div class="price-item"><span>💍 ذهب جديد (21)</span><span class="price-val">485.00</span></div>
            </div>

            <div class="glass p-6 mt-4">
                <h2 class="text-gray-400 font-bold mb-4 border-r-4 border-gray-400 pr-3">🏗️ مواد البناء</h2>
                <div class="price-item"><span>🧱 إسمنت (قنطار)</span><span class="price-val">45.00</span></div>
                <div class="price-item"><span>⛓️ حديد (طن)</span><span class="price-val">4100</span></div>
            </div>

            <div class="glass border-2 border-cyan-500/30 p-8 mt-6">
                <h3 class="text-center text-cyan-400 text-xs font-bold mb-6 uppercase tracking-widest">🔄 حاسبة Toro الأسطورية</h3>
                <div class="calc-box">
                    <span class="calc-label">الدينار الليبي (LYD)</span>
                    <input type="number" id="inp-lyd" oninput="calculate('lyd')" class="calc-input" placeholder="0.00">
                </div>
                <div class="grid grid-cols-2 gap-4">
                    <div class="calc-box">
                        <span class="calc-label">الدولار ($)</span>
                        <input type="number" id="inp-usd" oninput="calculate('usd')" class="calc-input !text-[20px]" placeholder="0.00">
                    </div>
                    <div class="calc-box">
                        <span class="calc-label">اليورو (€)</span>
                        <input type="number" id="inp-eur" oninput="calculate('eur')" class="calc-input !text-[20px]" placeholder="0.00">
                    </div>
                </div>
            </div>
        </div>
        <p class="text-center text-gray-600 text-[10px] mt-10">TORO LY LEGEND © 2026</p>
    </div>

    <script>
        const rateUsd = 8.65;
        const rateEur = 9.12;
        function calculate(source) {
            const lyd = document.getElementById('inp-lyd');
            const usd = document.getElementById('inp-usd');
            const eur = document.getElementById('inp-eur');
            if(source === 'lyd') {
                usd.value = (lyd.value / rateUsd).toFixed(2);
                eur.value = (lyd.value / rateEur).toFixed(2);
            } else if(source === 'usd') {
                lyd.value = (usd.value * rateUsd).toFixed(2);
                eur.value = ((usd.value * rateUsd) / rateEur).toFixed(2);
            } else if(source === 'eur') {
                lyd.value = (eur.value * rateEur).toFixed(2);
                usd.value = ((eur.value * rateEur) / rateUsd).toFixed(2);
            }
        }
    </script>
</body>
</html>
"""

# عرض الكود بدون أخطاء
st.components.v1.html(full_code, height=3000, scrolling=True)
