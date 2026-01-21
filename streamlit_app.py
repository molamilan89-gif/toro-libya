def calculate_toro_ly_gold():
    print("--- حاسبة كنز الذهب (TORO LY) ---")
    print("مرحباً يا أسطورة، أدخل الكميات التي جمعتها:")
    
    # إدخال البيانات
    cpus = int(input("عدد المعالجات (CPUs) القديمة: "))
    ram_weight = float(input("وزن الرامات بالكيلو (Kg): "))
    boards_weight = float(input("وزن اللوحات الأم بالكيلو (Kg): "))
    
    # أسعار افتراضية (يناير 2026) - يمكن تحديثها
    gold_price_per_oz = 2450.0  # سعر الأونصة بالدولار
    
    # حساب الذهب التقديري بالأونصة (Troy Ounce)
    # المعالج القديم يعطي حوالي 0.2 جرام ذهب
    # كيلو الرامات يعطي حوالي 1.2 جرام
    # كيلو اللوحات يعطي حوالي 0.5 جرام
    
    total_grams = (cpus * 0.2) + (ram_weight * 1.2) + (boards_weight * 0.5)
    total_ounces = total_grams / 31.103
    
    # حساب القيمة المالية
    total_value_usd = total_ounces * gold_price_per_oz
    
    print("\n" + "="*30)
    print(f"النتائج التقديرية لمخزن المزرعة:")
    print(f"إجمالي الذهب المتوقع: {total_ounces:.4f} أونصة")
    print(f"إجمالي الذهب بالجرام: {total_grams:.2f} جرام")
    print(f"القيمة السوقية التقريبية: ${total_value_usd:.2f} دولار")
    print("="*30)
    print("ملاحظة: هذه تقديرات مبنية على أجهزة قديمة جداً (أصلية).")

# تشغيل الحاسبة
calculate_toro_ly_gold()
