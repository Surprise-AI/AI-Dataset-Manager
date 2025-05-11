import argparse
import json
from ai_dataset_manager.data_management import add_data_to_json, add_data_to_csv, search_json, search_csv  # استيراد الدوال اللازمة

def main():
    parser = argparse.ArgumentParser(description="إضافة البيانات أو البحث في ملف JSON أو CSV")
    
    # إضافة الخيار save و add و search
    parser.add_argument('action', choices=['save', 'add', 'search'], help="العملية التي تريد تنفيذها")
    parser.add_argument('format', choices=['json', 'csv'], help="تنسيق الملف")
    parser.add_argument('file_path', help="مسار الملف")
    parser.add_argument('--data', help="البيانات لإضافتها (فقط للـ add)", required=False)
    parser.add_argument('--query', help="الكلمة المفتاحية للبحث", required=False)

    args = parser.parse_args()

    if args.action == 'add':
        if args.format == 'json':
            # تحويل البيانات من سلسلة إلى قاموس
            if args.data:
                data = json.loads(args.data)
                add_data_to_json(data, args.file_path)  # إضافة البيانات إلى ملف JSON
            else:
                print("يرجى توفير البيانات باستخدام --data.")
        elif args.format == 'csv':
            # تحويل البيانات من سلسلة إلى قاموس
            if args.data:
                data = json.loads(args.data)
                add_data_to_csv(data, args.file_path)  # إضافة البيانات إلى ملف CSV
            else:
                print("يرجى توفير البيانات باستخدام --data.")
    
    elif args.action == 'search':
        if args.query:
            if args.format == 'json':
                result = search_json(args.query, args.file_path)  # البحث في ملف JSON
            elif args.format == 'csv':
                result = search_csv(args.query, args.file_path)  # البحث في ملف CSV
            
            if result:
                print("النتائج:")
                for item in result:
                    print(item)
            else:
                print("لم يتم العثور على نتائج.")
        else:
            print("يرجى توفير كلمة بحث باستخدام --query.")



if __name__ == "__main__":
    main()
