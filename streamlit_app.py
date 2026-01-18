import streamlit as st

# إعدادات الصفحة الاحترافية - TORO LIBYA
st.set_page_config(page_title="Toro Libya - منصة وول ستريت ليبيا", page_icon="🐂", layout="centered")

# الكود الكامل مع دمج الأيقونات المتحركة التي ظهرت في صورك + الأقسام الجديدة
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
        .price-item { display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
        
        /* تأثير الأيقونة المركزية كما ظهر في صورك */
        .hero-icon { width: 120px; height: 120px; background: rgba(34, 211, 238, 0.15); border: 3px solid #22d3ee; border-radius: 35px; display: flex; align-items: center; justify-content: center; margin: 20px auto; box-shadow: 0 0 30px rgba(34, 211, 238, 0.3); position: relative; overflow: hidden; }
        .hero-icon::after { content: ''; position: absolute; width: 100%; height: 100%; background: linear-gradient(45deg, transparent, rgba(255,255,255,0.2), transparent); animation: shine 3s infinite; }
        @keyframes shine { 0% { transform: translateX(-100%); } 100% { transform: translateX(100%); } }

        .marquee-wrapper { width: 100%; position: fixed; top: 0; left: 0; background: rgba(8, 51, 68, 0.95); border-bottom: 1px solid #22d3ee; z-index: 9999; padding: 8px 0; }
        .animate-marquee { display: inline-block; white-space: nowrap; animation: marquee 25s linear infinite; font-size: 13px; font-weight: bold; color: #22d3ee; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

        .price-val { font-family: 'Verdana', sans-serif; font-weight: bold; }
        .status-badge { padding: 4px 10px; border-radius: 20px; font-size: 10px; font-weight: bold; }
        
        .calc-box { background: #111827; border: 1px solid #374151; border-radius: 12px; display: flex; align-items: center; padding: 0 15px; margin-bottom: 10px; }
        .calc-box input { background: transparent !important; border: none !important; padding: 12px 5px !important; width: 100% !important; color: white !important; direction: ltr !important; text-align: center !important; outline: none !important; font-weight: bold; font-size: 18px; }
    </style>
</head>
<body>
    <div class="marquee-wrapper">
        <div class="animate-marquee">
            📢 Toro Libya: تم تحديث أسعار العملات والذهب الآن .. مؤشر الكهرباء مستقر .. مبيعات الإسمنت تشهد هدوءاً .. 🐂
        </div>
    </div>

    <div class="main-container pt-20 px-5">
        <div class="text-center">
            <div class="inline-flex items-center gap-2 bg-green-500/10 text-green-400 px-3 py-1 rounded-full text-[10px] font-bold mb-2 border border-green-500/20">
                <span class="w-2 height-2 bg-green-400 rounded-full animate-pulse"></span> نظام Toro Ly المباشر
            </div>
            
            <div class="hero-icon">
                <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#22d3ee" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>
            </div>

            <h1 class="text-4xl font-black tracking-tighter uppercase">Toro <span class="text-cyan-400">Ly</span></h1>
            <p class="text-gray-500 text-[10px] mt-1 uppercase tracking-widest mb-8">The Legend of Libyan Market</p>
        </div>

        <div class="grid grid-cols-3 gap-3 mb-8">
            <div class="glass p-3 text-center border-b-2 border-cyan-500">
                <p class="text-[9px] text-gray-400 uppercase">USD</p>
                <p id="top-usd" class="text-sm font-bold price-val">8.65</p>
            </div>
            <div class="glass p-3 text-center border-b-2 border-yellow-500">
                <p class="text-[9px] text-gray-400 uppercase">Gold 18</p>
                <p class="text-sm font-bold price-val">415.5</p>
            </div>
            <div class="glass p-3 text-center border-b-2 border-green-500">
                <p class="text-[9px] text-gray-400 uppercase">BTC</p>
                <p class="text-sm font-bold price-val">96.4K</p>
            </div>
        </div>

        <div class="glass p-5 border-l-4 border-yellow-500">
            <h2 class="section-title">⚡ الخدمات والطاقة</h2>
            <div class="flex justify-between items-center mb-3">
                <span class="text-xs">طرح الأحمال (الغربية)</span>
                <span class="status-badge bg-green-500/20 text-green-400">ساعة واحدة</span>
            </div>
            <div class="flex justify-between items-center">
                <span class="text-xs">حالة محطات الوقود</span>
                <span class="status-badge bg-blue-500/20 text-blue-400">متوفر - ازدحام خفيف</span>
            </div>
        </div>

        <div class="glass p-5 mt-6">
            <h2 class="section-title">💵 أسعار العملات الموازية</h2>
            <div class="price-item"><span>🇺🇸 دولار موازي</span><span id="val-usd" class="price-val text-cyan-400">8.65</span></div>
            <div class="price-item"><span>🇪🇺 يورو موازي</span><span class="price-val">9.12</span></div>
            <div class="price-item"><span>🇹🇳 دينار تونسي</span><span class="price-val">2.65</span></div>
            <div class="price-item"><span>🇪🇬 جنيه مصري</span><span class="price-val text-green-400">0.17</span></div>
        </div>

        <div class="glass p-5">
            <h2 class="section-title">🏗️ مواد البناء</h2>
            <div class="price-item"><span>🧱 إسمنت (قنطار)</span><span class="price-val">45.00</span></div>
            <div class="price-item"><span>⛓️ حديد (طن)</span><span class="price-val">4100</span></div>
            <div class="price-item"><span>🌻 زيت (لتر)</span><span class="price-val text-yellow-500">7.50</span></div>
        </div>

        <div class="glass p-6 border-2 border-cyan-500/30">
            <h3 class="text-cyan-400 text-xs font-bold mb-4 text-center">🔄 حاسبة TORO الأسطورية</h3>
            <div class="calc-box"><input type="number" id="lyd" oninput="runCalc('lyd')" placeholder="0.00"><span class="text-cyan-400 font-bold ml-2 text-xs">LYD</span></div>
            <div class="grid grid-cols-2 gap-3">
                <div class="calc-box"><input type="number" id="usd" oninput="runCalc('usd')" placeholder="0.00"><span class="text-cyan-400 font-bold ml-2 text-xs">USD</span></div>
                <div class="calc-box"><input type="number" id="eur" oninput="runCalc('eur')" placeholder="0.00"><span class="text-cyan-400 font-bold ml-2 text-xs">EUR</span></div>
            </div>
        </div>

        <p class="text-gray-600 text-[10px] my-10 text-center uppercase tracking-widest">TORO LY LEGEND © 2026</p>
    </div>

    <script>
        const rateUsd = 8.65, rateEur = 9.12;
        function runCalc(id) {
            const l = document.getElementById('lyd'), u = document.getElementById('usd'), e = document.getElementById('eur');
            let val = parseFloat(document.getElementById(id).value) || 0;
            if(id === 'lyd'){ u.value = (val / rateUsd).toFixed(2); e.value = (val / rateEur).toFixed(2); }
            else if(id === 'usd'){ l.value = (val * rateUsd).toFixed(2); e.value = ((val * rateUsd) / rateEur).toFixed(2); }
            else if(id === 'eur'){ l.value = (val * rateEur).toFixed(2); u.value = ((val * rateEur) / rateUsd).toFixed(2); }
        }
    </script>
</body>
</html>
"""

st.components.v1.html(full_code, height=1800, scrolling=True)
