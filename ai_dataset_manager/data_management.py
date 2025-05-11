import csv
import json

def add_data_to_json(data, file_path):
    if isinstance(data, dict):
        data = [data]
    try:
        with open(file_path, 'r+', encoding='utf-8') as file:
            existing_data = json.load(file)
            existing_data.extend(data)  # Add data to existing data
            file.seek(0)
            json.dump(existing_data, file, ensure_ascii=False, indent=4)
            print("Data successfully added to JSON file.")
    except FileNotFoundError:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            print("New JSON file created with data.")
    except Exception as e:
        print(f"Error while adding data to JSON file: {e}")

def add_data_to_csv(data, file_path):
    if isinstance(data, dict):
        data = [data]
    try:
        with open(file_path, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            
            if file.tell() == 0:
                writer.writeheader()
            writer.writerows(data)
            print("Data successfully added to CSV file.")
    except Exception as e:
        print(f"Error while adding data to CSV file: {e}")

def search_json(query, file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            results = [item for item in data if query.lower() in json.dumps(item).lower()]
            return results
    except Exception as e:
        print(f"Error while searching JSON file: {e}")
        return []

def search_csv(query, file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            results = [row for row in reader if query.lower() in json.dumps(row).lower()]
            return results
    except Exception as e:
        print(f"Error while searching CSV file: {e}")
        return []

def save_json(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Data saved to JSON file successfully.")
    except Exception as e:
        print(f"Error while saving data to JSON file: {e}")

def save_csv(data, file_path):
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            if data:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            else:
                print("No data to save.")
    except Exception as e:
        print(f"Error while saving data to CSV file: {e}")
