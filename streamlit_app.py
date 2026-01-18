import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Toro Libya | تورو ليبيا", page_icon="🐂", layout="centered")

# 2. بناء الواجهة باستخدام HTML و CSS (التصميم العالمي)
full_design = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Tajawal', sans-serif; background: #0b1120; color: white; margin: 0; }
        .glass { background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; margin-bottom: 15px; padding: 20px; }
        .section-title { border-right: 4px solid #22d3ee; padding-right: 12px; margin-bottom: 15px; font-weight: 900; color: #22d3ee; }
        .price-item { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
        .marquee-container { width: 100%; overflow: hidden; background: #083344; py: 8px; position: fixed; top: 0; z-index: 100; border-bottom: 1px solid #22d3ee; }
        .marquee-text { display: inline-block; white-space: nowrap; animation: marquee 25s linear infinite; color: #22d3ee; font-size: 14px; font-weight: bold; padding: 5px 0; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
        .calc-input { background: #111827; border: 1px solid #374151; border-radius: 10px; padding: 12px; width: 100%; color: white; text-align: center; font-family: sans-serif; font-weight: bold; outline: none; margin-bottom: 10px; }
        .calc-input:focus { border-color: #22d3ee; }
    </style>
</head>
<body>
    <div class="marquee-container">
        <div class="marquee-text">
             📢 عاجل: Toro Libya يطلق التحديث الشامل لأسعار الذهب والعملات .. 🛢️ خام برنت مستقر عند 78.40$ .. 🏗️ أسعار الإسمنت والحديد اليوم في ليبيا ..
        </div>
    </div>

    <div style="padding: 60px 20px 350px 20px; max-width: 500px; margin: auto;">
        <div style="text-align: center; margin-bottom: 30px;">
            <h1 style="font-size: 48px; font-weight: 900; letter-spacing: 4px; margin: 0;">TORO <span style="color: #22d3ee;">LY</span></h1>
            <p style="color: #64748b; font-size: 12px; text-transform: uppercase;">المؤشر الاقتصادي الليبي المتكامل</p>
        </div>

        <div class="glass">
            <h2 class="section-title">💵 العملات والذهب</h2>
            <div class="price-item"><span>🇺🇸 دولار موازي</span><span style="color: #22d3ee; font-weight: bold;">8.65</span></div>
            <div class="price-item"><span>🇪🇺 يورو موازي</span><span style="font-weight: bold;">9.12</span></div>
            <div class="price-item"><span>✨ ذهب كسر (18)</span><span style="color: #eab308; font-weight: bold;">415.5</span></div>
        </div>

        <div class="glass">
            <h2 class="section-title">🪙 العملات الرقمية</h2>
            <div class="price-item"><span>₿ Bitcoin</span><span style="color: #4ade80; font-weight: bold;">$96
