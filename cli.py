import argparse
from ai_dataset_manager.data_format_support import save_json, save_csv  # استيراد الدوال من الملف المناسب

def main():
    parser = argparse.ArgumentParser(description="Surprise AI - Command Line Interface")
    
    # تعريف الأوامر
    parser.add_argument('action', choices=['save'], help="Choose an action: 'save' to store data")
    parser.add_argument('format', choices=['json', 'csv'], help="Choose the format: 'json' or 'csv'")
    parser.add_argument('file_path', help="Path to the output file")

    args = parser.parse_args()

    # تنفيذ الفعل بناءً على الاختيارات
    if args.action == 'save':
        if args.format == 'json':
            save_json({}, args.file_path)  # حفظ البيانات بتنسيق JSON
        elif args.format == 'csv':
            save_csv({}, args.file_path)  # حفظ البيانات بتنسيق CSV

if __name__ == "__main__":
    main()
