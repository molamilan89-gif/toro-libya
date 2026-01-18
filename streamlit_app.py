import streamlit as st

# إعدادات الصفحة الاحترافية - TORO LIBYA
st.set_page_config(page_title="Toro Ly - The Legend", page_icon="🐂", layout="centered")

# الكود الكامل مع اللوجو العالمي الجديد ونظام التحديث اللحظي
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
        :root { --main-cyan: #22d3ee; --gold: #facc15; --dark-bg: #0b1120; }
        body { font-family: 'Tajawal', sans-serif; background: var(--dark-bg); color: white; margin: 0; padding: 0; overflow-x: hidden; }
        
        /* تصميم اللوجو العالمي المقتبس من الصورة */
        .header-logo-section { display: flex; flex-direction: column; align-items: center; padding: 40px 0 20px 0; }
        .logo-frame { 
            position: relative; width: 140px; height: 140px; 
            background: rgba(30, 41, 59, 0.6); border-radius: 25px; 
            border: 2px solid rgba(255,255,255,0.1); 
            display: flex; align-items: center; justify-content: center;
            box-shadow: 0 20px 40px rgba(0,0,0,0.6), inset 0 0 20px rgba(34, 211, 238, 0.1);
            backdrop-filter: blur(10px);
        }
        .bull-head { width: 90px; height: 90px; filter: drop-shadow(0 0 10px rgba(34, 211, 238, 0.4)); }
        
        .brand-title-area { margin-top: 15px; text-align: center; }
        .brand-main-text { font-size: 42px; font-weight: 900; letter-spacing: -1px; display: flex; align-items: center; gap: 8px; }
        .brand-ly-badge { background: var(--main-cyan); color: var(--dark-bg); padding: 2px 8px; border-radius: 6px; font-size: 24px; display: flex; align-items: center; }

        /* العناصر الزجاجية */
        .glass-panel { background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 24px; padding: 20px; margin-bottom: 20px; }
        .section-header { border-right: 4px solid var(--main-cyan); padding-right: 12px; margin-bottom: 15px; font-weight: 900; color: var(--main-cyan); font-size: 18px; }
        .section-header.gold { border-right-color: var(--gold); color: var(--gold); }
        
        .price-row { display: flex; justify-content: space-between; align-items: center; padding: 12px 10px; border-bottom: 1px solid rgba(255, 255, 255, 0.03); }
        .val-text { font-family: 'Verdana', sans-serif; font-weight: bold; font-size: 18px; }
        .gold-color { color: var(--gold) !important; }

        /* شريط الأخبار العلوي */
        .ticker-wrap { position: fixed; top: 0; width: 100%; background: #083344; border-bottom: 1px solid var(--main-cyan); z-index: 1000; padding: 6px 0; }
        .ticker { display: inline-block; white-space: nowrap; animation: marquee 30s linear infinite; font-weight: bold; color: var(--main-cyan); font-size: 13px; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

        /* الحاسبة */
        .calc-input-box { background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 15px; display: flex; align-items: center; padding: 12px 15px; margin-bottom: 10px; }
        .calc-input-box input { background: transparent; border: none; width: 100%; color: white; text-align: center; font-size: 20px; font-weight: 800; outline: none; }
        
        .status-tag { padding: 4px 10px; border-radius: 8px; font-size: 11px; font-weight: bold; background: rgba(34, 211, 238, 0.1); color: var(--main-cyan); border: 1px solid rgba(34, 211, 238, 0.2); }
    </style>
</head>
<body>
    <div class="ticker-wrap">
        <div class="ticker">
             📢 تورو ليبيا: تحديثات مباشرة من قلب السوق .. الدولار 8.65 .. الذهب كسر بـ 415.5 .. سولانا تشهد صعوداً قوياً .. مزامنة غرف الواتساب نشطة الآن ..
        </div>
    </div>

    <div class="max-w-md mx-auto px-5 pt-20">
        <div class="header-logo-section">
            <div class="logo-frame">
                <svg class="bull-head" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                    <path d="M40,60 Q100,20 160,60 L150,90 Q100,70 50,90 Z" fill="white"/> <path d="M60,80 L140,80 L130,150 L100,170 L70,150 Z" fill="#ccc"/> <path d="M80,100 L120,100 L115,130 L85,130 Z" fill="#1e293b"/> <path d="M90,70 L110,40 L130,60 L160,20" stroke="#22d3ee" stroke-width="8" fill="none" stroke-linecap="round"/> <polygon points="160,20 150,35 170,25" fill="#22d3ee"/>
                </svg>
            </div>
            <div class="brand-title-area">
                <div class="brand-main-text">TORO <span class="brand-ly-badge">LY</span></div>
                <p class="text-[10px] text-gray-500 font-bold tracking-[0.3em] mt-2">THE LEGEND OF LIBYAN MARKET</p>
            </div>
        </div>

        <div class="grid grid-cols-3 gap-3 mb-8">
            <div class="glass-panel !p-3 text-center border-b-2 border-cyan-500">
                <p class="text-[10px] text-gray-400 font-bold">BTC</p>
                <p class="text-sm font-bold">96.4K</p>
            </div>
            <div class="glass-panel !p-3 text-center border-b-2 border-yellow-500">
                <p class="text-[10px] text-yellow-500 font-bold">GOLD 18</p>
                <p class="text-sm font-bold gold-color">415.5</p>
            </div>
            <div class="glass-panel !p-3 text-center border-b-2 border-cyan-500">
                <p class="text-[10px] text-gray-400 font-bold">USD</p>
                <p id="top-usd" class="text-sm font-bold">8.65</p>
            </div>
        </div>

        <div class="glass-panel">
            <div class="section-header">⚡ الخدمات ونبض السوق</div>
            <div class="price-row border-none"><span>طرح الأحمال</span><span class="status-tag">ساعة واحدة</span></div>
            <div class="price-row border-none"><span>محطات الوقود</span><span class="status-tag">متوفرة - مستقر</span></div>
            <div class="mt-4 p-3 bg-green-500/10 rounded-xl border border-green-500/20 text-center">
                <p class="text-[11px] text-green-400 font-bold">● متصل الآن بغرفة الواتساب الموثوقة</p>
            </div>
        </div>

        <div class="glass-panel">
            <div class="section-header">💵 العملات الموازية</div>
            <div class="price-row"><span>🇺🇸 دولار موازي</span><span id="val-usd" class="val-text text-cyan-400">8.65</span></div>
            <div class="price-row"><span>🇪🇺 يورو موازي</span><span class="val-text">9.12</span></div>
            <div class="price-row"><span>🇹🇳 دينار تونسي</span><span class="val-text">2.65</span></div>
            <div class="price-row"><span>🇪🇬 جنيه مصري</span><span class="val-text text-green-400">0.17</span></div>
        </div>

        <div class="glass-panel">
            <div class="section-header gold">✨ الذهب والمعادن</div>
            <div class="price-row"><span>💍 ذهب جديد (21)</span><span class="val-text gold-color">485.0</span></div>
            <div class="price-item py-3 flex justify-between px-2"><span>✨ ذهب كسر (18)</span><span class="val-text gold-color">415.5</span></div>
            <div class="price-row"><span>🥈 فضة (جرام)</span><span class="val-text text-gray-400">5.40</span></div>
            <div class="price-row"><span>🥉 نحاس (كيلو)</span><span class="val-text text-gray-400">42.0</span></div>
        </div>

        <div class="glass-panel">
            <div class="section-header">🪙 العملات الرقمية</div>
            <div class="price-row"><span>₿ Bitcoin (BTC)</span><span class="val-text text-green-400">$96,430</span></div>
            <div class="price-row"><span>Ξ Ethereum (ETH)</span><span class="val-text text-blue-400">$3,345</span></div>
            <div class="price-row"><span>☀️ Solana (SOL)</span><span class="val-text text-purple-400">$242.15</span></div>
        </div>

        <div class="glass-panel">
            <div class="section-header">🏗️ مواد البناء والسلع</div>
            <div class="price-row"><span>🧱 إسمنت (قنطار)</span><span class="val-text">45.00</span></div>
            <div class="price-row"><span>⛓️ حديد (طن)</span><span class="val-text">4100</span></div>
            <div class="price-row"><span>🌻 زيت (لتر)</span><span class="val-text">7.50</span></div>
        </div>

        <div class="glass-panel border-2 border-cyan-500/30">
            <h3 class="text-center text-xs font-black text-cyan-400 mb-6 uppercase tracking-widest">🔄 محول Toro الذكي</h3>
            <div class="calc-input-group">
                <div class="calc-input-box"><input type="number" id="lyd" oninput="runCalc('lyd')" placeholder="0.00"><span class="text-xs font-bold text-cyan-400">LYD</span></div>
                <div class="grid grid-cols-2 gap-3">
                    <div class="calc-input-box"><input type="number" id="usd" oninput="runCalc('usd')" placeholder="0.00"><span class="text-xs font-bold text-gray-500">USD</span></div>
                    <div class="calc-input-box"><input type="number" id="eur" oninput="runCalc('eur')" placeholder="0.00"><span class="text-xs font-bold text-gray-500">EUR</span></div>
                </div>
            </div>
        </div>

        <footer class="text-center py-12 opacity-20 text-[10px] font-bold tracking-[0.5em]">TORO LY LEGEND © 2026</footer>
    </div>

    <script>
        // نظام التحديث اللحظي للمحاكاة
        setInterval(() => {
            const p = (8.60 + Math.random() * 0.1).toFixed(2);
            if(document.getElementById('val-usd')) document.getElementById('val-usd').innerText = p;
            if(document.getElementById('top-usd')) document.getElementById('top-usd').innerText = p;
        }, 7000);

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

st.components.v1.html(full_code, height=3200, scrolling=True)
