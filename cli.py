import argparse
from ai_dataset_manager import data_format_support

def main():
    parser = argparse.ArgumentParser(description="AI-Dataset-Manager CLI Tool")
    parser.add_argument("action", choices=["load", "save"], help="Action to perform")
    parser.add_argument("file_type", choices=["json", "csv"], help="File format")
    parser.add_argument("file_path", help="File path for data")
    parser.add_argument("--output", help="Output file path for saving (only for save)")

    args = parser.parse_args()

    if args.action == "load":
        if args.file_type == "json":
            data = data_format_support.load_json(args.file_path)
            print(data)
        elif args.file_type == "csv":
            data = data_format_support.load_csv(args.file_path)
            print(data)

    elif args.action == "save":
        if not args.output:
            print("Error: You must provide --output path to save the data.")
            return
        # Dummy data to save (you can modify this)
        dummy_data = {"message": "Hello, World!"} if args.file_type == "json" else [{"name": "Ali", "age": 21}]
        if args.file_type == "json":
            data_format_support.save_json(dummy_data, args.output)
        elif args.file_type == "csv":
            import pandas as pd
            df = pd.DataFrame(dummy_data)
            data_format_support.save_csv(df, args.output)

if __name__ == "__main__":
    main()