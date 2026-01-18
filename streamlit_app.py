import streamlit as st

# إعدادات الصفحة الاحترافية
st.set_page_config(page_title="Toro Libya - منصة وول ستريت ليبيا", page_icon="🐂", layout="centered")

# الكود الكامل والمحسن
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
        .glass { background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; margin-bottom: 20px; }
        .section-title { border-right: 4px solid #22d3ee; padding-right: 12px; margin-bottom: 15px; font-weight: 900; color: #22d3ee; }
        .price-item { display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
        
        /* شريط الأخبار المباشر المحسن */
        .marquee-wrapper { width: 100%; position: fixed; top: 0; left: 0; background: rgba(8, 51, 68, 0.95); border-bottom: 1px solid #22d3ee; z-index: 9999; padding: 8px 0; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
        .animate-marquee { display: inline-block; white-space: nowrap; animation: marquee 25s linear infinite; font-size: 13px; font-weight: bold; color: #22d3ee; }
        
        /* مؤشر البث المباشر */
        .live-indicator { display: inline-flex; align-items: center; gap: 5px; color: #4ade80; font-size: 10px; font-weight: bold; margin-bottom: 10px; }
        .dot { width: 8px; height: 8px; background: #4ade80; border-radius: 50%; display: inline-block; animation: pulse 1.5s infinite; }
        @keyframes pulse { 0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.7); } 70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(74, 222, 128, 0); } 100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(74, 222, 128, 0); } }

        .main-container { padding: 60px 20px 350px 20px; display: flex; flex-direction: column; items: center; }
        
        /* إجبار الأرقام على الصيغة الإنجليزية */
        input { font-family: sans-serif !important; direction: ltr !important; background: #111827 !important; color: white !important; }
        input::placeholder { font-family: 'Tajawal', sans-serif; direction: rtl !important; }
    </style>
</head>
<body>
    <div class="marquee-wrapper">
        <div class="animate-marquee">
            📢 عاجل: Toro Libya يطلق التحديث الشامل لأسعار الذهب والعملات .. 🛢️ خام برنت مستقر عند 78.40$ .. 🏗️ أسعار الإسمنت والحديد اليوم في ليبيا .. 🐂 منصة تورو ليبيا: المؤشر الاقتصادي الأول في البلاد ..
        </div>
    </div>

    <div class="main-container">
        <div class="live-indicator">
            <span class="dot"></span> مباشر - تحديث تلقائي
        </div>

        <div class="text-center mb-8">
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
            </div>

            <div class="glass p-5">
                <h2 class="section-title">🪙 العملات الرقمية</h2>
                <div class="price-item"><span>₿ Bitcoin</span><span class="text-green-400 font-bold">$96,430</span></div>
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
            </div>

            <div class="glass p-5">
                <h2 class="section-title">🛒 السلع الأساسية</h2>
                <div class="price-item"><span>🌻 زيت (لتر)</span><span class="font-bold">7.50</span></div>
                <div class="price-item"><span>🍚 أرز (كيلو)</span><span class="font-bold">5.00</span></div>
            </div>
        </div>

        <div class="w-full max-w-md glass p-6 fixed bottom-4 border-2 border-cyan-500/40 z-[100] left-1/2 -translate-x-
