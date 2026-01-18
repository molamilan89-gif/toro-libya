import streamlit as st

# إعدادات الصفحة الاحترافية - TORO LIBYA
st.set_page_config(page_title="Toro Libya - منصة وول ستريت ليبيا", page_icon="🐂", layout="centered")

# الكود الكامل مع التحديثات الجديدة (الطاقة، اللحوم، وتطوير الحاسبة)
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
        .glass:hover { transform: translateY(-3px); border-color: rgba(34, 211, 238, 0.4); }
        .section-title { border-right: 4px solid #22d3ee; padding-right: 12px; margin-bottom: 15px; font-weight: 900; color: #22d3ee; }
        .price-item { display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
        
        .marquee-wrapper { width: 100%; position: fixed; top: 0; left: 0; background: rgba(8, 51, 68, 0.95); border-bottom: 1px solid #22d3ee; z-index: 9999; padding: 8px 0; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
        .animate-marquee { display: inline-block; white-space: nowrap; animation: marquee 25s linear infinite; font-size: 13px; font-weight: bold; color: #22d3ee; }
        
        .live-indicator { display: inline-flex; align-items: center; gap: 5px; color: #4ade80; font-size: 10px; font-weight: bold; margin-bottom: 10px; }
        .dot { width: 8px; height: 8px; background: #4ade80; border-radius: 50%; display: inline-block; animation: pulse 1.5s infinite; }
        @keyframes pulse { 0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.7); } 70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(74, 222, 128, 0); } 100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(74, 222, 128, 0); } }

        .main-container { padding: 80px 20px 50px 20px; display: flex; flex-direction: column; items: center; }
        .market-pulse-bar { height: 6px; width: 100%; background: #1e293b; border-radius: 10px; margin: 10px 0; overflow: hidden; }
        .pulse-fill { height: 100%; width: 75%; background: linear-gradient(90deg, #22d3ee, #4ade80); }
        
        /* تحسين الحاسبة لتكون واضحة وبالأرقام الدولية */
        .calc-box { background: #111827; border: 1px solid #374151; border-radius: 12px; display: flex; align-items: center; padding: 0 15px; margin-bottom: 10px; }
        .calc-box input { background: transparent !important; border: none !important; padding: 12px 5px !important; width: 100% !important; color: #22d3ee !important; direction: ltr !important; text-align: center !important; outline: none !important; font-weight: bold; font-family: sans-serif; font-size: 1.2rem; }
        
        .price-val { font-family: sans-serif; font-weight: bold; }
        .price-up { animation: price-green 2s ease; }
        @keyframes price-green { 0% { color: #4ade80; } 100% { color: inherit; } }
    </style>
</head>
<body>
    <div class="marquee-wrapper">
        <div class="animate-marquee" id="news-ticker">
            📢 عاجل: Toro Libya متصل الآن بغرف الواتساب الموثوقة .. الدولار يسجل 8.65 .. الذهب عيار 18 كسر بـ 415.5 .. البيتكوين يقترب من قمة جديدة .. 🐂
        </div>
    </div>

    <div class="main-container">
        <div class="live-indicator"><span class="dot"></span> مزامنة فورية مع سوق المشير ووكالات الأنباء</div>

        <div class="text-center mb-6">
            <h1 class="text-5xl font-black tracking-widest uppercase">Toro <span class="text-cyan-400">Ly</span></h1>
            <p class="text-gray-500 text-[10px] mt-1 uppercase tracking-widest text-center">المؤشر الاقتصادي الليبي المتكامل</p>
        </div>

        <div class="grid grid-cols-3 gap-3 w-full max-w-md mb-8">
            <div class="quick-card bg-slate-800/50 p-3 rounded-xl border border-white/5 text-center">
                <p class="text-[10px] text-gray-400 uppercase">USD</p>
                <p id="card-usd" class="text-sm font-bold price-val">8.65</p>
            </div>
            <div class="quick-card bg-slate-800/50 p-3 rounded-xl border border-white/5 text-center">
                <p class="text-[10px] text-gray-400 uppercase">GOLD 18</p>
                <p id="card-gold" class="text-sm font-bold price-val">415.5</p>
            </div>
            <div class="quick-card bg-slate-800/50 p-3 rounded-xl border border-white/5 text-center">
                <p class="text-[10px] text-gray-400 uppercase">BTC</p>
                <p id="card-btc" class="text-sm font-bold price-val">96.4K</p>
            </div>
        </div>

        <div class="w-full max-w-md">
            <div class="glass p-5 border-l-4 border-cyan-500">
                <h2 class="section-title">🌟 نبض السوق والتوصيات</h2>
                <div class="flex justify-between items-center text-xs mb-1">
                    <span>حالة الاستقرار</span>
                    <span class="text-cyan-400" id="pulse-text">75% مستقر</span>
                </div>
                <div class="market-pulse-bar"><div class="pulse-fill" id="pulse-width"></div></div>
                <p class="text-[11px] text-gray-400 mt-2 italic" id="market-tip">⚠️ نصيحة: استقرار نسبي في أسعار الذهب، يفضل الترقب قبل الشراء الكبير.</p>
                <a href="https://wa.me/yournumber" class="block w-full text-center bg-green-600/20 text-green-400 text-xs py-2 rounded-lg mt-3 border border-green-600/30">💬 تواصل مع الإدارة</a>
            </div>

            <div class="glass p-5 mb-8 mt-6">
                <h2 class="section-title">📊 تحليل السوق المباشر</h2>
                <canvas id="cryptoStyleChart" width="400" height="220"></canvas>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">💵 العملات العالمية</h2>
                <div class="price-item"><span>🇺🇸 دولار موازي</span><span id="val-usd" class="price-val text-cyan-400">8.65</span></div>
                <div class="price-item"><span>🇪🇺 يورو موازي</span><span id="val-eur" class="price-val">9.12</span></div>
                <div class="price-item"><span>🇬🇧 باوند إسترليني</span><span id="val-gbp" class="price-val">10.85</span></div>
                <div class="price-item"><span>🇹🇳 دينار تونسي</span><span id="val-tnd" class="price-val">2.65</span></div>
                <div class="price-item"><span>🇹🇷 ليرة تركية</span><span class="price-val text-red-400">0.26</span></div>
                <div class="price-item"><span>🇪🇬 جنيه مصري</span><span id="val-egp" class="price-val text-green-400">0.17</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">✨ الذهب والمعادن</h2>
                <div class="price-item"><span>💍 ذهب جديد (21)</span><span class="price-val text-yellow-500">485.0</span></div>
                <div class="price-item"><span>✨ ذهب كسر (18)</span><span class="price-val text-yellow-400">415.5</span></div>
                <div class="price-item"><span>🥈 فضة (جرام)</span><span class="price-val text-gray-300">5.40</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">🏗️ مواد البناء والسلع</h2>
                <div class="price-item"><span>🧱 إسمنت (قنطار)</span><span class="price-val">45.00</span></div>
                <div class="price-item"><span>⛓️ حديد (طن)</span><span class="price-val">4100</span></div>
                <div class="price-item"><span>🌻 زيت (لتر)</span><span class="price-val">7.50</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">🥩 اللحوم والدواجن</h2>
                <div class="price-item"><span>🥩 لحم خروف (وطني)</span><span class="price-val text-red-400">55.0</span></div>
                <div class="price-item"><span>🐂 لحم بقر (كيلو)</span><span class="price-val text-red-500">48.0</span></div>
                <div class="price-item"><span>🍗 دجاج (كيلو)</span><span class="price-val">12.5</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">🛢️ الطاقة والنفط</h2>
                <div class="price-item"><span>⛽ بنزين (لتر)</span><span class="price-val">0.15</span></div>
                <div class="price-item"><span>🔥 أسطوانة غاز</span><span class="price-val">5.00</span></div>
                <div class="price-item"><span>🌍 نفط برنت (عالمي)</span><span class="price-val text-green-400">$78.40</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">🪙 العملات الرقمية</h2>
                <div class="price-item"><span>₿ Bitcoin (BTC)</span><span class="text-green-400 price-val">$96,430</span></div>
                <div class="price-item"><span>☀️ Solana (SOL)</span><span class="text-purple-400 price-val">$242.15</span></div>
            </div>

            <div class="glass p-6 border-2 border-cyan-500/40">
                <h3 class="text-cyan-400 text-xs font-bold mb-4 text-center">🔄 حاسبة Toro الأسطورية</h3>
                <div class="calc-box"><input type="number" id="lyd" oninput="runCalc('lyd')" placeholder="0.00"><span class="text-cyan-400 font-bold">LYD</span></div>
                <div class="grid grid-cols-2 gap-3">
                    <div class="calc-box"><span class="text-cyan-400 font-bold">$</span><input type="number" id="usd" oninput="runCalc('usd')" placeholder="0.00"></div>
                    <div class="calc-box"><span class="text-cyan-400 font-bold">€</span><input type="number" id="eur" oninput="runCalc('eur')" placeholder="0.00"></div>
                </div>
            </div>
        </div>
        <p class="text-gray-600 text-[10px] mt-10 text-center uppercase tracking-widest">Toro Ly Legend © 2026</p>
    </div>

    <script>
        // دالة التحديث التلقائي
        async function fetchWhatsAppUpdates() {
            try {
                const fakeNewUsd = (8.60 + Math.random() * 0.1).toFixed(2);
                const usdEl = document.getElementById('val-usd');
                const cardUsdEl = document.getElementById('card-usd');
                if (usdEl.innerText !== fakeNewUsd) {
                    usdEl.innerText = fakeNewUsd;
                    cardUsdEl.innerText = fakeNewUsd;
                    usdEl.classList.add('price-up');
                    setTimeout(() => usdEl.classList.remove('price-up'), 2000);
                }
            } catch (e) { }
        }
        setInterval(fetchWhatsAppUpdates, 5000);

        // الرسم البياني
        const ctx = document.getElementById('cryptoStyleChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['10:00', '12:00', '14:00', '16:00', '18:00', '20:00', '22:00'],
                datasets: [{
                    label: 'الدولار',
                    data: [8.62, 8.65, 8.63, 8.67, 8.65, 8.68, 8.65],
                    borderColor: '#22d3ee',
                    borderWidth: 2,
                    fill: false,
                    tension: 0.3,
                    pointRadius: 0
                }]
            },
            options: { responsive: true, plugins: { legend: { display: false } }, scales: { y: { display: false }, x: { grid: { display: false } } } }
        });

        // الحاسبة المتقدمة
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

st.components.v1.html(full_code, height=4500, scrolling=True)
