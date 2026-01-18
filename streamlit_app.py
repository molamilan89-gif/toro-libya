import streamlit as st

# إعدادات الصفحة الاحترافية - TORO LIBYA
st.set_page_config(page_title="Toro Libya - منصة وول ستريت ليبيا", page_icon="🐂", layout="centered")

# الكود الشامل بتصميم موحد وفخم (الأصفر للذهب فقط)
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
        
        /* توحيد العناوين باللون السماوي */
        .section-title { border-right: 4px solid #22d3ee; padding-right: 12px; margin-bottom: 15px; font-weight: 900; color: #22d3ee; display: flex; align-items: center; gap: 8px; }
        
        /* الذهب فقط بالأصفر */
        .section-title.gold-title { border-right-color: #facc15; color: #facc15; }
        .gold-text { color: #facc15 !important; }

        .price-item { display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
        
        .main-logo-container { position: relative; width: 150px; height: 150px; margin: 20px auto; }
        .logo-box { width: 100%; height: 100%; background: radial-gradient(circle, rgba(34, 211, 238, 0.1) 0%, transparent 70%); border: 2px solid #22d3ee; border-radius: 40px; display: flex; align-items: center; justify-content: center; }
        .logo-inner { width: 80px; height: 80px; background: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; }
        .logo-inner svg { width: 50px; height: 50px; color: #0b1120; }

        .marquee-wrapper { width: 100%; position: fixed; top: 0; left: 0; background: rgba(8, 51, 68, 0.95); border-bottom: 1px solid #22d3ee; z-index: 9999; padding: 8px 0; }
        .animate-marquee { display: inline-block; white-space: nowrap; animation: marquee 25s linear infinite; font-size: 13px; font-weight: bold; color: #22d3ee; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

        .status-badge { padding: 4px 12px; border-radius: 8px; font-size: 11px; font-weight: bold; background: rgba(34, 211, 238, 0.1); color: #22d3ee; border: 1px solid rgba(34, 211, 238, 0.2); }
        .price-val { font-family: 'Verdana', sans-serif; font-weight: bold; }
        
        .top-card { background: rgba(30, 41, 59, 0.5); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 15px; padding: 15px; text-align: center; }
        .top-card.gold-border { border-bottom: 2px solid #facc15; }
        .top-card.cyan-border { border-bottom: 2px solid #22d3ee; }

        .calc-box { background: #111827; border: 1px solid #374151; border-radius: 12px; display: flex; align-items: center; padding: 0 15px; margin-bottom: 10px; }
        .calc-box input { background: transparent !important; border: none !important; padding: 15px 5px !important; width: 100% !important; color: white !important; text-align: center !important; outline: none !important; font-size: 20px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="marquee-wrapper">
        <div class="animate-marquee">
             📢 تورو ليبيا: الدولار 8.65 .. الذهب كسر 415.5 .. الإسمنت 45 .. سولانا 242.15 .. 🐂
        </div>
    </div>

    <div class="main-container pt-24 px-5 max-w-md mx-auto">
        <div class="text-center mb-6">
            <div class="inline-flex items-center gap-2 bg-cyan-500/10 text-cyan-400 px-4 py-1 rounded-full text-[11px] font-bold border border-cyan-500/20 mb-4">
                <span class="w-2 h-2 bg-cyan-400 rounded-full animate-pulse"></span> نظام Toro Ly المباشر
            </div>

            <div class="main-logo-container">
                <div class="logo-box">
                    <div class="logo-inner">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>
                    </div>
                </div>
            </div>

            <h1 class="text-5xl font-black tracking-tighter">TORO <span class="text-cyan-400">LY</span></h1>
            <p class="text-gray-500 text-[10px] mt-2 tracking-[0.2em] uppercase font-bold">The Legend of Libyan Market</p>
        </div>

        <div class="grid grid-cols-3 gap-3 mb-8">
            <div class="top-card cyan-border">
                <p class="text-[9px] text-gray-400 font-bold uppercase">BTC</p>
                <p class="text-sm font-bold price-val">96.4K</p>
            </div>
            <div class="top-card gold-border">
                <p class="text-[9px] text-gray-400 font-bold uppercase gold-text">GOLD 18</p>
                <p class="text-sm font-bold price-val gold-text">415.5</p>
            </div>
            <div class="top-card cyan-border">
                <p class="text-[9px] text-gray-400 font-bold uppercase">USD</p>
                <p id="top-usd" class="text-sm font-bold price-val">8.65</p>
            </div>
        </div>

        <div class="glass p-5 border-l-4 border-cyan-500">
            <h2 class="section-title">⚡ الخدمات والطاقة</h2>
            <div class="flex justify-between items-center mb-4">
                <span class="text-xs font-bold">طرح الأحمال (الغربية)</span>
                <span class="status-badge">ساعة واحدة</span>
            </div>
            <div class="flex justify-between items-center">
                <span class="text-xs font-bold">حالة محطات الوقود</span>
                <span class="status-badge">متوفر - ازدحام خفيف</span>
            </div>
        </div>

        <div class="glass p-5 mt-6 border-l-4 border-cyan-500">
            <h2 class="section-title">💵 أسعار العملات الموازية</h2>
            <div class="price-item"><span>🇺🇸 دولار موازي</span><span id="val-usd" class="price-val text-cyan-400 text-lg">8.65</span></div>
            <div class="price-item"><span>🇪🇺 يورو موازي</span><span class="price-val text-lg">9.12</span></div>
            <div class="price-item"><span>🇬🇧 باوند إسترليني</span><span class="price-val text-lg">10.85</span></div>
            <div class="price-item"><span>🇹🇳 دينار تونسي</span><span class="price-val text-lg">2.65</span></div>
            <div class="price-item"><span>🇪🇬 جنيه مصري</span><span class="price-val text-lg">0.17</span></div>
        </div>

        <div class="glass p-5 mt-6 border-l-4 border-yellow-500">
            <h2 class="section-title gold-title">✨ الذهب والمعادن</h2>
            <div class="price-item"><span>💍 ذهب جديد (21)</span><span class="price-val gold-text">485.0</span></div>
            <div class="price-item"><span>✨ ذهب كسر (18)</span><span class="price-val gold-text">415.5</span></div>
            <div class="price-item"><span>🥈 فضة (جرام)</span><span class="price-val text-gray-300">5.40</span></div>
            <div class="price-item"><span>🥉 نحاس (كيلو)</span><span class="price-val text-gray-300">42.0</span></div>
        </div>

        <div class="glass p-5 mt-6 border-l-4 border-cyan-500">
            <h2 class="section-title">🏗️ مواد البناء والسلع</h2>
            <div class="price-item"><span>🧱 إسمنت (قنطار)</span><span class="price-val">45.00</span></div>
            <div class="price-item"><span>⛓️ حديد (طن)</span><span class="price-val">4100</span></div>
            <div class="price-item"><span>🌻 زيت (لتر)</span><span class="price-val">7.50</span></div>
        </div>

        <div class="glass p-5 mt-6 border-l-4 border-cyan-500">
            <h2 class="section-title">🪙 العملات الرقمية</h2>
            <div class="price-item"><span>₿ Bitcoin (BTC)</span><span class="price-val">$96,430</span></div>
            <div class="price-item"><span>Ξ Ethereum (ETH)</span><span class="price-val">$3,345</span></div>
            <div class="price-item"><span>☀️ Solana (SOL)</span><span class="price-val">$242.15</span></div>
        </div>

        <div class="glass p-6 border-2 border-cyan-500/30 mt-8 mb-12">
            <h3 class="text-cyan-400 text-sm font-black mb-6 text-center uppercase">🔄 حاسبة TORO الأسطورية</h3>
            <div class="calc-box"><input type="number" id="lyd" oninput="runCalc('lyd')" placeholder="0.00"><span class="text-cyan-400 font-bold ml-2">LYD</span></div>
            <div class="grid grid-cols-2 gap-4 mt-4">
                <div class="calc-box"><input type="number" id="usd" oninput="runCalc('usd')" placeholder="0.00"><span class="text-cyan-400 font-bold ml-2">USD</span></div>
                <div class="calc-box"><input type="number" id="eur" oninput="runCalc('eur')" placeholder="0.00"><span class="text-cyan-400 font-bold ml-2">EUR</span></div>
            </div>
        </div>

        <p class="text-gray-700 text-[10px] pb-10 text-center uppercase tracking-[0.3em] font-bold">TORO LY LEGEND © 2026</p>
    </div>

    <script>
        setInterval(() => {
            const p = (8.60 + Math.random() * 0.1).toFixed(2);
            if(document.getElementById('val-usd')) document.getElementById('val-usd').innerText = p;
            if(document.getElementById('top-usd')) document.getElementById('top-usd').innerText = p;
        }, 8000);

        const rateUsd = 8.65, rateEur = 9.12;
        function runCalc(id) {
            const l = document.getElementById('lyd'), u = document.getElementById('usd'), e = document.getElementById('eur');
            let v = parseFloat(document.getElementById(id).value) || 0;
            if(id === 'lyd'){ u.value = (v / rateUsd).toFixed(2); e.value = (v / rateEur).toFixed(2); }
            else if(id === 'usd'){ l.value = (v * rateUsd).toFixed(2); e.value = ((v * rateUsd) / rateEur).toFixed(2); }
            else if(id === 'eur'){ l.value = (v * rateEur).toFixed(2); u.value = ((v * rateEur) / rateUsd).toFixed(2); }
        }
    </script>
</body>
</html>
"""

st.components.v1.html(full_code, height=2700, scrolling=True)
