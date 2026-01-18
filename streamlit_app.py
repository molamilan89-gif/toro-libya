import streamlit as st
import base64

# إعدادات الصفحة الاحترافية - TORO LIBYA
st.set_page_config(page_title="Toro Libya - النسخة الأسطورية", page_icon="🐂", layout="centered")

# دالة لمعالجة الصورة إذا كانت مرفوعة محلياً (logo.png)
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

# إذا كان لديك ملف شعار باسم logo.png ضعه في نفس المجلد
img_base64 = get_base64_of_bin_file('logo.png')

full_code = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Tajawal', sans-serif; background: #0b1120; color: white; margin: 0; padding: 0; overflow-x: hidden; }}
        .glass {{ background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; margin-bottom: 20px; transition: 0.3s ease; }}
        .section-title {{ border-right: 4px solid #22d3ee; padding-right: 12px; margin-bottom: 15px; font-weight: 900; color: #22d3ee; }}
        .price-item {{ display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }}
        
        /* شريط الأخبار المتحرك */
        .marquee-wrapper {{ width: 100%; position: fixed; top: 0; left: 0; background: rgba(8, 51, 68, 0.95); border-bottom: 1px solid #22d3ee; z-index: 9999; padding: 10px 0; }}
        @keyframes marquee {{ 0% {{ transform: translateX(100%); }} 100% {{ transform: translateX(-100%); }} }}
        .animate-marquee {{ display: inline-block; white-space: nowrap; animation: marquee 25s linear infinite; font-size: 14px; font-weight: bold; color: #22d3ee; }}
        
        /* تحسين الهوامش لتفادي التداخل مع شريط الأخبار */
        .main-container {{ padding: 120px 20px 50px 20px; display: flex; flex-direction: column; items: center; }}
        
        /* تصميم الشعار */
        .logo-container {{ text-align: center; margin-bottom: 25px; }}
        .logo-img {{ width: 140px; height: 140px; border-radius: 30px; box-shadow: 0 0 40px rgba(34, 211, 238, 0.25); border: 2px solid rgba(34, 211, 238, 0.4); margin: 0 auto; object-fit: cover; background: #111827; }}
        .logo-text {{ font-size: 2.8rem; font-weight: 900; letter-spacing: 4px; margin-top: 15px; text-transform: uppercase; color: white; }}

        /* بطاقات المؤشرات السريعة (مثل البورصة العالمية) */
        .quick-cards-grid {{ display: grid; grid-template-cols: repeat(3, 1fr); gap: 10px; width: 100%; max-width: 450px; margin-bottom: 25px; }}
        .card-stat {{ background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 15px; padding: 12px; text-align: center; }}
        .card-stat p {{ font-size: 10px; color: #94a3b8; text-transform: uppercase; margin-bottom: 4px; }}
        .card-stat span {{ font-size: 14px; font-weight: 900; color: #22d3ee; }}

        .live-indicator {{ display: inline-flex; align-items: center; gap: 6px; color: #4ade80; font-size: 11px; font-weight: bold; margin-
        
