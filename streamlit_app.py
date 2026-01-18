import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="Toro Libya", layout="centered")

# الكود البرمجي المتكامل
full_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Tajawal', sans-serif; background: #0b1120; color: white; margin: 0; padding: 0; }
        .glass { background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 20px; margin-bottom: 20px; }
        .section-header { border-right: 4px solid #22d3ee; padding-right: 10px; margin-bottom: 20px; font-weight: 900; color: #22d3ee; font-size: 1.2rem; }
        
        /* شريط الأخبار العلوي */
        .marquee { width: 100%; position: fixed; top: 0; background: rgba(8, 51, 68, 0.9); border-bottom: 2px solid #22d3ee; z-index: 1000; padding: 10px 0; overflow: hidden; }
        .marquee-content { display: inline-block; white-space: nowrap; animation: marquee 20s linear infinite; color: #22d3ee; font-weight: bold; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

        .container { padding: 100px 20px 50px; max-width: 500px; margin: auto; }
        .main-title { font-size: 3rem; font-weight: 900; text-align: center; letter-spacing: 5px; margin-bottom: 5px; }
        .sub-title { text-align: center; color: #64748b; font-size: 0.7rem; font-weight: 900; letter-spacing: 4px; margin-bottom: 40px; }

        .price-row { display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
        .price-val { font-family: sans-serif; font-weight: 900; color: #22d3ee; font-size: 1.1rem; }

        /* الحاسبة المحدثة بأرقام دولية */
        .calc-input { width: 100%; background: #0f172a; border: 2px solid #334155; border-radius: 12px; padding: 15px; text-align: center; font-size: 24px; font-weight: 900; color: #22d3ee; outline: none; font-family: sans-serif; margin-bottom: 15px; }
        input::-webkit-outer-spin-button, input::-webkit-inner-spin-button { -webkit-appearance: none; margin: 0; }
    </style>
</head>
<body>
    <div class="marquee">
        <div class="marquee-content">
            📢 Toro Libya: الدولار 8.65 .. اليورو 9.12 .. ذهب كسر 415.5 .. الإسمنت 45 .. الحديد 4100 .. زيت 7.50 .. 🐂
        </div>
    </div>

    <div class="container">
        <h1 class="main-title">TORO <span class="text-cyan-400">LY</span></h1>
        <p class="sub-title text-uppercase">The Legend of Libyan Market</p>

        <div class="glass">
            <div class="section-header">💵 أسعار العملات الموازية</div>
            <div class="price-row"><span>🇺🇸 دولار موازي</span><span class="price-val">8.65</span></div>
            <div class="price-row"><span>🇪🇺 يورو موازي</span><span class="price-val">9.12</span></div>
            <div class="price-row"><span>🇹🇷 ليرة تركية</span><span class="price-val">0.27</span></div>
            <div class="price-row"><span>🇹🇳 دينار تونسي</span><span class="price-val">2.65</span></div>
        </div>

        <div class="glass">
            <div class="section-header">✨ الذهب والمعادن</div>
            <div class="price-row"><span>💍 ذهب كسر (18)</span><span class="price-val text-yellow-400">415.50</span></div>
            <div class="price-row"><span>💍 ذهب جديد (21)</span><span class="price-val text-yellow-200">485.00</span></div>
            <div class="price-row"><span>🥈 فضة (جرام)</span><span class="price-val">5.40</span></div>
        </div>

        <div class="glass">
            <div class="section-header">🏗️ مواد البناء</div>
            <div class="price-row"><span>🧱 إسمنت (قنطار)</span><span class="price-val">45.00</span></div>
            <div class="price-row"><span>⛓️ حديد (طن)</span><span class="price-val">4100</span></div>
            <div class="price-row"><span>🏗️ طوب (1000 طوبة)</span><span class="price-val">1250</span></div>
        </div>

        <div class="glass">
            <div class="section-header">🌻 السلع التموينية</div>
            <div class="price-row"><span>🌻 زيت (لتر)</span><span class="price-val">7.50</span></div>
            <div class="price-row"><span>🍚 أرز (كيلو)</span><span class="price-val">6.50</span></div>
            <div class="price-row"><span>☕ قهوة (كيلو)</span><span class="price-val">45.00</span></div>
        </div>

        <div class="glass border-2 border-cyan-500/30">
            <div class="section-header text-center">🔄 حاسبة Toro الأسطورية</div>
            <p class="text-xs text-gray-400 mb-2">الدينار الليبي (LYD)</p>
            <input type="number" id="lyd" oninput="calc('lyd')" class="calc-input" placeholder="0.00">
            
            <div class="grid grid-cols-2 gap-4">
                <div>
                    <p class="text-xs text-gray-400 mb-2">الدولار ($)</p>
                    <input type="number" id="usd" oninput="calc('usd')" class="calc-input" placeholder="0.00">
                </div>
                <div>
                    <p class="text-xs text-gray-400 mb-2">اليورو (€)</p>
                    <input type="number" id="eur" oninput="calc('eur')" class="calc-input" placeholder="0.00">
                </div>
            </div>
        </div>

        <p class="text-center text-gray-600 text-[10px] mt-10">TORO LY LEGEND © 2026</p>
    </div>

    <script>
        const rUsd = 8.65;
        const rEur = 9.12;
        function calc(src) {
            const l = document.getElementById('lyd');
            const u = document.getElementById('usd');
            const e = document.getElementById('eur');
            if(src === 'lyd') {
                u.value = (l.value / rUsd).toFixed(2);
                e.value = (l.value / rEur).toFixed(2);
            } else if(src === 'usd') {
                l.value = (u.value * rUsd).toFixed(2);
                e.value = ((u.value * rUsd) / rEur).toFixed(2);
            } else if(src === 'eur') {
                l.value = (e.value * rEur).toFixed(2);
                u.value = ((e.value * rEur) / rUsd).toFixed(2);
            }
        }
    </script>
</body>
</html>
"""

# عرض الكود
st.components.v1.html(full_code, height=3000, scrolling=True)
