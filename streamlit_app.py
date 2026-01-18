import streamlit as st

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="Toro Libya - منصة وول ستريت ليبيا", page_icon="🐂", layout="centered")

# الكود الكامل مع تعديل لغة أرقام الحاسبة
full_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Toro Libya - منصة وول ستريت ليبيا</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Tajawal', sans-serif; background: #0b1120; color: white; margin: 0; padding: 0; }
        .glass { background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; margin-bottom: 20px; }
        .section-title { border-right: 4px solid #22d3ee; padding-right: 12px; margin-bottom: 15px; font-weight: 900; color: #22d3ee; }
        .price-item { display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
        .animate-marquee { display: inline-block; white-space: nowrap; animation: marquee 25s linear infinite; }
        .main-container { padding: 20px; display: flex; flex-direction: column; items: center; padding-bottom: 300px; }
        
        /* ضمان ظهور الأرقام بالصيغة الإنجليزية في الحاسبة */
        input { font-family: sans-serif !important; direction: ltr !important; }
        input::placeholder { font-family: 'Tajawal', sans-serif; direction: rtl !important; }
    </style>
</head>
<body>
    <div class="w-full fixed top-0 left-0 bg-cyan-950/90 py-2 z-[100] border-b border-cyan-500/30">
        <div class="animate-marquee text-cyan-400 text-xs font-bold">
            📢 عاجل: Toro Libya يطلق التحديث الشامل لأسعار الذهب والعملات .. 🛢️ خام برنت مستقر عند 78.40$ .. 🏗️ أسعار الإسمنت والحديد اليوم في ليبيا .. 🐂 منصة تورو ليبيا: المؤشر الاقتصادي الأول في البلاد ..
        </div>
    </div>

    <div class="main-container">
        <div class="text-center mt-12 mb-8">
            <h1 class="text-5xl font-black tracking-widest uppercase">Toro <span class="text-cyan-400">Ly</span></h1>
            <p class="text-gray-500 text-[10px] mt-1 uppercase tracking-widest text-center">المؤشر الاقتصادي الليبي المتكامل</p>
        </div>

        <div class="w-full max-w-md">
            <div class="glass p-5">
                <h2 class="section-title">💵 العملات والذهب</h2>
                <div class="price-item"><span>🇺🇸 دولار موازي</span><span class="font-bold text-cyan-400">8.65</span></div>
                <div class="price-item"><span>🇪🇺 يورو موازي</span><span class="font-bold">9.12</span></div>
                <div class="price-item"><span>🇬🇧 باوند إسترليني</span><span class="font-bold">10.85</span></div>
                <div class="price-item"><span>✨ ذهب كسر (18)</span><span class="font-bold text-yellow-500">415.5</span></div>
                <div class="price-item"><span>💍 ذهب جديد (21)</span><span class="font-bold text-yellow-600">485.0</span></div>
                <div class="price-item"><span>🛠️ ذهب مستعمل (18)</span><span class="font-bold text-yellow-400">425.0</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">🪙 العملات الرقمية</h2>
                <div class="price-item"><span>₿ Bitcoin</span><span class="text-green-400 font-bold">$96,430</span></div>
                <div class="price-item"><span>Ξ Ethereum</span><span class="text-green-400 font-bold">$3,750</span></div>
                <div class="price-item"><span>💠 Solana (SOL)</span><span class="text-green-400 font-bold">$195.20</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">⛽ الطاقة والنفط</h2>
                <div class="price-item"><span>🛢️ خام برنت</span><span class="font-bold text-green-400">$78.40</span></div>
                <div class="price-item"><span>🔥 غاز الطهي</span><span class="font-bold">5.00 LYD</span></div>
                <div class="price-item"><span>⛽ البنزين (لتر)</span><span class="font-bold text-red-400">0.15 LYD</span></div>
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
        </div>

        <div class="w-full max-w-md glass p-6 fixed bottom-4 border-2 border-cyan-500/40 z-[100] left-1/2 -translate-x-1/2">
            <h3 class="text-cyan-400 text-xs font-bold mb-4 text-center">🔄 محول العملات الذكي</h3>
            <input type="number" id="lyd" oninput="convert('lyd')" placeholder="دينار ليبي" class="w-full bg-gray-900 border border-gray-700 rounded-lg p-3 mb-3 text-lg font-bold text-white text-center outline-none">
            <div class="grid grid-cols-2 gap-3">
                <input type="number" id="usd" oninput="convert('usd')" placeholder="دولار $" class="w-full bg-gray-900 border border-gray-700 rounded-lg p-2 text-md font-bold text-cyan-400 text-center outline-none">
                <input type="number" id="eur" oninput="convert('eur')" placeholder="يورو €" class="w-full bg-gray-900 border border-gray-700 rounded-lg p-2 text-md font-bold text-white text-center outline-none">
            </div>
        </div>
    </div>

    <script>
        const rateUsd = 8.65, rateEur = 9.12;
        function convert(s) {
            const l = document.getElementById('lyd'), u = document.getElementById('usd'), e = document.getElementById('eur');
            if(s=='lyd'){ 
                u.value = (l.value / rateUsd).toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2, useGrouping: false}); 
                e.value = (l.value / rateEur).toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2, useGrouping: false}); 
            }
            else if(s=='usd'){ 
                l.value = (u.value * rateUsd).toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2, useGrouping: false}); 
                e.value = ((u.value * rateUsd) / rateEur).toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2, useGrouping: false}); 
            }
            else if(s=='eur'){ 
                l.value = (e.value * rateEur).toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2, useGrouping: false}); 
                u.value = ((e.value * rateEur) / rateUsd).toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2, useGrouping: false}); 
            }
        }
    </script>
</body>
</html>
"""

# تشغيل الكود في Streamlit
st.components.v1.html(full_code, height=1800, scrolling=True)
