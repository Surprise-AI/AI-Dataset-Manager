import csv
import json

def add_data_to_json(data, file_path):
    if isinstance(data, dict):
        data = [data]
    try:
        with open(file_path, 'r+', encoding='utf-8') as file:
            existing_data = json.load(file)
            existing_data.extend(data)  # Add new data to existing data
            file.seek(0)
            json.dump(existing_data, file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

def add_data_to_csv(data, file_path):
    if isinstance(data, dict):
        data = [data]
    try:
        with open(file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            if file.tell() == 0:
                writer.writeheader()  # Write headers if the file is empty
            writer.writerows(data)
    except Exception as e:
        print(f"Error while adding data to CSV: {e}")

def search_json(query, file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [item for item in data if query.lower() in json.dumps(item).lower()]
    except Exception as e:
        print(f"Error while searching JSON file: {e}")
        return []

def search_csv(query, file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader if query.lower() in json.dumps(row).lower()]
    except Exception as e:
        print(f"Error while searching CSV file: {e}")
        return []

def update_data_in_json(query, updated_data, file_path):
    try:
        with open(file_path, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            updated = False
            for item in data:
                if query.lower() in json.dumps(item).lower():
                    item.update(updated_data)  # Update the item with new data
                    updated = True
            if updated:
                file.seek(0)
                json.dump(data, file, ensure_ascii=False, indent=4)
                print("Data updated successfully in JSON file.")
            else:
                print("No matching data found to update.")
    except Exception as e:
        print(f"Error while updating JSON file: {e}")

def update_data_in_csv(query, updated_data, file_path):
    try:
        with open(file_path, 'r+', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            updated = False
            for row in rows:
                if query.lower() in json.dumps(row).lower():
                    row.update(updated_data)  # Update the row with new data
                    updated = True
            if updated:
                file.seek(0)
                writer = csv.DictWriter(file, fieldnames=rows[0].keys())
                writer.writeheader()
                writer.writerows(rows)
                print("Data updated successfully in CSV file.")
            else:
                print("No matching data found to update.")
    except Exception as e:
        print(f"Error while updating CSV file: {e}")

def delete_data_from_json(query, file_path):
    try:
        with open(file_path, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            data = [item for item in data if query.lower() not in json.dumps(item).lower()]
            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=4)
            print("Data deleted successfully from JSON file.")
    except Exception as e:
        print(f"Error while deleting data from JSON file: {e}")

def delete_data_from_csv(query, file_path):

    try:
        with open(file_path, 'r+', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            rows = [row for row in rows if query.lower() not in json.dumps(row).lower()]
            file.seek(0)
            writer = csv.DictWriter(file, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
            print("Data deleted successfully from CSV file.")
    except Exception as e:
        print(f"Error while deleting data from CSV file: {e}")

def save_json(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"File saved as JSON at {file_path}")
    except Exception as e:
        print(f"Error while saving JSON file: {e}")

def save_csv(data, file_path):
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            if data:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            print(f"File saved as CSV at {file_path}")
    except Exception as e:
        print(f"Error while saving CSV file: {e}")
