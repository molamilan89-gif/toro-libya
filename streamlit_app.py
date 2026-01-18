import streamlit as st

# إعدادات الصفحة الاحترافية - TORO LIBYA
st.set_page_config(page_title="Toro Libya - النسخة الأسطورية", page_icon="🐂", layout="centered")

# الكود الكامل: شعار الثور المدمج + حاسبة أسطورية + كافة الأقسام
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
        .glass { background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; margin-bottom: 20px; transition: 0.3s ease; }
        .section-title { border-right: 4px solid #22d3ee; padding-right: 12px; margin-bottom: 15px; font-weight: 900; color: #22d3ee; }
        
        /* شريط الأخبار العلوي */
        .marquee-wrapper { width: 100%; position: fixed; top: 0; left: 0; background: rgba(8, 51, 68, 0.95); border-bottom: 2px solid #22d3ee; z-index: 9999; padding: 10px 0; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
        .animate-marquee { display: inline-block; white-space: nowrap; animation: marquee 25s linear infinite; font-size: 14px; font-weight: bold; color: #22d3ee; }
        
        .main-container { padding: 140px 20px 50px 20px; display: flex; flex-direction: column; items: center; }
        
        /* 🔥 تصميم شعار الثور الأسطوري (برمجي بالكامل لضمان الظهور) */
        .logo-box { width: 160px; height: 160px; border-radius: 45px; background: linear-gradient(135deg, #1e293b 0%, #0891b2 100%); border: 4px solid #22d3ee; box-shadow: 0 0 50px rgba(34, 211, 238, 0.6); display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; position: relative; }
        
        /* كود رسم الثور SVG */
        .bull-logo { width: 100px; height: 100px; fill: white; filter: drop-shadow(0 0 15px rgba(255,255,255,0.5)); }

        .logo-text { font-size: 3rem; font-weight: 900; letter-spacing: 6px; text-transform: uppercase; color: white; line-height: 1; text-align: center; text-shadow: 0 0 20px rgba(34, 211, 238, 0.5); }
        
        /* بطاقات المؤشرات */
        .quick-grid { display: grid; grid-template-cols: repeat(3, 1fr); gap: 12px; width: 100%; max-width: 480px; margin-bottom: 30px; }
        .quick-card { background: rgba(15, 23, 42, 0.95); border: 2px solid rgba(34, 211, 238, 0.4); border-radius: 18px; padding: 15px 5px; text-align: center; }
        .quick-card p { font-size: 11px; color: #94a3b8; margin-bottom: 5px; font-weight: bold; }
        .quick-card span { font-size: 18px; font-weight: 900; color: #22d3ee; font-family: sans-serif; }

        .live-tag { display: inline-flex; align-items: center; gap: 8px; color: #4ade80; font-size: 12px; font-weight: bold; margin-bottom: 20px; background: rgba(74, 222, 128, 0.1); padding: 6px 18px; border-radius: 25px; border: 1px solid rgba(74, 222, 128, 0.3); }
        .dot { width: 10px; height: 10px; background: #4ade80; border-radius: 50%; animation: pulse 1.5s infinite; }
        @keyframes pulse { 0% { transform: scale(0.95); } 70% { transform: scale(1.1); box-shadow: 0 0 0 8px rgba(74, 222, 128, 0); } 100% { transform: scale(0.95); } }
        
        .price-item { display: flex; justify-content: space-between; align-items: center; padding: 14px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
        .price-val { font-family: sans-serif; font-weight: 900; font-size: 18px; }

        /* 🔄 الآلة الحاسبة الأسطورية المعدلة */
        .calc-box { width: 100%; background: #0f172a; border: 2px solid #334155; border-radius: 15px; padding: 20px; text-align: center; margin-bottom: 15px; transition: 0.3s; }
        .calc-box:focus-within { border-color: #22d3ee; box-shadow: 0 0 20px rgba(34, 211, 238, 0.2); }
        .calc-input { width: 100%; background: transparent; border: none; text-align: center; font-size: 30px; font-weight: 900; color: #22d3ee; outline: none; font-family: sans-serif; }
        .calc-label { font-size: 12px; color: #94a3b8; text-transform: uppercase; margin-bottom: 10px; display: block; font-weight: bold; }
    </style>
</head>
<body>
    <div class="marquee-wrapper">
        <div class="animate-marquee">
            📢 Toro Libya: تم تفعيل شعار الثور المدمج .. الأرقام الدولية مفعلة الآن .. الدولار 8.65 .. الذهب 415.5 .. الإسمنت 45 .. 🐂
        </div>
    </div>

    <div class="main-container">
        <div class="logo-container text-center">
            <div class="live-tag"><span class="dot"></span> نظام Toro Ly المباشر</div>
            
            <div class="logo-box">
                <svg class="bull-logo" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 2C10.5 2 9.2 3.2 8.5 4.5 7.8 3.2 6.5 2 5 2 2.8 2 1 3.8 1 6c0 2.2 2.8 6 11 14 8.2-8 11-11.8 11-14 0-2.2-1.8-4-4-4-1.5 0-2.8 1.2-3.5 2.5C14.8 3.2 13.5 2 12 2z" opacity="0.1"/>
                    <path d="M9 13l-3-3 1.4-1.4L9 10.2l5.6-5.6L16 6l-7 7z" fill="#22d3ee"/>
                    <path d="M12 4c-4.4 0-8 3.6-8 8s3.6 8 8 8 8-3.6 8-8-3.6-8-8-8zm0 14c-3.3 0-6-2.7-6-6s2.7-6 6-6 6 2.7 6 6-2.7 6-6 6z"/>
                </svg>
            </div>
            
            <h1 class="logo-text">TORO <span class="text-cyan-400">LY</span></h1>
            <p class="text-gray-500 text-[11px] tracking-[0.6em] uppercase font-black mt-4">The Legend of Libyan Market</p>
        </div>

        <div class="quick-grid mt-8">
            <div class="quick-card"><p>USD</p><span id="q-usd">8.65</span></div>
            <div class="quick-card"><p>GOLD 18</p><span id="q-gold">415.5</span></div>
            <div class="quick-card"><p>BTC</p><span id="q-btc">96.4K</span></div>
        </div>

        <div class="w-full max-w-md">
            <div class="glass p-6 border-l-4 border-cyan-500">
                <h2 class="section-title">🌟 نبض السوق والتوصيات</h2>
                <p class="text-[12px] text-green-400 font-bold italic">✅ شعار الثور الأسطوري والآلة الحاسبة يعملان الآن 100%.</p>
                <a href="https://wa.me/yournumber" class="block w-full text-center bg-green-600/20 text-green-400 text-sm py-3 rounded-xl mt-4 border border-green-600/30">💬 استشارة مباشرة (واتساب)</a>
            </div>

            <div class="glass p-6 mt-4">
                <h2 class="section-title">💵 العملات العالمية</h2>
                <div class="price-item"><span>🇺🇸 دولار موازي</span><span class="price-val text-cyan-400" id="p-usd">8.65</span></div>
                <div class="price-item"><span>🇪🇺 يورو موازي</span><span class="price-val">9.12</span></div>
                <div class="price-item"><span>🇬🇧 باوند إسترليني</span><span class="price-val">10.85</span></div>
                <div class="price-item"><span>🇹🇳 دينار تونسي</span><span class="price-val">2.65</span></div>
                <div class="price-item"><span>🇹🇷 ليرة تركية</span><span class="price-val">0.27</span></div>
            </div>

            <div class="glass p-6">
                <h2 class="section-title">✨ الذهب والمعادن</h2>
                <div class="price-item"><span>💍 ذهب جديد (21)</span><span class="price-val text-yellow-500">485.00</span></div>
                <div class="price-item"><span>🛠️ ذهب مستعمل (18)</span><span class="price-val text-yellow-600">425.00</span></div>
                <div class="price-item"><span>✨ ذهب كسر (18)</span><span class="price-val text-yellow-400">415.50</span></div>
                <div class="price-item"><span>🥈 فضة (جرام)</span><span class="price-val text-gray-300">5.40</span></div>
            </div>

            <div class="glass p-6">
                <h2 class="section-title">🪙 العملات الرقمية</h2>
                <div class="price-item"><span>₿ Bitcoin (BTC)</span><span class="price-val text-green-400">$96,430</span></div>
                <div class="price-item"><span>Ξ Ethereum (ETH)</span><span class="price-val text-blue-400">$3,345</span></div>
            </div>

            <div class="glass p-6">
                <h2 class="section-title">🏗️ مواد البناء والسلع</h2>
                <div class="price-item"><span>🧱 إسمنت (قنطار)</span><span class="price-val">45.00</span></div>
                <div class="price-item"><span>⛓️ حديد (الطن)</span><span class="price-val">4100</span></div>
                <div class="price-item"><span>🌻 زيت (لتر)</span><span class="price-val text-orange-300">7.50</span></div>
                <div class="price-item"><span>🍚 أرز (كيلو)</span><span class="price-val">6.50</span></div>
            </div>

            <div class="glass border-2 border-cyan-500/30 p-8">
                <h3 class="text-center text-cyan-400 text-sm font-bold mb-6 uppercase tracking-widest">🔄 حاسبة Toro الأسطورية</h3>
                <div class="space-y-5">
                    <div class="calc-box">
                        <span class="calc-label">الدينار الليبي (LYD)</span>
                        <input type="number" id="inp-lyd" oninput="runCalc('lyd')" class="calc-input" placeholder="0.00">
                    </div>
                    <div class="grid grid-cols-2 gap-4">
                        <div class="calc-box">
                            <span class="calc-label">الدولار ($)</span>
                            <input type="number" id="inp-usd" oninput="runCalc('usd')" class="calc-input !text-[20px]" placeholder="0.00">
                        </div>
                        <div class="calc-box">
                            <span class="calc-label">اليورو (€)</span>
                            <input type="number" id="inp-eur" oninput="runCalc('eur')" class="calc-input !text-[20px]" placeholder="0.00">
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <p class="text-center text-gray-600 text-[10px] mt-12 uppercase tracking-widest font-bold">Toro Ly Legend © 2026</p>
    </div>

    <script>
        const rateUsd = 8.65;
        const rateEur = 9.12;

        function runCalc(source) {
            const l = document.getElementById('inp-lyd');
            const u = document.getElementById('inp-usd');
            const e = document.getElementById('inp-eur');

            if(source === 'lyd') {
                u.value = (l.value / rateUsd).toFixed(2);
                e.value = (l.value / rateEur).toFixed(2);
            } else if(source === 'usd') {
                l.value = (u.value * rateUsd).toFixed(2);
                e.value = ((u.value * rateUsd) / rateEur).toFixed(2);
            } else if(source === 'eur') {
                l.value = (e.value * rateEur).toFixed(2);
                u.value = ((e.value * rateEur) / rateUsd).toFixed(2);
            }
        }

        // محاكاة التحديث
        setInterval(() => {
            let val = (8.62 + Math.random() * 0.05).toFixed(2);
            document.getElementById('p-usd').innerText = val;
            document.getElementById('q-usd').innerText = val;
        }, 12000);
    </script>
</body>
</html>
"""

st.components.v1.html(full_code, height=3800, scrolling=True)
