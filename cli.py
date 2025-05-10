import argparse
from ai_dataset_manager import data_format_support

def main():
    parser = argparse.ArgumentParser(description="AI-Dataset-Manager CLI Tool")
    parser.add_argument("action", choices=["load", "save"], help="Action to perform")
    parser.add_argument("file_type", choices=["json", "csv"], help="File format")
    parser.add_argument("file_path", help="File path for data")
    
    args = parser.parse_args()

    if args.action == "load":
        if args.file_type == "json":
            data = data_format_support.load_json(args.file_path)
            print(data)
        elif args.file_type == "csv":
            data = data_format_support.load_csv(args.file_path)
            print(data)
    elif args.action == "save":
        # Implement saving functionality here, similar to loading
        pass

if name == "main":
    main()
