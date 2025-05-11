import argparse
from ai_dataset_manager.data_format_support import save_json, save_csv  # استيراد الدوال اللازمة

def main():
    parser = argparse.ArgumentParser(description="AI Dataset Manager")
    
    # إضافة الخيارات لحفظ البيانات
    parser.add_argument('action', choices=['save'], help='Action to perform (save)')
    parser.add_argument('format', choices=['json', 'csv'], help='File format (json/csv)')
    parser.add_argument('file_path', help='Path to save the file')
    
    args = parser.parse_args()
    
    # تحديد الفعل الذي سيتم تنفيذه بناءً على المدخلات
    if args.format == 'json':
        save_json({}, args.file_path)  # حفظ البيانات بشكل فارغ كمثال
    elif args.format == 'csv':
        save_csv({}, args.file_path)  # حفظ البيانات بشكل فارغ كمثال

if __name__ == "__main__":
    main()
