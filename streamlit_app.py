import streamlit as st

# 1. إعدادات الصفحة الاحترافية - TORO LIBYA
st.set_page_config(
    page_title="Toro Libya - منصة وول ستريت ليبيا", 
    page_icon="🐂", 
    layout="centered"
)

# 2. الكود البرمجي المتكامل (HTML/CSS/JS)
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
        
        /* تصميم اللوجو في الأعلى */
        .header-logo-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding-top: 60px;
            margin-bottom: 20px;
        }
        .main-logo {
            width: 200px;
            border-radius: 20px;
            border: 2px solid #22d3ee;
            box-shadow: 0px 0px 30px rgba(34, 211, 238, 0.4);
            margin-bottom: 20px;
        }

        .glass { background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; margin-bottom: 20px; transition: 0.3s ease; }
        .glass:hover { transform: translateY(-3px); border-color: rgba(34, 211, 238, 0.4); }
        .section-title { border-right: 4px solid #22d3ee; padding-right: 12px; margin-bottom: 15px; font-weight: 900; color: #22d3ee; }
        .price-item { display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
        
        .marquee-wrapper { width: 100%; position: fixed; top: 0; left: 0; background: rgba(8, 51, 68, 0.95); border-bottom: 1px solid #22d3ee; z-index: 9999; padding: 8px 0; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
        .animate-marquee { display: inline-block; white-space: nowrap; animation: marquee 25s linear infinite; font-size: 13px; font-weight: bold; color: #22d3ee; }
        
        .live-indicator { display: inline-flex; align-items: center; gap: 5px; color: #4ade80; font-size: 11px; font-weight: bold; margin-bottom: 10px; }
        .dot { width: 8px; height: 8px; background: #4ade80; border-radius: 50%; display: inline-block; animation: pulse 1.5s infinite; }
        @keyframes pulse { 0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.7); } 70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(74, 222, 128, 0); } 100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(74, 222, 128, 0); } }

        .main-container { padding: 20px; display: flex; flex-direction: column; items: center; width: 100%; max-width: 500px; margin: auto; }
        .market-pulse-bar { height: 6px; width: 100%; background: #1e293b; border-radius: 10px; margin: 10px 0; overflow: hidden; }
        .pulse-fill { height: 100%; width: 75%; background: linear-gradient(90deg, #22d3ee, #4ade80); }
        .calc-box { background: #111827; border: 1px solid #374151; border-radius: 12px; display: flex; align-items: center; padding: 0 15px; margin-bottom: 10px; }
        .calc-box input { background: transparent !important; border: none !important; padding: 12px 5px !important; width: 100% !important; color: white !important; direction: ltr !important; text-align: center !important; outline: none !important; font-weight: bold; }
    </style>
</head>
<body>
    <div class="marquee-wrapper">
        <div class="animate-marquee">
            📢 عاجل: Toro Libya متصل الآن بغرف الواتساب الموثوقة لتحديث الأسعار لحظياً .. 🐂 تورو ليبيا: وجهتك الاقتصادية الأولى والوحيدة ..
        </div>
    </div>

    <div class="header-logo-container">
        <img src="https://raw.githubusercontent.com/molamilan89-gif/toro-libya/main/1000105722.jpg" class="main-logo" alt="Toro Logo">
        <h1 class="text-4xl font-black tracking-widest uppercase">Toro <span class="text-cyan-400">Ly</span></h1>
        <p class="text-gray-500 text-[10px] mt-1 uppercase tracking-widest text-center">THE LEGEND OF LIBYAN MARKET</p>
    </div>

    <div class="main-container">
        <div class="live-indicator"><span class="dot"></span> مزامنة فورية مع سوق المشير</div>

        <div class="grid grid-cols-3 gap-3 w-full mb-8">
            <div class="bg-slate-800/50 p-3 rounded-xl border border-white/5 text-center">
                <p class="text-[10px] text-gray-400 uppercase">USD</p>
                <p id="card-usd" class="text-sm font-bold text-cyan-400">8.65</p>
            </div>
            <div class="bg-slate-800/50 p-3 rounded-xl border border-white/5 text-center">
                <p class="text-[10px] text-gray-400 uppercase">GOLD 18</p>
                <p id="card-gold" class="text-sm font-bold text-yellow-500">415.5</p>
            </div>
            <div class="bg-slate-800/50 p-3 rounded-xl border border-white/5 text-center">
                <p class="text-[10px] text-gray-400 uppercase">BTC</p>
                <p id="card-btc" class="text-sm font-bold text-green-400">96.4K</p>
            </div>
        </div>

        <div class="w-full">
            <div class="glass p-5 border-l-4 border-cyan-500">
                <h2 class="section-title">🌟 نبض السوق والتوصيات</h2>
                <div class="flex justify-between items-center text-xs mb-1">
                    <span>حالة الاستقرار</span>
                    <span class="text-cyan-400">75% مستقر</span>
                </div>
                <div class="market-pulse-bar"><div class="pulse-fill"></div></div>
                <p class="text-[11px] text-gray-400 mt-2 italic">⚠️ جاري تحليل أحدث رسائل الواتساب الواردة من الغرفة الموثوقة...</p>
                <a href="https://wa.me/218XXXXXXXXX" class="block w-full text-center bg-green-600/20 text-green-400 text-xs py-2 rounded-lg mt-3 border border-green-600/30">💬 تواصل مع الإدارة</a>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">📊 تحليل السوق المباشر</h2>
                <canvas id="cryptoStyleChart" width="400" height="220"></canvas>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">💵 العملات العالمية</h2>
                <div class="price-item"><span>🇺🇸 دولار موازي</span><span class="font-bold text-cyan-400">8.65</span></div>
                <div class="price-item"><span>🇪🇺 يورو موازي</span><span class="font-bold">9.12</span></div>
                <div class="price-item"><span>✨ ذهب كسر (عيار 18)</span><span class="font-bold text-yellow-400">415.5</span></div>
            </div>

            <div class="glass p-6 border-2 border-cyan-500/40">
                <h3 class="text-cyan-400 text-xs font-bold mb-4 text-center">🔄 محول العملات اللحظي</h3>
                <div class="calc-box"><input type="text" id="lyd" oninput="runCalc('lyd')" placeholder="0.00"><span class="text-cyan-400 font-bold">LYD</span></div>
                <div class="grid grid-cols-2 gap-3">
                    <div class="calc-box"><span class="text-cyan-400 font-bold">$</span><input type="text" id="usd" oninput="runCalc('usd')" placeholder="0.00"></div>
                    <div class="calc-box"><span class="text-cyan-400 font-bold">€</span><input type="text" id="eur" oninput="runCalc('eur')" placeholder="0.00"></div>
                </div>
            </div>
        </div>
        <p class="text-gray-600 text-[10px] mt-10 text-center">Toro Ly Auto-Sync © 2026</p>
    </div>

    <script>
        // تشغيل التشارت
        const ctx = document.getElementById('cryptoStyleChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['10:00', '12:00', '14:00', '16:00', '18:00', '20:00'],
                datasets: [{
                    label: 'USD/LYD',
                    data: [8.60, 8.65, 8.63, 8.67, 8.65, 8.68],
                    borderColor: '#22d3ee',
                    backgroundColor: 'rgba(34, 211, 238, 0.1)',
                    fill: true,
                    tension: 0.4
                }]
            },
            options: { responsive: true, plugins: { legend: { display: false } } }
        });

        // نظام الحاسبة
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
