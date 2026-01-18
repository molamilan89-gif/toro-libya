import streamlit as st

# إعدادات الصفحة الاحترافية - TORO LIBYA
st.set_page_config(page_title="Toro Libya - منصة وول ستريت ليبيا", page_icon="🐂", layout="centered")

# الكود الكامل والنهائي الشامل لجميع الأقسام والميزات
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

        .quick-card { background: rgba(255, 255, 255, 0.05); border-radius: 12px; padding: 10px; text-align: center; border: 1px solid rgba(255, 255, 255, 0.1); }
        .trend-up { color: #4ade80; font-size: 0.7rem; }

        .main-container { padding: 80px 20px 50px 20px; display: flex; flex-direction: column; items: center; }
        
        .market-pulse-bar { height: 6px; width: 100%; background: #1e293b; border-radius: 10px; margin: 10px 0; overflow: hidden; }
        .pulse-fill { height: 100%; width: 75%; background: linear-gradient(90deg, #22d3ee, #4ade80); }

        .calc-wrapper { width: 100%; max-width: 448px; margin-top: 10px; }
        .calc-box { background: #111827; border: 1px solid #374151; border-radius: 12px; display: flex; align-items: center; padding: 0 15px; margin-bottom: 10px; }
        .calc-box input { background: transparent !important; border: none !important; padding: 12px 5px !important; width: 100% !important; color: white !important; font-family: sans-serif !important; direction: ltr !important; text-align: center !important; outline: none !important; font-weight: bold; font-size: 1.1rem; }
        .symbol { color: #22d3ee; font-weight: bold; font-size: 1.1rem; min-width: 35px; text-align: center; }
    </style>
</head>
<body>
    <div class="marquee-wrapper">
        <div class="animate-marquee">
            📢 عاجل: Toro Libya يعزز ثقة المتداولين بنظام التوصيات الجديد .. 🛢️ برنت $78.40 .. 💍 ذهب عيار 18 كسر بـ 415.5 دينار .. 🏗️ أسعار الإسمنت والحديد اليوم في ليبيا .. 🐂 تورو ليبيا: وجهتك الاقتصادية الأولى ..
        </div>
    </div>

    <div class="main-container">
        <div class="live-indicator"><span class="dot"></span> مباشر - تحديث تلقائي</div>

        <div class="text-center mb-6">
            <h1 class="text-5xl font-black tracking-widest uppercase">Toro <span class="text-cyan-400">Ly</span></h1>
            <p class="text-gray-500 text-[10px] mt-1 uppercase tracking-widest text-center">المؤشر الاقتصادي الليبي المتكامل</p>
        </div>

        <div class="grid grid-cols-3 gap-3 w-full max-w-md mb-8">
            <div class="quick-card">
                <p class="text-[10px] text-gray-400">USD/LYD</p>
                <p class="text-sm font-bold">8.65</p>
                <p class="trend-up">▲ 0.02%</p>
            </div>
            <div class="quick-card">
                <p class="text-[10px] text-gray-400">GOLD 18</p>
                <p class="text-sm font-bold">415.5</p>
                <p class="trend-up">▲ 1.10%</p>
            </div>
            <div class="quick-card">
                <p class="text-[10px] text-gray-400">BTC/USD</p>
                <p class="text-sm font-bold">96.4K</p>
                <p class="trend-up">▲ 0.45%</p>
            </div>
        </div>

        <div class="w-full max-w-md">
            <div class="glass p-5 border-l-4 border-cyan-500">
                <h2 class="section-title">🌟 نبض السوق والتوصيات</h2>
                <div class="flex justify-between items-center text-xs mb-1">
                    <span>حالة الاستقرار</span>
                    <span class="text-cyan-400">75% مستقر</span>
                </div>
                <div class="market-pulse-bar">
                    <div class="pulse-fill"></div>
                </div>
                <p class="text-[11px] text-gray-400 mt-2 italic">⚠️ نصيحة اليوم: استقرار نسبي في سعر الصرف، الوقت ملائم لشراء الذهب كادخار طويل الأمد.</p>
                <a href="https://wa.me/yournumber" class="block w-full text-center bg-green-600/20 text-green-400 text-xs py-2 rounded-lg mt-3 border border-green-600/30 hover:bg-green-600/40 transition">💬 استشارة مباشرة (واتساب)</a>
            </div>

            <div class="glass p-5 mb-8">
                <h2 class="section-title">📊 تحليل السوق المباشر</h2>
                <canvas id="cryptoStyleChart" width="400" height="220"></canvas>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">💵 العملات العالمية</h2>
                <div class="price-item"><span>🇺🇸 دولار موازي</span><span class="font-bold text-cyan-400">8.65</span></div>
                <div class="price-item"><span>🇪🇺 يورو موازي</span><span class="font-bold">9.12</span></div>
                <div class="price-item"><span>🇬🇧 باوند إسترليني</span><span class="font-bold">10.85</span></div>
                <div class="price-item"><span>🇹🇳 دينار تونسي</span><span class="font-bold text-blue-300">2.65</span></div>
                <div class="price-item"><span>🇹🇷 ليرة تركية</span><span class="font-bold text-red-400">0.26</span></div>
                <div class="price-item"><span>🇪🇬 جنيه مصري</span><span class="font-bold text-green-400">0.17</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">✨ الذهب والمعادن</h2>
                <div class="price-item"><span>💍 ذهب جديد (عيار 21)</span><span class="font-bold text-yellow-500">485.0</span></div>
                <div class="price-item"><span>🛠️ ذهب مستعمل (عيار 18)</span><span class="font-bold text-yellow-600">425.0</span></div>
                <div class="price-item"><span>✨ ذهب كسر (عيار 18)</span><span class="font-bold text-yellow-400">415.5</span></div>
                <div class="price-item"><span>🥈 فضة (جرام)</span><span class="font-bold text-gray-300">5.40</span></div>
                <div class="price-item"><span>🥉 نحاس (كيلو)</span><span class="font-bold text-orange-500">42.0</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">🪙 العملات الرقمية</h2>
                <div class="price-item"><span>₿ Bitcoin (BTC)</span><span class="text-green-400 font-bold">$96,430</span></div>
                <div class="price-item"><span>Ξ Ethereum (ETH)</span><span class="text-blue-400 font-bold">$3,345</span></div>
                <div class="price-item"><span>💠 Solana (SOL)</span><span class="text-green-400 font-bold">$195.20</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">⛽ الطاقة والنفط</h2>
                <div class="price-item"><span>🛢️ خام برنت</span><span class="font-bold text-green-400">$78.40</span></div>
                <div class="price-item"><span>🔥 غاز الطهي</span><span class="font-bold">5.00 LYD</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">🏗️ مواد البناء</h2>
                <div class="price-item"><span>🧱 إسمنت (قنطار)</span><span class="font-bold">45.00</span></div>
                <div class="price-item"><span>⛓️ حديد (الطن)</span><span class="font-bold">4100</span></div>
                <div class="price-item"><span>🧱 طوب (1000 قطعة)</span><span class="font-bold">1850</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">🛒 السلع الأساسية</h2>
                <div class="price-item"><span>🌻 زيت (لتر)</span><span class="font-bold">7.50</span></div>
                <div class="price-item"><span>🍚 أرز (كيلو)</span><span class="font-bold">5.00</span></div>
                <div class="price-item"><span>🥛 حليب (علبة)</span><span class="font-bold">4.50</span></div>
            </div>

            <div class="calc-wrapper glass p-6 border-2 border-cyan-500/40">
                <h3 class="text-cyan-400 text-xs font-bold mb-4 text-center">🔄 محول العملات الذكي</h3>
                <div class="calc-box"><input type="text" id="lyd" oninput="runCalc('lyd')" placeholder="0.00"><span class="symbol">LYD</span></div>
                <div class="grid grid-cols-2 gap-3">
                    <div class="calc-box"><span class="symbol">$</span><input type="text" id="usd" oninput="runCalc('usd')" placeholder="0.00"></div>
                    <div class="calc-box"><span class="symbol">€</span><input type="text" id="eur" oninput="runCalc('eur')" placeholder="0.00"></div>
                </div>
            </div>
        </div>
        
        <p class="text-gray-600 text-[10px] mt-10">Toro Ly Pro © 2026</p>
    </div>

    <script>
        const ctx = document.getElementById('cryptoStyleChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['10:00', '12:00', '14:00', '16:00', '18:00', '20:00', '22:00'],
                datasets: [{
                    label: 'السعر المباشر',
                    data: [8.62, 8.65, 8.63, 8.67, 8.65, 8.68, 8.65],
                    borderColor: '#4ade80',
                    borderWidth: 2,
                    fill: false,
                    tension: 0.1,
                    pointRadius: 2,
                    pointBackgroundColor: '#4ade80',
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { display: false } },
                scales: {
                    y: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#64748b', font: { size: 10 } } },
                    x: { grid: { display: false }, ticks: { color: '#64748b', font: { size: 10 } } }
                }
            }
        });

        const rateUsd = 8.65, rateEur = 9.12;
        function toEn(s) { return s.replace(/[٠-٩]/g, d => '٠١٢٣٤٥٦٧٨٩'.indexOf(d)).replace(/[^0-9.]/g, ''); }
        function runCalc(id) {
            const el = document.getElementById(id); el.value = toEn(el.value);
            let val = parseFloat(el.value) || 0;
            const l = document.getElementById('lyd'), u = document.getElementById('usd'), e = document.getElementById('eur');
            if(id === 'lyd'){ u.value = val > 0 ? (val / rateUsd).toFixed(2) : ""; e.value = val > 0 ? (val / rateEur).toFixed(2) : ""; }
            else if(id === 'usd'){ l.value = val > 0 ? (val * rateUsd).toFixed(2) : ""; e.value = val > 0 ? ((val * rateUsd) / rateEur).toFixed(2) : ""; }
            else if(id === 'eur'){ l.value = val > 0 ? (val * rateEur).toFixed(2) : ""; u.value = val > 0 ? ((val * rateEur) / rateUsd).toFixed(2) : ""; }
        }
    </script>
</body>
</html>
"""

st.components.v1.html(full_code, height=3500, scrolling=True)
