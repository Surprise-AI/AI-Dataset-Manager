import argparse
from ai_dataset_manager.data_format_support import save_json, save_csv  # استيراد دوال الحفظ
from ai_dataset_manager.data_management import add_data_to_json, add_data_to_csv  # استيراد دوال إضافة البيانات

def main():
    parser = argparse.ArgumentParser(description="Surprise AI - Command Line Interface")
    
    # تعريف الأوامر
    parser.add_argument('action', choices=['save', 'add'], help="Choose an action: 'save' to store data, 'add' to add new data")
    parser.add_argument('format', choices=['json', 'csv'], help="Choose the format: 'json' or 'csv'")
    parser.add_argument('file_path', help="Path to the output file")
    parser.add_argument('--data', type=str, help="Data to be added (in JSON format for 'add' action)")

    args = parser.parse_args()

    if args.action == 'save':
        if args.format == 'json':
            save_json({}, args.file_path)
        elif args.format == 'csv':
            save_csv({}, args.file_path)
    
    elif args.action == 'add':
        if args.data:
            # تحويل البيانات المدخلة من JSON
            data = json.loads(args.data)
            if args.format == 'json':
                add_data_to_json(data, args.file_path)
            elif args.format == 'csv':
                add_data_to_csv(data, args.file_path)
        else:
            print("Error: No data provided for 'add' action.")

if __name__ == "__main__":
    main()
