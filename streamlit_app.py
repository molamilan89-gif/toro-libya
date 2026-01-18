import streamlit as st

# إعدادات الصفحة الاحترافية - TORO LIBYA
st.set_page_config(page_title="Toro Libya - منصة وول ستريت ليبيا", page_icon="🐂", layout="centered")

# الكود الكامل: استعادة الشعار الأصلي + الأقسام السابقة + الإضافات الجديدة
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
        .glass { background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; margin-bottom: 20px; }
        .section-title { border-right: 4px solid #22d3ee; padding-right: 12px; margin-bottom: 15px; font-weight: 900; color: #22d3ee; display: flex; align-items: center; gap: 8px; }
        .price-item { display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
        
        /* استعادة الشعار الاحترافي من صورك */
        .main-logo-container { position: relative; width: 150px; height: 150px; margin: 20px auto; }
        .logo-box { width: 100%; height: 100%; background: radial-gradient(circle, rgba(34, 211, 238, 0.2) 0%, transparent 70%); border: 2px solid #22d3ee; border-radius: 40px; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 40px rgba(34, 211, 238, 0.2); }
        .logo-inner { width: 80px; height: 80px; background: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; }
        .logo-inner svg { width: 50px; height: 50px; color: #0b1120; }

        .marquee-wrapper { width: 100%; position: fixed; top: 0; left: 0; background: rgba(8, 51, 68, 0.95); border-bottom: 1px solid #22d3ee; z-index: 9999; padding: 8px 0; }
        .animate-marquee { display: inline-block; white-space: nowrap; animation: marquee 25s linear infinite; font-size: 13px; font-weight: bold; color: #22d3ee; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

        .status-badge { padding: 4px 12px; border-radius: 8px; font-size: 11px; font-weight: bold; }
        .price-val { font-family: 'Verdana', sans-serif; font-weight: bold; }
        
        /* تصميم البطاقات العلوية كما في الصورة */
        .top-card { background: rgba(30, 41, 59, 0.5); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 15px; padding: 15px; text-align: center; }
        
        .calc-box { background: #111827; border: 1px solid #374151; border-radius: 12px; display: flex; align-items: center; padding: 0 15px; margin-bottom: 10px; }
        .calc-box input { background: transparent !important; border: none !important; padding: 15px 5px !important; width: 100% !important; color: white !important; text-align: center !important; outline: none !important; font-size: 20px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="marquee-wrapper">
        <div class="animate-marquee">
             🐂 تورو ليبيا: وجهتك الاقتصادية الأولى .. الدولار 8.65 .. الذهب كسر 415.5 .. الإسمنت 45 .. ترقبوا تحديثات سلة المعيشة .. 📢
        </div>
    </div>

    <div class="main-container pt-24 px-5 max-w-md mx-auto">
        <div class="text-center mb-6">
            <div class="inline-flex items-center gap-2 bg-green-500/10 text-green-400 px-4 py-1 rounded-full text-[11px] font-bold border border-green-500/20 mb-4">
                <span class="w-2 h-2 bg-green-400 rounded-full animate-pulse"></span> نظام Toro Ly المباشر
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
            <div class="top-card border-b-2 border-green-500">
                <p class="text-[9px] text-gray-400 font-bold">BTC</p>
                <p class="text-sm font-bold price-val">96.4K</p>
            </div>
            <div class="top-card border-b-2 border-yellow-500">
                <p class="text-[9px] text-gray-400 font-bold">GOLD 18</p>
                <p class="text-sm font-bold price-val">415.5</p>
            </div>
            <div class="top-card border-b-2 border-cyan-500">
                <p class="text-[9px] text-gray-400 font-bold">USD</p>
                <p id="top-usd" class="text-sm font-bold price-val">8.65</p>
            </div>
        </div>

        <div class="glass p-5 border-l-4 border-yellow-500 shadow-lg shadow-yellow-500/5">
            <h2 class="section-title">⚡ الخدمات والطاقة</h2>
            <div class="flex justify-between items-center mb-4">
                <span class="text-xs font-bold text-gray-300">طرح الأحمال (الغربية)</span>
                <span class="status-badge bg-green-500/20 text-green-400 border border-green-500/30">ساعة واحدة</span>
            </div>
            <div class="flex justify-between items-center">
                <span class="text-xs font-bold text-gray-300">حالة محطات الوقود</span>
                <span class="status-badge bg-blue-500/20 text-blue-400 border border-blue-500/30">متوفر - ازدحام خفيف</span>
            </div>
        </div>

        <div class="glass p-5 mt-6 border-l-4 border-cyan-500">
            <h2 class="section-title">💵 أسعار العملات الموازية</h2>
            <div class="price-item">
                <span class="text-sm">🇺🇸 دولار موازي</span>
                <span id="val-usd" class="price-val text-cyan-400 text-lg">8.65</span>
            </div>
            <div class="price-item">
                <span class="text-sm">🇪🇺 يورو موازي</span>
                <span class="price-val text-lg">9.12</span>
            </div>
            <div class="price-item">
                <span class="text-sm">🇬🇧 باوند إسترليني</span>
                <span class="price-val text-lg text-blue-400">10.85</span>
            </div>
            <div class="price-item">
                <span class="text-sm">🇹🇳 دينار تونسي</span>
                <span class="price-val text-lg">2.65</span>
            </div>
            <div class="price-item">
                <span class="text-sm">🇪🇬 جنيه مصري</span>
                <span class="price-val text-lg text-green-400">0.17</span>
            </div>
        </div>

        <div class="glass p-5 mt-6 border-l-4 border-yellow-400">
            <h2 class="section-title">✨ الذهب والمعادن</h2>
            <div class="price-item"><span>💍 ذهب جديد (عيار 21)</span><span class="price-val text-yellow-500">485.0</span></div>
            <div class="price-item"><span>✨ ذهب كسر (عيار 18)</span><span class="price-val text-yellow-400">415.5</span></div>
            <div class="price-item"><span>🥈 فضة (جرام)</span><span class="price-val text-gray-300">5.40</span></div>
        </div>

        <div class="glass p-5 mt-6 border-l-4 border-orange-500">
            <h2 class="section-title">🏗️ مواد البناء والسلع</h2>
            <div class="price-item"><span>🧱 إسمنت (قنطار)</span><span class="price-val">45.00</span></div>
            <div class="price-item"><span>⛓️ حديد (طن)</span><span class="price-val">4100</span></div>
            <div class="price-item"><span>🌻 زيت (لتر)</span><span class="price-val text-yellow-500">7.50</span></div>
        </div>

        <div class="glass p-6 border-2 border-cyan-500/30 mt-8 mb-12">
            <h3 class="text-cyan-400 text-sm font-black mb-6 text-center">🔄 حاسبة TORO الأسطورية</h3>
            <p class="text-center text-[10px] text-gray-500 mb-2 uppercase tracking-widest">الدينار الليبي (LYD)</p>
            <div class="calc-box"><input type="number" id="lyd" oninput="runCalc('lyd')" placeholder="0.00"></div>
            
            <div class="grid grid-cols-2 gap-4 mt-4">
                <div>
                    <p class="text-center text-[10px] text-gray-500 mb-2 uppercase tracking-widest">الدولار ($)</p>
                    <div class="calc-box"><input type="number" id="usd" oninput="runCalc('usd')" placeholder="0.00"></div>
                </div>
                <div>
                    <p class="text-center text-[10px] text-gray-500 mb-2 uppercase tracking-widest">اليورو (€)</p>
                    <div class="calc-box"><input type="number" id="eur" oninput="runCalc('eur')" placeholder="0.00"></div>
                </div>
            </div>
        </div>

        <p class="text-gray-700 text-[10px] pb-10 text-center uppercase tracking-[0.3em] font-bold">TORO LY LEGEND © 2026</p>
    </div>

    <script>
        // نظام التحديث اللحظي المعتمد
        setInterval(() => {
            const fakePrice = (8.60 + Math.random() * 0.1).toFixed(2);
            document.getElementById('val-usd').innerText = fakePrice;
            document.getElementById('top-usd').innerText = fakePrice;
        }, 8000);

        // نظام الحاسبة المعتمد
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

st.components.v1.html(full_code, height=2200, scrolling=True)
