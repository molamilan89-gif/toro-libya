import streamlit as st

# إعدادات الصفحة الاحترافية - TORO LIBYA
st.set_page_config(page_title="Toro Libya - النسخة الأسطورية", page_icon="🐂", layout="centered")

# الكود الكامل مع معالجة الشعار والأقسام وآلة حاسبة ذكية تعمل فعلياً
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
        
        .marquee-wrapper { width: 100%; position: fixed; top: 0; left: 0; background: rgba(8, 51, 68, 0.95); border-bottom: 1px solid #22d3ee; z-index: 9999; padding: 10px 0; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
        .animate-marquee { display: inline-block; white-space: nowrap; animation: marquee 25s linear infinite; font-size: 14px; font-weight: bold; color: #22d3ee; }
        
        .main-container { padding: 130px 20px 50px 20px; display: flex; flex-direction: column; items: center; }
        
        /* تصميم الشعار الاحتياطي المضمون الظهور */
        .logo-box { width: 140px; height: 140px; border-radius: 30px; background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border: 3px solid #22d3ee; box-shadow: 0 0 30px rgba(34, 211, 238, 0.4); display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; overflow: hidden; }
        .logo-box svg { width: 80px; height: 80px; fill: #22d3ee; }
        
        .logo-text { font-size: 2.8rem; font-weight: 900; letter-spacing: 5px; text-transform: uppercase; color: white; line-height: 1; text-align: center; }
        
        .quick-grid { display: grid; grid-template-cols: repeat(3, 1fr); gap: 12px; width: 100%; max-width: 450px; margin-bottom: 30px; }
        .quick-card { background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(34, 211, 238, 0.2); border-radius: 15px; padding: 15px 5px; text-align: center; }
        .quick-card span { font-size: 16px; font-weight: 900; color: #22d3ee; }

        .live-tag { display: inline-flex; align-items: center; gap: 6px; color: #4ade80; font-size: 11px; font-weight: bold; margin-bottom: 15px; background: rgba(74, 222, 128, 0.1); padding: 5px 15px; border-radius: 20px; border: 1px solid rgba(74, 222, 128, 0.2); }
        .dot { width: 8px; height: 8px; background: #4ade80; border-radius: 50%; animation: pulse 1.5s infinite; }
        @keyframes pulse { 0% { transform: scale(0.95); } 70% { transform: scale(1.1); box-shadow: 0 0 0 8px rgba(74, 222, 128, 0); } 100% { transform: scale(0.95); } }
        
        .price-item { display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
        
        /* تحسين الحاسبة */
        .calc-input { width: 100%; background: #0f172a; border: 1px solid #334155; border-radius: 12px; padding: 12px; text-align: center; font-weight: bold; color: white; outline: none; transition: 0.3s; }
        .calc-input:focus { border-color: #22d3ee; box-shadow: 0 0 10px rgba(34, 211, 238, 0.2); }
    </style>
</head>
<body>
    <div class="marquee-wrapper">
        <div class="animate-marquee">
            📢 Toro Libya: تحديثات الواتساب تعمل الآن .. الدولار 8.65 .. الذهب 415.5 .. البيتكوين يتألق .. 🐂
        </div>
    </div>

    <div class="main-container">
        <div class="logo-container">
            <div class="live-tag text-center"><span class="dot"></span> نظام Toro Ly المباشر</div>
            <div class="logo-box">
                <svg viewBox="0 0 24 24"><path d="M12,2C6.47,2,2,6.47,2,12s4.47,10,10,10s10-4.47,10-10S17.53,2,12,2z M15.59,15.59L12,12L8.41,15.59L7,14.17l5-5l5,5L15.59,15.59z"/></svg>
            </div>
            <h1 class="logo-text">TORO <span class="text-cyan-400">LY</span></h1>
            <p class="text-center text-gray-500 text-[9px] tracking-[0.5em] uppercase font-black mt-2">The Legend of Libyan Market</p>
        </div>

        <div class="quick-grid">
            <div class="quick-card"><p class="text-[10px] text-gray-400">USD</p><span id="q-usd">8.65</span></div>
            <div class="quick-card"><p class="text-[10px] text-gray-400">GOLD 18</p><span id="q-gold">415.5</span></div>
            <div class="quick-card"><p class="text-[10px] text-gray-400">BTC</p><span id="q-btc">96.4K</span></div>
        </div>

        <div class="w-full max-w-md">
            <div class="glass p-5 border-l-4 border-cyan-500">
                <h2 class="section-title">🌟 نبض السوق والتوصيات</h2>
                <p class="text-[11px] text-green-400">✅ الحسابات تعمل الآن بدقة تامة بناءً على سعر السوق.</p>
                <a href="https://wa.me/yournumber" class="block w-full text-center bg-green-600/20 text-green-400 text-xs py-2 rounded-lg mt-3">💬 واتساب الإدارة</a>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">💵 العملات العالمية</h2>
                <div class="price-item"><span>🇺🇸 دولار موازي</span><span id="p-usd" class="font-bold text-cyan-400">8.65</span></div>
                <div class="price-item"><span>🇪🇺 يورو موازي</span><span class="font-bold">9.12</span></div>
                <div class="price-item"><span>🇬🇧 باوند إسترليني</span><span class="font-bold">10.85</span></div>
                <div class="price-item"><span>🇹🇳 دينار تونسي</span><span class="font-bold">2.65</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">✨ الذهب والمعادن</h2>
                <div class="price-item"><span>💍 ذهب جديد (21)</span><span class="font-bold text-yellow-500">485.0</span></div>
                <div class="price-item"><span>🛠️ ذهب كسر (18)</span><span class="font-bold text-yellow-400">415.5</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">🪙 العملات الرقمية</h2>
                <div class="price-item"><span>₿ Bitcoin (BTC)</span><span class="text-green-400 font-bold">$96,430</span></div>
                <div class="price-item"><span>Ξ Ethereum (ETH)</span><span class="text-blue-400 font-bold">$3,345</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">🏗️ مواد البناء والسلع</h2>
                <div class="price-item"><span>🧱 إسمنت (قنطار)</span><span class="font-bold">45.00</span></div>
                <div class="price-item"><span>🌻 زيت (لتر)</span><span class="font-bold">7.50</span></div>
            </div>

            <div class="glass border-2 border-cyan-500/30 p-6">
                <h3 class="text-center text-cyan-400 text-xs font-bold mb-4 uppercase">🔄 آلة حاسبة Toro الذكية</h3>
                <div class="space-y-3">
                    <div>
                        <label class="text-[10px] text-gray-400 mb-1 block">القيمة بالدينار الليبي (LYD)</label>
                        <input type="number" id="inp-lyd" oninput="calcFromLyd()" class="calc-input" placeholder="0.00">
                    </div>
                    <div class="grid grid-cols-2 gap-3">
                        <div>
                            <label class="text-[10px] text-gray-400 mb-1 block">بالدولار ($)</label>
                            <input type="number" id="inp-usd" oninput="calcFromUsd()" class="calc-input" placeholder="0.00">
                        </div>
                        <div>
                            <label class="text-[10px] text-gray-400 mb-1 block">باليورو (€)</label>
                            <input type="number" id="inp-eur" oninput="calcFromEur()" class="calc-input" placeholder="0.00">
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <p class="text-center text-gray-600 text-[10px] mt-10">Toro Ly Legend © 2026</p>
    </div>

    <script>
        const rateUsd = 8.65;
        const rateEur = 9.12;

        function calcFromLyd() {
            const lyd = document.getElementById('inp-lyd').value;
            document.getElementById('inp-usd').value = (lyd / rateUsd).toFixed(2);
            document.getElementById('inp-eur').value = (lyd / rateEur).toFixed(2);
        }

        function calcFromUsd() {
            const usd = document.getElementById('inp-usd').value;
            document.getElementById('inp-lyd').value = (usd * rateUsd).toFixed(2);
            document.getElementById('inp-eur').value = ((usd * rateUsd)
            
