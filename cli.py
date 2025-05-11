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
        sample_data = {"name": "Surprise AI", "type": "tool"}  # بيانات ثابتة للتجربة
        if args.file_type == "json":
            data_format_support.save_json(sample_data, args.file_path)
            print("JSON data saved successfully.")
        elif args.file_type == "csv":
            import pandas as pd
            df = pd.DataFrame([sample_data])
            data_format_support.save_csv(df, args.file_path)
            print("CSV data saved successfully.")

if __name__ == "__main__":
    main()