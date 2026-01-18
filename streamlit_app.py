import streamlit as st

# إعدادات الصفحة الاحترافية - TORO LIBYA
st.set_page_config(page_title="Toro Ly - The Legend", page_icon="🐂", layout="centered")

# الكود البرمجي بتصميم عالمي (نيون وفخامة)
full_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root { --neon-cyan: #22d3ee; --neon-gold: #facc15; --bg-dark: #0b1120; }
        body { font-family: 'Tajawal', sans-serif; background: var(--bg-dark); color: white; margin: 0; padding: 0; }
        
        /* تصميم الهيدر اللوجو العالمي */
        .header-container { padding: 40px 20px; text-align: right; display: flex; align-items: center; gap: 20px; }
        .logo-circle { width: 80px; height: 80px; background: rgba(34, 211, 238, 0.1); border: 2px solid var(--neon-cyan); border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 20px rgba(34, 211, 238, 0.3); }
        .logo-circle svg { width: 45px; height: 45px; fill: var(--neon-cyan); }
        .brand-name { font-size: 45px; font-weight: 900; letter-spacing: -2px; line-height: 1; }
        .brand-ly { background: var(--neon-cyan); color: var(--bg-dark); padding: 0 10px; border-radius: 8px; margin-right: 5px; }
        
        /* البطاقات العلوية - نمط زجاجي */
        .top-grid { display: grid; grid-cols: 3; gap: 15px; margin-bottom: 30px; }
        .glass-card { background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.05); border-radius: 20px; padding: 20px; position: relative; overflow: hidden; }
        .glass-card::before { content: ''; position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: var(--neon-cyan); }
        .glass-card.gold::before { background: var(--neon-gold); }
        
        /* الأقسام والجداول */
        .section-box { background: rgba(30, 41, 59, 0.4); border-radius: 24px; padding: 25px; margin-bottom: 25px; border: 1px solid rgba(255,255,255,0.03); }
        .section-header { display: flex; align-items: center; gap: 10px; margin-bottom: 20px; font-size: 20px; font-weight: 800; color: var(--neon-cyan); }
        .section-header.gold { color: var(--neon-gold); }
        
        .row-item { display: flex; justify-content: space-between; align-items: center; padding: 15px 10px; background: rgba(255,255,255,0.02); border-radius: 12px; margin-bottom: 8px; transition: 0.3s; }
        .row-item:hover { background: rgba(255,255,255,0.05); transform: scale(1.01); }
        
        .price-text { font-family: 'Verdana', sans-serif; font-weight: 700; font-size: 18px; }
        .gold-text { color: var(--neon-gold); }

        /* حاسبة احترافية */
        .calc-input-group { background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 15px; padding: 10px 20px; margin-bottom: 12px; }
        .calc-input-group input { background: transparent; border: none; width: 100%; color: white; font-size: 22px; font-weight: 700; outline: none; text-align: center; }
        
        .marquee-top { position: fixed; top: 0; width: 100%; background: #083344; padding: 6px 0; z-index: 100; font-size: 12px; font-weight: bold; border-bottom: 1px solid var(--neon-cyan); }
    </style>
</head>
<body>
    <div class="marquee-top">
        <marquee>📢 Toro Ly: الأسعار محدثة لحظياً من قلب سوق المشير .. الدولار مستقر عند 8.65 .. الذهب عيار 18 كسر بـ 415.5 ..</marquee>
    </div>

    <div class="max-w-xl mx-auto px-4 pt-16">
        <header class="header-container">
            <div class="logo-circle">
                <svg viewBox="0 0 24 24"><path d="M12,2C6.48,2,2,6.48,2,12s4.48,10,10,10s10-4.48,10-10S17.52,2,12,2z M15.5,14.5c-0.83,0-1.5-0.67-1.5-1.5s0.67-1.5,1.5-1.5 s1.5,0.67,1.5,1.5S16.33,14.5,15.5,14.5z M8.5,14.5c-0.83,0-1.5-0.67-1.5-1.5s0.67-1.5,1.5-1.5s1.5,0.67,1.5,1.5S9.33,14.5,8.5,14.5z M12,18c-2.33,0-4.31-1.46-5.11-3.5h10.22C16.31,16.54,14.33,18,12,18z"/></svg>
            </div>
            <div>
                <h1 class="brand-name">TORO<span class="brand-ly">Ly</span></h1>
                <p class="text-[10px] text-gray-500 font-bold uppercase tracking-widest mt-1">The Legend of Libian Market</p>
            </div>
        </header>

        <div class="grid grid-cols-3 gap-3 mb-8">
            <div class="glass-card">
                <p class="text-[10px] text-cyan-400 font-black">USD</p>
                <p class="price-text mt-1" id="top-usd">8.65</p>
            </div>
            <div class="glass-card gold">
                <p class="text-[10px] text-yellow-500 font-black">GOLD 18</p>
                <p class="price-text gold-text mt-1">415.5</p>
            </div>
            <div class="glass-card">
                <p class="text-[10px] text-cyan-400 font-black">BTC</p>
                <p class="price-text mt-1">96.4K</p>
            </div>
        </div>

        <div class="section-box">
            <div class="section-header">⚡ الخدمات والطاقة</div>
            <div class="row-item"><span>طرح الأحمال (طرابلس)</span><span class="text-cyan-400 font-bold">1 - 2 ساعة</span></div>
            <div class="row-item"><span>محطات الوقود</span><span class="text-green-400 font-bold">متوفرة</span></div>
        </div>

        <div class="section-box border-r-4 border-cyan-500">
            <div class="section-header">💵 العملات الموازية</div>
            <div class="row-item"><span>🇺🇸 دولار موازي</span><span class="price-text text-cyan-400" id="val-usd">8.65</span></div>
            <div class="row-item"><span>🇪🇺 يورو موازي</span><span class="price-text">9.12</span></div>
            <div class="row-item"><span>🇬🇧 باوند إسترليني</span><span class="price-text">10.85</span></div>
            <div class="row-item"><span>🇹🇳 دينار تونسي</span><span class="price-text">2.65</span></div>
            <div class="row-item"><span>🇪🇬 جنيه مصري</span><span class="price-text text-green-500">0.17</span></div>
        </div>

        <div class="section-box border-r-4 border-yellow-500">
            <div class="section-header gold">✨ الذهب والمعادن</div>
            <div class="row-item"><span>💍 ذهب جديد (21)</span><span class="price-text gold-text">485.0</span></div>
            <div class="row-item"><span>✨ ذهب كسر (18)</span><span class="price-text gold-text">415.5</span></div>
            <div class="row-item"><span>🥈 فضة (جرام)</span><span class="price-text text-gray-400">5.40</span></div>
            <div class="row-item"><span>🥉 نحاس (كيلو)</span><span class="price-text text-gray-400">42.0</span></div>
        </div>

        <div class="section-box border-r-4 border-cyan-500">
            <div class="section-header">🏗️ مواد البناء والسلع</div>
            <div class="row-item"><span>🧱 إسمنت (قنطار)</span><span class="price-text">45.00</span></div>
            <div class="row-item"><span>⛓️ حديد (طن)</span><span class="price-text">4100</span></div>
            <div class="row-item"><span>🌻 زيت (لتر)</span><span class="price-text">7.50</span></div>
        </div>

        <div class="section-box border-r-4 border-cyan-500">
            <div class="section-header">🪙 العملات الرقمية</div>
            <div class="row-item"><span>₿ Bitcoin (BTC)</span><span class="price-text text-green-400">$96,430</span></div>
            <div class="row-item"><span>Ξ Ethereum (ETH)</span><span class="price-text text-blue-400">$3,345</span></div>
            <div class="row-item"><span>☀️ Solana (SOL)</span><span class="price-text text-purple-400">$242.15</span></div>
        </div>

        <div class="section-box border-2 border-cyan-500/30">
            <div class="section-header justify-center mb-6">🔄 حاسبة TORO الذكية</div>
            <div class="calc-input-group"><input type="number" id="lyd" oninput="runCalc('lyd')" placeholder="0.00"><p class="text-[10px] text-cyan-400 font-bold">دينار ليبي</p></div>
            <div class="grid grid-cols-2 gap-4">
                <div class="calc-input-group"><input type="number" id="usd" oninput="runCalc('usd')" placeholder="0.00"><p class="text-[10px] text-gray-500 font-bold">دولار</p></div>
                <div class="calc-input-group"><input type="number" id="eur" oninput="runCalc('eur')" placeholder="0.00"><p class="text-[10px] text-gray-500 font-bold">يورو</p></div>
            </div>
        </div>

        <footer class="text-center py-10 opacity-30 text-[10px] font-bold tracking-[0.5em]">TORO LY LEGEND © 2026</footer>
    </div>

    <script>
        // محاكاة التحديث اللحظي
        setInterval(() => {
            const p = (8.60 + Math.random() * 0.1).toFixed(2);
            document.getElementById('val-usd').innerText = p;
            document.getElementById('top-usd').innerText = p;
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

st.components.v1.html(full_code, height=3200, scrolling=True)
