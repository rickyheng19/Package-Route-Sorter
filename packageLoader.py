import csv
from package import Package
from hashmap import HashMap

def load_packages_from_csv(file_path):
    package_list = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header line
        for row in csvreader:
            if len(row) == 9:
                package_id, address, city, state, zip_code, deadline, weight, _, special_notes = row
                package = Package(package_id, address, city, state, zip_code, deadline, weight, special_notes)
                package_list.append(package)

    return package_list

def print_all_packages(package_list):
    for package in package_list:
        print(f"Package ID: {package.package_id}")
        print(f"Address: {package.address}")
        print(f"City: {package.city}")
        print(f"State: {package.state}")
        print(f"Zip Code: {package.zip_code}")
        print(f"Deadline: {package.deadline}")
        print(f"Weight: {package.weight}")
        print(f"Special Notes: {package.special_notes}")
        print("-" * 30)  # Just for formatting