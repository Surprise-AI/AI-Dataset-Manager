import argparse
from ai_dataset_manager.data_format_support import load_json, load_csv, save_json, save_csv

# دالة لتنفيذ الأوامر
def main():
    parser = argparse.ArgumentParser(description="AI Dataset Manager CLI")
    parser.add_argument('command', choices=['save'], help="The command to execute")
    parser.add_argument('format', choices=['json', 'csv'], help="The format of the data")
    parser.add_argument('file_path', help="The path to save the data")

    args = parser.parse_args()

    if args.command == "save":
        if args.format == "json":
            save_json({}, args.file_path)  # حفظ البيانات بشكل فارغ كمثال
        elif args.format == "csv":
            save_csv({}, args.file_path)  # حفظ البيانات بشكل فارغ كمثال

if __name__ == "__main__":
    main()
