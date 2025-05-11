import argparse
from ai_dataset_manager.data_format_support import load_json, load_csv, save_json, save_csv  # تعديل الاستيراد هنا

def main():
    parser = argparse.ArgumentParser(description="AI-Dataset-Manager CLI Tool")
    parser.add_argument("action", choices=["load", "save"], help="Action to perform")
    parser.add_argument("file_type", choices=["json", "csv"], help="File format")
    parser.add_argument("file_path", help="File path for data")
    
    args = parser.parse_args()

    if args.action == "load":
        if args.file_type == "json":
            data = load_json(args.file_path)  # استدعاء الدالة هنا
            print(data)
        elif args.file_type == "csv":
            data = load_csv(args.file_path)  # استدعاء الدالة هنا
            print(data)
    elif args.action == "save":
        if args.file_type == "json":
            save_json({}, args.file_path)  # حفظ البيانات بشكل فارغ كمثال
        elif args.file_type == "csv":
            save_csv({}, args.file_path)  # حفظ البيانات بشكل فارغ كمثال

if name == "main":
    main()
