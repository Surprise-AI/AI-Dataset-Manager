import argparse
import json
from ai_dataset_manager.data_management import (
    add_data_to_json, add_data_to_csv, search_json, search_csv, 
    save_json, save_csv, update_data_in_json, update_data_in_csv, 
    delete_data_from_json, delete_data_from_csv
)

def main():
    parser = argparse.ArgumentParser(description="Add, update, delete, or search data in a JSON or CSV file")
    
    # Add action choices (save, add, update, delete, search)
    parser.add_argument('action', choices=['save', 'add', 'update', 'delete', 'search'], help="The action you want to perform")
    parser.add_argument('format', choices=['json', 'csv'], help="The file format")
    parser.add_argument('file_path', help="The file path")
    parser.add_argument('--data', help="Data to add, update, or delete (only for add, update, and delete)", required=False)
    parser.add_argument('--query', help="The query keyword for search, update or delete (only for search, update, and delete)", required=False)
    
    args = parser.parse_args()

    if args.action == 'add':
        if args.format == 'json':
            data = json.loads(args.data)
            add_data_to_json(data, args.file_path)
        elif args.format == 'csv':
            data = json.loads(args.data)
            add_data_to_csv(data, args.file_path)
    
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
    
    elif args.action == 'update':
        if not args.query or not args.data:
            print("Please provide both a query and updated data using --query and --data")
            return
        updated_data = json.loads(args.data)
        if args.format == 'json':
            update_data_in_json(args.query, updated_data, args.file_path)
        elif args.format == 'csv':
            update_data_in_csv(args.query, updated_data, args.file_path)

    elif args.action == 'delete':
        if not args.query:
            print("Please provide a query keyword using --query")
            return
        if args.format == 'json':
            delete_data_from_json(args.query, args.file_path)
        elif args.format == 'csv':
            delete_data_from_csv(args.query, args.file_path)
    
    elif args.action == 'save':
        if args.format == 'json':
            save_json([], args.file_path)
        elif args.format == 'csv':
            save_csv([], args.file_path)



if __name__ == "__main__":
    main()
