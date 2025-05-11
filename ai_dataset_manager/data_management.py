import json

def add_data_to_json(data, file_path):
    # فتح الملف والقراءة
    try:
        with open(file_path, "r") as file:
            existing_data = json.load(file)  # تحميل البيانات الموجودة
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []  # إذا كان الملف فارغًا أو غير موجود، نبدأ من قائمة فارغة
    
    # التأكد من أن existing_data هو قائمة
    if isinstance(existing_data, list):
        existing_data.append(data)  # إضافة البيانات الجديدة إلى القائمة
    else:
        print("البيانات الموجودة ليست بصيغة قائمة!")
        return
    
    # حفظ البيانات المعدلة في الملف
    with open(file_path, "w") as file:
        json.dump(existing_data, file, indent=4)  # حفظ البيانات بتنسيق جميل
