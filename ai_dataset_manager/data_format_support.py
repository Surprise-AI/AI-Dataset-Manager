import pandas as pd

# دالة لتحميل بيانات JSON
def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# دالة لتحميل بيانات CSV
def load_csv(file_path):
    return pd.read_csv(file_path)

# دالة لحفظ البيانات بتنسيق JSON
def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)

# دالة لحفظ البيانات بتنسيق CSV
def save_csv(data, file_path):
    # تحويل القاموس إلى DataFrame
    df = pd.DataFrame(data)
    # حفظ البيانات في ملف CSV
    df.to_csv(file_path, index=False)
