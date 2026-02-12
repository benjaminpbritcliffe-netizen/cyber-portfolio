import os
import shutil
from datetime import datetime
from tqdm import tqdm
from tabulate import tabulate

source_path = "D:/BBritcliffe/"
date_string = "21/07/2024"  # DD/MM/YYYY format

# Convert the date string to a datetime object
date = datetime.strptime(date_string, "%d/%m/%Y")

def collect_file_details(source_path, date):
    """Collect details of files modified or created after the specified date."""
    file_details = []
    total_size = 0  # Initialize total size
    for root, dirs, files in os.walk(source_path):
        for file in tqdm(files, desc="Processing files"):
            file_path = os.path.join(root, file)
            file_stats = os.stat(file_path)
            last_modified_time = datetime.fromtimestamp(file_stats.st_mtime)
            creation_time = datetime.fromtimestamp(file_stats.st_ctime)

            if last_modified_time > date or creation_time > date:
                file_size = file_stats.st_size
                total_size += file_size  # Accumulate total size
                file_details.append({
                    'FullName': file_path,
                    'Size': f"{file_size} bytes",
                    'LastWriteTime': last_modified_time.strftime("%d/%m/%Y %H:%M:%S"),
                    'CreationTime': creation_time.strftime("%d/%m/%Y %H:%M:%S")
                })
    return file_details, total_size

def print_file_details(file_details, total_size):
    """Print file details and total file size in a neat tabular format."""
    if file_details:
        print(tabulate(file_details, headers="keys", tablefmt="fancy_grid"))
        print(f"\nTotal File Size: {total_size} bytes")
    else:
        print("No files found that match the criteria.")
        print(f"\nTotal File Size: {total_size} bytes")

def copy_files(file_details, destination_path):
    """Copy the collected files to the specified destination."""
    for file in tqdm(file_details, desc="Copying files"):
        src = file['FullName']
        dest = os.path.join(destination_path, os.path.relpath(src, source_path))
        os.makedirs(os.path.dirname(dest), exist_ok=True)  # Create destination directory if needed
        shutil.copy2(src, dest)  # Copy file with metadata

# Collect and print file details
file_details, total_size = collect_file_details(source_path, date)
print_file_details(file_details, total_size)

# Ask user if they want to copy the files
copy_decision = input("\nDo you want to copy these files to a new directory? (yes/no): ").strip().lower()
if copy_decision == 'yes':
    destination_path = input("Please enter the destination directory path: ").strip()
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
    copy_files(file_details, destination_path)
    print(f"\nFiles have been copied to {destination_path}")
else:
    print("No files were copied.")
