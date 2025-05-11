import csv
import json

def add_data_to_json(data, file_path):
    """إضافة البيانات إلى ملف JSON"""
    if isinstance(data, dict):
        data = [data]  # تحويل البيانات إلى قائمة إذا كانت قاموسًا واحدًا
    try:
        with open(file_path, 'r+', encoding='utf-8') as file:
            existing_data = json.load(file)
            existing_data.extend(data)  # إضافة البيانات إلى البيانات الموجودة
            file.seek(0)
            json.dump(existing_data, file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

def add_data_to_csv(data, file_path):
    """إضافة البيانات إلى ملف CSV"""
    if isinstance(data, dict):
        data = [data]  # تحويل البيانات إلى قائمة إذا كانت قاموسًا واحدًا

    try:
        with open(file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            
            # إذا كان الملف فارغًا، نكتب رؤوس الأعمدة
            if file.tell() == 0:
                writer.writeheader()
                
            # كتابة البيانات الجديدة إلى الملف
            writer.writerows(data)
    except Exception as e:
        print(f"حدث خطأ أثناء إضافة البيانات إلى الملف: {e}")
