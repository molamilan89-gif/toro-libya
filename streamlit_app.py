import streamlit as st

# إعدادات الصفحة الاحترافية - TORO LIBYA
st.set_page_config(page_title="Toro Libya - النسخة الشاملة", page_icon="🐂", layout="centered")

# الكود الكامل: إرجاع العملات الرقمية وضمان وجود كل الأقسام
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
        .price-item { display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
        
        .marquee-wrapper { width: 100%; position: fixed; top: 0; left: 0; background: rgba(8, 51, 68, 0.95); border-bottom: 1px solid #22d3ee; z-index: 9999; padding: 8px 0; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
        .animate-marquee { display: inline-block; white-space: nowrap; animation: marquee 25s linear infinite; font-size: 13px; font-weight: bold; color: #22d3ee; }
        
        .live-indicator { display: inline-flex; align-items: center; gap: 5px; color: #4ade80; font-size: 10px; font-weight: bold; margin-bottom: 10px; }
        .dot { width: 8px; height: 8px; background: #4ade80; border-radius: 50%; display: inline-block; animation: pulse 1.5s infinite; }
        @keyframes pulse { 0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.7); } 70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(74, 222, 128, 0); } 100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(74, 222, 128, 0); } }

        .main-container { padding: 80px 20px 50px 20px; display: flex; flex-direction: column; items: center; }
        .updated { animation: flash-green 1.5s; }
        @keyframes flash-green { 0% { background: rgba(74, 222, 128, 0.2); } 100% { background: transparent; } }
    </style>
</head>
<body>
    <div class="marquee-wrapper">
        <div class="animate-marquee">
            📢 Toro Libya: تحديثات فورية من غرف الواتساب الموثوقة .. ₿ بيتكوين يتجاوز 96 ألف دولار .. 💍 الذهب يحافظ على مستوياته في السوق الليبي .. 🏗️ أسعار البناء اليوم ..
        </div>
    </div>

    <div class="main-container">
        <div class="live-indicator"><span class="dot"></span> اتصال مباشر بسوق المشير والبورصات</div>

        <div class="text-center mb-6">
            <h1 class="text-5xl font-black tracking-widest uppercase">Toro <span class="text-cyan-400">Ly</span></h1>
            <p class="text-gray-500 text-[10px] mt-1 uppercase tracking-widest text-center">المؤشر الاقتصادي الليبي المتكامل</p>
        </div>

        <div class="w-full max-w-md">
            <div class="glass p-5 border-l-4 border-cyan-500">
                <h2 class="section-title">🌟 نبض السوق والتوصيات</h2>
                <p class="text-[11px] text-green-400 italic">✅ النظام يراقب غرف الواتساب الآن لتحديث الأسعار...</p>
                <a href="https://wa.me/yournumber" class="block w-full text-center bg-green-600/20 text-green-400 text-xs py-2 rounded-lg mt-3">💬 تواصل مع الإدارة</a>
            </div>

            <div class="glass p-5 mt-6">
                <h2 class="section-title">📊 تحليل السوق المباشر</h2>
                <canvas id="liveChart" width="400" height="220"></canvas>
            </div>

            <div class="glass p-5 mt-6">
                <h2 class="section-title">💵 العملات العالمية</h2>
                <div id="row-usd" class="price-item"><span>🇺🇸 دولار موازي</span><span id="price-usd" class="font-bold text-cyan-400">8.65</span></div>
                <div class="price-item"><span>🇪🇺 يورو موازي</span><span class="font-bold">9.12</span></div>
                <div class="price-item"><span>🇬🇧 باوند إسترليني</span><span class="font-bold">10.85</span></div>
                <div class="price-item"><span>🇹🇳 دينار تونسي</span><span class="font-bold">2.65</span></div>
                <div class="price-item"><span>🇪🇬 جنيه مصري</span><span class="font-bold text-green-400">0.17</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">✨ الذهب والمعادن</h2>
                <div class="price-item"><span>💍 ذهب جديد (21)</span><span class="font-bold text-yellow-500">485.0</span></div>
                <div class="price-item"><span>🛠️ ذهب مستعمل (18)</span><span class="font-bold text-yellow-600">425.0</span></div>
                <div class="price-item"><span>✨ ذهب كسر (18)</span><span class="font-bold text-yellow-400">415.5</span></div>
                <div class="price-item"><span>🥈 فضة (جرام)</span><span class="font-bold text-gray-300">5.40</span></div>
                <div class="price-item"><span>🥉 نحاس (كيلو)</span><span class="font-bold text-orange-500">42.0</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">🪙 العملات الرقمية</h2>
                <div class="price-item"><span>₿ Bitcoin (BTC)</span><span id="btc-price" class="text-green-400 font-bold">$96,430</span></div>
                <div class="price-item"><span>Ξ Ethereum (ETH)</span><span class="text-blue-400 font-bold">$3,345</span></div>
                <div class="price-item"><span>💠 Solana (SOL)</span><span class="text-purple-400 font-bold">$195.20</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">⛽ الطاقة والنفط</h2>
                <div class="price-item"><span>🛢️ خام برنت</span><span class="font-bold text-green-400">$78.40</span></div>
                <div class="price-item"><span>🔥 غاز الطهي</span><span class="font-bold">5.00 LYD</span></div>
            </div>

            <div class="glass p-5">
                <h2 class="section-title">🏗️ مواد البناء والسلع</h2>
                <div class="price-item"><span>🧱 إسمنت (قنطار)</span><span class="font-bold">45.00</span></div>
                <div class="price-item"><span>⛓️ حديد (الطن)
