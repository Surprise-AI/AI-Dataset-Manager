import json
import csv

def validate_json(data):
    # تحقق من أن البيانات هي قائمة أو قاموس
    if not isinstance(data, (dict, list)):
        raise ValueError("البيانات يجب أن تكون قائمة أو قاموس.")
    if isinstance(data, dict):
        data = [data]
    return data

def add_data_to_json(data, file_path):
    data = validate_json(data)  # التحقق من البيانات
    try:
        with open(file_path, 'r+', encoding='utf-8') as file:
            existing_data = json.load(file)
            existing_data.extend(data)  # إضافة البيانات إلى البيانات الموجودة
            file.seek(0)
            json.dump(existing_data, file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            
def validate_csv(data):
    # تحقق من أن البيانات عبارة عن قائمة من القواميس
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("البيانات يجب أن تكون قائمة من القواميس.")
    return data

def add_data_to_csv(data, file_path):
    data = validate_csv(data)  # التحقق من البيانات
    try:
        with open(file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            if file.tell() == 0:
                writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"حدث خطأ أثناء إضافة البيانات إلى الملف: {e}")
