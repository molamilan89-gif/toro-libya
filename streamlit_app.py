import streamlit as st

# إعدادات الصفحة الاحترافية - TORO LIBYA
st.set_page_config(page_title="Toro Libya - منصة وول ستريت ليبيا", page_icon="🐂", layout="centered")

# الكود الكامل مع كافة الأقسام (العملات، الذهب، البناء، السلع، الرقمية) + الحاسبة الموضعية
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
        
        /* شريط الأخبار العلوي */
        .marquee-wrapper { width: 100%; position: fixed; top: 0; left: 0; background: rgba(8, 51, 68, 0.95); border-bottom: 1px solid #22d3ee; z-index: 9999; padding: 8px 0; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
        .animate-marquee { display: inline-block; white-space: nowrap; animation: marquee 25s linear infinite; font-size: 13px; font-weight: bold; color: #22d3ee; }
        
        .main-container { padding: 100px 20px 50px 20px; display: flex; flex-direction: column; items: center; }
        
        /* الأرقام الدولية */
        .price-val { font-family: 'Verdana', sans-serif; font-weight: 900; }
        
        /* الآلة الحاسبة الموضعية */
        .calc-box { background: #111827; border: 1px solid #374151; border-radius: 12px; display: flex; align-items: center; padding: 0 15px; margin-bottom: 10px; }
        .calc-box input { background: transparent !important; border: none !important; padding: 12px 5px !important; width: 100% !important; color: #22d3ee !important; direction: ltr !important; text-align: center !important; outline: none !important; font-weight: bold; font-family: 'Verdana', sans-serif; font-size: 20px; }
    </style>
</head>
<body>
    <div class="marquee-wrapper">
        <div class="animate-marquee">
            📢 Toro Libya: تم تفعيل كافة الأقسام (العملات، الذهب، مواد البناء، السلع، الرقمية) .. تحديثات مباشرة من سوق المشير .. 🐂
        </div>
    </div>

    <div class="main-container">
        <div class="text-center mb-8">
            <h1 class="text-6xl font-black tracking-widest uppercase">Toro <span class="text-cyan-400">Ly</span></h1>
            <p class="text-gray-500 text-[10px] mt-2 uppercase tracking-[0.5em] font-bold">The Legend of Libyan Market</p>
        </div>

        <div class="w-full max-w-md">
            <div class="glass p-5">
                <h2 class="section-title">💵 العملات العالمية</h2>
                <div class="price-item"><span>🇺🇸 دولار موازي</span><span class="price-val text-cyan-400">8.65</span></div>
                <div class="price-item"><span>🇪🇺 يورو موازي</span><span class="price-val">9.12</span></div>
                <div class="price-item"><span>🇬🇧 باوند إسترليني</span><span class="price-val">10.85</span></div>
                <div class="price-item"><span>🇹🇳 دينار تونسي</span><span class="price-val">2.65</span></div>
                <div class="price-item"><span>🇹🇷 ليرة تركية</span><span class="price-val">0.26</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">✨ الذهب والمعادن</h2>
                <div class="price-item"><span>💍 ذهب كسر (عيار 18)</span><span class="price-val text-yellow-400">415.5</span></div>
                <div class="price-item"><span>💍 ذهب جديد (عيار 21)</span><span class="price-val text-yellow-500">485.0</span></div>
                <div class="price-item"><span>🥈 فضة (جرام)</span><span class="price-val">5.40</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">🏗️ مواد البناء والطاقة</h2>
                <div class="price-item"><span>🧱 إسمنت (قنطار)</span><span class="price-val">45.00</span></div>
                <div class="price-item"><span>⛓️ حديد (طن)</span><span class="price-val">4100</span></div>
                <div class="price-item"><span>🛢️ نفط برنت</span><span class="price-val text-green-400">$78.40</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">🌻 السلع واللحوم</h2>
                <div class="price-item"><span>🌻 زيت (لتر)</span><span class="price-val">7.50</span></div>
                <div class="price-item"><span>🍚 أرز (كيلو)</span><span class="price-val">6.50</span></div>
                <div class="price-item"><span>🥩 لحم خروف (كيلو)</span><span class="price-val">55.0</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">🪙 العملات الرقمية</h2>
                <div class="price-item"><span>₿ Bitcoin (BTC)</span><span class="price-val text-green-400">$96,430</span></div>
                <div class="price-item"><span>☀️ Solana (SOL)</span><span class="price-val text-purple-400">$245.20</span></div>
            </div>

            <div class="glass p-6 border-2 border-cyan-500/40">
                <h3 class="text-cyan-400 text-xs font-bold mb-4 text-center">🔄 حاسبة Toro الأسطورية</h3>
                <div class="calc-box">
                    <input type="number" id="lyd" oninput="runCalc('lyd')" placeholder="0.00">
                    <span class="text-cyan-400 font-bold ml-2">LYD</span>
                </div>
                <div class="grid grid-cols-2 gap-3">
                    <div class="calc-box">
                        <span class="text-cyan-400 font-bold mr-2">$</span>
                        <input type="number" id="usd" oninput="runCalc('usd')" placeholder="0.00">
                    </div>
                    <div class="calc-box">
                        <span class="text-cyan-400 font-bold mr-2">€</span>
                        <input type="number" id="eur" oninput="runCalc('eur')" placeholder="0.00">
                    </div>
                </div>
            </div>
        </div>
        <p class="text-gray-600 text-[10px] mt-10 text-center uppercase tracking-widest font-bold">Toro Ly Legend © 2026</p>
    </div>

    <script>
        const rateUsd = 8.65, rateEur = 9.12;
        function runCalc(id) {
            const l = document.getElementById('lyd'), u = document.getElementById('usd'), e = document.getElementById('eur');
            let val = parseFloat(document.getElementById(id).value) || 0;
            if(id === 'lyd'){ 
                u.value = (val / rateUsd).toFixed(2); 
                e.value = (val / rateEur).toFixed(2); 
            } else if(id === 'usd'){ 
                l.value = (val * rateUsd).toFixed(2); 
                e.value = ((val * rateUsd) / rateEur).toFixed(2); 
            } else if(id === 'eur'){ 
                l.value = (val * rateEur).toFixed(2); 
                u.value = ((val * rateEur) / rateUsd).toFixed(2); 
            }
        }
    </script>
</body>
</html>
"""

st.components.v1.html(full_code, height=3500, scrolling=True)
