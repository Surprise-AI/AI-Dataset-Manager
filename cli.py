import argparse
import json
from ai_dataset_manager.data_management import add_data_to_json, add_data_to_csv  # فقط استيراد الدوال المتاحة

def main():
    parser = argparse.ArgumentParser(description="إضافة البيانات إلى ملف JSON أو CSV")
    
    # إضافة الخيار save و add
    parser.add_argument('action', choices=['save', 'add'], help="العملية التي تريد تنفيذها")
    parser.add_argument('format', choices=['json', 'csv'], help="تنسيق الملف")
    parser.add_argument('file_path', help="مسار الملف")
    parser.add_argument('--data', help="البيانات لإضافتها (فقط للـ add)", required=False)
    
    args = parser.parse_args()

    if args.action == 'add':
        if args.format == 'json':
            # تحويل البيانات من سلسلة إلى قاموس
            data = json.loads(args.data)
            add_data_to_json(data, args.file_path)  # إضافة البيانات إلى ملف JSON
        elif args.format == 'csv':
            # تحويل البيانات من سلسلة إلى قاموس
            data = json.loads(args.data)
            add_data_to_csv(data, args.file_path)  # إضافة البيانات إلى ملف CSV
        else:
            print("الدعم لإضافة البيانات في هذا التنسيق غير مفعّل بعد.")


if __name__ == "__main__":
    main()
