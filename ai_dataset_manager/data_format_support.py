mport json
import pandas as pd  # مكتبة pandas لمعالجة البيانات في تنسيق CSV

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)  # حفظ البيانات في ملف JSON

def save_csv(data, file_path):
    # تحويل البيانات إلى DataFrame ثم حفظها كملف CSV
    df = pd.DataFrame([data])
    df.to_csv(file_path, index=False)
