import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Toro Libya", page_icon="🐂", layout="centered")

# الكود المصلح بالكامل (تم حل مشكلة الاقتباس والشعار المفقود)
full_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Tajawal', sans-serif; background: #0b1120; color: white; margin: 0; padding: 0; }
        .glass { background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 20px; margin-bottom: 20px; }
        
        /* شريط الأخبار العلوي */
        .marquee-wrapper { width: 100%; position: fixed; top: 0; left: 0; background: rgba(8, 51, 68, 0.95); border-bottom: 2px solid #22d3ee; z-index: 9999; padding: 10px 0; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
        .animate-marquee { display: inline-block; white-space: nowrap; animation: marquee 25s linear infinite; font-size: 14px; font-weight: bold; color: #22d3ee; }

        .main-container { padding: 140px 20px 50px 20px; display: flex; flex-direction: column; items: center; }

        /* 🔥 شعار الثور المرسوم برمجياً (SVG) - سيظهر دائماً */
        .logo-box { width: 160px; height: 160px; border-radius: 40px; background: linear-gradient(135deg, #0891b2 0%, #0e7490 100%); border: 4px solid #22d3ee; box-shadow: 0 0 40px rgba(34, 211, 238, 0.5); display: flex; align-items: center; justify-content: center; margin-bottom: 20px; }
        
        .logo-text { font-size: 2.5rem; font-weight: 900; letter-spacing: 4px; text-transform: uppercase; color: white; text-align: center; line-height: 1; }
        
        /* أسعار العملات */
        .price-row { display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
        .price-val { font-family: 'Arial', sans-serif; font-weight: 900; color: #22d3ee; font-size: 1.2rem; }

        /* حاسبة الأرقام الدولية */
        .calc-input { width: 100%; background: #0f172a; border: 2px solid #334155; border-radius: 12px; padding: 15px; text-align: center; font-size: 28px; font-weight: 900; color: #22d3ee; outline: none; font-family: 'Arial', sans-serif; margin-bottom: 15px; }
        .calc-label { font-size: 12px; color: #94a3b8; font-weight: bold; display: block; margin-bottom: 5px; }
    </style>
</head>
<body>
    <div class="marquee-wrapper">
        <div class="animate-marquee">
            📢 Toro Libya: تم إصلاح الشعار والآلة الحاسبة بنجاح .. الدولار 8.65 .. ذهب كسر 415.5 .. الإسمنت 45 .. 🐂
        </div>
    </div>

    <div class="main-container">
        <div class="logo-box">
            <svg viewBox="0 0 24 24" width="100" height="100" fill="white">
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-5-9h10v2H7z"/>
                <path d="M12 4l-4 4h8l-4-4zM12 20l4-4H8l4 4z" opacity="0.5"/>
            </svg>
        </div>
        
        <h1 class="logo-text">TORO <span class="text-cyan-400">LY</span></h1>
        <p class="text-gray-500 text-[10px] tracking-[0.5em] font-black mt-2">THE LEGEND OF LIBYAN MARKET</p>

        <div class="w-full max-w-md mt-8">
            <div class="glass">
                <h2 class="text-cyan-400 font-bold mb-4 border-r-4 border-cyan-400 pr-3">💵 أسعار العملات</h2>
                <div class="price-row"><span>🇺🇸 دولار موازي</span><span class="price-val">8.65</span></div>
                <div class="price-row"><span>🇪🇺 يورو موازي</span><span class="price-val">9.12</span></div>
                <div class="price-row"><span>🇹🇷 ليرة تركية</span><span class="price-val">0.27</span></div>
            </div>

            <div class="glass">
                <h2 class="text-yellow-400 font-bold mb-4 border-r-4 border-yellow-400 pr-3">✨ الذهب والمعادن</h2>
                <div class="price-row"><span>💍 ذهب كسر (18)</span><span class="price-val text-yellow-500">415.50</span></div>
                <div class="price-row"><span>💍 ذهب جديد (21)</span><span class="price-val">485.00</span></div>
            </div>

            <div class="glass border-2 border-cyan-500/30">
                <h3 class="text-center text-cyan-400 text-xs font-bold mb-4 uppercase">🔄 حاسبة Toro الأسطورية</h3>
                <label class="calc-label">الدينار الليبي (LYD)</label>
                <input type="number" id="lyd" oninput="conv('lyd')" class="calc-input" placeholder="0.00">
                
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="calc-label">الدولار ($)</label>
                        <input type="number" id="usd" oninput="conv('usd')" class="calc-input !text-[20px]" placeholder="0.00">
                    </div>
                    <div>
                        <label class="calc-label">اليورو (€)</label>
                        <input type="number" id="eur" oninput="conv('eur')" class="calc-input !text-[20px]" placeholder="0.00">
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        const rUsd = 8.65;
        const rEur = 9.12;
        function conv(src) {
            const l = document.getElementById('lyd');
            const u = document.getElementById('usd');
            const e = document.getElementById('eur');
            if(src === 'lyd') {
                u.value = (l.value / rUsd).toFixed(2);
                e.value = (l.value / rEur).toFixed(2);
            } else if(src === 'usd') {
                l.value = (u.value * rUsd).toFixed(2);
                e.value = ((u.value * rUsd) / rEur).toFixed(2);
            } else if(src === 'eur') {
                l.value = (e.value * rEur).toFixed(2);
                u.value = ((e.value * rEur) / rUsd).toFixed(2);
            }
        }
    </script>
</body>
</html>
"""

st.components.v1.html(full_code, height=2500, scrolling=True)
