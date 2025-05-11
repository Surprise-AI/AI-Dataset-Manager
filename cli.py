import argparse
import json
from ai_dataset_manager.data_management import add_data_to_json, add_data_to_csv, search_json, search_csv, save_json, save_csv

def main():
    parser = argparse.ArgumentParser(description="Add data to a JSON or CSV file")
    
    # Add save, add, and search actions
    parser.add_argument('action', choices=['save', 'add', 'search'], help="The action you want to perform")
    parser.add_argument('format', choices=['json', 'csv'], help="The file format")
    parser.add_argument('file_path', help="The file path")
    parser.add_argument('--data', help="Data to add or search for (only for add and search)", required=False)
    parser.add_argument('--query', help="The query keyword for search (only for search)", required=False)

    args = parser.parse_args()

    if args.action == 'add':
        if args.format == 'json':
            data = json.loads(args.data)
            add_data_to_json(data, args.file_path)
            print("Data successfully added to JSON file.")
        elif args.format == 'csv':
            data = json.loads(args.data)
            add_data_to_csv(data, args.file_path)
            print("Data successfully added to CSV file.")
    
    elif args.action == 'search':
        if not args.query:
            print("Please provide a query keyword using --query")
            return
        if args.format == 'json':
            results = search_json(args.query, args.file_path)
            if results:
                print("Found results in JSON file:", results)
            else:
                print("No results found in JSON file.")
        elif args.format == 'csv':
            results = search_csv(args.query, args.file_path)
            if results:
                print("Found results in CSV file:", results)
            else:
                print("No results found in CSV file.")
    
    elif args.action == 'save':
        if args.format == 'json':
            save_json([], args.file_path)
            print("JSON file saved successfully.")
        elif args.format == 'csv':
            save_csv([], args.file_path)
            print("CSV file saved successfully.")



if __name__ == "__main__":
    main()
