import json

def add_data_to_json(data, file_path):
    # إذا كانت البيانات عبارة عن قاموس واحد، نحولها إلى قائمة تحتوي على هذا القاموس
    if isinstance(data, dict):
        data = [data]
    
    try:
        # فتح الملف في وضع القراءة والكتابة
        with open(file_path, 'r+') as file:
            try:
                # قراءة البيانات الموجودة في الملف
                existing_data = json.load(file)
                # التأكد من أن البيانات الموجودة هي قائمة
                if not isinstance(existing_data, list):
                    existing_data = []
            except json.JSONDecodeError:
                # إذا كان الملف فارغًا أو يحتوي على بيانات غير صالحة، نبدأ من قائمة فارغة
                existing_data = []
            
            # إضافة البيانات الجديدة إلى البيانات الحالية
            existing_data.extend(data)
            
            # العودة إلى بداية الملف وكتابة البيانات الجديدة
            file.seek(0)
            json.dump(existing_data, file, indent=4)
    except Exception as e:
        print(f"حدث خطأ أثناء إضافة البيانات إلى الملف: {e}")
