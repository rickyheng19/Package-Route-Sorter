import csv
from Package import Package

def packageReader(file):
    #Make new package list
    PackageList = []

    # Replace this with the actual path to your CSV file
    file_path = file

    # Open the CSV file and create a CSV reader
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        # Iterate through each row in the CSV file
        for row in csvreader:
            package_id = row[0]
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = row[4]
            delivery_time = row[5]
            weight = row[6]
            status = "at hub"

            # Create a Package object using the constructor
            package = Package(package_id, address, city, state, zip_code, delivery_time, weight, status)

            # Add the Package object to the hashmap using the package_id as the key
            PackageList.append(package)

    return PackageList