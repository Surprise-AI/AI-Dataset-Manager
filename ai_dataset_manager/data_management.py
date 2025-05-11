import json
import csv

# إضافة البيانات إلى JSON
def add_data_to_json(data, file_path):
    if isinstance(data, dict):
        data = [data]  # إذا كانت البيانات عبارة عن قاموس، نحولها إلى قائمة
    try:
        with open(file_path, 'r+', encoding='utf-8') as file:
            existing_data = json.load(file)
            existing_data.extend(data)  # إضافة البيانات إلى البيانات الموجودة
            file.seek(0)
            json.dump(existing_data, file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

# إضافة البيانات إلى CSV
def add_data_to_csv(data, file_path):
    if isinstance(data, dict):
        data = [data]  # إذا كانت البيانات عبارة عن قاموس، نحولها إلى قائمة
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

# البحث في JSON
def search_json(query, file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # تصفية البيانات بناءً على البحث
            result = [item for item in data if query.lower() in item.get('name', '').lower()]
            return result
    except FileNotFoundError:
        print("الملف غير موجود.")
        return []

# البحث في CSV
def search_csv(query, file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            result = [row for row in reader if query.lower() in row.get('name', '').lower()]
            return result
    except FileNotFoundError:
        print("الملف غير موجود.")
        return []
