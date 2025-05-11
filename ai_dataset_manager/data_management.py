import json
import pandas as pd

# إضافة بيانات في ملف JSON
def add_data_to_json(data, file_path):
    try:
        # قراءة البيانات الحالية في الملف
        with open(file_path, 'r') as f:
            existing_data = json.load(f)
        
        # إضافة البيانات الجديدة إلى البيانات الموجودة
        existing_data.append(data)
        
        # حفظ البيانات المعدلة
        with open(file_path, 'w') as f:
            json.dump(existing_data, f, indent=4)
        print("Data added successfully to JSON.")
    except FileNotFoundError:
        # في حالة عدم وجود الملف، إنشاء الملف وكتابة البيانات فيه
        with open(file_path, 'w') as f:
            json.dump([data], f, indent=4)
        print("New file created and data added.")

# إضافة بيانات في ملف CSV
def add_data_to_csv(data, file_path):
    try:
        # تحويل البيانات إلى DataFrame
        df = pd.DataFrame([data])
        
        # إضافة البيانات إلى الملف
        df.to_csv(file_path, mode='a', header=False, index=False)
        print("Data added successfully to CSV.")
    except FileNotFoundError:
        # في حالة عدم وجود الملف، إنشاء الملف وكتابة البيانات فيه
        df = pd.DataFrame([data])
        df.to_csv(file_path, index=False)
        print("New file created and data added.")
