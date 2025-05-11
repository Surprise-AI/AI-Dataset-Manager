import argparse
import json
from ai_dataset_manager.data_management import add_data_to_json, add_data_to_csv, save_json, save_csv  # استيراد الدوال اللازمة

def main():
    parser = argparse.ArgumentParser(description="إضافة البيانات أو حفظها في ملف JSON أو CSV")
    
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
            print("تنسيق الملف غير مدعوم بعد.")
    
    elif args.action == 'save':
        if args.format == 'json':
            # حفظ البيانات في ملف JSON
            save_json({}, args.file_path)  # يمكن تعديل البيانات حسب الحاجة
        elif args.format == 'csv':
            # حفظ البيانات في ملف CSV
            save_csv({}, args.file_path)  # يمكن تعديل البيانات حسب الحاجة
        else:
            print("تنسيق الملف غير مدعوم بعد.")


if __name__ == "__main__":
    main()
