import streamlit as st

# إعدادات الصفحة الاحترافية - TORO LIBYA
st.set_page_config(page_title="Toro Libya - النسخة الأسطورية", page_icon="🐂", layout="centered")

# الكود الكامل: الشعار المدمج + الحاسبة بالأرقام الدولية + جميع الأقسام
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
        .marquee-wrapper { width: 100%; position: fixed; top: 0; left: 0; background: rgba(8, 51, 68, 0.95); border-bottom: 1px solid #22d3ee; z-index: 9999; padding: 10px 0; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
        .animate-marquee { display: inline-block; white-space: nowrap; animation: marquee 25s linear infinite; font-size: 14px; font-weight: bold; color: #22d3ee; }
        
        .main-container { padding: 130px 20px 50px 20px; display: flex; flex-direction: column; items: center; }
        
        /* تصميم الشعار المطور (SVG ثور + سهم صاعد) */
        .logo-box { width: 150px; height: 150px; border-radius: 40px; background: linear-gradient(135deg, #1e293b 0%, #0891b2 100%); border: 3px solid #22d3ee; box-shadow: 0 0 40px rgba(34, 211, 238, 0.5); display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; position: relative; }
        .logo-box svg { width: 100px; height: 100px; fill: white; filter: drop-shadow(0 0 15px rgba(255,255,255,0.4)); }
        
        .logo-text { font-size: 2.8rem; font-weight: 900; letter-spacing: 5px; text-transform: uppercase; color: white; line-height: 1; text-align: center; }
        
        /* بطاقات المؤشرات السريعة */
        .quick-grid { display: grid; grid-template-cols: repeat(3, 1fr); gap: 10px; width: 100%; max-width: 450px; margin-bottom: 30px; }
        .quick-card { background: rgba(15, 23, 42, 0.9); border: 1px solid rgba(34, 211, 238, 0.3); border-radius: 15px; padding: 15px 5px; text-align: center; }
        .quick-card p { font-size: 10px; color: #94a3b8; margin-bottom: 5px; font-weight: bold; }
        .quick-card span { font-size: 16px; font-weight: 900; color: #22d3ee; }

        .live-tag { display: inline-flex; align-items: center; gap: 6px; color: #4ade80; font-size: 11px; font-weight: bold; margin-bottom: 15px; background: rgba(74, 222, 128, 0.1); padding: 5px 15px; border-radius: 20px; border: 1px solid rgba(74, 222, 128, 0.2); }
        .dot { width: 8px; height: 8px; background: #4ade80; border-radius: 50%; animation: pulse 1.5s infinite; }
        @keyframes pulse { 0% { transform: scale(0.95); } 70% { transform: scale(1.1); box-shadow: 0 0 0 8px rgba(74, 222, 128, 0); } 100% { transform: scale(0.95); } }
        
        .price-item { display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
        .price-val { font-family: 'Tajawal', sans-serif; font-weight: 900; }

        /* الآلة الحاسبة المحدثة بالأرقام الدولية */
        .calc-box { width: 100%; background: #0f172a; border: 1px solid #334155; border-radius: 12px; padding: 15px; text-align: center; margin-bottom: 10px; }
        .calc-input { width: 100%; background: transparent; border: none; text-align: center; font-size: 26px; font-weight: 900; color: #22d3ee; outline: none; }
        /* إجبار الأرقام لتكون دولية */
        input::-webkit-outer-spin-button, input::-webkit-inner-spin-button { -webkit-appearance: none; margin: 0; }
        .calc-label { font-size: 11px; color: #94a3b8; text-transform: uppercase; margin-bottom: 8px; display: block; font-weight: bold; }
    </style>
</head>
<body>
    <div class="marquee-wrapper">
        <div class="animate-marquee">
            📢 Toro Libya: تم تحديث الشعار والآلة الحاسبة بنجاح .. الدولار 8.65 .. ذهب كسر 18 بـ 415.5 .. البيتكوين $96,430 .. الإسمنت 45.00 .. 🐂
        </div>
    </div>

    <div class="main-container">
        <div class="logo-container text-center">
            <div class="live-tag"><span class="dot"></span> نظام Toro Ly المباشر</div>
            <div class="logo-box">
                <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-1-13h2v6h3l-4 4-4-4h3V7z"/>
                    <path d="M7 10l2-2 3 3 3-3 2 2-5 5-5-5z" opacity=".3"/>
                </svg>
            </div>
            <h1 class="logo-text">TORO <span class="text-cyan-400">LY</span></h1>
            <p class="text-gray-500 text-[10px] tracking-[0.5em] uppercase font-black mt-3">The Legend of Libyan Market</p>
        </div>

        <div class="quick-grid mt-6">
            <div class="quick-card"><p>USD/LYD</p><span class="price-val" id="q-usd">8.65</span></div>
            <div class="quick-card"><p>GOLD 18</p><span class="price-val" id="q-gold">415.5</span></div>
            <div class="quick-card"><p>BTC/USD</p><span class="price-val" id="q-btc">96.4K</span></div>
        </div>

        <div class="w-full max-w-md">
            <div class="glass p-5 border-l-4 border-cyan-500">
                <h2 class="section-title">🌟 نبض السوق والتوصيات</h2>
                <p class="text-[11px] text-green-400 font-bold">✅ تم ضبط الأرقام الدولية وتحسين ظهور الشعار.</p>
                <a href="https://wa.me/yournumber" class="block w-full text-center bg-green-600/20 text-green-400 text-xs py-2 rounded-lg mt-3 border border-green-600/30">💬 استشارة مباشرة (واتساب)</a>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">💵 العملات العالمية</h2>
                <div class="price-item"><span>🇺🇸 دولار موازي</span><span class="price-val text-cyan-400" id="p-usd">8.65</span></div>
                <div class="price-item"><span>🇪🇺 يورو موازي</span><span class="price-val">9.12</span></div>
                <div class="price-item"><span>🇬🇧 باوند إسترليني</span><span class="price-val">10.85</span></div>
                <div class="price-item"><span>🇹🇳 دينار تونسي</span><span class="price-val">2.65</span></div>
                <div class="price-item"><span>🇹🇷 ليرة تركية</span><span class="price-val">0.27</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">✨ الذهب والمعادن</h2>
                <div class="price-item"><span>💍 ذهب جديد (21)</span><span class="price-val text-yellow-500">485.00</span></div>
                <div class="price-item"><span>🛠️ ذهب مستعمل (18)</span><span class="price-val text-yellow-600">425.00</span></div>
                <div class="price-item"><span>✨ ذهب كسر (18)</span><span class="price-val text-yellow-400">415.50</span></div>
                <div class="price-item"><span>🥈 فضة (جرام)</span><span class="price-val text-gray-300">5.40</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">🪙 العملات الرقمية</h2>
                <div class="price-item"><span>₿ Bitcoin (BTC)</span><span class="price-val text-green-400">$96,430</span></div>
                <div class="price-item"><span>Ξ Ethereum (ETH)</span><span class="price-val text-blue-400">$3,345</span></div>
                <div class="price-item"><span>💠 Solana (SOL)</span><span class="price-val text-purple-400">$195.20</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">🏗️ مواد البناء والسلع</h2>
                <div class="price-item"><span>🧱 إسمنت (قنطار)</span><span class="price-val">45.00</span></div>
                <div class="price-item"><span>⛓️ حديد (الطن)</span><span class="price-val">4100</span></div>
                <div class="price-item"><span>🌻 زيت (لتر)</span><span class="price-val text-orange-300">7.50</span></div>
            </div>

            <div class="glass border-2 border-cyan-500/30 p-6">
                <h3 class="text-center text-cyan-400 text-xs font-bold mb-4 uppercase">🔄 حاسبة Toro الأسطورية</h3>
                <div class="space-y-4">
                    <div class="calc-box">
                        <span class="calc-label">الدينار الليبي (LYD)</span>
                        <input type="number" id="inp-lyd" oninput="calculate('lyd')" class="calc-input" placeholder="0.00" dir="ltr">
                    </div>
                    <div class="grid grid-cols-2 gap-3">
                        <div class="calc-box">
                            <span class="calc-label">الدولار ($)</span>
                            <input type="number" id="inp-usd" oninput="calculate('usd')" class="calc-input !text-[18px]" placeholder="0.00" dir="ltr">
                        </div>
                        <div class="calc-box">
                            <span class="calc-label">اليورو (€)</span>
                            <input type="number" id="inp-eur" oninput="calculate('eur')" class="calc-input !text-[18px]" placeholder="0.00" dir="ltr">
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <p class="text-center text-gray-600 text-[10px] mt-10 uppercase tracking-widest">Toro Ly Legend © 2026</p>
    </div>

    <script>
        const rateUsd = 8.65;
        const rateEur = 9.12;

        function calculate(source) {
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

        // محاكاة التحديث الفوري للأسعار
        setInterval(() => {
            let val = (8.60 + Math.random() * 0.1).toFixed(2);
            document.getElementById('p-usd').innerText = val;
            document.getElementById('q-usd').innerText = val;
        }, 10000);
    </script>
</body>
</html>
"""

st.components.v1.html(full_code, height=3500, scrolling=True)
