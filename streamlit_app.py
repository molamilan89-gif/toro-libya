import streamlit as st

# إعدادات الصفحة الاحترافية - TORO LIBYA
st.set_page_config(page_title="Toro Libya - النسخة الأسطورية", page_icon="🐂", layout="centered")

# الكود الكامل: شعار مضمون + حاسبة شغالة + جميع الأقسام
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
        
        /* تحسين الهوامش لتفادي تداخل الشعار */
        .main-container { padding: 130px 20px 50px 20px; display: flex; flex-direction: column; items: center; }
        
        /* تصميم الشعار المضمون الظهور (SVG كود) */
        .logo-box { width: 140px; height: 140px; border-radius: 35px; background: linear-gradient(135deg, #1e293b 0%, #0891b2 100%); border: 3px solid #22d3ee; box-shadow: 0 0 35px rgba(34, 211, 238, 0.4); display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; }
        .logo-box svg { width: 85px; height: 85px; fill: white; filter: drop-shadow(0 0 10px rgba(255,255,255,0.5)); }
        
        .logo-text { font-size: 2.8rem; font-weight: 900; letter-spacing: 5px; text-transform: uppercase; color: white; line-height: 1; text-align: center; }
        
        /* بطاقات المؤشرات (زي الصور) */
        .quick-grid { display: grid; grid-template-cols: repeat(3, 1fr); gap: 10px; width: 100%; max-width: 450px; margin-bottom: 30px; }
        .quick-card { background: rgba(15, 23, 42, 0.9); border: 1px solid rgba(34, 211, 238, 0.3); border-radius: 15px; padding: 15px 5px; text-align: center; }
        .quick-card p { font-size: 10px; color: #94a3b8; margin-bottom: 5px; font-weight: bold; }
        .quick-card span { font-size: 16px; font-weight: 900; color: #22d3ee; }

        .live-tag { display: inline-flex; align-items: center; gap: 6px; color: #4ade80; font-size: 11px; font-weight: bold; margin-bottom: 15px; background: rgba(74, 222, 128, 0.1); padding: 5px 15px; border-radius: 20px; border: 1px solid rgba(74, 222, 128, 0.2); }
        .dot { width: 8px; height: 8px; background: #4ade80; border-radius: 50%; animation: pulse 1.5s infinite; }
        @keyframes pulse { 0% { transform: scale(0.95); } 70% { transform: scale(1.1); box-shadow: 0 0 0 8px rgba(74, 222, 128, 0); } 100% { transform: scale(0.95); } }
        
        .price-item { display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }

        /* الآلة الحاسبة */
        .calc-box { width: 100%; background: #0f172a; border: 1px solid #334155; border-radius: 12px; padding: 15px; text-align: center; }
        .calc-input { width: 100%; background: transparent; border: none; text-align: center; font-size: 24px; font-weight: 900; color: #22d3ee; outline: none; }
        .calc-label { font-size: 11px; color: #94a3b8; text-transform: uppercase; margin-bottom: 8px; display: block; }
    </style>
</head>
<body>
    <div class="marquee-wrapper">
        <div class="animate-marquee">
            📢 Toro Libya: تم إصلاح الشعار والآلة الحاسبة .. نظام التحديث الفوري يعمل الآن .. الدولار 8.65 .. الذهب كسر 18 بـ 415.5 .. ₿ البيتكوين 96,430$ .. 🐂
        </div>
    </div>

    <div class="main-container">
        <div class="logo-container">
            <div class="live-tag"><span class="dot"></span> نظام Toro Ly المباشر</div>
            <div class="logo-box">
                <svg viewBox="0 0 24 24"><path d="M12,2C6.47,2,2,6.47,2,12s4.47,10,10,10s10-4.47,10-10S17.53,2,12,2z M15.59,15.59L12,12L8.41,15.59L7,14.17l5-5l5,5L15.59,15.59z"/></svg>
            </div>
            <h1 class="logo-text">TORO <span class="text-cyan-400">LY</span></h1>
            <p class="text-gray-500 text-[9px] tracking-[0.5em] uppercase font-black mt-2 text-center">The Legend of Libyan Market</p>
        </div>

        <div class="quick-grid">
            <div class="quick-card"><p>USD</p><span id="q-usd">8.65</span></div>
            <div class="quick-card"><p>GOLD 18</p><span id="q-gold">415.5</span></div>
            <div class="quick-card"><p>BTC</p><span id="q-btc">96.4K</span></div>
        </div>

        <div class="w-full max-w-md">
            <div class="glass p-5 border-l-4 border-cyan-500">
                <h2 class="section-title">🌟 نبض السوق والتوص
